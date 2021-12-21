import requests

#pet_id можно найти запустив get_list_of_pets.py

id = "8775a9bf-2290-46cd-9167-c1177c27fcee"
delete_headers = {"auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040", "pet_id": id}

delete_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + id

delete_params = delete_headers

def delete_pet(link, del_params, del_headers):
    response = requests.delete(link, params = del_params, headers = del_headers)
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(delete_pet_link, delete_params, delete_headers))
