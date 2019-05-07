from search_engine.reader import Reader
from image_transfer.transfer import Transfer
from image_manager.autotagger import tags_from as tag

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


def tagger(pettition: dict) -> dict:
    assert pettition is not None, "No petition found"
    assert pettition['image'], "Image not found"
    return tag(pettition['image'])

def transfer(petition: dict):
    assert petition is not None, "No petition found"
    origin = petition["source"]
    target = petition["target"]
    callback = petition["callback"]
    duplicate_callback = petition["duplicate_callback"] if petition["duplicate_callback"] else None
    transfer = Transfer()
    transfer.set_base_dir(origin)
    transfer.set_dest_dir(target)
    transfer.transfer_all(callback)
    if duplicate_callback is not None and transfer.has_duplicates():
        duplicate_callback(transfer.get_duplicates())