import os
class Transfer:
    __base_dir__ = ''
    __dest_dir__ = ''
    __ext_file__ = 'f.ext'
    __extensions__ = None

    def __mkdir__(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)
        return self

    def set_base_dir(self, dir):
        self.__base_dir__ = dir
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
        list = []
        for r, d, f in os.walk(self.__base_dir__):
            for file in f:
                for ext in self.read_extension():
                    if file.endswith(ext):
                        list.append(os.path.join(r,file))
        return list
p = Transfer()
p.set_base_dir('/home/marck/Downloads')
print(p.list_dir())
