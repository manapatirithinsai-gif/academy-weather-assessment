import requests

# OpenWeather API key
# this should be stored securely , this is just for assessment
API_KEY = "22327dd3151e11b34134028a7d18e873"

# Maximum number of favourite cities will be allowed
MAX_FAVOURITES = 3

# List to store favourite cities (stored in memory only)
favourites = []


def get_weather(city):
    """
    This function will calls the OpenWeather API and
    returns weather details for the given city.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    weather_info = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    }

    return weather_info


   

def search_weather():
    city = input("Enter city name: ")
    weather = get_weather(city)

    if weather is None:
        print("City not found or error occurred.")
        return

    print("\nWeather Details")
    print("City:", weather["city"])
    print("Temperature:", weather["temp"], "°C")
    print("Description:", weather["desc"])


def add_favourite():
    if len(favourites) >= MAX_FAVOURITES:
        print("You can only add up to 3 favourite cities.")
        return

    city = input("Enter city to add to favourites: ")

    if city.lower() in [c.lower() for c in favourites]:
        print("City already exists in favourites.")
        return

    weather = get_weather(city)

    if weather is None:
        print("Invalid city name.")
        return

    favourites.append(weather["city"])
    print(weather["city"], "added to favourites.")


def list_favourites():
    if len(favourites) == 0:
        print("No favourite cities added.")
        return

    print("\nFavourite Cities Weather:")
    for city in favourites:
        weather = get_weather(city)
        if weather:
            print(
                weather["city"],
                "-",
                weather["temp"],
                "°C -",
                weather["desc"]
            )


def remove_favourite():
    city = input("Enter city to remove from favourites: ")

    for fav in favourites:
        if fav.lower() == city.lower():
            favourites.remove(fav)
            print(fav, "removed from favourites.")
            return

    print("City not found in favourites.")


def main():
    while True:
        print("\n--- Weather Application ---")
        print("1. Search weather by city")
        print("2. Add city to favourites")
        print("3. List favourite cities")
        print("4. Remove favourite city")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_weather()
        elif choice == "2":
            add_favourite()
        elif choice == "3":
            list_favourites()
        elif choice == "4":
            remove_favourite()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")


# Program starts here
main()
