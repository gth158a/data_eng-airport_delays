# Airport Delays
Data Engineering project using U.S. Department of Transportation Federal Aviation Administration delays API.

The live site is located at:
[Delay.io](http://best-first-flask.us-west-1.elasticbeanstalk.com/)

## Architecture

![Data Pipeline][architecture]

[architecture]: /images/architecture.png "Data Pipeline"

# Dataset

I will be working with delay information from the <u>top 20 busiest US airports</u> according to **"Calendar Year 2015 Revenue Enplanements at Commercial Service Airports" (PDF). Federal Aviation Administration.**

| Rank | Name   | IATA code | City Served | 2015 |
|------|---------------|-----------|------|-------|
| 1	   |Hartsfield–Jackson Atlanta International Airport|	ATL	| Atlanta	GA |	49,340,732 |
|2	| Los Angeles International Airport|	LAX	|Los Angeles	CA	|36,351,226	|
|3	|O'Hare International Airport |	ORD	| Chicago	IL	| 36,305,668 |		
|4	| Dallas/Fort Worth International Airport |	DFW	| Dallas/Fort Worth	TX |	31,589,832 |		
|5	|John F. Kennedy International Airport |	JFK |	New York	NY |	27,717,503		|
|6	|Denver International Airport |	DEN	 | Denver	CO	| 26,280,043		|
|7	|San Francisco International Airport |	SFO |	San Francisco	CA |	24,190,549		|
|8	|Charlotte Douglas International Airport |	CLT	| Charlotte	NC |	21,913,156		|
|9	|McCarran International Airport |	LAS	| Las Vegas	NV |	21,824,231		|
|10|	Phoenix Sky Harbor International Airport	| PHX	| Phoenix	AZ	| 21,351,445		|
|11|	Miami International Airport |	MIA	| Miami	FL	| 20,986,341		|
|12|	George Bush Intercontinental Airport |	IAH	 | Houston	TX	 | 20,595,874		|
|13|	Seattle–Tacoma International Airport |	SEA	| Seattle/Tacoma	WA |	20,148,980		|
|14|	Orlando International Airport |	MCO	| Orlando	FL	| 18,759,938		|
|15|	Newark Liberty International Airport |	EWR |	Newark/New York	NJ |	18,684,765		|
|16|	Minneapolis–Saint Paul International Airport |	MSP	| Minneapolis/St. Paul	MN |	17,634,252		|
|17|	Logan International Airport	| BOS	| Boston	MA	| 16,290,323		|
|18|	Detroit Metropolitan Airport |	DTW	| Detroit	MI | 16,255,507		|
|19|	Philadelphia International Airport | PHL	| Philadelphia	PA |	15,101,318		|
|20|	LaGuardia Airport |	LGA	 | New York	NY	| 14,319,924 |

## Objective

[architecture]: /images/architecture.png "Data Pipeline"

The objective of the project is to collect historical information about airport delays and present two views of the data:
+ real time map with delays,
+ and a link from each airport to their historical information

## Project Structure:
The content of the project is broken down in the following sections:

+ [Data Stream](/notebooks/Data_Stream.ipynb)
: A way to continuously query data from a website or API (at least one, but preferably two sources of data)
+ Storage: Storage for all unstructured data in its entirety
+ Structured Data: Separate storage for structured data in 3NF (similar to how we stored raw tweets in s3 and structured tables in postgres)
+ Data Transformations: Some sort of batch process/transformation with Spark
+ Front-end: A way to communicate the results of your pipeline such as a static website or flask app

## 8 Desired properties of a big data system

| Property | System have it? | How could it be improved |
|:---------|-----------------|-------------------------:|
|**Robustness and fault tolerance** |Data is captured from FAA site with EC2 instance. The requirements for the streaming machine are listed in reequirements.txt and the python script querying the source is in the same repo. If the number of records in S3 is less than 4 email is sent. | This property can be improved with the use of amazon's cloudwatch service by monitoring the status of the EC2 instances and automating deployment of second instance if one fails.|
|**Low latency reads and updates**| Yes. Using lambda architecture. Hourly batch jobs will be scheduled and the readings for the current hour will be processed with spark Streaming. | Reducing the window for streaming from 1 hour to 30 minutes. |
|**Scalability **| Yes. The system currently collects data for 20 airports but the pipeline could expand horizontally by the addition of airports without too much hesitation. | This can be improved by having ec2 instances for distinct geographic areas. |
| **Generalization**| Yes. The system is general enough that could be used for a different purpose and each of the pieces could be upgraded at any time. | |
| **Extensibility** | Yes. The initial idea is to have dealy and weather data but adding news and tweets relevant to the airport city is possible.|  |
| **Ad hoc queries**| Yes. I will use PySpark to query PostgreSQL database for aggregation charts and Streaming but real-time updates | A predictive model could be used to predict the delay outlook for each of the airports.|
| **Minimal maintenance** | Yes. In the case that the predictive models are deployed, then most of the maintenance will revolve around updating training on a daily basis which could be scripted and scheduled with airflow. | |
| **Debuggability** | Yes. Errors during data collection are stored independently for further analysis. | I have not Implemented a tool to keep the pulse of each of the components. Nonetheless, Amazon's Cloudwatch seems to help monitoring status and logging issues. |
