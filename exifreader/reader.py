import exifread
# reed all exif tag from image
def read(img):
    # open the img file in binary mode and only to read
    with open(img, "rb") as file:
        # set the file content to the reader
        data = exifread.process_file(file)
        # in data we have a hash map with all exif tags
        file.close()
        return data
# para seleccinar las etiquetas primero crearemos una lista y luego comprobaremos si
# la clave está en esa lista. Para la comprobación podremos utilizar 'in': if var in ('a','b')