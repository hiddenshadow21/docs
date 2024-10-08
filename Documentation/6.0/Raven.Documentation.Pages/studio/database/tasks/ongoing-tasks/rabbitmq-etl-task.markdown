﻿# RabbitMQ ETL Task
---

{NOTE: }

* RavenDB ETL tasks for **RabbitMQ** -  
   * **Extract** selected data from RavenDB documents  
   * **Transform** the data to new JSON objects and add the new objects to CloudEvents messages.  
   * **Load** the messages to a **RabbitMQ exchange**.  
 
* The RabbitMQ exchange enqueues incoming messages at the tail of RabbitMQ queue/s.  
  When the enqueued messages advance to the queue head, RabbitMQ clients can access and consume them.  
 
* RabbitMQ ETL tasks transfer **documents only**.  
  Document extensions like attachments, counters, or time series, are not transferred.  
 
* This page explains how to create a RabbitMQ ETL task using the Studio.  
  [Learn here](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq) how to define a RabbitMQ ETL task using code.  
 
* In this page:  
  * [Open RabbitMQ ETL Task View](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task#open-rabbitmq-etl-task-view)  
  * [Define RabbitMQ ETL Task](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task#define-rabbitmq-etl-task)  
  * [Options Per Exchange](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task#options-per-exchange)  
  * [Edit Transformation Script](../../../../studio/database/tasks/ongoing-tasks/rabbitmq-etl-task#edit-transformation-script)  

{NOTE/}

---

{PANEL: Open RabbitMQ ETL Task View}

![Ongoing Tasks View](images/queue/ongoing-tasks.png "Ongoing Tasks View")

1. **Ongoing Tasks**  
   Click to open the ongoing tasks view.  
2. **Add a Database Task**  
   Click to create a new ongoing task.  

---

![Define ETL Task](images/queue/rabbitmq_task-selection.png "Define ETL Task")

* **RabbitMQ ETL**  
  Click to define a RabbitMQ ETL task.  
   
{PANEL/}

{PANEL: Define RabbitMQ ETL Task}

![Define RabbitMQ ETL Task](images/queue/rabbitmq_etl-define-task.png "Define RabbitMQ ETL Task")

1. **Task Name** (Optional)  
   * Enter a name for your task  
   * If no name is provided, the server will create a name based on the defined connection string,  
     e.g. *Queue ETL to conStr*  

2. **Task State**  
   Select the task state:  
   Enabled - The task runs in the background, transforming and sending documents as defined in this view.  
   Disabled - No documents are transformed and sent.  

3. **Set Preferred Responsible Node** (Optional)  
  * Select a node from the [Database Group](../../../../studio/database/settings/manage-database-group) to be responsible for this task.  
  * If no node is selected, the cluster will assign a responsible node (see [Members Duties](../../../../studio/database/settings/manage-database-group#database-group-topology---members-duties)).  

4. **Skip Automatic Exchange/Queue Declaration**  
   When enabled:  
    * We declare the exchange and queue using the same name.  
    * We bind The exchange and queue using a default (empty) routing key.  
    * The declared exchange's type is **Fanout**.  

5. **Create new RabbitMQ connection String**  
    * Select an existing connection string from the list or create a new one.  
    * The connection string defines the location of the destination RabbitMQ exchange/queue.  
    * **Name** - Enter a name for the connection string.  
    * **Connection String**  
      This is a single string that includes all the options required to connect the 
      RabbitMQ server.  
      E.g. -  `amqp://<username>:<password>@<URL>:<portnumber>`  
      {NOTE: }
       Learn more about RabbitMQ connection strings [here](https://www.rabbitmq.com/uri-spec.html).  
      {NOTE/}

6. **Test Connection**  
   Click after defining the connection string, to test the connection to 
   the RabbitMQ exchange.  

     ![Successful Connection](images/queue/rabbitmq_successful-connection.png "Successful Connection")

{PANEL/}  

{PANEL: Options Per Exchange}

![Click for Advanced Options](images/queue/rabbitmq_click-for-advanced-options.png "Click for Advanced Options")

Clicking the Advanced button will display per-exchange options.  
In it, you'll find the option to delete documents from RavenDB 
while they were processed by the selected queue.  

![Options Per Queue - Delete Processed Documents](images/queue/rabbitmq_options-per-queue.png "Options Per Queue - Delete Processed Documents")

1. **The Exchange**  
   `loadToOrders` is the script instruction to transfer documents to the `Orders` Exchange.  
2. **Add Queue Options**  
   Click to add a per-queue option.  
3. **Queue Name**  
   This is the name of the RabbitMQ exchange the documents are loaded to.  
4. **Delete Processed Documents**  
   Enabling this option will remove from the RavenDB collection documents that 
   were processed and loaded to the RabbitMQ exchange.  
   {WARNING: }
    Enabling this option will **remove processed documents** from the database.  
    The documents will be deleted after the messages are pushed.  
   {WARNING/}

{PANEL/}

{PANEL: Edit Transformation Script}

![Add or Edit Transformation Script](images/queue/add-or-edit-script.png "Add or Edit Transformation Script")

---

![Add or Edit Transform Script](images/queue/rabbitmq_transformation-script.png "Add or Edit Transform Script")

1. **Script Name**  
   Enter a name for the script (Optional).  
   A default name will be generated if no name is entered, e.g. Script_1  

2. **Script**  
   Edit the transformation script.  
   * Define a **document object** whose contents will be extracted from 
     RavenDB documents and sent to the RabbitMQ exchange.  
     E.g., `var orderData` in the above example.  
   * Make sure that one of the properties of the document object 
     is given the value `id(this)`. This property will contain the 
     RavenDB document ID.  
   * Use the `loadTo<ExchangeName>` method to pass the document object 
     to the RabbitMQ destination.  

3. **Syntax**  
   Click for a transformation script Syntax Sample.  

4. **Collections**  
    * **Select (or enter) a collection**  
      Type or select the names of the collections your script is using.  
    * **Collections Selected**  
      A list of collections that were already selected.  

5. **Apply script to documents from beginning of time (Reset)**  
    * When this option is **enabled**:  
      The script will be executed over **all existing documents in the 
      specified collections** the first time the task runs.  
    * When this option is **disabled**:  
      The script will be executed **only over new and modified documents**.  

6. **Add/Update**  
   Click to add a new script or update the task with changes made in an existing script.  

7. **Cancel**  
   Click to cancel your changes.  

8. **Test Script**  
   Click to **test** the transformation script.  

{PANEL/}

## Related Articles

### Server

- [ETL Basics](../../../../server/ongoing-tasks/etl/basics)
- [Queue ETL Overview](../../../../server/ongoing-tasks/etl/queue-etl/overview)
- [Kafka ETL](../../../../server/ongoing-tasks/etl/queue-etl/kafka)
- [RabbitMQ ETL](../../../../server/ongoing-tasks/etl/queue-etl/rabbit-mq)

### Studio

- [Studio: Kafka ETL Task](../../../../studio/database/tasks/ongoing-tasks/kafka-etl-task)
