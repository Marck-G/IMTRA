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


class DBManager:
    """
        Class DataBase Manager
    """
    conn = sqlite3.connect("DB_INTRA.db")
    create_file = "create_database.sql"
    delete_file = "delete_database.sql"
    __instance__ = None

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

    def __get_db_columns__(self, table):
        """

        :param table: table to index
        :return: the table columns name in array
        """
        # create the sql query for the table
        sql_query = "select * from {}". format(table)
        # execute the query and save the response
        response = self.conn.execute(sql_query)
        # get the cursor metadata
        columns = [col[0] for col in response.description]
        return columns

db_manager = DBManager()

# db_manager.create_database()

print(db_manager.__get_columns__("img"))