# How to Check for Entity Changes
---

{NOTE: }

* The Session [tracks all changes](../../../client-api/session/what-is-a-session-and-how-does-it-work#tracking-changes) made to all entities that it has either loaded, stored, or queried for,  
  and persists to the server only what is needed when `SaveChanges()` is called.

* This article describes how to check for changes made in a specific __entity__ within a session.  
  To check for changes on all tracked entities, see [Check for session changes](../../../client-api/session/how-to/check-if-there-are-any-changes-on-a-session).

* In this page:
    * [Check for entity changes](../../../client-api/session/how-to/check-if-entity-has-changed#check-for-entity-changes)
    * [Get entity changes](../../../client-api/session/how-to/check-if-entity-has-changed#get-entity-changes)
    * [Syntax](../../../client-api/session/how-to/check-if-entity-has-changed#syntax)

{NOTE/}

---

{PANEL: Check for entity changes }

* The session's advanced property `HasChanged` indicates whether the specified entity was added, modified, or deleted within the session.

* Note: The _HasChanged_ property is cleared after calling `SaveChanges()`.

---

{CODE changes_1@ClientApi\Session\HowTo\EntityChanges.cs /}

{PANEL/}

{PANEL: Get entity changes }

* Use the session's advanced method `WhatChangedFor()` to get all changes made in the specified entity  
  within the session.

* Details will include:
    * The name and path of the changed field
    * Its old and new values
    * The type of change

---

##### Example I

{CODE changes_2@ClientApi\Session\HowTo\EntityChanges.cs /}

##### Example II

{CODE changes_3@ClientApi\Session\HowTo\EntityChanges.cs /}

{PANEL/}

{PANEL: Syntax}

{CODE syntax_1@ClientApi\Session\HowTo\EntityChanges.cs /}
{CODE syntax_2@ClientApi\Session\HowTo\EntityChanges.cs /}

| ReturnValue          |                                    |
|----------------------|------------------------------------|
| `DocumentsChanges[]` | List of changes made in the entity |

{CODE syntax_3@ClientApi\Session\HowTo\EntityChanges.cs /}

{PANEL/}

## Related Articles

### Session

- [What is a session and how does it work](../../../client-api/session/what-is-a-session-and-how-does-it-work)
- [How to check for session changes](../../../client-api/session/how-to/check-if-there-are-any-changes-on-a-session)
- [Evict entity from session](../../../client-api/session/how-to/evict-entity-from-a-session)
- [Refresh entity](../../../client-api/session/how-to/refresh-entity)
