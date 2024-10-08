# How to Create a Data Subscription
---

{NOTE: }

* A subscription task can be created in two ways:
    * **From the client API**:  
      The client can create a subscription task on the server using this [creation API](../../../client-api/data-subscriptions/creation/api-overview#subscription-creation).
    * **From the Studio**:  
      See [creating subscription task](../../../studio/database/tasks/ongoing-tasks/subscription-task) to learn how to create a subscription task on the server via the Studio.

* Once created, it's definition and progress will be stored on the cluster, and not in a single server.  

* Upon subscription creation, the cluster will choose a preferred node that will run the subscription  
  (unless client has stated a mentor node).  

* From that point and on, clients that will connect to a server in order to consume the subscription will be redirected to the node mentioned above.  

* In this page:  
   * [Subscription creation](../../../client-api/data-subscriptions/creation/how-to-create-data-subscription#subscription-creation)   
   * [Subscription name](../../../client-api/data-subscriptions/creation/how-to-create-data-subscription#subscription-name)  
   * [Responsible node](../../../client-api/data-subscriptions/creation/how-to-create-data-subscription#responsible-node)  

{NOTE/}

---

{PANEL: Subscription creation}

Data subscription is a batch processing mechanism that sends documents that meet specific criteria to connected clients.

In order to create a data subscription, we first need to define the criteria.  
The basic requirement is to specify the collection from which the subscription will retrieve documents.  
However, the criteria can be a complex RQL-like expression defining JavaScript functions that filter documents and project their content.  

* The following is a simple subscription definition:

    {CODE:nodejs create_whole_collection_generic1@client-api\dataSubscriptions\dataSubscriptions.js /}

* For more complex subscription creation scenarios, see the these [examples](../../../client-api/data-subscriptions/creation/examples).

* A subscription also can be modified after it has been created, see [update existing subscription](../../../client-api/data-subscriptions/creation/examples#update-existing-subscription).

{PANEL/}

{PANEL: Subscription name}

In order to consume a data subscription, a subscription name is required to identify it.  
If you don't specify a name when creating the subscription, the server will automatically generate a default name.  
However, you have the option to provide a custom name for the subscription.  

A dedicated name can be useful for use cases like dedicated, long-running batch processing mechanisms,  
where it'll be more comfortable to use a human-readable name in the code and even use the same name between different environments
(as long as subscription creation is taken care of upfront).

{CODE:nodejs create_whole_collection_generic_with_name@client-api\dataSubscriptions\dataSubscriptions.js /}

{INFO: Uniqueness}
Note that subscription name is unique and it will not be possible to create two subscriptions with the same name in the same database.
{INFO/}

{PANEL/}

{PANEL: Responsible node}

As stated above, upon creation, the cluster will choose a node that will be responsible for managing the subscription task on the server-side.
Once chosen, that node will be the only node to manage the subscription.

There is an enterprise license level feature that supports subscription (and any other ongoing task) failover between nodes,
but eventually, as long as the originally assigned node is online, it will be the one to manage the data subscription task.

Nevertheless, there is an option to manually decide which node will be responsible for managing the subscription task.
Provide the tag of the node you wish to be responsible in the `mentorNode` property as follows:

{CODE:nodejs create_whole_collection_generic_with_mentor_node@client-api\dataSubscriptions\dataSubscriptions.js /}

Manually setting the node can help choose a more suitable server based on factors such as resources, client proximity, or other considerations.

{PANEL/}

## Related Articles

**Data Subscriptions**:

- [What are Data Subscriptions](../../../client-api/data-subscriptions/what-are-data-subscriptions)
- [How to Consume a Data Subscription](../../../client-api/data-subscriptions/consumption/how-to-consume-data-subscription)

**Knowledge Base**:

- [JavaScript Engine](../../../server/kb/javascript-engine)
