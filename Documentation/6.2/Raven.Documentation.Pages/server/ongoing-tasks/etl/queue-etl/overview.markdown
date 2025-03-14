﻿# Queue ETL Overview
---

{NOTE: }

* Message brokers are high-throughput, distributed messaging services that host data they receive  
  from **producer** applications and serve it to **consumer** clients via FIFO data queues.

* RavenDB can operate as a _Producer_ within this architecture to the following message brokers:
  * **Apache Kafka**
  * **RabbitMQ**
  * **Azure Queue Storage**

* This functionality is achieved by defining [Queue ETL tasks](../../../../server/ongoing-tasks/etl/queue-etl/overview#queue-etl-tasks) within a RavenDB database.

* RavenDB can also function as a _Consumer_.  
  To learn about RavenDB's role as a _Consumer_ please refer to the [Queue Sink section](../../../../server/ongoing-tasks/queue-sink/overview).

* In this page:
    * [Queue ETL tasks](../../../../server/ongoing-tasks/etl/queue-etl/overview#queue-etl-tasks)
    * [Data delivery](../../../../server/ongoing-tasks/etl/queue-etl/overview#data-delivery)
        * [What is transferred](../../../../server/ongoing-tasks/etl/queue-etl/overview#what-is-transferred)
        * [How are messages produced and consumed](../../../../server/ongoing-tasks/etl/queue-etl/overview#how-are-messages-produced-and-consumed)
        * [Idempotence and message duplication](../../../../server/ongoing-tasks/etl/queue-etl/overview#idempotence-and-message-duplication)
    * [CloudEvents](../../../../server/ongoing-tasks/etl/queue-etl/overview#cloudevents)
    * [Task statistics](../../../../server/ongoing-tasks/etl/queue-etl/overview#task-statistics)

{NOTE/}

---

{PANEL: Queue ETL tasks}

RavenDB produces messages to broker queues via the following Queue ETL tasks:

* **Kafka ETL Task**  
  You can define a Kafka ETL Task from [Studio](../../../../studio/database/tasks/ongoing-tasks/kafka-etl-task) 
  or using the [Client API](../../../../server/ongoing-tasks/etl/queue-etl/kafka).  
* **RabbitMQ ETL Task**  
  You can define a RabbitMQ ETL Task from [Studio](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task) 
  or using the [Client API](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq).  
* **Azure Queue Storage ETL Task**  
  You can define an Azure Queue Storage ETL Task from [Studio](../../../../studio/database/tasks/ongoing-tasks/azure-queue-storage-etl) 
  or using the [Client API](../../../../server/ongoing-tasks/etl/queue-etl/azure-queue).  

---

The above ETL tasks:  

* **Extract** selected data from RavenDB documents from specified collections.  
* **Transform** the data to new JSON objects.  
* Wrap the JSON objects as [CloudEvents messages](https://cloudevents.io)  
  and **Load** them to the designated message broker.  

{PANEL/}

{PANEL: Data delivery}

#### What is transferred:

* **Documents only**  
  A Queue ETL task transfers documents only.  
  Document extensions like attachments, counters, or time series, will not be transferred.
* **CloudEvents messages**  
  JSON objects produced by the task's transformation script are wrapped
  and delivered as [CloudEvents Messages](../../../../server/ongoing-tasks/etl/queue-etl/overview#cloudevents).

#### How are messages produced and consumed:

* The Queue ETL task will send the messages it produces to the target using a **connection string**,  
  which specifies the destination and credentials required to authorize the connection.  
  Find the specific syntax for defining a connection string per task in each task's documentation.
* Each message will be added to the tail of its assigned queue according to the transformation script.  
  As earlier messages are processed, it will advance to the head of the queue, becoming available for consumers.
* RavenDB publishes messages to the designated brokers using [transactions and batches](../../../../server/ongoing-tasks/etl/basics#batch-processing),  
  creating a batch of messages and opening a transaction to the destination queue for the batch.

#### Idempotence and message duplication:

* RavenDB is an **idempotent producer**, which typically does not send duplicate messages to queues.
* However, it is possible that duplicate messages will be sent to the broker.   
  For example:    
  Different nodes of a RavenDB cluster are regarded as different producers by the broker.  
  If the node responsible for the ETL task fails while sending a batch of messages,  
  the new responsible node may resend messages that were already received by the broker.
* Therefore, if processing each message only once is important to the consumer,  
  it is **the consumer's responsibility** to verify the uniqueness of each consumed message.

{PANEL/}

{PANEL: CloudEvents}

* After preparing a JSON object that needs to be sent to a message broker,  
  the ETL task wraps it as a CloudEvents message using the [CloudEvents Library](https://cloudevents.io).  

* To do that, the JSON object is provided with additional [required attributes](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#required-attributes),  
  added as headers to the message, including:   

    | Attribute       | Type     | Description                                                                                               | Default Value                                        |
    |-----------------|----------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------|
    | **id**          | `string` | [Event identifier](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#id)                  | The document Change Vector                           |
    | **type**        | `string` | [Event type](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#type)                      | "ravendb.etl.put"                                    |
    | **source**      | `string` | [Event context](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#source-1)               | `<ravendb-node-url>/<database-name>/<etl-task-name>` |

* The optional 'partitionkey' attribute can also be added.  
  Currently, it is only implemented by [Kafka ETL](../../../../server/ongoing-tasks/etl/queue-etl/kafka).  

    | Optional Attribute   | Type       | Description                                                                                                                                  | Default Value    |
    |----------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------|
    | **partitionkey**     | `string`   | [Events relationship/grouping definition](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/partitioning.md#partitionkey) | The document ID  |

{PANEL/}

{PANEL: Task statistics}

Use the Studio [Ongoing tasks stats](../../../../studio/database/stats/ongoing-tasks-stats/overview) view 
to see various statistics related to data extraction, transformation, and loading to the target broker.  

![Queue Brokers Stats](images/overview_stats.png "Ongoing tasks stats view")

{PANEL/}


## Related Articles

### Server

- [ETL Basics](../../../../server/ongoing-tasks/etl/basics)
- [Kafka ETL](../../../../server/ongoing-tasks/etl/queue-etl/kafka)
- [RabbitMQ ETL](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq)
- [Azure Queue Storage ETL](../../../../server/ongoing-tasks/etl/queue-etl/azure-queue)

### Studio

- [Studio: Kafka ETL Task](../../../../studio/database/tasks/ongoing-tasks/kafka-etl-task)
- [Studio: RabbitMQ ETL Task](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task)
- [Studio: Azure Queue Storage ETL Task](../../../../studio/database/tasks/ongoing-tasks/azure-queue-storage-etl)
