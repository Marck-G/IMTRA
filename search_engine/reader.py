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
import exifread


class Reader:
    """
    Class for work with exif tags
    """
    data = None

    def __init__(self, img):
        self.image = img
    # reed all exif tag from image

    def __read__(self):
        """
        Read the image exif tags
        """
        # open the img file in binary mode and only to read
        with open(self.image, "rb") as file:
            # set the file content to the reader
            self.data = exifread.process_file(file)
            # in data we have a hash map with all exif tags
            file.close()

    def get_data(self) -> dict:
        """
        :return: full image exif tags
        """
        if self.data is None:
            self.__read__()
        return self.data

    def set_image(self, img):
        self.image = img
        self.data = None

    def get_filter_tag(self, filter_list: list) -> dict:
        """:param filter_list list of tags to return
        :return map with the requires tags and values
        """
        if filter_list is None:
            return -1
        map_out = {}
        for key in self.get_data():
            if key in filter_list:
                map_out[key] = self.get_data().get(key)
        if len(map_out.keys()) == 0:
            return None
        return map_out

    def key_replace(self, map, apply=False):
        """
        Replace the original key of the data map to the passed key
        :param map: hash map with the original and new keys -> {original_key: new_key}
        :param apply: if we want to apply the change in the current object
        :return: the map with the news keys
        """
        if map is None:
            raise NoMapSetError("Need a map with the key to replace")
        temp_map = {}
        for key in map:
            temp_map[map[key]] = self.get_data()[key]
        # apply change for the object if dev want
        if apply:
            self.data = temp_map
        return temp_map


class NoMapSetError(Exception):
    pass
