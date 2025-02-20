import requests
import pytest

login_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

@pytest.mark.api
def test_get_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 201 or 200 or 204

@pytest.mark.api
def test_login_user():
    response = requests.post("https://reqres.in/api/login", json=login_payload)
    assert response.status_code == 201 or 200 or 204

    data = response.json()
    
    assert "token" in data, "Login does not contain token"
    print(f"Login successful! Token: {data['token']}") 
 
@pytest.mark.parametrize("payload", [
    {"email": "eve.holt@reqres.in", "password": "wrongpassword"},
    {"email": "eve.holt@reqres.in"}
])

@pytest.mark.api
def test_failed_login(payload):
    response = requests.post("https://reqres.in/api/login", json=payload)
    assert response.status_code == 400 or 401 or 404
    
    data = response.json()
    assert "error" in data and data["error"], "ERROR NOT FOUND"