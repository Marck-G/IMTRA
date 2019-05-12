import eel as app
from gui import show_dir_chouser as select_dir


app.init('views')

@app.expose
def chouse_folder(targe, title='Selection', initialdir=False):
    directory = select_dir(title=title, initialdir= None if not initialdir else initialdir )
    set_by_id(targe, str(directory))


def set_by_id(id, content):
    app.setById(id, content)