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
    # TODO: set the proyect data estructure
    conn = sqlite3.connect("DB_INTRA.db")
    create_file = "create_database.sql"
    delete_file = "delete_database.sql"
    __instance__ = None
    __dic__ = None
    __db__ = {}

    # singleton
    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
            return cls.__instance__

    def create_database(self):
        """
        Create the database
        :return:
        """
        qry = open('create_database.sql', 'r').read()
        c = self.conn.cursor()
        c.executescript(qry)
        c.close()
        self.conn.commit()

    def delete_data_base(self):
        """
        Delete the database
        :return:
        """
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
        """
        Set the EXIF tag: columns dictionary
        :param dic:
        """
        self.__dic__ = dic

    def __get_db_tables__(self):
        """
        :return: all db tables in array
        """
        # the query to execute
        cur = self.conn.execute("Select * from sqlite_master where type='table'")
        # get the array with the tab names
        tab_names = [tab_name[1] for tab_name in cur]
        return tab_names

    def __make_dic__(self):
        """
        Create the database dictionary
        :return:
        """
        for table in self.__get_db_tables__():
            self.__db__[table] = self.__get_db_columns__(table)

    def add_item(self, dic):
        """
        Insert data into database from data dictionary
        :param dic: data to insert in db
        :return:
        """
        # general insert into string
        insert_sql = "INSERT INTO {}({}) values({})"
        # get the db columns that match with the dict keys
        arr_cols = [self.__dic__[tag] for tag in dic.keys()]
        # we create a dictionary with the column name and the value
        value_dic = {}
        for i, key in enumerate(dic.keys()):
            value_dic[arr_cols[i]] = dic[key]
        # we want to create a dictionary with the table_name and the before dictionary
        # { table1 : { col1 : value, col2: value2}, table2: { col1: value, col2: value2} }
        dici = {}
        for col in arr_cols:
            for table in self.__db__.keys():
                # if the current col is in the tables' columns update the dictionary entry
                if col in self.__db__[table]:
                    dici[table].update({col: value_dic[col]})
        for table in dici:
            # create the insert query for each table
            insert = insert_sql.format(table, ",".join(table.keys()), ",".join(table.values()))
            # execute the command
            self.conn.execute(insert)
        # save al changes
        self.conn.commit()


# MAIN
db_manager = DBManager()
# db_manager.create_database()
# db_manager.delete_database()


# db_manager.create_database()

print(db_manager.__get_db_columns__("img"))
for table in tab_name:
    print(table)
    print([col for col in db_manager.__get_db_columns__(table)])
