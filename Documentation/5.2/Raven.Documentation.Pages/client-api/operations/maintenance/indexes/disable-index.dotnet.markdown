# Disable Index

 ---

{NOTE: }

* You can __disable a specific index__ by either of the following:  
  * From the Client API - using `DisableIndexOperation`  
  * From the Studio - see [indexes list view](../../../../studio/database/indexes/indexes-list-view#indexes-list-view---actions)  
  * Via the file system

* To learn how to enable a disabled index see article [Enable index operation](../../../../client-api/operations/maintenance/indexes/enable-index).

* In this page:

    * [Overview](../../../../client-api/operations/maintenance/indexes/disable-index#overview)
      * [On which node the index is disabled](../../../../client-api/operations/maintenance/indexes/disable-index#on-which-node-the-index-is-disabled) 
      * [When index is disabled](../../../../client-api/operations/maintenance/indexes/disable-index#when-index-is-disabled) 
  
    * [Disable index from the Client API](../../../../client-api/operations/maintenance/indexes/disable-index#disable-index-from-the-client-api)     
        * [Disable index - single node](../../../../client-api/operations/maintenance/indexes/disable-index#disable-index---single-node)
        * [Disable index - cluster wide](../../../../client-api/operations/maintenance/indexes/disable-index#disable-index---cluster-wide)
        * [Syntax](../../../../client-api/operations/maintenance/indexes/disable-index#syntax)
  
    * [Disable index manually via the file system](../../../../client-api/operations/maintenance/indexes/disable-index#disable-index-manually-via-the-file-system)

{NOTE/}

---

{PANEL: Overview}

{NOTE: }

<a id="on-which-node-the-index-is-disabled" /> __On which node the index is disabled__:

---

* The index can be disabled either:  
    * On a single node, or  
    * Cluster wide - on all database-group nodes.  

* When disabling the index from the __client API__ on a single node:  
  The index will be disabled on the [preferred node](../../../../client-api/configuration/load-balance/overview#the-preferred-node) only, and Not on all the database-group nodes.  

* When disabling an index from the __Studio__ (from the [indexes list view](../../../../studio/database/indexes/indexes-list-view#indexes-list-view---actions)),  
  The index will be disabled on the local node the browser is opened on, even if it is Not the preferred node.  

* When disabling the index [manually](../../../../client-api/operations/maintenance/indexes/disable-index#disable-index-via-the-file-system),  
  The index will be disabled on the [preferred node](../../../../client-api/configuration/load-balance/overview#the-preferred-node) only, and Not on all the database-group nodes.

{NOTE/}
{NOTE: }

<a id="when-index-is-disabled" /> __When index is disabled__:  

---

* No indexing will be done by a disabled index on the node where index is disabled.  
  However, new data will be indexed by the index on other database-group nodes where it is not disabled.

* You can still query the index,  
  but results may be stale when querying a node on which the index was disabled.  

* Disabling an index is a __persistent operation__:  
  * The index will remain disabled even after restarting the server or after [disabling/enabling](../../../../client-api/operations/server-wide/toggle-databases-state) the database.  
  * To only pause the index and resume after a restart see: [pause index operation](../../../../client-api/operations/maintenance/indexes/stop-index).  

{NOTE/}
{PANEL/}

{PANEL: Disable index from the Client API}

{NOTE: }

<a id="disable-index---single-node" /> __Disable index - single node__:

---

{CODE-TABS}
{CODE-TAB:csharp:Sync disable_1@ClientApi\Operations\Maintenance\Indexes\DisableIndex.cs /}
{CODE-TAB:csharp:Async disable_1_async@ClientApi\Operations\Maintenance\Indexes\DisableIndex.cs /}
{CODE-TABS/}

{NOTE/}
{NOTE: }

<a id="disable-index---cluster-wide" /> __Disable index - cluster wide__:  

{CODE-TABS}
{CODE-TAB:csharp:Sync disable_2@ClientApi\Operations\Maintenance\Indexes\DisableIndex.cs /}
{CODE-TAB:csharp:Async disable_2_async@ClientApi\Operations\Maintenance\Indexes\DisableIndex.cs /}
{CODE-TABS/}

{NOTE/}
{NOTE: }

<a id="syntax" /> __Syntax__:  

{CODE:csharp syntax@ClientApi\Operations\Maintenance\Indexes\DisableIndex.cs /}

| Parameter       | Type   | Description                                                                                                              |
|-----------------|--------|--------------------------------------------------------------------------------------------------------------------------|
| __indexName__   | string | Name of index to disable                                                                                                 |
| __clusterWide__ | bool   | `true` - Disable index on all database-group nodes<br>`false` - Disable index only on a single node (the preferred node) |

{NOTE/}
{PANEL/}

{PANEL: Disable index manually via the file system}

* It may sometimes be useful to disable an index manually, through the file system.  
  For example, a faulty index may load before [DisableIndexOperation](../../../../client-api/operations/maintenance/indexes/disable-index#disableindexoperation) gets a chance to disable it.  
  Manually disabling the index will ensure that the index is not loaded.  

* To __manually disable__ an index:  

  * Place a file named `disable.marker` in the [index directory](../../../../server/storage/directory-structure).  
    Indexes are kept under the database directory, each index in a directory whose name is similar to the index's.   
  * The `disable.marker` file can be empty,  
    and can be created by any available method, e.g. using the File Explorer, a terminal, or code.  

* Attempting to use a manually disabled index will generate the following exception:  

           Unable to open index: '{IndexName}', 
           it has been manually disabled via the file: '{disableMarkerPath}.  
           To re-enable, remove the disable.marker file and enable indexing.`

* To __enable__ a manually disabled index:  

  * First, remove the `disable.marker` file from the index directory.
  * Then, enable the index by any of the options described in: [How to enable an index](../../../../client-api/operations/maintenance/indexes/enable-index#how-to-enable-an-index).

{PANEL/}

## Related Articles

### Indexes

- [What are Indexes](../../../../indexes/what-are-indexes)
- [Creating and Deploying Indexes](../../../../indexes/creating-and-deploying)
- [Index Administration](../../../../indexes/index-administration)
- [Enable Index](../../../../client-api/operations/maintenance/indexes/enable-index)

### Operations

- [What are operations](../../../../client-api/operations/what-are-operations)
- [How to Enable Index](../../../../client-api/operations/maintenance/indexes/enable-index)
- [How to Pause Index Until Restart](../../../../client-api/operations/maintenance/indexes/stop-index)
