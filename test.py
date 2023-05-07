import meilisearch
import utils as utl

client = meilisearch.Client('http://localhost:7700')

movies = utl.load_json('movies.json')
client.index('movies').add_documents(movies)

