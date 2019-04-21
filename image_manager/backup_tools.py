import tarfile as tar
import os


class ImageBackup:
    __instance__ = None
    _dir = None
    _out_file = None

    # SINGLETON
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def set_dir(self, directory):
        self._dir = directory
        return self

    def set_out_file(self, name):
        self._out_file = name
        return self

    def __create_index__(self):
        with open(os.path.join(self._dir, '.index'), "w") as file:
            file.write("{\n\t'origin_dir': '%s'\n}" % self._dir)

    def compress(self):
        """
        compress the dir
        :return:
        """
        # check if all needed fields are not None
        assert self._dir is None, "No origin dir set"
        assert self._out_file is None, "No output file name set"
        # create the index
        self.__create_index__()
        # Created the compressed file
        with tar.open(self._out_file, "w:gz") as c_file:
            # list the origin directory
            for parent, directories, files in os.walk(str(self._dir)):
                for f in files:
                    file = os.path.join(parent, f)
                    # add to the compressed file
                    c_file.add(file)
