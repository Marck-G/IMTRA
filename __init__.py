from exifreader import reader
# url of image that will read the exif tags
# TODO: en el archivo reader crear una funcion que selecione solo ciertas etiquetas exif
img_url = 'img.jpeg'
tags = reader.read(img_url)
for key in tags.keys():
    print("{} : {}".format(key, tags.get(key)))
