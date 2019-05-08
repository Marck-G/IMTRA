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


class Manager:
    """
            Class DataBase Manager
    """
    # TODO: set the proyect data estructure

    __db_create__ = 'imtr.cre.db.sql'
    __db_delete__ = 'imtr.cre.db.sql'
    __bd_name__ = 'transfer.db'
    conn = db.connect()
    __instance__ = None

    # SINGLETON
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def create_db(self):
        pass

    def delete_db(self):
        pass

    def save_item(self, data: dict):
        """
        Recive un diccionario con los datos y se guardan en la base de datos
        :param data: diccionario con la estructura: { origin: origen, dest: destino, date : fecha}
        :return:
        """
        pass

    def get_item(self) -> dict:
        # realiza la consulta y coge los 5 primeros elementos de la consulta
        # el resultado será en
        pass
