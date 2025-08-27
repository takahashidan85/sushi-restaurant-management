def test_create_sushi_item(client):
    response = client.post("/sushi_items/", json={"name": "Salmon Roll", "price": 12.5})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Salmon Roll"


def test_get_sushi_item(client):
    created = client.post("/sushi_items/", json={"name": "Tuna Roll", "price": 10.0}).get_json()
    response = client.get(f"/sushi_items/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["id"] == created["id"]


def test_update_sushi_item(client):
    created = client.post("/sushi_items/", json={"name": "Eel Roll", "price": 15.0}).get_json()
    response = client.put(f"/sushi_items/{created['id']}", json={"name": "Eel Roll Deluxe", "price": 18.0})
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Eel Roll Deluxe"
    assert data["price"] == 18.0


def test_delete_sushi_item(client):
    created = client.post("/sushi_items/", json={"name": "Tempura Roll", "price": 20.0}).get_json()
    response = client.delete(f"/sushi_items/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "deleted"
