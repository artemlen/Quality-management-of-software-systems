import pytest
import requests

# Параметры (данные)
post_simple_headers = {"auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040", "name": "Masha", "animal_type": "ovechka", "age": '10'}
post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


get_key_headers = {
    "email": "204493@edu.fa.ru",
    "password": "111020la"
}
get_key_params = get_key_headers
api_key_link = "https://petfriends1.herokuapp.com/api/key"


get_headers_my_pets = {
    "auth_key ": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040",
    "filter": "my_pets"
}
get_params_my_pets = get_headers_my_pets
my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


post_new_pet_headers = {
    "auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040",
    "name": "Evgeniy",
    "animal_type": "parrot",
    "age": '3',
    "pet_photo": ""
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


post_set_photo_headers = {
    "auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040",
    "pet_id": "8db29198-9e34-4b70-8a0c-3777e29ad035"
}
post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "8db29198-9e34-4b70-8a0c-3777e29ad035"


delete_pet_headers = {
    "auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040",
    "pet_id": "e40b4a22-5586-41a8-91f9-b490afed2708"
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "0f1b6134-dbdb-4fee-8f47-3e213895cb42"


put_info_headers = {
    "auth_key": "12f6fa2ab241920547690ea22e0123bb8299ca3f3142c746bba35040",
    "pet_id": "8db29198-9e34-4b70-8a0c-3777e29ad035"
}
put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "8db29198-9e34-4b70-8a0c-3777e29ad035"


# фикстуры
@pytest.fixture
def post_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def post_info_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('parrot.jpeg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        return True


@pytest.fixture
def put_info():
    response = requests.put(put_info_link,
                            params=put_info_params,
                            headers=put_info_headers
                            )
    return response.ok


# тесты
@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (create_pet_simple_POST_link, post_simple_params, post_simple_headers, True),


                             (new_pet_POST_link, post_new_pet_params, post_new_pet_headers, False),


                             pytest.param(set_photo_POST_link, post_set_photo_params, post_set_photo_headers, False),
                         ]
                         )
def test_post(link, params, header, expected_result):
    response = requests.post(link,
                             params=params,
                             headers=header
                             )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # get_api_key
                             (api_key_link, get_key_params, get_key_headers, True),

                             # get_pets_list
                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ]
                         )
def test_get(link, params, header, expected_result):
    response = requests.get(link,
                            params=params,
                            headers=header
                            )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ]
                         )
def test_delete(link, params, header, expected_result):
    response = requests.delete(link,
                               params=params,
                               headers=header
                               )
    assert response.ok == expected_result


def test_put(put_info):
    assert put_info == True
