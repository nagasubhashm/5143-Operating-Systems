## Replicated File System

**Replicated file Distributed system project idea** explains a simple way to increase the likelihood
that a critical data file is always accessible is to keep a back-up copy of the file on another
disk, usually one that is attached to a different machine. The file system provides transparent
replication. In particular, suppose there are n copies of a data file and n server modules. Each
server provides access to one copy of the file. A client interacts with any one of the server
modules. The servers interact with each other to present clients with the illusion that there is a
single copy of the file. Each file exports four operations: open, close, read and write for client.
The file servers interact with each other to ensure that copies of the file are kept consistent and
that at most one client at a time is permitted to write into the file. Each file servers has a local
lock manager process that implements a solution to the readers/writer problem. Some points to bear
in mind.

**a.** Each fileserver exports two sets of operations: those called by its clients and those called
by other file servers. Each server module keeps track of current access mode by using a lock
manager. For example, the file is not written if it was opened for reading. Multiple readings
however are allowed. If a certain operation needs to get permission from all lock managers, please
acquire the locks in the same order for all clients. Otherwise, deadlock may occur.

**b.** Within write procedure, a module first update its local copy then concurrently updates every
remote copy. It is analogous to using a write-through cache update policy. An alternative approach would be
to update the remote copy when the file is closed.

**Demo purpose:** Store duplicated simple text files in several fileservers for demo purpose. Write
operation just simply appends more text to the file. Client gets connected to any fileserver in a graphical
user interface.
