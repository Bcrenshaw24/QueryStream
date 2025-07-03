"use client"
import Dropdown from "./components/headers/Dropdown";
import { useState } from "react";

export default function Home() { 
  interface SearchResult {
  title: string;
  desc: string;
}
  const [results, setResults] = useState<SearchResult[]>([]);

  const handleSearch = async (query: string) => { 
    try {
      const res = await fetch('http://127.0.0.1:8000/search', { 
        method: 'POST', 
        headers: { 
          'Content-Type': 'application/json'
        }, 
        body: JSON.stringify({ sentence: query })
      });
      const data = await res.json();
      setResults(data);
    } catch (error) {
      console.error("Search failed:", error);
    }
  };

  return ( 
    <main className="flex flex-col items-center p-4">
      <Dropdown onSearch={handleSearch} />

      <div className="mt-4 w-full max-w-xl">
        {results.length === 0 ? (
          <p className="text-gray-500 text-center">Enter a query to see results.</p>
        ) : (
         <ul className="space-y-2">
           {results.map((result, idx) => (
          <li key={idx} className="border p-3 rounded bg-white shadow">
            <h2 className="font-semibold text-lg text-black">{result.title}</h2>
            <p className="text-gray-700">{result.desc}</p>
          </li>
  ))}
</ul>
        )}
      </div>
    </main>
  );
}
