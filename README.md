# TwitterstreamFirehose 
<h2> Data processing pipeline for Twitter </h2>

![](AWS2.gif)

<img src= "image/arch.png" width= "600">


Python script consume data from Twitter streaming API using Tweepy library

The data is then pushed into AWS firehose data delivery stream, Firehose then push data to AWS Opensearch 
Opensearch (Elastic search) is used for log analysis and visualisation of data

<h2> Architecture : </h2>




