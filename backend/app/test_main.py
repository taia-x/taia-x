from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_fetch_data():
    json_test = {
        "nft_id": "tk1",
        "sig": "edsigtwdx5PQq25GaBZj895dx5ZvKmzh1vJncsHQJgGfMz9Z5PM6GpXpKXDLnJLfdcbGHRY93CaTbvcDk3Mb7CJpusoUkmbNtAD",
        "pbkey": "edpkugjv7zR7CNiEZH8f1otn49iCzgRKeDMhuimA7djN4NQFvU76NM"
    }
    response = client.post(url="/download/1", json=json_test)
    print(response)


test_fetch_data()
