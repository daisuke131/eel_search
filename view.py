import eel

import desktop
from search import search

app_name = "html"
end_point = "index.html"
size = (700, 600)


@eel.expose
def search_character(csv_name: str, search_word: str):
    search(csv_name, search_word)


desktop.start(app_name, end_point, size)
