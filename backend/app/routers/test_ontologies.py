import json
from ..test_main import client


class TestOntologiesRouter:

    def test_post_empty_ontology(self):
        response = client.post("/ontology/", json={})
        print(response.json())
        assert response.status_code == 422

    def test_post_right_ontology(self):
        payload = {
            "name": "test_ontology",
            "ontology": {
                "@id": "string",
                "@type": "Interface",
                "@context": "dtmi:dtdl:context;2",
                "comment": "string"
            }
        }
        response = client.post("/ontology/", json=payload)
        assert response.status_code == 200