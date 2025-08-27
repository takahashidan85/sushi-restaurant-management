def test_create_menu_and_list(client):
    rv = client.post('/api/menu/', json={'name': 'Tuna Roll', 'price': 6.0, 'category': 'rolls'})
    assert rv.status_code == 201
    d = rv.get_json()
    assert d['name'] == 'Tuna Roll'
    assert d['price'] == 6.0

    rv2 = client.get('/api/menu/')
    assert rv2.status_code == 200
    items = rv2.get_json()
    assert isinstance(items, list)
    assert len(items) == 1
