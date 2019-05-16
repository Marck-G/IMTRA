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

# MANAGER
from .reader import Reader
from .db_manager import DBManager


class SearchEngine:
    __reader__ = Reader("")
    __filter__ = None  # filter for tags
    __replace_map__ = None  # for replace the tags
    __column_separator__ = ";"
    __value_separator__ = ":"
    __replaces_key__ = []

    def __init__(self):
        self.__db_manager__ = DBManager()
        self.set_replace_map(db_manager.getReplaceMap())
        self.__filter__ = db_manager.getFilter()

    def __read__(self, img):
        """
        Read the img EXIF Tags
        :param img: image url
        :return:
        """
        if img is None:
            raise NoImageSetError("Image not set for read the EXIF tags. Search Engine Error!")

        # set the image to read
        self.__reader__.set_image(img)
        if self.__filter__ is not None:
            # read the tags and return the data
            return self.__reader__.get_filter_tag(self.__filter__)
        else:
            return self.__reader__.get_data()

    def __db_store__(self):
        self.__db_manager__.add_item(self.__reader__.get_data())

    def set_filter(self, fil: list):
        if fil is None:
            raise NoImageSetError("No Filter found. Search Engine Error!")
        self.__filter__ = fil

    def process_image(self, img):
        # when read all data save in the object __reader__
        self.__read__(img)
        if self.__replace_map__ is not None:
            self.__reader__.key_replace(self.__replace_map__, True)
        self.__db_store__()
        pass

    def set_replace_map(self, map):
        if map is None:
            raise NoReplaceMapSetError("Need a replace Map. Search Engine Error!")
        self.__replace_map__ = map
        for key in map:
            self.__replaces_key__.append(map[key])

    def search(self, data: dict):
        """
        with the dictionary make the database request and return the images ids
        :param data: search dict
        :return: list with the images referenced id
        """
        table = data['table']
        if table == 'lens':
            return self.__db_manager__.get_lens(data= data)
        if table == 'camera':
            return self.__db_manager__.get_camera(data=data)
        if table == 'studio':
            return self.__db_manager__.get_img_studio(data=data)
        if table == 'gps':
            return self.__db_manager__.get_gps(latitude=data['lat'], longitude=data['log'])
        if table == 'place':
            return self.__db_manager__.get_place(data=data)


class NoImageSetError(Exception):
    pass


class NoFilterSetError(Exception):
    pass


class NoReplaceMapSetError(Exception):
    pass
