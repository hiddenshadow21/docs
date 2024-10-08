﻿# Append & Update Time Series

---

{NOTE: }

* Use `TimeSeriesFor.Append` for the following actions:
    * **Creating a new time series**  
      Appending an entry to a time series that doesn't exist yet  
      will create the time series and add it the new entry.
    * **Creating a new time series entry**  
      Appending a new entry to an existing time series  
      will add the entry to the series at the specified timestamp.
    * **Modifying an existing time series entry**  
      Use `Append` to update the data of an existing entry with the specified timestamp.

* Each call to `Append` handles a **single** [time series entry](../../../../document-extensions/timeseries/design#time-series-entries).  

* To append **multiple** entries in a single transaction you can:  
  * Call `Append` as many times as needed before calling `session.SaveChanges`, as shown in the examples below.
  * Use patching to update the time series. Learn more in [Patch time series entries](../../../../document-extensions/timeseries/client-api/session/patch).
  * Append entries directly on the _Store_ via [Operations](../../../../client-api/operations/what-are-operations). 
    Learn more in [Append time series operations](../../../../document-extensions/timeseries/client-api/operations/append-and-delete). 

---

* In this page:
    * [`Append` usage](../../../../document-extensions/timeseries/client-api/session/append#append-usage)
    * [Examples](../../../../document-extensions/timeseries/client-api/session/append#examples)
        * [Append entries with a single value](../../../../document-extensions/timeseries/client-api/session/append#append-entries-with-a-single-value)
        * [Append entries with multiple values](../../../../document-extensions/timeseries/client-api/session/append#append-entries-with-multiple-values)
    * [Syntax](../../../../document-extensions/timeseries/client-api/session/append#syntax)

{NOTE/}

---

{PANEL: `Append` usage}

**Flow**:

* Open a session.
* Create an instance of `TimeSeriesFor` and pass it the following:
    * Provide an explicit document ID, -or-  
      pass an [entity tracked by the session](../../../../client-api/session/what-is-a-session-and-how-does-it-work#unit-of-work-pattern),
      e.g. a document object returned from [session.Query](../../../../client-api/session/querying/how-to-query) or from [session.Load](../../../../client-api/session/loading-entities#load).
    * Specify the time series name.
* Call `TimeSeriesFor.Append` and pass it the time series entry details.
* Call `session.SaveChanges` for the action to take effect on the server.

**Note**:

* A `DocumentDoesNotExistException` exception is thrown if the specified document does not exist.

{PANEL/}

{PANEL: Examples}

#### Append entries with a single value:

* In this example, entries are appended with a single value.
* Although a loop is used to append multiple entries,  
  all entries are appended in a single transaction when `SaveChanges` is executed.

{CODE timeseries_region_TimeSeriesFor-Append-TimeSeries-Range@DocumentExtensions\TimeSeries\TimeSeriesTests.cs /}

---

#### Append entries with multiple values:

* In this example, we append multi-value StockPrice entries.  
* Notice the clarity gained by [naming the values](../../../../document-extensions/timeseries/client-api/named-time-series-values).  

{CODE-TABS}
{CODE-TAB:csharp:Native timeseries_region_Append-Unnamed-Values-2@DocumentExtensions\TimeSeries\TimeSeriesTests.cs /}
{CODE-TAB:csharp:Using_named_values timeseries_region_Append-Named-Values-2@DocumentExtensions\TimeSeries\TimeSeriesTests.cs /}
{CODE-TABS/}

{PANEL/}

{PANEL: Syntax}

{CODE TimeSeriesFor-Append-definition-double@DocumentExtensions\TimeSeries\TimeSeriesTests.cs /}

{CODE TimeSeriesFor-Append-definition-inum@DocumentExtensions\TimeSeries\TimeSeriesTests.cs /}

| Parameter     | Type                  | Description                   |
|---------------|-----------------------|-------------------------------|
| **timestamp** | `DateTime`            | Time series entry's timestamp |
| **value**     | `double`              | Entry's value                 |
| **values**    | `IEnumerable<double>` | Entry's values                |
| **tag**       | `string`              | An optional tag for the entry |

{PANEL/}

## Related articles

**Client API**  
[Time Series API Overview](../../../../document-extensions/timeseries/client-api/overview)

**Studio Articles**  
[Studio Time Series Management](../../../../studio/database/document-extensions/time-series)

**Querying and Indexing**  
[Time Series Querying](../../../../document-extensions/timeseries/querying/overview-and-syntax)  
[Time Series Indexing](../../../../document-extensions/timeseries/indexing)

**Policies**  
[Time Series Rollup and Retention](../../../../document-extensions/timeseries/rollup-and-retention)  
