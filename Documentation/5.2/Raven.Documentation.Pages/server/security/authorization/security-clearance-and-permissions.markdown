# Authorization: Security Clearance and Permissions

* X.509 certificates are used for authentication - validating that users are who they say they are. 
  Once a connection is authenticated, RavenDB uses the certificate for authorization as well. 

* Each certificate is associated with a security clearance and access permissions per database.

* It is the administrator's responsibility to generate client certificates and assign permissions. 
  Read more in the [Certificate Management](../authentication/certificate-management) page.

* A client certificate's security clearance can be one of the following: Cluster Admin, Operator, User.

* In this page:
   * [Cluster Admin](../../../server/security/authorization/security-clearance-and-permissions#cluster-admin)
   * [Operator](../../../server/security/authorization/security-clearance-and-permissions#operator)
   * [User](../../../server/security/authorization/security-clearance-and-permissions#user)  
      * [Admin](../../../server/security/authorization/security-clearance-and-permissions#section)  
      * [Read/Write](../../../server/security/authorization/security-clearance-and-permissions#section-1) 
      * [Read Only](../../../server/security/authorization/security-clearance-and-permissions#section-2)

{PANEL:Cluster Admin}

`Cluster Admin` is the highest security clearance. There are no restrictions. A `Cluster Admin` certificate has admin permissions to all databases. It also has the ability to modify the cluster itself.

{NOTE The server certificate security clearance is called `Cluster Node`. The server certificate can also be used as a client certificate, and in that case `Cluster Node` is equivalent to `Cluster Admin` in terms of permissions. /}

The following operations are allowed **only** for `Cluster Admin` certificates:

- All cluster operations
- Manage `Cluster Admin` certificates
- Replace and renew server certificates
- Use the Admin JS Console
- Activate or update the license
- Get SNMP used OIDs

{PANEL/}

{PANEL:Operator}

A client certificate with an `Operator` security clearance has admin access to all databases 
but is unable to modify the cluster. It cannot perform operations such as 
add/remove/promote/demote nodes from the cluster. This is useful in a hosted solution 
(such as **RavenDB Cloud**). If you are running on your own machines, you'll typically ignore 
that level in favor of `Cluster Admin` or `User`.

The following operations are allowed for **both** `Operator` and `Cluster Admin` certificates and are not allowed for `User` certificates:

- Operations on databases (put, delete, enable, disable)
- Manage `Operator` and `User` certificates
- Enable and disable an ongoing task
- Define External Replication
- Create and delete RavenDB ETL and SQL ETL
- Migrate databases
- View cluster observer logs
- View admin logs
- Gather local and cluster debug info (process, memory, cpu, threads) 
- Use smuggler
- Use the traffic watch
- Put cluster-wide client configuration (Max number of requests per session, Read balance behavior)
- Get the database record
- Manage database groups in the cluster
- Restore databases from backup
- Perform database and index compaction
- Get server metrics (request/sec, indexed/sec, batch size, etc...)
- Get remote server build info

{PANEL/}

{PANEL:User}

A client certificate with a `User` security clearance cannot perform any admin operations at the cluster level.  
Unlike the other clearance levels, a `User` client certificate can grant different access levels to different databases.  
These access levels are, from highest to lowest:  

* **Admin**  
* **Read/Write**  
* **Read Only**  

If no access level is defined for a particular database, the certificate doesn't grant access to that database at all.  

---

### `Admin`

The following operations are permitted at the `Admin` access level but not for `Read/Write` or `Read Only`:

- Operations on indexes (put, delete, start, stop, enable and disable)
- Solve replication conflicts
- Configure revisions and delete revision documents
- Define expiration
- Create backups and define periodic backups
- Operations on connection strings (put, get, delete)
- Put client configuration for the database (Max number of requests per session, Read balance behavior)
- Get transaction info
- Perform SQL migration

---

### `Read/Write`

A `User` certificate with a `Read/Write` access level can perform all operations **except** for those listed above in the 'Admin' and 'Operator'sections.  

  * [JavaScript static indexes](../../../indexes/javascript-indexes) are permitted by default with Read/Write User certificates.  
    To configure a server or database so that only Admin certificates will be able to deploy JavaScript static indexes,  
    set [Indexing.Static.RequireAdminToDeployJavaScriptIndexes](../../../server/configuration/indexing-configuration#indexing.static.requireadmintodeployjavascriptindexes) 
    to `true`.

---

### `Read Only`

The `ReadOnly` access level **allows** clients to: 

- Read data from a database, but not to write or modify data.  
- Be subscription workers to consume data subscriptions.  
- Query the databases that are configured in the client certificate.  
  {NOTE: }
  [An Auto-index](../../../indexes/creating-and-deploying#auto-indexes) 
  is built if there is no existing index that satisfies a query.  
  {NOTE/}

{INFO: Unauthorized actions for ReadOnly client certificates}

The following operations are **forbidden**:  

- Creating documents or modifying existing documents  
- Changing any configurations or settings  
- Creating or modifying [ongoing tasks](../../../studio/database/tasks/ongoing-tasks/general-info)  
- Defining [static indexes](../../../indexes/creating-and-deploying#static-indexes) (the database will create 
[auto-indexes](../../../indexes/creating-and-deploying#auto-indexes) if there is no existing index that satisfies a query.)


{INFO/}

Learn more about the `Read Only` access level [here](../../../studio/server/certificates/read-only-access-level).

{PANEL/}

## Related articles

### Security

- [Certificate Management](../../../server/security/authentication/certificate-management)
- [Configuring Certificates via Powershell](../../../server/security/authentication/client-certificate-usage#example-ii---using-powershell-and-wget-in-windows)
- [Common Errors and FAQ](../../../server/security/common-errors-and-faq)

### Studio

- [Certificate Management](../../../studio/server/certificates/server-management-certificates-view)
- [Studio: Read-Only Access Level](../../../studio/server/certificates/read-only-access-level)
