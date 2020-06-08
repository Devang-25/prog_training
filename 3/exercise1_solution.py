import requests

def get_category():
    url = "https://api.chucknorris.io/jokes/categories"
    category = requests.get(url)
    category = category.json()
    return category

def get_joke(category):
    url = "https://api.chucknorris.io/jokes/random"
    params = {"category":category}
    joke = requests.get(url, params=params)
    joke = joke.json()
    return joke["value"]

while True:
    print("Welcome to the Chuck Norris joke application!")
    print("Available categories:")
    categories = get_category()
    i = 1
    for category in categories:
        print("{}. {}".format(i, category))
        i = i+1
    selection = input("Which category joke would you like to hear? Select a number! ")
    try:
        selection = int(selection)
        joke = get_joke(categories[selection-1])
        print("Here is your joke:")
        print(joke)
    except ValueError:
        print("You need to select a number")
        continue
    except IndexError:
        print("You need to select a category from the list!")
        continue

    selection = input("Would you like to hear another joke? (yes/no) ")
    if selection == "yes":
        continue
    else:
        break
