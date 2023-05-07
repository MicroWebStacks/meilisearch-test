# meilisearch-test

## installation
docker install
https://www.meilisearch.com/docs/learn/getting_started/installation

```bash
docker pull getmeili/meilisearch:v1.1

# Launch Meilisearch in development mode with a master key
docker run -it --rm \
    -p 7700:7700 \
    -e MEILI_ENV='development' \
    -v $(pwd)/meili_data:/meili_data \
    getmeili/meilisearch:v1.1
```
copy master key from interactive console output
