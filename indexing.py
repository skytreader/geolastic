from elasticsearch import Elasticsearch

import time

if __name__ == "__main__":
    es = Elasticsearch([{"host": "localhost", "port": 9200}])
    backoff_base = 2
    backoff_exp = 0

    while not es.ping():
        print("Could not connect, waiting off...")
        time.sleep(backoff_base ** backoff_exp)
        es = Elasticsearch([{"host": "localhost", "port": 9200}])

    print("finally, connected")
