﻿# Queue ETL: RabbitMQ
---

{NOTE: }

* **RabbitMQ** exchanges are designed to disperse data to multiple queues, 
  making for a flexible data channeling system that can easily handle complex 
  message streaming scenarios.  

* RabbitMQ's ETL support allows RavenDB to take the role of a producer 
  in a RabbitMQ architecture.  

* You can create a RavenDB RabbitMQ ETL task to Extract data from the 
  database, Transform it by your custom script, and Load the resulting 
  JSON object to a RabbitMQ exchange as a CloudEvents message.  

* In this page:  
  * [Transformation Script](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#transformation-script)  
     * [Alternative Syntaxes](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#alternative-syntaxes)  
  * [Data Delivery](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#data-delivery)  
     * [What is Transferred](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#what-is-transferred)  
     * [How Are Messages Produced and Consumed](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#how-are-messages-produced-and-consumed)  
     * [Message Duplication](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#message-duplication)  
  * [Client API](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#client-api)  
     * [Add a RabbitMQ Connection String](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#add-a-rabbitmq-connection-string)  
     * [Add a RabbitMQ ETL Task](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#add-a-rabbitmq-etl-task)  
     * [Delete Processed Documents](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#delete-processed-documents)  
{NOTE/}

---

{PANEL: Transformation Script}

The [basic characteristics](../../../../server/ongoing-tasks/etl/basics) of a RabbitMQ ETL script 
are similar to those of the other ETL types.  
The script defines what data to **Extract** from the database, how to **Transform** this data, and 
which queue/s to **Load** it to.  

To load the data to RabbitMQ, use the [loadTo\\<Exchange\\>](../../../../server/ongoing-tasks/etl/basics#transform) 
command as follows:  
`loadTo<Exchange>(obj, routingKey, {attributes})`  

* **Exchange**:  
  The RabbitMQ exchange name  
* **obj**:  
  The object to transfer  
* **routingKey**:  
  A message attribute that the exchange checks when it decides how to route the 
  message to queues (depending on the exchange type)  
* **attributes**:  
  [Optional attributes](../../../../server/ongoing-tasks/etl/queue-etl/overview#cloudevents)  

For example:  

{CODE-BLOCK: JavaScript}
// Create an OrderData JSON object
var orderData = {
    Id: id(this), 
    OrderLinesCount: this.Lines.length,
    TotalCost: 0
};

// Update orderData's TotalCost field
for (var i = 0; i < this.Lines.length; i++) {
    var line = this.Lines[i];
    var cost = (line.Quantity * line.PricePerUnit) * ( 1 - line.Discount);
    orderData.TotalCost += cost;
}

// Exchange name: Orders
// Loaded object name: orderData
// Routing key: users 
// Attributes: Id, PartitionKey, Type, Source
loadToOrders(orderData, `users`, {  
    Id: id(this),
    Type: 'special-promotion',
    Source: '/promotion-campaigns/summer-sale'
});
{CODE-BLOCK/}

---

### Alternative Syntaxes

Alternative supported syntaxes include:  

* The exchange name can be provided separately, as a string:  
  `loadTo('exchange-name', obj, 'routing-key', { attributes })`  
  E.g. -  `loadTo('Orders', orderData, 'users')`
  
    Using this syntax, you can replace the exchange name with 
    an **empty string**, as in: `loadTo('', orderData, 'users')`  
    When an empty string is sent this way the message is pushed 
    directly to queues, using a default exchange (pre-defined 
    by the broker).  
    In the above example, `loadTo('', orderData, 'users')`, the 
    message is pushed directly to the `users` queue.  

* The routing key can be omitted, as in: `loadToOrders(orderData)`  
  In the lack of a routing key messages delivery will depend 
  upon the type of exchange you use.  

* Additional attributes (like the Cloudevents-specific `Id`, 
  `Type`, and `Source` attributes) can be omitted.  

{PANEL/}


{PANEL: Data Delivery}

#### What is Transferred

* **Only Documents**  
  A RabbitMQ ETL task transfers **documents only**.  
  Document extensions like attachments, counters, or time series, will not be transferred.  

* **As JSON Messages**  
  JSON objects produced by the task's transformation script are wrapped 
  and delivered as [CloudEvents Messages](../../../../server/ongoing-tasks/etl/queue-etl/overview#cloudevents).  

---

#### How Are Messages Produced and Consumed  

The ETL task will use the address provided in your 
[connection string](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#add-a-rabbitmq-connection-string), 
and send the JSON messages it produces to a RabbitMQ **exchange**.  

Each message will then be pushed to the tail of the queue assigned to it in the transformation script, 
advance in the queue as preceding messages are pulled, and finally reach the queue's head and become 
available for consumers.  

{INFO: }
RavenDB publishes messages to RabbitMQ using **transactions and batches**, 
creating a batch of messages and opening a transaction to the exchange for the batch.  
{INFO/}

{NOTE: }
Read more about RabbitMQ in the platform's [official documentation](https://www.rabbitmq.com/) 
or a variety of other sources.  
{NOTE/}

---

#### Message Duplication

It **is** possible that duplicate messages will be sent to the exchange.  

If, for example, the RavenDB node responsible for the ETL task fails while 
sending messages, the new responsible node may resend some of the messages 
that were already enqueued.  

It is therefore **the consumer's own responsibility** (if processing each 
message only once is important to it) to verify the uniqueness of each consumed 
message.  

{PANEL/}

{PANEL: Client API}

This section explains how to create a RabbitMQ ETL task using code.  
[Learn here](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task) 
how to define a RabbitMQ ETL task using Studio.  

---

#### Add a RabbitMQ Connection String

Prior to defining an ETL task, add a **connection string** that the task 
will use to connect RabbitMQ.  

To create the connection string:  

* Prepare a `QueueConnectionString`object with the connection string configuration.  
* Pass this object to the `PutConnectionStringOperation` store operation to add the connection string.  

**Code Sample**:  
{CODE add_rabbitMQ_connection-string@Server\OngoingTasks\ETL\Queue\Queue.cs /}

* `QueueConnectionString`:  
  {CODE QueueConnectionString@Server\OngoingTasks\ETL\Queue\Queue.cs /}
  `QueueBrokerType`:  
  {CODE QueueBrokerType@Server\OngoingTasks\ETL\Queue\Queue.cs /}

    | Property | Type | Description |
    |:-------------|:-------------|:-------------|
    | **Name** | `string` | Connection string name |
    | **BrokerType** | `QueueBrokerType` | Set to `QueueBrokerType.RabbitMq` for a Kafka connection string |
    | **RabbitMqConnectionSettings** | `RabbitMqConnectionSettings` | A single string that specifies the RabbitMQ exchange connection details |

---

#### Add a RabbitMQ ETL Task

To create the ETL task:  

* Prepare a `QueueEtlConfiguration`object with the ETL task configuration.  
* Pass this object to the `AddEtlOperation` store operation to add the ETL task.  

**Code Sample**:  
{CODE add_rabbitmq_etl-task@Server\OngoingTasks\ETL\Queue\Queue.cs /}

* `QueueEtlConfiguration`:  

    | Property | Type | Description |
    |:-------------|:-------------|:-------------|
    | **Name** | `string` | The ETL task name |
    | **ConnectionStringName** | `string` | The registered connection string name |
    | **Transforms** | `List<Transformation>[]` | You transformation script |
    | **Queues** | `List<EtlQueue>` | Optional actions to take when a document is processed, see [Delete Processed Documents](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq#delete-processed-documents) below.  |
    | **BrokerType** | `QueueBrokerType` | Set to `QueueBrokerType.RabbitMq` to define a RabbitMQ ETL task |
    | **SkipAutomaticQueueDeclaration** | `bool` | Set to `true` to skip automatic queue declaration <br> Use this option when you prefer to define Exchanges, Queues & Bindings manually. |

{INFO: }
By default we define exchanges on our own with **Fanout** type so the routing keys are ignored.
{INFO/}

---

### Delete Processed Documents

You can include an optional `EtlQueue` property in the ETL configuration to 
trigger additional actions.  
An action that you can trigger this way, is the **deletion of RavenDB documents** 
once they've been processed by the ETL task.  

`EtlQueue`
{CODE EtlQueueDefinition@Server\OngoingTasks\ETL\Queue\Queue.cs /}

| Property | Type | Description |
|:-------------|:-------------|:-------------|
| **Name** | `string` | Queue name |
| **DeleteProcessedDocuments** | `bool` | if `true`, delete processed documents from RavenDB |

**Code Sample**:  
{CODE rabbitmq_EtlQueue@Server\OngoingTasks\ETL\Queue\Queue.cs /}

{PANEL/}

## Related Articles

### Server

- [ETL Basics](../../../../server/ongoing-tasks/etl/basics)
- [Queue ETL Overview](../../../../server/ongoing-tasks/etl/queue-etl/overview)
- [Kafka ETL](../../../../server/ongoing-tasks/etl/queue-etl/kafka)

### Studio

- [Studio: RabbitMQ ETL Task](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task)
- [Studio: Kafka ETL Task](../../../../studio/database/tasks/ongoing-tasks/kafka-etl-task)
