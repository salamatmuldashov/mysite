This document provides an overview of the distributed database architecture for PostgreSQL, focusing on replication, consistency models, and configuration. The system includes:

1. Primary Database: Handles write operations.
2. Replica Database: Handles read queries.


1. Configuration and running on different ports

- Primary Database
# /Library/PostgreSQL/14/data/postgresql.conf

Command for start primary server: pg_ctl -D /Library/PostgreSQL/14/data start 

Primary Configuration File:
wal_level = replica
max_wal_senders = 3
port=5432
listen_addresses = '*'

- Replice Database

# /Library/PostgreSQL/14/data/pg_replica/postgresql.conf

Command for start primary server: pg_ctl -D /Library/PostgreSQL/14/data/pg_replica start 

Replica Configuration File:
wal_level = replica
max_wal_senders = 3
port=5433
listen_addresses = '*'


2. I implemented a custom database router in Django to direct read queries to the replica and write queries to the primary database.

class ReadReplicaRouter:
    def db_for_read(self, model, **hints):
        return 'replica'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'replica')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'