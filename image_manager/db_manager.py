import sqlite3

class Manager:
    __instance__ = None
    database_name = 'imtra.im.bd'
    conn = sqlite3.connect(database_name)


    # SINGLETON
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def create_bd(self):
        pass

    def delete_bd(self):
        pass

    def get_tags(self, img: str):
        pass
