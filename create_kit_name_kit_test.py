import sender_stand_request
import data

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json().get("authToken")

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def assert_positive_response(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def assert_negative_response_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    assert response.status_code == 400


def test_1_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    assert_positive_response(kit_body)

def test_2_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    assert_positive_response(kit_body)

def test_3_create_kit_0_letters_in_name_get_error_response():
    kit_body = get_kit_body("")
    assert_negative_response_400(kit_body)

def test_4_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    assert_negative_response_400(kit_body)

def test_5_create_kit_special_characters_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")
    assert_positive_response(kit_body)

def test_6_create_kit_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    assert_positive_response(kit_body)

def test_7_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    assert_positive_response(kit_body)

def test_8_create_kit_no_name_get_error_response():
    kit_body = {} 
    assert_negative_response_400(kit_body)

def test_9_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    assert_negative_response_400(kit_body)
