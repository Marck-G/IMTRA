from search_engine.reader import Reader


def search(data):
    pass


def read(petition: dict) -> dict:
    assert petition is not None, "Not data found"
    key_list = petition.keys()
    assert 'image' in key_list, "Image not found in data"
    image = petition["image"]
    tag_list = petition['filter'] if 'filter' in key_list else None
    rd = Reader(image)
    out = {}
    out['image'] = image
    out['result'] = {}
    if tag_list is not None:
        _data = rd.get_filter_tag(tag_list)
        for tag in _data.keys():
            out['result'][tag] = _data[tag]
    else:
        _data = rd.get_data()
        for tag in _data.keys():
            out['result'][tag] = _data[tag]
    return out


def tagger(img):
    pass

