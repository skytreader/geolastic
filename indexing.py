from elasticsearch import Elasticsearch

import json
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
    backoff_base = 2
    backoff_exp = 0

    while not es.ping():
        print("Could not connect, waiting off...")
        time.sleep(backoff_base ** backoff_exp)
        es = Elasticsearch([{"host": "localhost", "port": 9200}])

    print("finally, connected")
    print("indexing...", end="")
    index_doc(es, "geolastic", "geolastic_type", {"point": {"lat": 14.35, "lon": 120.56}})
    print("done")
    print("searching...")
    print(search(es, "geolastic", lat=14.35, lon=120.56))
