from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_url():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Welcome!"}


def test_specific_groups():
    res = client.get("/api/v1/group/tag22")
    assert res.status_code == 200
    assert res.json() == [{
        "group": {
            "id": "60e9b739284e60e0d45bbda4",
            "name": "TAG22",
            "vendor_des": "Recorded Future",
            "target_sector": ["Academia","Telecom","Research Institutes"],
            "target_locale": ["Philippines","Taiwan","Nepal"],
            "attrib_country": "China",
            "first_seen": "Sep 2020",
            "malware": ["ShadowPad","Winnti","Spyder","Cobalt Strike"],

            }
        }]

#TODO test for bad values 
