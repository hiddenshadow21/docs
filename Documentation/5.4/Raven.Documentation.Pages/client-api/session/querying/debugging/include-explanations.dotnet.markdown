# Include Query Explanations

---

{NOTE: }

* When making a query, each document in the query results is assigned a **score**.  
  This score determines the order by which the documents come back in the results when requesting   
  to [order by score](../../../../client-api/session/querying/sort-query-results#order-by-score).

* Each document in the results includes this score under the `@index-score` property in its metadata.

* **To get the score details** and see how it was calculated,  
  you can use `IncludeExplanations` when querying with a [DocumentQuery](../../../../client-api/session/querying/document-query/what-is-document-query). 

* In this page:
    * [Include explanations in a query](../../../../client-api/session/querying/debugging/include-explanations#include-explanations-in-a-query)  
    * [View explanations](../../../../client-api/session/querying/debugging/include-explanations#view-explanations)  
    * [Syntax](../../../../client-api/session/querying/debugging/include-explanations#syntax)  
{NOTE/}

---

{PANEL: Include explanations in a query}

{CODE-TABS}
{CODE-TAB:csharp:DocumentQuery explain@ClientApi\Session\Querying\Debugging\IncludeExplanations.cs /}
{CODE-TAB:csharp:DocumentQuery_async explain_async@ClientApi\Session\Querying\Debugging\IncludeExplanations.cs /}
{CODE-TAB-BLOCK:sql:RQL}
from "Products"
where search(Name, "Syrup") or search(Name, "Lager")
include explanations()
{CODE-TAB-BLOCK/}
{CODE-TABS/}

{PANEL/}

{PANEL: View explanations}

* The detailed explanations can be viewed from the **Query view** in Studio.  

* Running a query with `include explanations()` will show an additional **Explanations Tab**.

![Figure 1. Explanations in the Studio](images/include-explanations-1.png "Include explanations")

* Sample score details:

![Figure 2. View explanations](images/include-explanations-2.png "View explanation")

{PANEL/}

{PANEL: Syntax}

{CODE syntax@ClientApi\Session\Querying\Debugging\IncludeExplanations.cs /}

| Parameters | Data type | Description |
| - | - | - |
| **explanations** | `Explanations` | An _out_ param that will be filled with the explanations results |

| `Explanations` | |
| - | - |
| `string[] GetExplanations(string docId)` | <ul><li>Pass the resulting document ID for which to get score details.</li><li>Returns a list with all explanations.</li></ul> |

{PANEL/}
