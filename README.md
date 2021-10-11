# TwitterStream-Firehose
<h2> Data processing pipeline for Twitter </h2>

Python script consume data from Twitter streaming API using Tweepy library

![](AWS2.gif)


The data is then pushed into AWS firehose data delivery stream, Firehose then push data to AWS Opensearch 
Opensearch (Elastic search) is used for log analysis and visualisation of data

<h2> Architecture : </h2>
<img src= "/firehose.png" width = "700">

<h2> Kibana visualisation dashboard</h2>

<img src= "/kibana.png" width = "700">


 




