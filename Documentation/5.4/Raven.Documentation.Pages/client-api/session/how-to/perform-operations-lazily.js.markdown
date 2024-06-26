# Perform requests lazily
---

{NOTE: }

* __Lazy request__:

    * You can define a lazy request within a session (e.g. a lazy-query or a lazy-load request)  
      and defer its execution until actually needed.

    * The lazy request definition is stored in the session and a `Lazy` instance is returned.  
      The request will be sent to the server and executed only when you access the value of this instance.

* __Multiple lazy requests__:

    * Multiple lazy requests can be defined within the same session.

    * When triggering the deferred execution (whether implicitly or explicitly),  
      ALL pending lazy requests held up by the session will be sent to the server in a single call.  
      This can help reduce the number of remote calls made to the server over the network.

* In this page:
    * [Requests that can be executed lazily:](../../../client-api/session/how-to/perform-operations-lazily#requests-that-can-be-executed-lazily)
        * [Load entities](../../../client-api/session/how-to/perform-operations-lazily#loadEntities)
        * [Load entities with include](../../../client-api/session/how-to/perform-operations-lazily#loadWithInclude)
        * [Load entities starting with](../../../client-api/session/how-to/perform-operations-lazily#loadStartingWith)
        * [Conditional load](../../../client-api/session/how-to/perform-operations-lazily#conditionalLoad)
        * [Run query](../../../client-api/session/how-to/perform-operations-lazily#runQuery)
        * [Get revisions](../../../client-api/session/how-to/perform-operations-lazily#getRevisions)
        * [Get compare-exchange value](../../../client-api/session/how-to/perform-operations-lazily#getCompareExchange)
    * [Multiple lazy requests](../../../client-api/session/how-to/perform-operations-lazily#multiple-lazy-requests)
        * [Execute all requests - implicitly](../../../client-api/session/how-to/perform-operations-lazily#implicit)
        * [Execute all requests - explicitly](../../../client-api/session/how-to/perform-operations-lazily#explicit)

{NOTE/}

---

{PANEL: Operations that can be executed lazily}

{NOTE: }
<a id="loadEntities" /> __Load entities__

* ['load'](../../../client-api/session/loading-entities#load) loads a document entity from the database into the session.  
  Loading entities can be executed __lazily__.   

{CODE:nodejs lazy_load@client-api\Session\HowTo\lazy.js /}
{NOTE/}

{NOTE: }
<a id="loadWithInclude" /> __Load entities with include__

* ['load' with include](../../../client-api/session/loading-entities#load-with-includes) loads both the document and the specified related document.    
  Loading entities with include can be executed __lazily__.

{CODE-TABS}
{CODE-TAB:nodejs:Lazy_load_with_include lazy_loadWithInclude@client-api\Session\HowTo\lazy.js /}
{CODE-TAB:nodejs:The_document lazy_productClass@client-api\Session\HowTo\lazy.js /}
{CODE-TABS/}
{NOTE/}

{NOTE: }
<a id="loadStartingWith" /> __Load entities starting with__

* ['loadStartingWith'](../../../client-api/session/loading-entities#loadstartingwith) loads entities whose ID starts with the specified prefix.  
  Loading entities with a common prefix can be executed __lazily__.

{CODE:nodejs lazy_loadStartingWith@client-api\Session\HowTo\lazy.js /}
{NOTE/}

{NOTE: }
<a id="conditionalLoad" /> __Conditional load__

* ['conditionalLoad'](../../../client-api/session/loading-entities#conditionalload) logic is: 
  * If the entity is already loaded to the session:  
    no server call is made, the tracked entity is returned.    
  * If the entity is Not already loaded to the session:  
    the document will be loaded from the server only if the change-vector provided to the method is older than the one in the server
    (i.e. if the document in the server is newer).
  * Loading entities conditionally can be executed __lazily__.  

{CODE:nodejs lazy_conditionalLoad@client-api\Session\HowTo\lazy.js /}
{NOTE/}

{NOTE: }
<a id="runQuery" /> __Run query__

* A Query can be executed __lazily__.  
  Learn more about running queries lazily in [lazy queries](../../../client-api/session/querying/how-to-perform-queries-lazily).

{CODE:nodejs lazy_query@client-api\Session\HowTo\lazy.js /}
{NOTE/}

{NOTE: }
<a id="getRevisions" /> __Get revisions__

* All methods for [getting revisions](../../../document-extensions/revisions/client-api/session/loading) and their metadata can be executed __lazily__.

{CODE:nodejs lazy_revisions@client-api\Session\HowTo\lazy.js /}
{NOTE/}

{NOTE: }
<a id="getCompareExchange" /> __Get compare-exchange value__

* [Getting compare-exchange](../../../client-api/session/cluster-transaction/compare-exchange#get-compare-exchange) values can be executed __lazily__.

{CODE:nodejs lazy_compareExchange@client-api\Session\HowTo\lazy.js /}
{NOTE/}

{PANEL/}

{PANEL: Multiple lazy requests }

{NOTE: }

<a id="implicit" /> __Execute all requests - implicitly__

Accessing the value of ANY of the lazy instances will trigger
the execution of ALL pending lazy requests held up by the session, 
in a SINGLE server call.  

{CODE:nodejs lazy_ExecuteAll_Implicit@client-api\Session\HowTo\lazy.js /}

{NOTE/}

{NOTE: }
<a id="explicit" /> __Execute all requests - explicitly__

Explicitly calling `executeAllPendingLazyOperations` will execute 
ALL pending lazy requests held up by the session, in a SINGLE server call.  

{CODE:nodejs lazy_ExecuteAll_Explicit@client-api\Session\HowTo\lazy.js /}

{NOTE/}

{PANEL/}

## Related Articles

### Session

- [How to Perform Queries Lazily](../../../client-api/session/querying/how-to-perform-queries-lazily)
- [Cluster Transaction - Overview](../../../client-api/session/cluster-transaction/overview)
