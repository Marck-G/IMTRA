from search_engine import *
import image_transfer as it
# url of image that will read the exif tags
# TODO: en el archivo reader crear una funcion que selecione solo ciertas etiquetas exif
img_url = 'img.jpeg'


def show(data):
    """
    Print map
    :param data: map to print
    :return:
    """
    for key in data.keys():
        print("{}: {}".format(key, data.get(key)))

bd = DBManager()
bd.set_db_file_folder('./search_engine')
r = Reader(img_url)
# show all data
print("="*40, "\n", "ALL")
show(r.get_data())
# set the filter to show
print("="*40, "\n", "FILTER")
filter = ('Image Make', 'EXIF ExposureTime', 'EXIF FNumber',
          'EXIF ISOSpeedRatings', 'Image Software')
show(r.get_filter_tag(filter))

tr = it.Transfer()
tr.set_base_dir('/home/marck/Pictures')
tr.set_dest_dir('/home/marck/Documents/test')
print('Inicio')
print(tr.list_dir())
def show(data):
    print(data)
print(tr.get_size())
tr.transfer_all(show)
print('Fin programa')