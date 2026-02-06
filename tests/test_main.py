from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def testroot():

    res = client.get("/")
    assert res.status_code == 200


def testUI():

    res = client.get("/docs")
    assert res.status_code == 200


