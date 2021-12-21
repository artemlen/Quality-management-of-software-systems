import requests

id = "e40b4a22-5586-41a8-91f9-b490afed2708"
put_inf_headers = {"auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040", "pet_id": id}

put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + id

put_inf_params = put_inf_headers



def put_pet_info(link, p_params, p_headers):
    response = requests.put(link, params=p_params, headers=p_headers)
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_inf_params, put_inf_headers))
