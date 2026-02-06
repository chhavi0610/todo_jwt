import sys
import os
from fastapi.testclient import TestClient
from main import app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ["TESTING"] = "true"


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200




def testUI():

    res = client.get("/docs")
    assert res.status_code == 200


