import sqlite3

class Manager:
    __instance__ = None
    # creation file name
    __db_file__ = 'imtr.cre.db.sql'
    __db_name__ = 'transfer.db'
    # sqlite connection
    conn = sqlite3.connect(__db_name__)


    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def add_item(self, data):
        assert data is not None, 'No data set for save in database'
        assert 'src' in data.keys(), 'Not found the source dir'
        assert 'des' in data.keys(), 'Not found destination dir'
        with self.conn.cursor() as cursor:
            query = 'INSERT INTO transfer_data values({},{})'.format(data['src'], data['dest'])
            cursor.execute(query)

    def create_db(self):
        pass

    def delete_db(self):
        pass

    def get_last_elements(self):
        pass