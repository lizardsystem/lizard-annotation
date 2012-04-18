Changelog of lizard-annotation
===================================================


0.5.3 (2012-04-18)
------------------

- Add possibility to relate measures to annotations
- Change column name in form
- Widen popup space usage
- Enable subareas to be selected


0.5.2 (2012-04-16)
------------------

- Add dependency on lizard_map to migration.


0.5.1 (2012-04-16)
------------------

- Remove debugger statement from form.
- Add securityfields and corresponding migration.


0.5 (2012-04-13)
----------------

- Remove mongo-management commands
- Create portal form and view for annotation viewing, editing and creation.


0.4 (2012-03-27)
----------------

- Reworked models to use postgres instead of mongodb

0.3 (2011-12-27)
----------------

- Adds rudimentary fixture capability for mongoengine

- Adds basic authentication - all operations are now forbidden when not
  authenticated


0.2.1 (2011-12-08)
------------------

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
