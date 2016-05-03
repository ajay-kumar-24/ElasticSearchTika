#!/usr/bin/env python2.7
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

# Computing pairwise jaccard similarity for a given directory of files

from tika import parser
import os, itertools, argparse, csv
import sys
import pdb
import json

def computeScores(inputDir, outCSV):

    with open(outCSV, "wb") as outF:


      a = csv.writer(outF, delimiter=',')
      #a.writerow(["x-coordinate","y-coordinate","Similarity_score"])
      json_data=open(inputDir).read()
      data=json.loads(json_data)
      allLocations = reduce(lambda a, l: a + l, data.values(), [ ])
      #pdb.set_trace()
      totalNumberOfLocations = len(allLocations)
      #files_tuple = itertools.combinations(data.keys(), 1)
      jac={}
      file2=data.keys()[0]
      for file1 in data.keys():
        intersection = set()
        f1MetaData = data[file1]
        f2MetaData = data[file2]
        intersection = set(f1MetaData) & set(f2MetaData)
        union = set(f1MetaData) | set(f2MetaData)
        #isCoExistant = lambda k: ( k in f2MetaData) and ( f1MetaData[k] == f2MetaData[k] )
        #intersection = reduce(lambda m,k: (m + 1) if isCoExistant(k) else m, f1MetaData.keys(), 0)


        #union = len(f1MetaData.keys()) + len(f2MetaData.keys()) - intersection
        

        jaccard = float(len(intersection)+1) / float(len(union) + totalNumberOfLocations)
        #pdb.set_trace()
        jac[file1] = jaccard          
      
      maximum=max(jac.values())
      for file1 in data.keys():

        a.writerow([file1, jac[file1]/maximum,data[file1]])



if __name__ == "__main__":

    argParser = argparse.ArgumentParser('Jaccard similarity based file metadata')
    argParser.add_argument('--input', required=True, help='path to directory containing files')
    argParser.add_argument('--out', required=True, help='path to directory for storing the output CSV File, containing pair-wise Jaccard similarity Scores')
    args = argParser.parse_args()

    if args.input and args.out:
        computeScores(args.input, args.out)
