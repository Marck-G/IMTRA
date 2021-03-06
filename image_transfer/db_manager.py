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

import sqlite3 as db
from os import path
from utils.logger import Logger


class Manager:
    """
            Class DataBase Manager
    """
    # TODO: set the proyect data estructure

    __instance__ = None

    # creation file name
    __db_file__ = 'imtr.cre.db.sql'
    __bd_name__ = 'transfer.db'

    # database deletion file name
    __db_file_delete__ = 'imtr.del.db.sql'

    # set the files folders
    __db_folder__ = "./"
    __log_folder__ = "./"

    # sqlite connection
    conn = db.connect(__bd_name__)

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
        self.__log__('Created The DatBase')
        return self

    def delete_db(self):
        """
           Delete the database
           :return:
        """
        qry = open(self.__db_folder__ + self.__db_file_delete__, 'r').read()
        c = self.conn.cursor()
        c.executescript(qry)
        c.close()
        self.conn.commit()
        self.__log__('delete the database')
        return self

    def add_item(self, data: dict):
        """
        Recive un diccionario con los datos y se guardan en la base de datos
        :param data: diccionario con la estructura: { origin: origen, dest: destino, date : fecha}
        :return:
        """
        # general insert into string
        insert_sql = "INSERT INTO {}({}) values({})"
        table = "transfer"
        # coment Here
        insert = insert_sql.format(table, ",".join(data.keys()), ",".join(data.values()))
        self.__log__(insert)
        # execute the command
        self.conn.execute(insert)
        # save al changes
        self.conn.commit()
        return self

    def get_dest(self) -> dict:
       """
       Find in the database the dest dir more used.
       return: dict with the destination dir
       """
        out = {}
        response = cur = self.conn.execute("SELECT path, count(path) c, ( SELECT max(trf_date) d FROM transfer WHERE main.path = path ) dat FROM transfer main WHERE type = 'D' GROUP BY path ORDER BY c DESC, dat DESC").fetchmany(5)
        # generate the output dictionary
        for col in response.keys():
            out[col] = response[col]
        return out
    
    def get_src(self) -> dict:
       """
       Find in the database the origin dir more used.
       return: dict with the origin dirs
       """
        out = {}
        response = cur = self.conn.execute("SELECT path, count(path) c, ( SELECT max(trf_date) d FROM transfer WHERE main.path = path ) dat FROM transfer main WHERE type = 'O' GROUP BY path ORDER BY c DESC, dat DESC").fetchmany(5)
        # generate the output dictionary
        for col in response.keys():
            out[col] = response[col]
        return out


    def __log__(self, text):
        """
        Create a log file with de date and the text
        :param text: to include in the log file
        """
        Logger(prefix=' Image Transfer').log(text)

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

    def get_transfer(self, *args, data):
        cur = self.conn.execute('SELECT * FROM transfer where {} like "*{}*" '.format(data['col'], data['value']))
        response = {}
        for col in cur:
            response[col] = cur[col]


class ConditionsNotFoundError(Exception):
    pass





