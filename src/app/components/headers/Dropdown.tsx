import React from 'react'
import { useState } from "react";

interface SearchBarProps {
  onSearch: (query: string) => void;
}

function Dropdown({ onSearch }: SearchBarProps) {
  const [query, setQuery] = useState<string>("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim() !== "") {
      onSearch(query.trim());
    }
  };

  return (
    <div className="w-full bg-white sticky top-0 shadow z-10">
      <form onSubmit={handleSubmit} className="flex items-center p-4 max-w-xl mx-auto">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search..."
          className="flex-1 border rounded-l px-4 py-2 focus:outline-none focus:ring focus:border-blue-400 text-black"
        />
        <button
          type="submit"
          className="bg-blue-500 hover:cursor-pointer text-white px-4 py-2 rounded-r transition-colors"
        >
          Search
        </button>
      </form>
    </div>
  );
}

export default Dropdown
