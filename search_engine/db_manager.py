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
    __dic__ = None
    __db__ = {}

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

    def set_dic(self, dic):
        self.__dic__ = dic

    def __get_db_tables__(self):
        """
        :return: all db tables in array
        """
        # the query to execute
        cur = self.conn.execute(
            "Select * from sqlite_master where type='table'")
        # get the array with the tab names
        tab_names = [tab_name[1] for tab_name in cur]
        return tab_names

    def __get_db_colums__(self, tab_name):
        cur = self.conn.execute("Select * from  {}".format(tab_name))
        tab_names = [tab_names[0] for tab_names in cur.description]
        return tab_names

    def __make_dic__(self):
        for table in self.__get_db_tables__():
            self.__db__[table] = self.__get_db_colums__(table)

    def add_item(self, dic):
        insert_sql = "INSERT INTO {}({}) values({})"
        arr_cols = [self.__dic__[tag] for tag in dic.keys()]
        value_dic = {}
        for i, key in enumerate(dic.keys()):
            value_dic[arr_cols[i]] = dic[key]
        camera_tab = []
        dici = {}
        for col in arr_cols:
            for table in self.__db__.keys():
                if col in self.__db__[table]:
                    dici[table].update({col: value_dic[col]})

        for table in dici:
            insert = insert_sql.format(table, ",".join(
                table.keys()), ",".join(table.values()))
            self.conn.execute(insert)

        self.conn.commit()


# MAIN
db_manager = DBManager()
# db_manager.create_database()
# db_manager.delete_database()


# db_manager.create_database()

print(db_manager.__get_columns__("img"))
for table in tab_name:
    print(table)
    print([col for col in db_manager.__get_db_colums__(table)])
