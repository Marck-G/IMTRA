window.inputs = (options) => {
    let _class = 'file-btn';
    let watcher_attr = 'watcher'
    if (options) {
        _class = options.target ? options.target : _class;
        watcher_attr = options.watcher ? options.watcher : watcher_attr;
    }

    // get all elements with the class
    let elements = document.getElementsByClassName(_class);
    for (let i = 0; i < elements.length; i++) {
        let e = elements[i];
        let watcher = {};
        watcher.id = e.getAttribute(watcher_attr) ? e.getAttribute(watcher_attr) : false;
        e.onclick = evt => {
            // we send the petition to python
            eel.folder_input(watcher.id);
        }
    }
}

eel.expose(watcher);
function watcher(id, content) {
    let target = document.getElementById(id);
    target.value = content;
}