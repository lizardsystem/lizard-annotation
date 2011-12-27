lizard-annotation
==========================================

Introduction

Manages annotations of various object.

Setting up the test database
----------------------------
For the tests to work, one needs to be able to connect to a database named
annotation as user buildout::

  $ mongo
  > use admin
  > db.addUser('[ADMIN_NAME]','[ADMIN_PASSWORD]')
  > db.auth('[ADMIN_NAME]','[ADMIN_PASSWORD]')
  > use annotation
  > db.addUser('buildout','buildout')

Of course, creating a test postgis database is necessary as well, but since the
use of a mongodb is still somewhat recent, this is explicitly described above.

It is possible to dump and load mongo data in the same way as django data via
The management commands mongo-dumpdata and mongo-loaddata, for example::

    # Dump all data to fixture
    bin/django mongo-dumpdata lizard_annotation > lizard_annotation.mongo
    # Dump Annotation collection
    bin/django mongo-dumpdata lizard_annotation.Annotation

    bin/django mongo-loaddata lizard_annotation.mongo


