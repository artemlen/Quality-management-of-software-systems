import requests


#auth_key = ключ который мы нашли
get_headers = {"auth_key ": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040", "filter": "my_pets"}

get_params = get_headers

my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


def get_list_of_pets(link, sett, headers):
    response = requests.get(link, params = sett, headers = headers)

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(get_list_of_pets(my_pets_link, get_params, get_headers))
