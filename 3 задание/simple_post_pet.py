import requests



post_simple_headers = { "auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040", "name": "Vasiliy", "animal_type": "Cat", "age": '1'}

create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"

post_simple_sett = post_simple_headers



def post_simple_pet(link, post_sett, post_headers):
    response = requests.post(link, params = post_sett, headers=post_headers)

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_sett, post_simple_headers))

