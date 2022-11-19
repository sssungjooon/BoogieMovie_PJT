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
            data["id"] = movie["id"]
            data["model"] = "movies.movie"
            movie_key = movie["id"]
            fields = {}
            fields["title"] = movie["title"]
            fields["overview"] = movie["overview"]
            fields["genres"] = movie["genre_ids"]
            fields["release_date"] = movie["release_date"]
            fields["vote_count"] = movie["vote_count"]
            fields["vote_average"] = movie["vote_average"]
            # 배우 정보 가져오기 
            request_credits = f"https://api.themoviedb.org/3/movie/{movie_key}/credits?api_key={TMDB_API_KEY}&append_to_response=videos&language=ko"
            credits = requests.get(request_credits).json()
            actors_total = []
            actors = []
            for i in range(5):
                # 배우 id 번호만 장르처럼 movies에 넣고, 다른 정보들은 model에 넣기
                actors.append(credits["cast"][i]["id"])
                actor_data = {}
                actor_data["actor_id"] = credits["cast"][i]["id"]
                #actor_data["pk"] = credits["cast"][i]["id"]
                actor_data["model"] = "movies.actor"
                # 배우 사진 주소를 넣기
                photo = credits["cast"][i]["profile_path"]
                profile_paths = f"https://image.tmdb.org/t/p/original{photo}"
                actor_data["fields"] = {
                    "name" : credits["cast"][i]["name"],
                    "profile_path" : profile_paths,
                }
                actors_total.append(actor_data)
            fields["actor_ids"] = actors

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
            # 키워드 정보를 담아서 모델로 넣을 키워드 토탈
            keywords_total = []
            # 키워드 번호로 담을 키워드넘
            keywords_num = []
            if keywords["keywords"] :
                tmp = len(keywords["keywords"])
                for i in range(tmp):
                    # 숫자만 키워드넘에 넣고
                    keywords_num.append(keywords["keywords"][i]["id"])
                    keyword_data = {}
                    keyword_data["keyword_id"] = keywords["keywords"][i]["id"]
                    #keyword_data["pk"] = keywords["keywords"][i]["id"]
                    keyword_data["model"] = "movies.keyword"
                    keyword_data["fields"] = {"name" : keywords["keywords"][i]["name"] }
                    keywords_total.append(keyword_data)
                    
            fields["keywords"] = keywords_num

            data["fields"] = fields
            # 배우정보도 따로 배우모델에 넣기
            result.append(actors_total)
            # 키워드 정보도 따로 키워드 모델에 넣기
            result.append(keywords_total)
            result.append(data)
            
    return result

with open('../movies/fixtures/movies_movie.json', 'w', encoding="UTF-8") as f :
    json.dump(get_movie_Data(), f, ensure_ascii=False, indent=2)