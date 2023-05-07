docker run -it --rm \
    -p 7700:7700 \
    -e MEILI_ENV='production' \
    -e MEILI_MASTER_KEY=$MEILIKEY \
    -e MEILI_NO_ANALYTICS=true \
    -e MEILI_LOG_LEVEL='INFO' \
    -v $(pwd)/meili_data:/meili_data \
    getmeili/meilisearch:v1.1
