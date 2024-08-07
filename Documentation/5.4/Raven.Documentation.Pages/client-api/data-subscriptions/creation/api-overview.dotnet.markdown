# Data Subscriptions: Creation and Update API Overview

---

{NOTE: }

* In this page:  
   * [Subscription Creation](../../../client-api/data-subscriptions/creation/api-overview#subscription-creation)  
   * [SubscriptionCreationOptions](../../../client-api/data-subscriptions/creation/api-overview#subscriptioncreationoptions)  
   * [SubscriptionCreationOptions&lt;T&gt;](../../../client-api/data-subscriptions/creation/api-overview#subscriptioncreationoptions<t>)  
   * [Update Subscription](../../../client-api/data-subscriptions/creation/api-overview#update-subscription)  
   * [SubscriptionUpdateOptions](../../../client-api/data-subscriptions/creation/api-overview#subscriptionupdateoptions)  
   * [Subscription query](../../../client-api/data-subscriptions/creation/api-overview#subscription-query)  

{NOTE/}

---

{PANEL:Subscription Creation}

Subscription creation is accessible through `DocumentStore`'s `Subscriptions` Property, of type `DocumentSubscriptions`:
{CODE subscriptionCreationOverloads@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

 | Parameter | Type | Description |
 | ------------- | ------------- | ----- |
| **predicate** | `Expression<Func<T, bool>>` | Predicate that returns a boolean, describing filter of the subscription documents |
| **options** | `SubscriptionCreationOptions<T>` | Contains subscription creation options |
| **database** | `string` | Name of database to create a data subscription. If `null`, default database configured in DocumentStore will be used. |
| **token** | `CancellationToken` | Cancellation token used in order to halt the subscription creation process. |

| Return value | Description |
| ------------- | ----- |
| `string` | Created data subscription name. If Name was provided in SubscriptionCreationOptions, it will be returned, otherwise, a unique name will be generated by server. |

{PANEL/}

{PANEL:SubscriptionCreationOptions}

Non generic version of the class, relies on user's full knowledge of the RQL query structure

| Member | Type | Description |
|--------|:-----|-------------| 
| **Name** | `string` | User defined name of the subscription: allows to have a human readable identification of a subscription. The name must be unique in the database. |
| **Query** | `string` | **Required.** RQL query that describes the subscription. That RQL comes with additional support to JavaScript clause inside the 'Where' statement and special semantics for subscriptions on documents revisions. |
| **ChangeVector** | `string` | Allows to define a change vector, from which the subscription will start processing. It might be useful for ad-hoc processes that need to process only recent changes in data, for that specific use, the field may receive a special value: "LastDocument", that will take the latest change vector in the machine. |
| **MentorNode** | `string` | Allows to define a specific node in the cluster that we want to treat the subscription. That's useful in cases when one server is preffered over other, either because of stronger hardware or closer geographic proximity to clients etc. |

{PANEL/}

{PANEL:SubscriptionCreationOptions&lt;T&gt;}

An RQL statement will be built based on the fields.

{CODE sub_create_options_strong@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

| Member | Type | Description |
|--------|:-----|-------------| 
| **&lt;T&gt;** | type | Type of the object, from which the collection will be derived. |
| **Name** | `string` | User defined name of the subscription: allows to have a human readable identification of a subscription. The name must be unique in the database. |
| **Filter** | `Expression<Func<T, bool>>` | Lambda describing filter logic for the subscription. Will be translated to a JavaScript function. |
| **Projection** | `Expression<Func<T, object>>` | Lambda describing the projection of returned documents. Will be translated to a JavaScript function. |
| **Includes** | `Action<ISubscriptionIncludeBuilder<T>>` | Action with an [ISubscriptionIncludeBuilder](../../../client-api/data-subscriptions/creation/examples#create-subscription-with-include-statement) parameter that allows you to define an include clause for the subscription. Methods can be chained to include documents as well as [counters](../../../client-api/data-subscriptions/creation/examples#including-counters). |
| **ChangeVector** | `string` | Allows to define a change vector, from which the subscription will start processing. It might be useful for ad-hoc processes that need to process only recent changes in data, for that specific use, the field may receive a special value: "LastDocument", that will take the latest change vector in the machine. |
| **MentorNode** | `string` | Allows to define a specific node in the cluster that we want to treat the subscription. That's useful in cases when one server is preffered over other, either because of stronger hardware or closer geographic proximity to clients etc. |

{PANEL/}

{PANEL: Update Subscription}

Modifies an existing data subscription. These methods are accessible at `DocumentStore.Subscriptions`.  

{CODE updating_subscription@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

| Parameter | Type | Description |
| - | - | - |
| **options** | `SubscriptionUpdateOptions` | A subscription update options object |
| **database** | `string` | Name of database to create a data subscription. If `null`, default database configured in DocumentStore will be used. |
| **token** | `CancellationToken` | Cancellation token used in order to halt the updating process. |

| Return value | Description |
| ------------- | ----- |
| `string` | The updated data subscription's name. |

{PANEL/}

{PANEL: SubscriptionUpdateOptions}

Inherits from `SubscriptionCreationOptions` and has all the same fields (see [above](../../../client-api/data-subscriptions/creation/api-overview#subscriptioncreationoptions)) plus the two additional fields described below:  

{CODE sub_update_options@ClientApi\DataSubscriptions\DataSubscriptions.cs /}

| Parameter | Type | Description |
| - | - | - |
| **Id** | `long?` | Unique server-side ID of the data subscription, see description of the [subscription state object](../../../client-api/data-subscriptions/advanced-topics/maintenance-operations#getting-subscription-status). `Id` can be used instead of the subscription update options `Name` field, and takes precedence over it. This allows you to change the subscription's name: submit a subscription's ID, and submit a different name in the `Name` field. |
| **CreateNew** | `bool` | If set to `true`, and the specified subscription does not exist, the subscription is created. If set to `false`, and the specified subscription does not exist, an exception is thrown. |

{PANEL/}

{PANEL: Subscription query} 

All subscriptions, are eventually translated to an RQL-like statement. These statements has four parts:

* Functions definition part, like in ordinary RQL. Those functions can contain any JavaScript code,
  and also supports `load` and `include` operations.

* From statement, defining the documents source, ex: `from Orders`. The from statement can only address collections, therefore, indexes are not supported.    

* Where statement describing the criteria according to which it will be decided to either 
send the documents to the worker or not. Those statements supports either RQL like `equality` operations (`=`, `==`) ,  
plain JavaScript expressions or declared function calls, allowing to perform complex filtering logic.  
The subscriptions RQL does not support any of the known RQL searching keywords.

* Select statement, that defines the projection to be performed. 
The select statements can contain function calls, allowing complex transformations.

* Include statement allowing to define include path in document.  

{INFO: Keywords}
Although subscription's query syntax has an RQL-like structure, it supports only the `declare`, `select` and `where` keywords, usage of all other RQL keywords is not supported.  
Usage of JavaScript ES5 syntax is supported.
{INFO/}

{INFO: Paths}
Paths in subscriptions RQL statements are treated as JavaScript indirections and not like regular RQL paths.  
It means that a query that in RQL would look like:  

```
from Orders as o
where o.Lines[].Product = "products/1-A"
```

Will look like that in subscriptions RQL:

```
declare function filterLines(doc, productId)
{
    if (!!doc.Lines){
        return doc.Lines.filter(x=>x.Product == productId).length >0;
    }
    return false;
}

from Orders as o
where filterLines(o, "products/1-A")
```
{INFO/}  

{INFO: Revisions}
In order to define a data subscription that uses documents revisions, there first has to be revisions configured for the specific collection.  
The subscription should be defined in a special way:  
* In case of the generic API, the `SubscriptionCreationOptions<>` generic parameter should be of the generic type `Revision<>`, while it's generic parameter correlates to the collection to be processed.  Ex: `new SubscriptionCreationOptions<Revision<Order>>()`  
* For RQL syntax, the `(Revisions = true)` statement should be concatenated to the collection to be queries.  Ex: `From orders(Revisions = true) as o`

{INFO/}
  
{PANEL/}

## Related Articles

**Data Subscriptions**:  

- [What are Data Subscriptions](../../../client-api/data-subscriptions/what-are-data-subscriptions)
- [How to Create a Data Subscription](../../../client-api/data-subscriptions/creation/how-to-create-data-subscription)
- [How to Consume a Data Subscription](../../../client-api/data-subscriptions/consumption/how-to-consume-data-subscription)

**Knowledge Base**:

- [JavaScript Engine](../../../server/kb/javascript-engine)


