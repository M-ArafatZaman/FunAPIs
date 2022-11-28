
"""
Test the api/barplot/ route 
"""
def test_barplot(client):

    # Test without any data
    expect_400 = client.get("/api/barplot/")

    assert expect_400.status_code == 400

