﻿# Time Series: Client API Overview
---

{NOTE: }

The Time Series client API includes a set of [session](../../../client-api/session/what-is-a-session-and-how-does-it-work) 
methods and [store](../../../client-api/what-is-a-document-store) 
[operations](../../../client-api/operations/what-are-operations).  
You can use the API to **append** (create and update), **get**, 
**delete**, **include**, **patch** and **query** time series data.  

* In this page:  
  * [Creating and Removing Time Series](../../../document-extensions/timeseries/client-api/overview#creating-and-removing-time-series)  
  * [`session` Methods -vs- `document-store` Operations](../../../document-extensions/timeseries/client-api/overview#session-methods--vs--document-store-operations)  
  * [Available Time Series `session` methods](../../../document-extensions/timeseries/client-api/overview#available-time-series-session-methods)  
  * [Available Time Series `store` Operations](../../../document-extensions/timeseries/client-api/overview#available-time-series-store-operations)  

{NOTE/}

---

{PANEL: Creating and Removing Time Series}

A time series is constructed of time series **entries**, which can 
be created and deleted using the API.  
There is no need to explicitly create or delete a time series:  

  * A time series is created when the first entry is appended to it.  
  * A time series is deleted when all entries are deleted from it.  

{PANEL/}

{PANEL: `session` Methods -vs- `document-store` Operations}

Some time series functions are available through both `session` methods 
and `document-store` operations:  
You can **append**, **delete**, **get** and **patch** time series data 
through both interfaces.  

---

There are also functionalities unique to each interface.  

* **Time series functionalities unique to the `session`interface**:  
   * `session` methods provide a **transactional guarantee**.  
     Use them when you want to guarantee that your actions would 
     be processed in a [single ACID transaction](../../../client-api/faq/transaction-support).  
     You can, for instance, gather multiple session actions 
     (e.g. the update of a time series and the modification 
     of a document) and execute them in a single transaction 
     by calling `session.SaveChanges`, to ensure that they 
     would all be completed or all be reverted.  
   * You can use `session` methods to `include` time series while 
     loading documents.  
     Included time series data is held by the client's session, 
     and can be handed to the user instantly when requested 
     without issuing an additional request to the server  
* **Time series functionalities unique to the `store`interface**:  
   * Getting the data of **multiple time series** in a single operation.  
   * Managing time series **rollup and retention policies**.  
   * Patching time series data to **multiple documents** located by a query.  
{PANEL/}

{PANEL: Available Time Series `session` methods}

* [TimeSeriesFor.Append](../../../document-extensions/timeseries/client-api/session/append)  
  Use this method to **Append entries to a time series** 
  (creating the series if it didn't previously exist).  
* [TimeSeriesFor.Delete](../../../document-extensions/timeseries/client-api/session/delete)  
  Use this method to **delete a range of entries from a time series** 
  (removing the series completely if all entries have been deleted).  
* [TimeSeriesFor.Get](../../../document-extensions/timeseries/client-api/session/get/get-entries)  
  Use this method to **Retrieve raw time series entries** 
  for all entries or for a chosen entries range.  
* [Advanced.GetTimeSeriesFor](../../../document-extensions/timeseries/client-api/session/get/get-names)  
  Use this method to **Retrieve time series Names**.  
  Series names are fetched by `GetTimeSeriesFor` directly from their parent documents' 
  metadata, requiring no additional server roundtrips.  
* [session.Advanced.Defer](../../../document-extensions/timeseries/client-api/session/patch)  
  Use this method to **patch time series data to a document**.  
* **To include time series data** -  
   * [Use IncludeTimeSeries while loading a document via session.Load](../../../document-extensions/timeseries/client-api/session/include/with-session-load)  
   * [Use IncludeTimeSeries while retrieving a document via session.Query](../../../document-extensions/timeseries/client-api/session/include/with-session-query)  
   * [Use RQL while running a raw query](../../../document-extensions/timeseries/client-api/session/include/with-raw-queries)  
{PANEL/}

{PANEL: Available Time Series `store` Operations}

* [TimeSeriesBatchOperation](../../../document-extensions/timeseries/client-api/operations/append-and-delete)  
  Use this operation to **append and delete time series entries**.  
  You can bundle a series of Append and/or Delete operations in a list and 
  execute them in a single call.  
* [GetTimeSeriesOperation](../../../document-extensions/timeseries/client-api/operations/get#gettimeseriesoperation)  
  Use this operation to Get entries from a single time series.  
* [GetMultipleTimeSeriesOperation](../../../document-extensions/timeseries/client-api/operations/get#getmultipletimeseriesoperation)  
  Use this operation to Get entries from multiple time series.  
* [ConfigureTimeSeriesOperation](../../../document-extensions/timeseries/rollup-and-retention)  
  Use this operation to **manage time series roll-up and retention policies**.  
* [PatchOperation](../../../document-extensions/timeseries/client-api/operations/patch#patchoperation)  
  Use this operation to append/delete time series entries to/from a single document.  
* [PatchByQueryOperation](../../../document-extensions/timeseries/client-api/operations/patch#patchbyqueryoperation)  
  Use this operation to run a query and append/delete time series entries to/from 
  matching documents.
* [BulkInsert.TimeSeriesFor.Append](../../../document-extensions/timeseries/client-api/bulk-insert/append-in-bulk)  
  Use this operation to append time series entries in bulk.  

{PANEL/}

## Related articles

**Time Series Overview**  
[Time Series Overview](../../../document-extensions/timeseries/overview)  

**Studio Articles**  
[Studio Time Series Management](../../../studio/database/document-extensions/time-series)  
[Time Series Settings View](../../../studio/database/settings/time-series-settings)  


**Querying and Indexing**  
[Time Series Querying](../../../document-extensions/timeseries/querying/overview-and-syntax)  
[Time Series Indexing](../../../document-extensions/timeseries/indexing)  

**Policies**  
[Time Series Rollup and Retention](../../../document-extensions/timeseries/rollup-and-retention)  
