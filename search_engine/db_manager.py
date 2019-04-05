# MIT License
#
# Copyright (c) 2019 MARCK C. GUZMAN
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


class DBManager:
    """
        Class DataBase Manager
    """
    conn = sqlite3.connect("DB_INTRA.db")
    create_file = "create_database.sql"
    delete_file = "delete_database.sql"
    __instance__ = None
    __dic__ = None

    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
            return cls.__instance__

    def create_database(self):
        qry = open('create_database.sql', 'r').read()
        c = self.conn.cursor()
        c.executescript(qry)
        c.close()
        self.conn.commit()

    def delete_data_base(self):
        qry = open('delete_database.sql', 'r').read()
        c = self.conn.cursor()
        c.executescript(qry)
        c.close()
        self.conn.commit()

    def set_dic(self , dic):
        self.__dic__ =  dic

    #def add_item(self):

    def __get_db_tables__(self):
        tab_names = []
        cur = self.conn.execute("Select * from sqlite_master where type='table'")
        tab_names = [tab_name[1] for tab_name in cur]
        return tab_names

    def __get_db_colums__(self,tab_name):
        col_name = []
        cur = self.conn.execute("Select * from  {}".format(tab_name))
        tab_names = [tab_names[0] for tab_names in cur.description]
        return tab_names

#MAIN
db_manager = DBManager()
#db_manager.create_database()
tab_name = db_manager.__get_db_tables__()
col_name = db_manager.__get_db_colums__(tab_name[0])
#print("\n".join(tab_name))

for table in tab_name:
    print(table)
    print([col for col in db_manager.__get_db_colums__( table )])
