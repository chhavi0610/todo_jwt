import os
os.environ["TESTING"] = "true"

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200



def testUI():

    res = client.get("/docs")
    assert res.status_code == 200


