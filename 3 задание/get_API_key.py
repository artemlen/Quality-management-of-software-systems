import requests

api_link = "https://petfriends1.herokuapp.com/api/key"
get_headers = {"email": "204493@edu.fa.ru", "password": "111020la"}
get_params = get_headers



def get_key(link, sett, headers):

    resp = requests.get(link, params = sett, headers = headers)
    if resp.status_code == 200:
        print("OK")

    if resp.ok:
        print("OK")

    return resp.text

print(get_key(api_link, get_params, get_headers))