# geolastic

Have access to an ElasticSearch instance. You can install one natively on your
machine but this assumes you are using a docker container:

    docker run -d --name geolastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:latest

Check that it is running properly:

    curl -v localhost:9200/_cat/health

## Getting started with ES from scratch

1. **Create an index for your documents.**

    ```bash
    curl -X PUT "localhost:9200/geolastic"
    ```
    
    Check that the index was created successfully:

    ```bash
    curl localhost:9200/_cat/indices?v
    ```

2. **Define the schema in your index.** Note that the schema is provided for you
in this repo.

    ```bash
    curl -X PUT "localhost:9200/geolastic/geolastic_type/_mapping" -H "Content-Type: application/json" -d @schema.json
    ```
