# Data Subscriptions: Common Data Subscription Creation Examples

---

{NOTE: }

* In this page:  
   * [Create subscription on all documents in a collection](../../../client-api/data-subscriptions/creation/examples#create-subscription-on-all-documents-in-a-collection)  
   * [Create subscription with filtering](../../../client-api/data-subscriptions/creation/examples#create-subscription-with-filtering)  
   * [Create subscription with filtering and projection](../../../client-api/data-subscriptions/creation/examples#create-subscription-with-filtering-and-projection)  
   * [Create subscription with load document in filter projection](../../../client-api/data-subscriptions/creation/examples#create-subscription-with-load-document-in-filter-projection)  
   * [Create subscription with include statement](../../../client-api/data-subscriptions/creation/examples#create-subscription-with-include-statement)  
      * [Including counters](../../../client-api/data-subscriptions/creation/examples#including-counters)  
   * [Update existing subscription](../../../client-api/data-subscriptions/creation/examples#update-existing-subscription)  
{NOTE/}

---

{PANEL:Create subscription on all documents in a collection}

Here we create a plain subscription on the Orders collection, without any constraint or transformation.
{CODE-TABS}
{CODE-TAB:python:Generic-syntax create_whole_collection_generic_with_name@ClientApi\DataSubscriptions\DataSubscriptions.py /}
{CODE-TAB:python:RQL-syntax create_whole_collection_RQL@ClientApi\DataSubscriptions\DataSubscriptions.py /}
{CODE-TABS/}

{PANEL/}

{PANEL:Create subscription with filtering}

Here we create a subscription on the Orders collection, for total order revenues greater than 100.
{CODE:python create_filter_only_RQL@ClientApi\DataSubscriptions\DataSubscriptions.py /}

{PANEL/}

{PANEL:Create subscription with filtering and projection}

Here we create a subscription on the Orders collection, for total order revenues greater than 100,
and return only the ID and total revenue.
{CODE:python create_filter_and_projection_RQL@ClientApi\DataSubscriptions\DataSubscriptions.py /}

{PANEL/}

{PANEL:Create subscription with load document in filter projection}

Here we create a subscription on the Orders collection, for total order revenue greater than 100, 
and return the ID, total revenue, shipping address and responsible employee name.
{CODE:python create_filter_and_load_document_RQL@ClientApi\DataSubscriptions\DataSubscriptions.py /}

{PANEL/}

{PANEL:Create subscription with include statement}

Here we create a subscription on the Orders collection, which returns the orders and brings along 
all products mentioned in the order as included documents.  

{CODE-TABS}
{CODE-TAB:python:Builder-syntax create_subscription_with_includes_strongly_typed@ClientApi\DataSubscriptions\DataSubscriptions.py /}
{CODE-TAB:python:RQL-path-syntax create_subscription_with_includes_rql_path@ClientApi\DataSubscriptions\DataSubscriptions.py /}
{CODE-TAB:python:RQL-javascript-syntax create_subscription_with_includes_rql_javascript@ClientApi\DataSubscriptions\DataSubscriptions.py /}
{CODE-TABS/}

Include statements can be added to a subscription in the raw RQL, or using `SubscriptionIncludeBuilder`.  
The subscription include builder is assigned to the `includes` option of `SubscriptionCreationOptions` 
(see [subscription API overview](../../../client-api/data-subscriptions/creation/api-overview)). 
It supports methods for including documents as well as counters. These methods can be chained.  

In raw RQL, include statements come in two forms, like in any other RQL statements:  

1. Include statement in the end of the query, starting with the `include` keyword, followed by paths to the 
   field containing the IDs of the documents to include.  
   If projection is performed, the mechanism will look for the paths in the projected result, rather then the 
   original document.  
   It is recommended to prefer this approach when possible both because of clarity of the query and slightly 
   better performance.  
2. Include function call inside a 'declared' function.  

## Including Counters

`SubscriptionIncludeBuilder` has three methods for including counters:  

{CODE:python include_builder_counter_methods@ClientApi\DataSubscriptions\DataSubscriptions.py /}

`include_counter` is used to specify a single counter.  
`include_counters` is used to specify multiple counters.  
`include_all_counters` retrieves all counters from all subscribed documents.  

| Parameters | Type | Description |
| - | - | - |
| **name** | `str` | The name of a counter. The subscription will include all counters with this name that are contained in the documents the subscription retrieves. |
| **\*names** | `str` | Array of counter names. |

In the below example we create a subscription that uses all three methods to include counters, demonstrating 
how the methods can be chained (stating the obvious, calling `include_all_counters` makes the other two methods 
redundant).  

{CODE:python create_subscription_include_counters_builder@ClientApi\DataSubscriptions\DataSubscriptions.py /}

{PANEL/}


{PANEL:Update existing subscription}

Here we update the filter query of an existing data subscription named "my subscription".  

{CODE:python update_subscription_example_0@ClientApi\DataSubscriptions\DataSubscriptions.py /}

In addition to names, subscriptions also have a **subscription ID** on the server side. The 
ID can be used to identify the subscription instead of using its name. This allows use to change 
an existing subscription's name by specifying the subscription with the ID, and submitting 
a new string in the `name` field of the `SubscriptionUpdateOptions`.  

{CODE:python update_subscription_example_1@ClientApi\DataSubscriptions\DataSubscriptions.py /}

{PANEL/}

## Related Articles

**Data Subscriptions**:

- [What are Data Subscriptions](../../../client-api/data-subscriptions/what-are-data-subscriptions)
- [How to Create a Data Subscription](../../../client-api/data-subscriptions/creation/how-to-create-data-subscription)
- [How to Consume a Data Subscription](../../../client-api/data-subscriptions/consumption/how-to-consume-data-subscription)

**Knowledge Base**:

- [JavaScript Engine](../../../server/kb/javascript-engine)
