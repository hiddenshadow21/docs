# What are Operations

---

{NOTE: }

* The RavenDB Client API is built with the notion of layers.  
  At the top, and what you will usually interact with, are the **[DocumentStore](../../client-api/what-is-a-document-store)**
  and the **[Session](../../client-api/session/what-is-a-session-and-how-does-it-work)**.  
  They in turn are built on top of the lower-level __Operations__ and __RavenCommands__ API.

* __RavenDB provides access to this lower-level API__, so that instead of using the higher session API,  
  you can generate requests directly to the server by executing operations on the DocumentStore.

* In this page:  
  * [Why use operations](../../client-api/operations/what-are-operations#why-use-operations)  
  * [How operations work](../../client-api/operations/what-are-operations#how-operations-work)  
<br>
  * __Operation types__: 
      * [Common operations](../../client-api/operations/what-are-operations#common-operations)  
      * [Maintenance operations](../../client-api/operations/what-are-operations#maintenance-operations)  
      * [Server-maintenance operations](../../client-api/operations/what-are-operations#server-maintenance-operations)  
  * [Wait for completion](../../client-api/operations/what-are-operations#wait-for-completion)  

{NOTE/}

---

{PANEL: Why use operations}

* Operations provide __management functionality__ that is Not available in the context of the session, e.g.:  
  create/delete a database, execute administrative tasks, assign permissions, change server configuration, etc.

* Some operations (e.g. _PatchOperation_) can also be carried out via the session (e.g. _session.advanced.patch()_).  
  However, while a session wraps multiple actions into a single business transaction,  
  the operation is an __individual action__ that is Not part of the session transaction.

{PANEL/}

{PANEL: How operations work}

* __Sending the request__:  
  Each Operation creates an HTTP request message to be sent to the relevant server endpoint.  
  The DocumentStore `OperationExecutor` sends the request and processes the results.
* __Target node__:  
  By default, the operation will be executed on the server node that is defined by the [client configuration](../../client-api/configuration/load-balance/overview#client-logic-for-choosing-a-node).  
  However, server-maintenance operations can be executed on a specific node by using the [forNode](../../client-api/operations/how-to/switch-operations-to-a-different-node) method.  
* __Target database__:  
  By default, operations work on the default database defined in the DocumentStore.  
  However, common operations & maintenance operations can operate on a different database by using the [forDatabase](../../client-api/operations/how-to/switch-operations-to-a-different-database) method.  
* __Transaction scope__:  
  Operations execute as a single-node transaction.  
  If needed, data will then replicate to the other nodes in the database-group.
* __Background operations__:  
  Some operations may take a long time to complete and can be awaited for completion.   
  Learn more [below](../../client-api/operations/what-are-operations#wait-for-completion).

{PANEL/}

{PANEL: Common operations}

{NOTE: }

* All common operations implement the `IOperation` interface.  
  The operation is executed within the __database scope__.  
  Use [forDatabase](../../client-api/operations/how-to/switch-operations-to-a-different-database) to operate on a specific database other than the default defined in the store.  

* These operations include set-based operations such as _PatchOperation_, _CounterBatchOperation_,  
  document-extensions related operations such as getting/putting an attachment, and more.  
  See all available operations [below](../../client-api/operations/what-are-operations#operations-list).

* To execute a common operation request,  
  use the `send` method on the `operations` property in the DocumentStore.

__Example__:

{CODE:nodejs operations_ex@ClientApi\Operations\whatAreOperations.js /}

{NOTE/}

{NOTE: }

__Send syntax__:

{CODE:nodejs operations_send@ClientApi\Operations\whatAreOperations.js /}

{NOTE/}

{NOTE: }

<span id="operations-list"> __The following common operations are available:__ </span>

---

* __Attachments__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PutAttachmentOperation](../../client-api/operations/attachments/put-attachment)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetAttachmentOperation](../../client-api/operations/attachments/get-attachment)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DeleteAttachmentOperation](../../client-api/operations/attachments/delete-attachment)  

* __Counters__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [CounterBatchOperation](../../client-api/operations/counters/counter-batch)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetCountersOperation](../../client-api/operations/counters/get-counters)  

* __Time series__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TimeSeriesBatchOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetMultipleTimeSeriesOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetTimeSeriesOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetTimeSeriesStatisticsOperation  

* __Revisions__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetRevisionsOperation  

* __Patching__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PatchOperation](../../client-api/operations/patching/single-document)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PatchByQueryOperation](../../client-api/operations/patching/set-based)  

* __Delete by query__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DeleteByQueryOperation](../../client-api/operations/delete-by-query)   

* __Compare-exchange__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutCompareExchangeValueOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetCompareExchangeValueOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetCompareExchangeValuesOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteCompareExchangeValueOperation  

{NOTE/}
{PANEL/}

{PANEL: Maintenance operations}

{NOTE: }

* All maintenance operations implement the `IMaintenanceOperation` interface.  
  The operation is executed within the __database scope__.  
  Use [forDatabase](../../client-api/operations/how-to/switch-operations-to-a-different-database) to operate on a specific database other than the default defined in the store.

* These operations include database management operations such as setting client configuration,  
  managing indexes & ongoing-tasks operations, getting stats, and more.  
  See all available maintenance operations [below](../../client-api/operations/what-are-operations#maintenance-list).
 
* To execute a maintenance operation request,  
  use the `send` method on the `maintenance` property in the DocumentStore.

__Example__:

{CODE:nodejs maintenance_ex@ClientApi\Operations\whatAreOperations.js /}

{NOTE/}

{NOTE: }

__Send syntax__:

{CODE:nodejs maintenance_send@ClientApi\Operations\whatAreOperations.js /}

{NOTE/}

{NOTE: }

<span id="maintenance-list"> __The following maintenance operations are available:__ </span>

---

* __Statistics__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetStatisticsOperation](../../client-api/operations/maintenance/get-statistics)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetDetailedStatisticsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetCollectionStatisticsOperation](../../client-api/operations/maintenance/get-collection-statistics)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetDetailedCollectionStatisticsOperation  

* __Client Configuration__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PutClientConfigurationOperation](../../client-api/operations/maintenance/configuration/put-client-configuration)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetClientConfigurationOperation](../../client-api/operations/maintenance/configuration/get-client-configuration)  

