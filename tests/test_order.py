def test_create_order_and_add_item(client):
    # create menu item
    rv = client.post('/api/menu/', json={'name': 'Salmon Nigiri', 'price': 3.5, 'category': 'nigiri'})
    assert rv.status_code == 201
    item = rv.get_json()
    item_id = item['id']

    # create order
    rv2 = client.post('/api/orders/', json={'table_number': 5})
    assert rv2.status_code == 201
    order = rv2.get_json()
    order_id = order['id']

    # add item
    rv3 = client.post(f'/api/orders/{order_id}/items', json={'menu_item_id': item_id, 'quantity': 2})
    assert rv3.status_code == 200
    res = rv3.get_json()
    assert 'total' in res
    assert res['total'] > 0
