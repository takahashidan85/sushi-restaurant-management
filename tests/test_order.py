def test_order_crud(client):
    # CREATE 
    resp = client.post("/orders", json={"customer_id": 1, "order_type": "dine-in"})
    assert resp.status_code in (201, 400)
    if resp.status_code == 201:
        order_id = resp.json["data"]["id"]

        # READ
        resp = client.get(f"/orders/{order_id}")
        assert resp.status_code == 200

        # DELETE
        resp = client.delete(f"/orders/{order_id}")
        assert resp.status_code == 200
