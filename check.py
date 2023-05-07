import meilisearch
import utils as utl
import json

client = meilisearch.Client('http://localhost:7700')

print(json.dumps(client.get_task(0),indent=4))
