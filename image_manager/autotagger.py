from clarifai.rest import ClarifaiApp
from image_manager.__api__ import API_KEY


async def tags_from(img):
    """
    get tags from image using an api rest
    :param img:
    :return: dictionary with the tags
    """
    app = ClarifaiApp(api_key=API_KEY)
    model = app.public_models.general_model
    res = model.predict_by_filename(img)
    out = {}
    try:
        for tag in res["outputs"][0]["data"]["concepts"]:
            out[tag["name"]] = tag["value"]
        return out
    except Exception:
        return None
