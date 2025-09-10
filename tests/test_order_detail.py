def test_order_detail_list(client):
    resp = client.get("/order-details")
    assert resp.status_code == 200
    assert "data" in resp.json