* __Indexes__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PutIndexesOperation](../../client-api/operations/maintenance/indexes/put-indexes)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [SetIndexesLockOperation](../../client-api/operations/maintenance/indexes/set-index-lock)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [SetIndexesPriorityOperation](../../client-api/operations/maintenance/indexes/set-index-priority)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetIndexErrorsOperation](../../client-api/operations/maintenance/indexes/get-index-errors)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetIndexOperation](../../client-api/operations/maintenance/indexes/get-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetIndexesOperation](../../client-api/operations/maintenance/indexes/get-indexes)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetTermsOperation](../../client-api/operations/maintenance/indexes/get-terms)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetIndexPerformanceStatisticsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetIndexStatisticsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetIndexesStatisticsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetIndexingStatusOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetIndexStalenessOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetIndexNamesOperation](../../client-api/operations/maintenance/indexes/get-index-names)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [StartIndexOperation](../../client-api/operations/maintenance/indexes/start-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [StartIndexingOperation](../../client-api/operations/maintenance/indexes/start-indexing)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [StopIndexOperation](../../client-api/operations/maintenance/indexes/stop-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [StopIndexingOperation](../../client-api/operations/maintenance/indexes/stop-indexing)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ResetIndexOperation](../../client-api/operations/maintenance/indexes/reset-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DeleteIndexOperation](../../client-api/operations/maintenance/indexes/delete-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DeleteIndexErrorsOperation](../../client-api/operations/maintenance/indexes/delete-index-errors)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DisableIndexOperation](../../client-api/operations/maintenance/indexes/disable-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [EnableIndexOperation](../../client-api/operations/maintenance/indexes/enable-index)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [IndexHasChangedOperation](../../client-api/operations/maintenance/indexes/index-has-changed)   

* __Analyzers__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutAnalyzersOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteAnalyzerOperation  

* __Ongoing tasks__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetOngoingTaskInfoOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteOngoingTaskOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ToggleOngoingTaskStateOperation  

* __ETL tasks__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AddEtlOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdateEtlOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ResetEtlOperation](../../client-api/operations/maintenance/etl/reset-etl)

* __Replication tasks__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutPullReplicationAsHubOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetPullReplicationTasksInfoOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetReplicationHubAccessOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetReplicationPerformanceStatisticsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RegisterReplicationHubAccessOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UnregisterReplicationHubAccessOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdateExternalReplicationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdatePullReplicationAsSinkOperation

* __Backup__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; BackupOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetPeriodicBackupStatusOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; StartBackupOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdatePeriodicBackupOperation  

* __Connection strings__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutConnectionStringOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RemoveConnectionStringOperation  

* __Transaction recording__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; StartTransactionsRecordingOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; StopTransactionsRecordingOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ReplayTransactionsRecordingOperation  

* __Database settings__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutDatabaseSettingsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetDatabaseSettingsOperation  

* __Identities__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetIdentitiesOperation](../../client-api/operations/maintenance/identities/get-identities)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NextIdentityForOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SeedIdentityForOperation  

* __Time series__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureTimeSeriesOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureTimeSeriesPolicyOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureTimeSeriesValueNamesOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RemoveTimeSeriesPolicyOperation  

* __Revisions__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureRevisionsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteRevisionsOperation  

* __Sorters__:   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutSortersOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteSorterOperation  

