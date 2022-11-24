# from django.http.response import JsonResponse
import requests
import json

def get_movie_Data() :
    TMDB_API_KEY = "b490976b819d28133d6448f4ef4ef0d8"

    for i in range(1, 2):
        request_url_up = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko"

        movies = requests.get(request_url_up).json()
        result = []

        for movie in movies["results"] :
            data = {}
            data["pk"] = movie["id"]
            data["model"] = "movies.movie"
            movie_key = movie["id"]
            fields = {}
            fields["popularity"] = movie["popularity"]
            fields["overview"] = movie["overview"]
            fields["title"] = movie["title"]
            fields["release_date"] = movie["release_date"]
            fields["vote_average"] = movie["vote_average"]
            fields["genre_ids"] = movie["genre_ids"]
            fields["poster_path"] = movie["poster_path"]
            # video_path 가져오기
            request_videos = f"https://api.themoviedb.org/3/movie/{movie_key}/videos?api_key={TMDB_API_KEY}&append_to_response=videos&language=ko"
            videos = requests.get(request_videos).json()
            if videos["results"] :
                fields["video_path"] = videos["results"][0].get("key")
            else :
                continue
            # key_word 가져오기
            request_keywords = f"https://api.themoviedb.org/3/movie/{movie_key}/keywords?api_key={TMDB_API_KEY}&append_to_response=videos&language=ko"
            keywords = requests.get(request_keywords).json()
            keyword_data = []
            if keywords["keywords"] :
                tmp = len(keywords["keywords"])
                for i in range(tmp):
                    keyword_data.append(keywords["keywords"][i]["name"])
            fields["keywords"] = keyword_data

            data["fields"] = fields
            result.append(data)
            
    return result

with open('../makejson/movie_list.json', 'w', encoding="UTF-8") as f :
    json.dump(get_movie_Data(), f, ensure_ascii=False, indent=2)