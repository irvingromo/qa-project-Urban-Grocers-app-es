import sender_stand_request
import data


# Función para obtener el token de un nuevo usuario
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json().get("authToken")


# Función para cambiar el nombre en el cuerpo del kit
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Funciones de aserción (positiva y negativa)
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400

# Prueba 1: 1 caracter
def test_1_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


# Prueba 2: 511 caracteres
def test_2_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)


# Prueba 3: 0 caracteres
def test_3_create_kit_0_letters_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


# Prueba 4: 512 caracteres
def test_4_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)


# Prueba 5: Caracteres especiales
def test_5_create_kit_special_characters_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)


# Prueba 6: Espacios permitidos
def test_6_create_kit_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)


# Prueba 7: Números permitidos (como string)
def test_7_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)


# Prueba 8: El parámetro no se pasa
def test_8_create_kit_no_name_get_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)


# Prueba 9: Tipo de parámetro diferente (número en lugar de string)
def test_9_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
