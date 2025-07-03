from fastapi import FastAPI, Request
from main import search 
from pydantic import BaseModel
import nltk 
from nltk.corpus import brown
from collections import Counter
from pybktree import BKTree
import Levenshtein   
from fastapi.middleware.cors import CORSMiddleware

class SentenceInput(BaseModel): 
    sentence: str  

    
word_list = [w.lower() for w in brown.words() if w.isalpha()]
word_freq = Counter(word_list)
word_list = [word for word, freq in word_freq.items() if freq >= 3]
tree = BKTree(Levenshtein.distance, word_list) 

def correction(words): 
    corpus = words.lower().split()

    for word in range(len(corpus)): 
        matches = tree.find(corpus[word], 2) 
        if matches:
            corpus[word] = matches[0][1] 
    return ' '.join(corpus) 


app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/search")
def root(req: SentenceInput): 
    query = req.sentence 
    cleaned = correction(query)
    return search(cleaned)


