# TwitterstreamFirehose
Data processing pipeline for Twitter 

Python script consume data from Twitter streaming API using Tweepy library
The data is then pushed into AWS firehose data delivery stream, using firehose API (Put_record, put_record_batch)
Firehose can be used to load streaming data into data lakes, data stores (Amazon S3, Amazon Redshift, Amazon OpenSearch Service (Elasticsearch)
With new updates in firhose, we can now directly send data to AWS Opensearch instead of using s3 and lambda, and s3 also can be used to load raw data or failed data logs
Elastic search is used for log analytics, full-text search, security intelligence, business analytics and Kibana is used for visualising





