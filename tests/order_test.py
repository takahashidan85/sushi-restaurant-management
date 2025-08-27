def test_create_order(client):
    customer = client.post("/customers/", json={"name": "Alice", "email": "alice@example.com"}).get_json()
    response = client.post("/orders/", json={"customer_id": customer["id"]})
    assert response.status_code == 201
    assert response.get_json()["customer_id"] == customer["id"]


def test_get_order(client):
    customer = client.post("/customers/", json={"name": "Bob", "email": "bob@example.com"}).get_json()
    created = client.post("/orders/", json={"customer_id": customer["id"]}).get_json()
    response = client.get(f"/orders/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["id"] == created["id"]


def test_update_order(client):
    customer = client.post("/customers/", json={"name": "Charlie", "email": "charlie@example.com"}).get_json()
    created = client.post("/orders/", json={"customer_id": customer["id"]}).get_json()
    response = client.put(f"/orders/{created['id']}", json={"customer_id": customer["id"]})
    assert response.status_code == 200
    assert response.get_json()["id"] == created["id"]


def test_delete_order(client):
    customer = client.post("/customers/", json={"name": "Dave", "email": "dave@example.com"}).get_json()
    created = client.post("/orders/", json={"customer_id": customer["id"]}).get_json()
    response = client.delete(f"/orders/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "deleted"
