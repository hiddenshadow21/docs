# Data Subscription Creation Examples
---

{NOTE: }

* This page contains examples of **creating a subscription**.  
  To learn how to consume and process documents sent by the subscription, see these [examples](../../../client-api/data-subscriptions/consumption/examples).  

* For a detailed syntax of the available subscription methods and objects, see this [API overview](../../../client-api/data-subscriptions/creation/api-overview).  

* In this page:  
   * [Create subscription - for all documents in a collection](../../../client-api/data-subscriptions/creation/examples#create-subscription---for-all-documents-in-a-collection)  
   * [Create subscription - filter documents](../../../client-api/data-subscriptions/creation/examples#create-subscription---filter-documents)  
   * [Create subscription - filter and project fields](../../../client-api/data-subscriptions/creation/examples#create-subscription---filter-and-project-fields)  
   * [Create subscription - project data from a related document](../../../client-api/data-subscriptions/creation/examples#create-subscription---project-data-from-a-related-document)  
   * [Create subscription - include documents](../../../client-api/data-subscriptions/creation/examples#create-subscription---include-documents)  
   * [Create subscription - include counters](../../../client-api/data-subscriptions/creation/examples#create-subscription---include-counters)  
   * [Create subscription - subscribe to revisions](../../../client-api/data-subscriptions/creation/examples#create-subscription---subscribe-to-revisions)  
   * [Create subscription - via update](../../../client-api/data-subscriptions/creation/examples#create-subscription---via-update)
   * [Update existing subscription](../../../client-api/data-subscriptions/creation/examples#update-existing-subscription)

{NOTE/}

---

{PANEL: Create subscription - for all documents in a collection}

Here we create a plain subscription on the _Orders_ collection without any constraints or transformations.  
The server will send ALL documents from the _Orders_ collection to a client that connects to this subscription.

{CODE-TABS}
{CODE-TAB:csharp:Generic-syntax create_whole_collection_generic_with_name@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-syntax create_whole_collection_RQL@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

{PANEL/}

{PANEL: Create subscription - filter documents}

Here we create a subscription for documents from the _Orders_ collection where the total order revenue is greater than 100. 
Only documents that match this condition will be sent from the server to a client connected to this subscription.

{CODE-TABS}
{CODE-TAB:csharp:Generic-syntax create_filter_only_generic@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-syntax create_filter_only_RQL@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

{PANEL/}

{PANEL: Create subscription - filter and project fields}

Here, again, we create a subscription for documents from the _Orders_ collection where the total order revenue is greater than 100.
However, this time we only project the document ID and the Total Revenue properties in each object sent to the client.

{CODE-TABS}
{CODE-TAB:csharp:Generic-syntax create_filter_and_projection_generic@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-syntax create_filter_and_projection_RQL@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

{PANEL/}

{PANEL: Create subscription - project data from a related document} 

In this subscription, in addition to projecting the document fields,  
we also project data from a [related document](../../../indexes/indexing-related-documents#what-are-related-documents) that is loaded using the `Load` method.

{CODE-TABS}
{CODE-TAB:csharp:Generic-syntax create_filter_and_load_document_generic@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-syntax create_filter_and_load_document_RQL@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

{PANEL/}

{PANEL: Create subscription - include documents}

Here we create a subscription on the _Orders_ collection, which will send all the _Order_ documents.  

In addition, the related _Product_ documents associated with each Order are **included** in the batch sent to the client. 
This way, when the subscription worker that processes the batch in the client accesses a _Product_ document, no additional call to the server will be made.

See how to consume this type of subscription [here](../../../client-api/data-subscriptions/consumption/examples#subscription-that-uses-included-documents).

{CODE-TABS}
{CODE-TAB:csharp:Builder-syntax create_subscription_with_includes_strongly_typed@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-path-syntax create_subscription_with_includes_rql_path@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-javascript-syntax create_subscription_with_includes_rql_javascript@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

{NOTE: }

**Include using builder**:

Include statements can be added to the subscription with `ISubscriptionIncludeBuilder`.  
This builder is assigned to the  `Includes` property in [SubscriptionCreationOptions&lt;T&gt;](../../../client-api/data-subscriptions/creation/api-overview#subscriptioncreationoptions<t>).  
It supports methods for including documents as well as [counters](../../../client-api/data-subscriptions/creation/examples#create-subscription---include-counters). 
These methods can be chained.

To include related documents, use method `IncludeDocuments`.  
(See the _Builder-syntax_ tab in the example above).

{NOTE/}
{NOTE: }

**Include using RQL**:

The include statements can be written in two ways:  
 
1. Use the `include` keyword at the end of the query, followed by the paths to the fields containing the IDs of the documents to include.
   It is recommended to prefer this approach whenever possible, both for the clarity of the query and for slightly better performance.  
   (See the _RQL-path-syntax_ tab in the example above).

2. Define the `include` within a JavaScript function that is called from the `select` clause.  
   (See the _RQL-javascript-syntax_ tab in the example above).

{NOTE/}

{INFO: }

If you include documents when making a [projection](../../../client-api/data-subscriptions/creation/examples#create-subscription---filter-and-project-fields), 
the include will search for the specified paths in the projected fields rather than in the original document.

{INFO/}
{PANEL/}

{PANEL: Create subscription - include counters}

Here we create a subscription on the _Orders_ collection, which will send all the _Order_ documents.  
In addition, values for the specified counters will be **included** in the batch.

Note:  
Modifying an existing counter's value after the document has been sent to the client does Not trigger re-sending.  
However, adding a new counter to the document or removing an existing one will trigger re-sending the document.  

{CODE-TABS}
{CODE-TAB:csharp:Builder-syntax create_subscription_include_counters_builder@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-syntax create_subscription_include_counters_rql@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

`ISubscriptionIncludeBuilder` has three methods for including counters:  

{CODE:csharp include_builder_counter_methods@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

| Parameter  | Type       | Description                                                                                                                                      |
|------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **name**   | `string`   | The name of a counter. The subscription will include all counters with this name that are contained in the documents the subscription retrieves. |
| **names**  | `string[]` | Array of counter names.                                                                                                                          |

**All include methods can be chained**:  
For example, the following subscription includes multiple counters and documents:

{CODE:csharp create_subscription_include_chained_builder@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

{PANEL/}

{PANEL: Create subscription - subscribe to revisions}

Here we create a simple revisions subscription on the _Orders_ collection that will send pairs of subsequent document revisions to the client.

{CODE-TABS}
{CODE-TAB:csharp:Generic-syntax create_simple_revisions_subscription_generic@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TAB:csharp:RQL-syntax create_simple_revisions_subscription_RQL@ClientApi\DataSubscriptions\DataSubscriptions.cs /}
{CODE-TABS/}

Learn more about subscribing to document revisions in [subscriptions: revisions support](../../../client-api/data-subscriptions/advanced-topics/subscription-with-revisioning).

{PANEL/}

{PANEL: Create subscription - via update}

When attempting to update a subscription that does Not exist,  
you can request a new subscription to be created by setting `CreateNew` to `true`.  
In such a case, a new subscription will be created with the provided query.

{CODE:csharp create_by_update@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

{PANEL/}

{PANEL: Update existing subscription}

**Update subscription by name**:  
The subscription definition can be updated after it has been created.  
In this example we update the filtering **query** of an existing subscription named "my subscription".  

{CODE:csharp update_subscription_example_0@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

---

**Update subscription by id**:  
In addition to the subscription name, each subscription is assigned a subscription ID when it is created by the server.
This ID can be used instead of the name when updating the subscription.  

{CODE:csharp update_subscription_example_1@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

Using the subscription ID allows you to modify the subscription name:

{CODE:csharp update_subscription_example_2@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

{PANEL/}

## Related Articles

**Data Subscriptions**:

- [What are Data Subscriptions](../../../client-api/data-subscriptions/what-are-data-subscriptions)
- [How to Create a Data Subscription](../../../client-api/data-subscriptions/creation/how-to-create-data-subscription)
- [How to Consume a Data Subscription](../../../client-api/data-subscriptions/consumption/how-to-consume-data-subscription)

**Knowledge Base**:

- [JavaScript Engine](../../../server/kb/javascript-engine)
