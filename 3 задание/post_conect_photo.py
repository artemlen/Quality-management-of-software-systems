import requests

id = "e40b4a22-5586-41a8-91f9-b490afed2708"
post_conect_photo_headers = {"auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040","pet_id": id}

post_conect_photo_params = post_conect_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + id


def post_conect_photo(link, post_params, post_headers):

    response = requests.post(link, params=post_params, headers=post_headers,files={"pet_photo": open('cat.jpg', 'rb')})

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_conect_photo(set_photo_POST_link, post_conect_photo_params, post_conect_photo_headers))
