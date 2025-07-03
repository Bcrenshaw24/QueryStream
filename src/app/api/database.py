from dotenv import load_dotenv
load_dotenv()
from supabase import create_client, Client
import os

def load_database(embed, title):
    url = os.environ.get("URL")
    key = os.environ.get("KEY")

    db = create_client(url, key) 

    db.table("recipes").insert({"title": title, "embed": embed}).execute() 
def search_database(embed):
    url = os.environ.get("URL")
    key = os.environ.get("KEY") 

    db = create_client(url, key) 
    try:
        response = db.rpc("match_docs", {
            "query_embed": embed, 
            "match_count": 10
        }).execute()
        return response.data 
    except Exception as e: 
        print("Error", e)
        return None


    
