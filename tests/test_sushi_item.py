import time

def test_sushi_item_crud(client):
    # CREATE
    resp = client.post("/sushi-items", json={
        "name": f"Sushi_{int(time.time())}",
        "price": 20000,
        "category": "nigiri",
        "description": "Test sushi item"
    })
    assert resp.status_code == 201
    sushi_id = resp.json["data"]["id"]

    # READ
    resp = client.get(f"/sushi-items/{sushi_id}")
    assert resp.status_code == 200

    # UPDATE
    resp = client.put(f"/sushi-items/{sushi_id}", json={"price": 25000})
    assert resp.status_code == 200

    # DELETE
    resp = client.delete(f"/sushi-items/{sushi_id}")
    assert resp.status_code == 200
