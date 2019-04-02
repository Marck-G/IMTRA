# MIT License
#
# Copyright (c) 2019 MARCK C. GUZMAN
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


class SearchEngine:
    __reader__ = Reader("")
    __db_manager__ = None  # db manager
    __filter__ = None  # filter for tags
    __replace_map__ = None  # for replace the tags

    def __init__(self, db_manager):
        self.__db_manager__ = db_manager
        self.__replace_map__ = db_manager.getReplaceMap()
        self.__filter__ = db_manager.getFilter()

    def __read__(self, img):
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
        self.__db_manager__.addItem(self.__reader__.get_data())
        pass

    def __set_fiter__(self, fil):
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


class NoImageSetError(Exception):
    pass


class NoFilterSetError(Exception):
    pass


class NoReplaceMapSetError(Exception):
    pass
