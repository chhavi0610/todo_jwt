import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def testroot():

    res = client.get("/")
    assert res.status_code == 200


def testUI():

    res = client.get("/docs")
    assert res.status_code == 200


