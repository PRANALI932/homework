# Dictionary of 2025 movies
movies_2025 = {
    "Captain America: Brave New World": {
        "genre": "Superhero",
        "director": "Julius Onah",
        "year": 2025
    },
    "Mission: Impossible – The Final Reckoning": {
        "genre": "Action",
        "director": "Christopher McQuarrie",
        "year": 2025
    },
    
    
    "Jurassic World Rebirth": {
        "genre": "Sci-Fi / Adventure",
        "director": "Gareth Edwards",
        "year": 2025
    },
    "Avatar: Fire and Ash": {
        "genre": "Science Fiction",
        "director": "James Cameron",
        "year": 2025
    }
}

# 1️⃣ Using keys()
print("---- Using keys() ----")
for movie in movies_2025.keys():
    print(movie)

# 2️⃣ Using values()
print("\n---- Using values() ----")
for details in movies_2025.values():
    print(details)

# 3️⃣ Using items()
print("\n---- Using items() ----")
for movie, details in movies_2025.items():
    print(movie, "->", details)

# 4️⃣ Using get()
print("\n---- Using get() ----")
movie_name = "Avatar: Fire and Ash"
details = movies_2025.get(movie_name)

if details:
    print("Movie:", movie_name)
    print("Genre:", details.get("genre"))
    print("Director:", details.get("director"))
    print("Year:", details.get("year"))