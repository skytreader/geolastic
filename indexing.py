from elasticsearch import Elasticsearch

import time

def index_doc(es_client, index, doc_type, record):
    es_client.index(index=index, doc_type=doc_type, body=record)

if __name__ == "__main__":
    es = Elasticsearch([{"host": "localhost", "port": 9200}])
    backoff_base = 2
    backoff_exp = 0

    while not es.ping():
        print("Could not connect, waiting off...")
        time.sleep(backoff_base ** backoff_exp)
        es = Elasticsearch([{"host": "localhost", "port": 9200}])

    print("finally, connected")
    print("indexing")
    index_doc(es, "geolastic", "geolastic_type", {"point": {"lat": 14.35, "lon": 120.56}})
    print("done")
