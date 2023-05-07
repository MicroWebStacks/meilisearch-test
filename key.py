import os
from dotenv import load_dotenv
import meilisearch

load_dotenv()
print(os.getenv('MEILIKEY'))
client = meilisearch.Client('http://localhost:7700',os.getenv('MEILIKEY'))

print(client.health())
print(client.get_keys())

