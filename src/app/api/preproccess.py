import pandas as pd 
from datasets import load_dataset
import numpy
from sentence_transformers import SentenceTransformer, util 
from database import load_database
import torch
from tqdm import tqdm

dataset = load_dataset("corbt/all-recipes", split="train[:10000]")

model = SentenceTransformer("all-MiniLM-L6-v2") 
sentences = ["This is an example", "Here’s another one"]
      

for example in tqdm(dataset, desc="Preparing recipe texts"):
    title = example["input"] 

    embed = model.encode(title, convert_to_tensor=True).cpu().numpy().tolist()
    load_database(embed, title)  




 
    


    

