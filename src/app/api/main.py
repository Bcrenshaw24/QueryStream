import numpy
from sentence_transformers import SentenceTransformer, util 
from database import load_database
import torch 
from database import search_database

model = SentenceTransformer("all-MiniLM-L6-v2")

def search(word): 
    embed = model.encode(word, convert_to_tensor=True).cpu().numpy().tolist()
    data = search_database(embed)
    return data
    
    

