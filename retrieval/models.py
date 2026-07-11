# need to do this to always use cached version and not look online every time. saves latency
import os
os.environ["HF_HUB_OFFLINE"] = "1"

from sentence_transformers import SentenceTransformer
import chromadb


_embedder = None
_client = None

def get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer("all-MiniLM-L6-v2")
    return _embedder

def get_client():
    global _client
    if _client is None:
        # _client = chromadb.PersistentClient(path="./chroma_db",
                                            
        _client = chromadb.HttpClient(host="localhost", port=8000, settings=chromadb.Settings(allow_reset=True))
    return _client