import requests

post_new_pet_headers = {"auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040", "name": "philip", "animal_type": "Dog", "age": '5', "pet_photo": ""}

post_new_pet_params = post_new_pet_headers
new_pet_post_link = "https://petfriends1.herokuapp.com/api/pets"


def new_pet_post(link, post_params, post_headers):

    response = requests.post(link, params = post_params, headers = post_headers, files={"pet_photo": open('dog.jpg', 'rb')})

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text

print(new_pet_post(new_pet_post_link, post_new_pet_params, post_new_pet_headers))
