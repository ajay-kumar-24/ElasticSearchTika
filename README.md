# ElasticSearchTika
To do ElasticSearch on a particular key (sweet, location, date, authors ,related-publications). 

-> python ES.py --metadata key
		-> output will be in output-key.txt

To run Jaccard on the ES data.

-> python jaccard.py --input (input file) --out (output file)


To create the clusters.json file for cluster visualization :

python cluster-scores.py [-t threshold] input-file


Then open clusters-d3.html for visualization


threshold for sweet 				: 0.3 -> No of clusters -> 12
threshold for geo 					: 0.7 -> No of clusters -> 19
threshold for related-publications	: 0.00007 -> No of clusters -> 13
threshold for authors 				: 0.001 -> No of clusters -> 20
threshold for date 					: 0.26 -> No of clusters -> 9
