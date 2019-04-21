from datetime import datetime


class Logger:
    """
    Generate the log file with all the app info
    """
    __instance__ = None
    output_file = None
    prefix = None

    # SINGLETON
    def __new__(cls, *args, output_file=False, prefix=False):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        if output_file:
            cls.__instance__.output_file = output_file
        if prefix:
            cls.__instance__.prefix = prefix
        return cls.__instance__

    def log(self, msg):
        with open(self.output_file, "a+") as out:
            line = "{}\t {}: {}\n"
            date = datetime.now()
            w = line.format( date, self.prefix, msg)
            out.writelines(w)
