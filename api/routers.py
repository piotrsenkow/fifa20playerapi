# coding: utf-8

class ApiDatabaseRouter:
    """
    A router to control all database operations on models in the
    api application.
    """
    def db_for_read(self, model, **hints):

        try:
            return model.Database.using
        except:
            return None

    def db_for_write(self, model, **hints):

        try:
            return model.Database.using
        except:
            return None