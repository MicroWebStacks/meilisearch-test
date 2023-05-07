import os
import meilisearch
import utils as utl
import json
from dotenv import load_dotenv

load_dotenv()
client = meilisearch.Client('http://localhost:7700',os.getenv('SEARCH_KEY'))

result = client.index('movies').search('botman')

print(json.dumps(result, indent=4))
