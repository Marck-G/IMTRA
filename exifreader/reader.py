import exifread;

def read(img):
    # open the img file in binary mode and only to read
    with open(img,"rb") as file:
        # set the file content to the reader
        data = exifread.process_file(file)
        # in data we have a hashmap with all exif tags
        # TODO: Select the diferent tags that we will use for the app
        for key in data.keys():
            print( "{} : {}".format(key, data.get(key)))
        return data

