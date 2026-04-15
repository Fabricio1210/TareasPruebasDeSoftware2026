import os
import json

def search(search: str) -> list[str]:
    cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
    with open(cities_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        cities = data["cities"]
    result = []
    if search == "*":
        return cities
    if len(search) < 2:
        return result 
    for city in cities:
        if search.lower() in city.lower():
            result.append(city)
    return result