import requests
import os
from db_handler import WriteData

# ---- API SECTION ------------- #
MOVIE_SEARCH = "https://api.themoviedb.org/3/search/movie"
ID_SEARCH = "https://api.themoviedb.org/3/movie/"

API_KEY = os.environ['YOUR-API-KEY']

def MovieSearch(title):
    parameters = {
        "api_key": API_KEY,
        "query": title
    }

    response = requests.get(url=MOVIE_SEARCH, params=parameters)
    movies_dict = {}

    for item in response.json()["results"]:
        try:
            if len(item["release_date"]) > 1:
                movies_dict[item["id"]] = {"title": item["original_title"], "date": item["release_date"]}
        except KeyError:
            pass
        
    return movies_dict

def IdSearch(id):

    parameters = {
        "api_key": API_KEY,
    }

    img_url_head = "https://image.tmdb.org/t/p/w500/"
    response = requests.get(url=ID_SEARCH+id,params=parameters)
    result = response.json()

    # During this stage we add the selected movie to the database
    row_id = WriteData(title=result["original_title"],
                year=result["release_date"],
                descr=result["overview"],
                ranking=0,
                rating=0,
                review="Write a review!",
                img_url=img_url_head+result["poster_path"])

    return row_id
# ------------------------------ #