import elasticsearch
import sys
import json
import argparse

def find_metadata(key):
	end=9320
	entries={}
	if(key == 'location'):
		key = 'geo'
	if(key == 'date'):
		key = 'DATE'
	for x in range(0,end,10):
		es = elasticsearch.Elasticsearch('http://104.236.190.155:9200')
		data=es.search(index="polar", doc_type='application-pdf', size="10", body={
		"from": x
		})
		loc=data['hits']['hits']
		for obj in loc:
			l = []
			id  = obj['_id']
			print id
			value='name'
			flag = 0
			if key == 'geo':
				if(key in obj['_source']):
					metadata = obj['_source'][key]
					flag=flag+1
			if (key == 'sweet' or key == 'DATE'):
				if(key in obj['_source']['entities']):
					metadata = obj['_source']['entities'][key]
					flag=flag+1
			if (key == 'authors'):
				if(key in obj['_source']['journal']):
					metadata = obj['_source']['journal'][key]
					flag=flag+1
			if(key== 'related-publications'):
				if(key in obj['_source']['journal']):
					metadata = obj['_source']['journal'][key]
					flag=flag+1
					value='URL'
			if flag != 0:
				for entity in metadata:
					l = l + [entity[value]]			
					entries[id] = l

	file1= 'output-'+key+'.txt'
	out = open(file1,'w+')
	out.write(json.dumps(entries))
if __name__ == "__main__":

    argParser = argparse.ArgumentParser('Jaccard similarity based file metadata')
    argParser.add_argument('--metadata', required=True, help='path to directory containing files')
    args = argParser.parse_args()

    if args.metadata:
        find_metadata(args.metadata)
	