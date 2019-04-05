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
from _datetime import datetime
from os import path

class DBManager:
    """
        Class DataBase Manager
    """
    # TODO: set the proyect data estructure
    __db_file__ =  "DB_IMTRA.db"
    conn = sqlite3.connect(__db_file__)
    create_file = "create_database.sql"
    delete_file = "delete_database.sql"
    __log_file__ = "../.log"
    __instance__ = None
    __dic__ = None
    __db__ = {}

    # singleton
    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
            cls.__instance__.__db_init__()
            return cls.__instance__

    def create_database(self):
        """
        Create the database
        :return:
        """
        qry = open('create_database.sql', 'r').read()
        with self.conn.cursor() as c:
            c.executescript(qry)
            c.close()
            self.conn.commit()
            self.__log__('Created the database')
        return self

    def delete_data_base(self):
        """
        Delete the database
        :return:
        """
        qry = open('delete_database.sql', 'r').read()
        with self.conn.cursor() as c:
            c.executescript(qry)
            c.close()
            self.conn.commit()
        self.__log__('delete the database')
        return self

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
        return self

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
            self.__log__(insert)
            # execute the command
            self.conn.execute(insert)
        # save al changes
        self.conn.commit()
        return self

    def __log__(self, text):
        """
        Create a log file with de date and the text
        :param text: to include in the log file
        :return:
        """
        # open the file in append mode, the plus is for create the file if not exif
        with open(self.__log_file__, "a+") as log_file:
            line = "{}\t Search Engine: {}\n"
            date = datetime.now()
            # write in th efile
            log_file.write(line.format(date,text))

    def __exists__(self):
        """
        Check if the db exists and have its tables
        :return: boolean
        """
        # check if db file exist
        exist_file = path.exists(self.__db_file__)
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


# MAIN
db_manager = DBManager()
# db_manager.create_database()
# db_manager.delete_database()


# db_manager.create_database()

print(db_manager.__get_db_columns__("img"))
db_manager.__log__("test")
