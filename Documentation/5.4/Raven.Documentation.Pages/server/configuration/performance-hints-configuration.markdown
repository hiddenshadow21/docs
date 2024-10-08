# Configuration: Performance Hints Options
---

{NOTE: }

* In this page:  
  * [PerformanceHints.Documents.HugeDocumentsCollectionSize](../../server/configuration/performance-hints-configuration#performancehints.documents.hugedocumentscollectionsize)
  * [PerformanceHints.Documents.HugeDocumentSizeInMb](../../server/configuration/performance-hints-configuration#performancehints.documents.hugedocumentsizeinmb)
  * [PerformanceHints.Indexing.AlertWhenSourceDocumentIncludedInOutput](../../server/configuration/performance-hints-configuration#performancehints.indexing.alertwhensourcedocumentincludedinoutput)
  * [PerformanceHints.Indexing.MaxDepthOfRecursionInLinqSelect](../../server/configuration/performance-hints-configuration#performancehints.indexing.maxdepthofrecursioninlinqselect)
  * [PerformanceHints.Indexing.MaxIndexOutputsPerDocument](../../server/configuration/performance-hints-configuration#performancehints.indexing.maxindexoutputsperdocument)  
  * [PerformanceHints.Indexing.MaxNumberOfLoadsPerReference](../../server/configuration/performance-hints-configuration#performancehints.indexing.maxnumberofloadsperreference)
  * [PerformanceHints.MaxNumberOfResults](../../server/configuration/performance-hints-configuration#performancehints.maxnumberofresults)
  * [PerformanceHints.Memory.MinSwapSizeInMb](../../server/configuration/performance-hints-configuration#performancehints.memory.minswapsizeinmb)
  * [PerformanceHints.TooLongRequestThresholdInSec](../../server/configuration/performance-hints-configuration#performancehints.toolongrequestthresholdinsec)

{NOTE/}

---

{PANEL: PerformanceHints.Documents.HugeDocumentsCollectionSize}

The maximum size of the huge documents collection.

- **Type**: `int`
- **Default**: `100`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.Documents.HugeDocumentSizeInMb}

The size of a document after which it will get into the huge documents collection.  
Value is in MB.

- **Type**: `int`
- **Default**: `5`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.Indexing.AlertWhenSourceDocumentIncludedInOutput}

Alert when source document in indexed as field.

- **Type**: `bool`
- **Default**: `true`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.Indexing.MaxDepthOfRecursionInLinqSelect}

Maximum depth of recursion in LINQ Select clause.

- **Type**: `int`
- **Default**: `32`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.Indexing.MaxIndexOutputsPerDocument}

The maximum number of index outputs per document after which we will create a performance hint.

- **Type**: `int`
- **Default**: `1024`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.Indexing.MaxNumberOfLoadsPerReference}

The maximum number of `LoadDocument()` / `LoadCompareExchangeValue()` calls per a document/compare-exchange reference value 
after which we will create a performance hint.

- **Type**: `int`
- **Default**: `1024`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.MaxNumberOfResults}

The maximum number of query results after which we will create a performance hint.

- **Type**: `int`
- **Default**: `2048`
- **Scope**: Server-wide or per database

{PANEL/}

{PANEL: PerformanceHints.Memory.MinSwapSizeInMb}

* The minimum swap size (Linux only) in Megabytes.  
  If the swap size is below this value, a notification will be triggered.

* The default value is set by the constructor of class `PerformanceHintsConfiguration`:  
  * If the total physical memory is less than 8 GB,  
    the default value is set to 1 GB.
  * If the total physical memory is greater than or equal to 8 GB,  
    the default value is set to the smaller value between half of the total physical memory and 8 GB.

---

- **Type**: `int`
- **Default**: `DefaultValueSetInConstructor`
- **Scope**: Server-wide only

{PANEL/}

{PANEL: PerformanceHints.TooLongRequestThresholdInSec}

Request latency threshold before the server would issue a performance hint.  
Value is in seconds.

- **Type**: `int`
- **Default**: `30`
- **Scope**: Server-wide or per database

{PANEL/}
