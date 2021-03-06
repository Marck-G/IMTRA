# MIT License
#
# Copyright (c) 2019 MARCK C. GUZMAN, UNAI DIAZ DE GARAYO
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sqlite3
from os import path
from utils.logger import Logger


class Manager:
    """
        Class DataBase Manager
    """
    # TODO: set the proyect data estructure

    __instance__ = None

    # creation file name
    __db_file__ = 'im.cre.db.sql'
    __db_name__ = 'manager.db'

    # sqlite connection
    conn = sqlite3.connect(__db_name__)

    # Insert comment here
    __db_file_delete__ = "im.del.db.sql"

    # Insert comment here
    __db_folder__ = "./"
    __log_folder__ = "./"

    # SINGLETON
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def set_db_file_folder(self, base_dir):
        self.__db_folder__ = base_dir if str(base_dir).endswith('/') else base_dir + '/'
        return self

    def set_log_folder(self, base_dir):
        self.__log_folder__ = base_dir if str(base_dir).endswith('/') else base_dir + '/'
        return self

    def create_db(self):
        """
        Create the database
        :return:
        """
        qry = open(self.__db_folder__+self.__db_file__, 'r').read()
        c = self.conn.cursor()
        c.executescript(qry)
        self.conn.commit()
        self.__log__('Created the DataBase')
        return self

    def delete_db(self):
        """
        Delete the database
        :return:
        """
        qry = open(self.__db_folder__ + self.delete_file, 'r').read()
        c = self.conn.cursor()
        c.executescript(qry)
        c.close()
        self.conn.commit()
        self.__log__('delete the database')
        return self

    # Insert comment here
    def add_item(self, data):
        assert data is not None, 'No data set for save in database'
        assert 'src' in data.keys(), 'Not found the source dir'
        assert 'des' in data.keys(), 'Not found destination dir'
        with self.conn.cursor() as cursor:
            query = 'INSERT INTO transfer_data values({},{})'.format(data['src'], data['dest'])
            cursor.execute(query)

    def __log__(self, text):
        """
        Create a log file with de date and the text
        :param text: to include in the log file
        """
        Logger(prefix=' Image Manager').log(text)

    def __exists__(self):
        """
        Check if the db exists and have its tables
        :return: boolean
        """
        # check if db file exist
        exist_file = path.exists(self.__db_name__)
        if exist_file:
            if len( self.__get_db_tables__()) != 0:
                return True
            else:
                self.__log__('No tables found')
        else:
            self.__log__('Not found db file')
        return False

    def __db_init__(self):
        if not self.__exists__():
            self.create_database()

    def get_tag(self, *args, data):
        cur = self.conn.execute('SELECT * FROM tag where {} like "*{}*" '.format(data['col'], data['value']))
        response = {}
        for col in cur:
            response[col] = cur[col]

    def get_image(self, *args, data):
        cur = self.conn.execute('SELECT * FROM image where {} like "*{}*" '.format(data['col'], data['value']))
        response = {}
        for col in cur:
            response[col] = cur[col]


class ConditionsNotFoundError(Exception):
    pass
