import time

def test_customer_crud(client):
    # CREATE
    resp = client.post("/customers", json={
        "name": "Alice",
        "email": f"alice_{int(time.time())}@example.com"
    })
    assert resp.status_code == 201
    customer_id = resp.json["data"]["id"]

    # READ
    resp = client.get(f"/customers/{customer_id}")
    assert resp.status_code == 200

    # DELETE
    resp = client.delete(f"/customers/{customer_id}")
    assert resp.status_code == 200
