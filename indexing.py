from elasticsearch import Elasticsearch
from faker import Faker

import json
import random
import time

def index_doc(es_client, index, doc_type, record):
    es_client.index(index=index, doc_type=doc_type, body=record)

def search(es_client, index, lat, lon):
    search_object = {
        "query": {
            "bool": {
                "must": {
                    "match_all": {}
                },
                "filter": {
                    "geo_distance": {
                        "distance": "1km",
                        "point": {
                            "lat": lat,
                            "lon": lon
                        }
                    }
                }
            }
        }
    }

    return es_client.search(index=index, body=json.dumps(search_object))

if __name__ == "__main__":
    es = Elasticsearch([{"host": "localhost", "port": 9200}])
    fake = Faker()
    backoff_base = 2
    backoff_exp = 0

    while not es.ping():
        print("Could not connect, waiting off...")
        time.sleep(backoff_base ** backoff_exp)
        es = Elasticsearch([{"host": "localhost", "port": 9200}])

    print("finally, connected")
    for i in range(1000):
        print("indexing %s..." % (i + 1), end="")
        latlon = fake.local_latlng(country_code=random.choice(("ID", "PH")), coords_only=True)
        index_doc(es, "geolastic", "geolastic_type", {"point": {"lat": float(latlon[0]), "lon": float(latlon[1])}})
        print("done")

    print("searching...")
    print(search(es, "geolastic", lat=14.35, lon=120.56))
