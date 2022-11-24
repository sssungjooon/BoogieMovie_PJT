import requests
import json

def get_genre_Data() :
    TMDB_API_KEY = "b490976b819d28133d6448f4ef4ef0d8"

    # 우선 모든 장르부터 받자
    result = []
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko"
    genre_get = requests.get(genre_url).json()

    for gen in genre_get["genres"] :
        data = {}
        # data["genre_id"] = gen["id"]
        data["genre_id"] = gen["id"]
        data["model"] = "movies.genre"
        fields = {
            "name" : gen["name"]
        }
        data["fields"] = fields
        result.append(data)

    return result

with open('../movies/fixtures/genre_list.json', 'w', encoding="UTF-8") as f :
    json.dump(get_genre_Data(), f, ensure_ascii=False, indent=2)