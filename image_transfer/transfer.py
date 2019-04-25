import os
import datetime
from search_engine import reader
from utils.logger import Logger
from image_transfer.data_interpreter import dir as DIR

class Transfer:
    __name__ = 'Image Transfer Module'
    __base_dir__ = None
    __dest_dir__ = None
    __ext_file__ = 'f.ext'
    __extensions__ = None # list with allowed extension
    __imgs__ = None # list of base dir img
    __dirs_format__ = None

    duplicated_images = []

    def __mkdir__(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
        return self

    def set_base_dir(self, dir):
        self.__base_dir__ = dir
        # if dir not exists raise an error
        if not os.path.exists(dir):
            Logger(prefix=self.__name__).log('Dir {} not found'.format(str(dir)))
            raise FileNotFoundError('Dir {} not found'.format(str(dir)))
        self.__imgs__ = None  # reset the file list
        self.duplicated_images = []  # reset the duplicate images
        return self

    def set_transfer_format(self, format):
        self.__dirs_format__ = format
        return self

    def set_dest_dir(self, dir):
        self.__dest_dir__ = dir
        return self

    def read_extension(self):
        """
        read the extension file
        :return: list with all allowed extensions
        """
        if self.__extensions__ is not None:
            return self.__extensions__
        lines = []
        with open(self.__ext_file__, 'r') as ext:
            for e in ext.readlines():
                lines.append(e.replace('\n',''))

        return lines

    def list_dir(self):
        """
        List the base dir attending the extension that are allowed
        :return: list with files' path
        """
        if self.__imgs__ is not None:
            return self.__imgs__
        else:
            list = []
            for r, d, f in os.walk(self.__base_dir__):
                for file in f:
                    for ext in self.read_extension():
                        if file.lower().endswith(ext.lower()):
                            list.append(os.path.join(r,file))
            self.__imgs__ = list
            return list

    def __read_date__(self, img):
        """
        Search in image metadata data and if there not found nothing read the file creation date
        :param img: to read the date
        :return: the image date
        """
        rdr = reader.Reader(img)
        result = rdr.get_filter_tag(['Image DateTime', 'EXIF DateTimeOriginal'])
        if result is None or len(result.keys()) == 0:
            date = os.path.getctime(img)
            date = datetime.datetime.fromtimestamp(date)
            return date.__str__()
        if len(result) == 2:
            return result['EXIF DateTimeOriginal']
        else:
            return result['Image DateTime']

    def __exists_img__(self, img):
        return os.path.exists(img)

    def hasDuplicates(self):
        return self.duplicated_images is not None and len(self.duplicated_images) != 0

    def get_duplicates(self):
        return self.duplicated_images

    def get_size(self):
        """
        :return: the total file in the origin folder
        """
        return len(self.list_dir())



    def transfer(self, image):
        """
        transfer one image
        :param image: the image to transfer
        :return if there are duplicate images
        """
        if self.__base_dir__ is None:
            raise self.BaseErrorNotFoundError("The origin directory must set", Logger(prefix=self.__name__))
        if self.__dest_dir__ is None:
            raise self.DestErrorNotFoundError("The destination directory must set", Logger(prefix=self.__name__))
        date = self.__read_date__(image)
        dest_dir = self.__dest_dir__ + DIR(date)
        img = image.split(os.path.sep)
        # get the last part of the split
        img = img[len(img) - 1]
        img = os.path.join(dest_dir, img)
        # check if exist in the destination folder
        exists = self.__exists_img__(img)
        if exists:
            # add to the duplicate list
            self.duplicated_images.append(img)
        else:
            self.__mkdir__(dest_dir)
            with open(image, "rb") as _input:
                with open(img, "wb") as _output:
                    size = os.path.getsize(image)
                    _output.write(_input.read(size))

    def transfer_all(self, callback):
        for i, image in enumerate(self.list_dir()):
            try:
                self.transfer(image)
                callback( {"image": image,
                       "status": "ok",
                       "number": i + 1,
                       "total": self.get_size()})
            except Exception as e:
                callback(  {"image": image,
                       "status": "error",
                       "number": i + 1,
                       "total": self.get_size(),
                       "error": e})

    class BaseErrorNotFoundError (Exception):
        def __init__(self, msg, log):
            Exception.__init__(msg)
            log.log("{} {}".format(self.__class__.__name__, msg))

    class DestErrorNotFoundError (Exception):
        def __init__(self, msg, log):
            Exception.__init__(msg)
            log.log("{} {}".format(self.__class__.__name__, msg))