* __Misc__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureExpirationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureRefreshOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdateDocumentsCompressionConfigurationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DatabaseHealthCheckOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetOperationStateOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CreateSampleDataOperation  

{NOTE/}
{PANEL/}

{PANEL: Server-maintenance operations}

{NOTE: }

* All server-maintenance operations implement the `IServerOperation` interface.  
  The operation is executed within the __server scope__.   
  Use [forNode](../../client-api/operations/how-to/switch-operations-to-a-different-node) to operate on a specific node other than the default defined in the client configuration.

* These operations include server management and configuration operations.  
  See all available operations [below](../../client-api/operations/what-are-operations#server-list).

* To execute a server-maintenance operation request,  
  use the `send` method on the `maintenance.server` property in the DocumentStore.   

__Example__:

{CODE:nodejs server_ex@ClientApi\Operations\whatAreOperations.js /}

{NOTE/}

{NOTE: }

__Send syntax__:

{CODE:nodejs server_send@ClientApi\Operations\whatAreOperations.js /}

{NOTE/}

{NOTE: }

<span id="server-list"> __The following server-maintenance operations are available:__ </span>

---

* __Client certificates__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PutClientCertificateOperation](../../client-api/operations/server-wide/certificates/put-client-certificate)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [CreateClientCertificateOperation](../../client-api/operations/server-wide/certificates/create-client-certificate)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetCertificatesOperation](../../client-api/operations/server-wide/certificates/get-certificates)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DeleteCertificateOperation](../../client-api/operations/server-wide/certificates/delete-certificate)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; EditClientCertificateOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetCertificateMetadataOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ReplaceClusterCertificateOperation  

* __Server-wide client configuration__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PutServerWideClientConfigurationOperation](../../client-api/operations/server-wide/configuration/put-serverwide-client-configuration)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetServerWideClientConfigurationOperation](../../client-api/operations/server-wide/configuration/get-serverwide-client-configuration)   

* __Database management__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [CreateDatabaseOperation](../../client-api/operations/server-wide/create-database)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [DeleteDatabasesOperation](../../client-api/operations/server-wide/delete-database)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ToggleDatabasesStateOperation](../../client-api/operations/server-wide/toggle-databases-state)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetDatabaseNamesOperation](../../client-api/operations/server-wide/get-database-names)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [AddDatabaseNodeOperation](../../client-api/operations/server-wide/add-database-node)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [PromoteDatabaseNodeOperation](../../client-api/operations/server-wide/promote-database-node)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ReorderDatabaseMembersOperation](../../client-api/operations/server-wide/reorder-database-members)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [CompactDatabaseOperation](../../client-api/operations/server-wide/compact-database)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetDatabaseRecordOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SetDatabasesLockOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CreateDatabaseOperationWithoutNameValidation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SetDatabaseDynamicDistributionOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ModifyDatabaseTopologyOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdateDatabaseOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UpdateUnusedDatabasesOperation  

* __Server-wide ongoing tasks__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteServerWideTaskOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ToggleServerWideTaskStateOperation  

* __Server-wide replication tasks__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutServerWideExternalReplicationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetServerWideExternalReplicationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetServerWideExternalReplicationsOperation  

* __Server-wide backup tasks__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutServerWideBackupConfigurationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetServerWideBackupConfigurationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetServerWideBackupConfigurationsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RestoreBackupOperation

* __Server-wide analyzers__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutServerWideAnalyzersOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteServerWideAnalyzerOperation

* __Server-wide sorters__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutServerWideSortersOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeleteServerWideSorterOperation

* __Logs & debug__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SetLogsConfigurationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetLogsConfigurationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetClusterDebugInfoPackageOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [GetBuildNumberOperation](../../client-api/operations/server-wide/get-build-number)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetServerWideOperationStateOperation

* __Traffic watch__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PutTrafficWatchConfigurationOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GetTrafficWatchConfigurationOperation

* __Misc__:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ConfigureRevisionsForConflictsOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ModifyConflictSolverOperation  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OfflineMigrationOperation

{NOTE/}
{PANEL/}

{PANEL: Wait for completion}

* Some operations may take a long time to complete.  
  Those operations will run in the server background and can be awaited for completion.  
* Those operations implement an interface with result type `OperationIdResult`.  
* For those operations, the `send` method returns a promise for an object that can be awaited on that Id.  

__Example__:  

{CODE:nodejs wait_ex@ClientApi\Operations\whatAreOperations.js /}

__Syntax__:

{CODE:nodejs waitForCompletion_syntax@ClientApi\Operations\whatAreOperations.js /}

{PANEL/}

## Related articles

### Document Store

- [What is a Document Store](../../client-api/what-is-a-document-store)

### Operations

- [How to Switch Operations to a Different Database](../../client-api/operations/how-to/switch-operations-to-a-different-database)
- [How to Switch Operations to a Different Node](../../client-api/operations/how-to/switch-operations-to-a-different-node)