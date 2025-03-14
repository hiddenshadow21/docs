﻿# Storage Engine - Voron
---

{NOTE: }

* RavenDB uses an in-house managed storage engine called Voron to persist your data (documents, indexes, and configuration).
  It is a high performance storage engine designed and optimized for RavenDB's needs.

* Voron employs the following structures to efficiently organize data on persistent storage:
  * **B+Tree** - Supports variable-size keys and values.
  * **Fixed Sized B+Tree** - Uses `Int64` keys and fixed-size values (defined at creation time).  
    This structure enables various optimizations.
  * **Raw Data Section** – Allows storage of raw data (e.g., document content) and provides an identifier for O(1) data access.
  * **Table** – Combines Raw Data Sections with any number of indexes, which internally are implemented as regular or  
    Fixed-Sized B+Trees.

* In this page:
  * [Transaction support](../../server/storage/storage-engine#transaction-support)
  * [Single write model](../../server/storage/storage-engine#single-write-model)
  * [Memory-mapped files](../../server/storage/storage-engine#memory-mapped-files)
  * [Requirements](../../server/storage/storage-engine#requirements)
  * [Limitations](../../server/storage/storage-engine#limitations)

{NOTE/}

---

{PANEL: Transaction support}

Voron is a fully transactional storage engine that ensures atomicity and durability using a Write-Ahead Journal (WAJ).
All modifications made within a transaction are first written to a journal file (using unbuffered I/O and write-through) before being applied to the main data file and synced to disk.
The journals act as a transaction log, preserving the durability property of ACID transactions.
The application of the WAJ occurs in the background.

In the event of an ungraceful server shutdown, the journals serve as the recovery source.  
If a process stops unexpectedly, leaving modifications not yet applied to the data file, 
Voron recovers the database state during the next database startup by replaying the transactions stored in the journal files. 

Because journals are flushed and synced to disk before a transaction commit is completed, this guarantees that changes will survive process or system crashes. 
Each transaction is written to the journal once it's committed, and a successful response is returned _only_ if the commit completes successfully.
This ensures that transactions can be easily recovered if necessary.

Multi-Version Concurrency Control (MVCC) is implemented using scratch files,
which are temporary files that maintain concurrent versions of the data for active transactions.

Each transaction operates on a snapshot of the database, ensuring that write transactions do not modify the data being accessed by other transactions.
Snapshot isolation for concurrent transactions is maintained using Page Translation Tables.

{PANEL/}

{PANEL: Single write model}

Voron supports only single write processes (but there can be multiple read processes).  
Having only a single write transaction simplifies the handling of writes.

To achieve high performance, RavenDB implements transaction merging on top of Voron's single write model.  
This approach provides a tremendous performance boost, particularly in high-load scenarios.

Additionally, Voron includes support for asynchronous transaction commits.
These commits must meet specific requirements to seamlessly integrate with RavenDB's transaction merging mechanism. 
The actual transaction lock handoff and early lock release are managed at a higher layer, where more detailed system information is available.

{PANEL/}

{PANEL: Memory-mapped files}

Voron is based on memory mapped files.

{INFO: Running on 32 bits}

Since RavenDB 4.0, Voron has no limits when running in 32 bits mode. The issue of running out of address space when mapping files into memory 
has been addressed by providing a dedicated pager (component responsible for mapping) for a 32 bits environments.

Instead of mapping an entire file, it maps just the pages that are required and only for the duration of the transaction.

{INFO/}

{PANEL/}

{PANEL: Requirements}

The storage hardware / file system must support:

* fsync
* `[Windows]` UNBUFFERED_IO / WRITE_THROUGH
* `[Windows]` [Hotfix for Windows 7 and Windows Server 2008 R2](https://support.microsoft.com/en-us/help/2731284/33-dos-error-code-when-memory-memory-mapped-files-are-cleaned-by-using)
* `[Posix]` O_DIRECT

{PANEL/}

{PANEL: Limitations}

- The key size must be less than 2025 bytes in UTF8

{PANEL/}

## Related Articles

### Transactions

- [Transaction Support in RavenDB](../../client-api/faq/transaction-support)

### Storage

- [Directory Structure](../../server/storage/directory-structure)

### Configuration

- [Storage](../../server/configuration/storage-configuration)


