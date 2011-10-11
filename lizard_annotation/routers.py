class AnnotationRouter(object):
    """A router to control all database operations on models in
    the lizard-annotation application"""

    def db_for_read(self, model, **hints):
        "Point all operations on lizard-annotation models to 'mongodb'"
        if model._meta.app_label == 'lizard-annotation':
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on lizard-annotation models to 'mongodb'"
        if model._meta.app_label == 'lizard-annotation':
            return 'mongodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "There are no hints regarding relations."
        return None

    def allow_syncdb(self, db, model):
        "There are no hints regarding relations."
        return None
