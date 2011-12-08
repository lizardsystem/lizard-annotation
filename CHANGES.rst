Changelog of lizard-annotation
===================================================


0.3 (unreleased)
----------------

- Adds filtering on object_ident in the api grid view


0.2 (2011-12-07)
----------------

- Changed the Django database backend to sqlite3 (from PostGIS).

- Many improvements and bugfixes.


0.1.1 (2011-10-24)
------------------

- Cleaned up the api code.


0.1 (2011-10-24)
----------------

- Initial library skeleton created by nensskel.  [Alexandr Seleznev]

- Added routers.py

- Added models.py

- Changed annotation model, reference_objects expects a dict. object
  where key is a string of [model_name + record_id] and value is ReferenceObject().

- Added djangorestframework and an api module with urls and views for the
  various annotation models
