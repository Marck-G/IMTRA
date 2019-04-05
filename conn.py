
class Test:
    dic_col_tag = {
        "EXIF CreationDate": "make_date",
        "Image Make":"camera",
        "Image CameraModel":  "model",
        "EXIF IsoSpeedRatio": "iso"}
    strings = ["make_date", "model", "camera"]

    def add_item(self, map):
        insert_sql = "INSERT INTO {}({}) values({})"
        # recorremos el diccionario introducido y a su vez recuperamos el nombre de
        # la columna que le corresponde segun el diccionario
        ar_cols = [self.dic_col_tag[key] for key in map.keys()]
        cols = ",".join(ar_cols)
        # creamos un array con todos los valores, abria que mirar si se modifica el orden
        values = [map[i] for i in map.keys()]
        values = ['"{}"'.format(item) if ar_cols[i] in self.strings else item for i, item in enumerate(values)]
        # creamos la parte del value con el join
        vals = ",".join(values)
        insert_sql = insert_sql.format( cols, vals )
        return insert_sql

dic_datos = {
        "EXIF CreationDate": "20/06/2018",
        "Image Make": "Canon",
        "EXIF IsoSpeedRatio": "100"
    }


db_manager = Test()

print(db_manager.add_item(dic_datos))
