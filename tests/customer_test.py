def test_create_customer(client):
    response = client.post("/customers/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_get_customer(client):
    created = client.post("/customers/", json={"name": "Bob", "email": "bob@example.com"}).get_json()
    response = client.get(f"/customers/{created['id']}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == created["id"]


def test_update_customer(client):
    created = client.post("/customers/", json={"name": "Charlie", "email": "charlie@example.com"}).get_json()
    response = client.put(f"/customers/{created['id']}", json={"name": "Charlie Updated", "email": "newcharlie@example.com"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Charlie Updated"


def test_delete_customer(client):
    created = client.post("/customers/", json={"name": "Dave", "email": "dave@example.com"}).get_json()
    response = client.delete(f"/customers/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "deleted"
