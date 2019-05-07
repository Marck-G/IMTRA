import sqlite3 as db

class Manager:
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