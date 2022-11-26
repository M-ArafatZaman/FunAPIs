
"""
Test the /ping/ route
"""
def test_ping(client):
    response = client.get("/ping/")
    print(response)

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json.get("status") == "OK"
