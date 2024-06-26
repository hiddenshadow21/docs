﻿# Include Compare Exchange Values
---

{NOTE: }

* Compare-Exchange items can be included when [loading entities](../../../client-api/session/loading-entities) 
  and when making [queries](../../../client-api/session/querying/how-to-query).

* The Session [tracks](../../../client-api/session/what-is-a-session-and-how-does-it-work#tracking-changes) 
  the included Compare Exchange items which means their value can be accessed  
  in that Session without making an additional call to the server.

* The Compare Exchange include syntax is based on the [include method](../../../client-api/how-to/handle-document-relationships#includes).  

* In this page:  
  * [Syntax](../../../client-api/operations/compare-exchange/include-compare-exchange#syntax)  
  * [Examples](../../../client-api/operations/compare-exchange/include-compare-exchange#examples)  

{NOTE/}

---

{PANEL: Syntax}

#### Include method

Chain the method `IncludeCompareExchangeValue()` to include compare exchange values 
along with `Session.Load()` or LINQ queries.  

{CODE:csharp include_builder@ClientApi/Operations/CompareExchange/CompareExchange.cs /}

| Parameter | Type | Description |
| - | - | - |
| **path** | `string`;<br/>`Expression<Func<T, string>>`;<br/>`Expression<Func<T, IEnumerable<string>>>` | The key of the compare exchange value you want to include, a path to the key, or a path to a `string[]` of keys. |

#### RQL

In an RQL query, you can use the [`include` keyword](../../../client-api/session/querying/what-is-rql#include) 
followed by `cmpxchg()` to include a compare exchange value:  

{CODE-BLOCK:sql }
include cmpxchg(key)
{CODE-BLOCK/}

In [javascript functions](../../../client-api/session/querying/what-is-rql#declare) within queries, 
use `includes.cmpxchg()` (see the RawQuery example 
[below](../../../client-api/operations/compare-exchange/include-compare-exchange#examples)):  

{CODE-BLOCK:javascript }
includes.cmpxchg(key);
{CODE-BLOCK/}

| Parameter | Type | Description |
| - | - | - |
| **key** | `string`;<br/>path to `string` | The key of the compare exchange value you want to include, or a path to the key. |

{PANEL/}

{PANEL: Examples}

{CODE-TABS}
{CODE-TAB:csharp:Load include_load@ClientApi/Operations/CompareExchange/CompareExchange.cs /}
{CODE-TAB:csharp:LoadAsync include_load_async@ClientApi/Operations/CompareExchange/CompareExchange.cs /}
{CODE-TAB:csharp:Query include_linq_query@ClientApi/Operations/CompareExchange/CompareExchange.cs /}
{CODE-TAB:csharp:RawQuery(RQL) include_raw_query@ClientApi/Operations/CompareExchange/CompareExchange.cs /}
{CODE-TABS/}

{PANEL/}

## Related Articles

### Client API

- [Session Change Tracking](../../../client-api/session/what-is-a-session-and-how-does-it-work#tracking-changes)
- [How to: Handle Document Relationships](../../../client-api/how-to/handle-document-relationships)
- [Compare Exchange Overview](../../../client-api/operations/compare-exchange/overview)

### Indexes

- [Indexing Compare Exchange Values](../../../indexes/indexing-compare-exchange-values)
