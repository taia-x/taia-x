from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200


#TODO: update test
def test_fetch_data():
    json_test = {
        "nft_id": "01",
        "sig": "edsigu2YBd7tXnM43hVq9D8zd4CXBoZ2ryBef5mx7t1sE9njNEiZRUxBpQjBaoo4gPaxRqyvzFqPrN71RNDYhVaJT6xtbYcDrXR",
        "pbkey": "edpkugjv7zR7CNiEZH8f1otn49iCzgRKeDMhuimA7djN4NQFvU76NM"
    }
    response = client.post(url="/download/1", json=json_test)
    print(response)


test_fetch_data()
