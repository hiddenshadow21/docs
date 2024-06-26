# Fuzzy Search

Fuzzy search is supported via `fuzzy` method.  
This method is available only from [DocumentQuery](../../../../client-api/session/querying/document-query/what-is-document-query) level and can only be performed on single term values.  
Because of that it can be used only right after `whereEquals` method.

## Syntax

{CODE:java fuzzy_1@ClientApi\Session\Querying\TextSearch\FuzzySearch.java /}

| Parameters | | |
| ------------- | ------------- | ----- |
| **fuzzy** | `double` | Value between 0.0 and 1.0 where 1.0 means closer match. |

## Example

{CODE-TABS}
{CODE-TAB:java:Java fuzzy_2@ClientApi\Session\Querying\TextSearch\FuzzySearch.java /}
{CODE-TAB-BLOCK:sql:RQL}
from Companies
where fuzzy(Name = 'Ernts Hnadel', 0.5)
{CODE-TAB-BLOCK/}
{CODE-TABS/}

## Related Articles

### Session

- [Querying: Basics](../../../../indexes/querying/query-index)
- [Full-text search](../../../../client-api/session/querying/text-search/full-text-search)
