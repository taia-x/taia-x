from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_fetch_data():
    json_test = {
        "nft_id": "2",
        "sig": "edsigu4f3h8i2vp29D91c3HJQgjsyNRieYUY1AsVw7Cx1n1N7Dn6YcCRFJ9mktXoTyDmLKojdnLW4UgXb5V5U9xDbM26fEtkvaG",
        "pbkey": "edpkv2PkEkoaYN9KP769GrFgshMoVn8cvHUuYVUkogxiqZMctxPbB8",
        "message": "050132"
    }
    response = client.post(url="/download/1", json=json_test)
    print(response)


test_fetch_data()
