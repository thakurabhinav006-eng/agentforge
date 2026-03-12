import { useState } from "react";
import { useAgents } from "@/hooks/useAgents";
import AgentCard from "@/components/AgentCard";
import type { Agent } from "@/types";

interface Props {
  onSelect: (agent: Agent) => void;
}

export default function Dashboard({ onSelect }: Props) {
  const { agents, categories, loading } = useAgents();
  const [filter, setFilter] = useState("all");
  const [search, setSearch] = useState("");

  const filtered = agents.filter((a) => {
    const matchCat = filter === "all" || a.category === filter;
    const matchSearch = a.name.toLowerCase().includes(search.toLowerCase());
    return matchCat && matchSearch;
  });

  return (
    <div style={container}>
      <div style={hero}>
        <h1 style={title}>AgentForge</h1>
        <p style={subtitle}>20 AI agents ready to work for you</p>
      </div>

      <div style={controls}>
        <input
          style={searchBox}
          placeholder="Search agents..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <div style={tabs}>
          <button style={filter === "all" ? activeTab : tab} onClick={() => setFilter("all")}>All</button>
          {categories.map((c) => (
            <button key={c} style={filter === c ? activeTab : tab} onClick={() => setFilter(c)}>
              {c}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div style={loadingStyle}>Loading agents...</div>
      ) : (
        <div style={grid}>
          {filtered.map((a) => (
            <AgentCard key={a.id} agent={a} onClick={() => onSelect(a)} />
          ))}
        </div>
      )}

      {!loading && filtered.length === 0 && (
        <div style={loadingStyle}>No agents found</div>
      )}
    </div>
  );
}

const container: React.CSSProperties = { minHeight: "100vh", background: "#0f172a", color: "#f1f5f9", padding: "0 16px 40px" };
const hero: React.CSSProperties = { textAlign: "center", padding: "48px 0 24px" };
const title: React.CSSProperties = { fontSize: 36, fontWeight: 700, background: "linear-gradient(135deg, #3b82f6, #8b5cf6)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" };
const subtitle: React.CSSProperties = { color: "#94a3b8", marginTop: 6, fontSize: 15 };
const controls: React.CSSProperties = { maxWidth: 900, margin: "0 auto", display: "flex", flexDirection: "column", gap: 12, marginBottom: 24 };
const searchBox: React.CSSProperties = { padding: "10px 16px", borderRadius: 8, border: "1px solid #334155", background: "#1e293b", color: "#f1f5f9", fontSize: 14, outline: "none" };
const tabs: React.CSSProperties = { display: "flex", gap: 6, flexWrap: "wrap" };
const tab: React.CSSProperties = { padding: "6px 14px", borderRadius: 20, border: "1px solid #334155", background: "transparent", color: "#94a3b8", fontSize: 13, cursor: "pointer", textTransform: "capitalize" };
const activeTab: React.CSSProperties = { ...tab, background: "#3b82f6", color: "#fff", borderColor: "#3b82f6" };
const grid: React.CSSProperties = { maxWidth: 900, margin: "0 auto", display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(380, 1fr))", gap: 12 };
const loadingStyle: React.CSSProperties = { textAlign: "center", color: "#475569", padding: 40 };
