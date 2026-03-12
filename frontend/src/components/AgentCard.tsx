import type { Agent } from "@/types";
import { getIcon } from "@/components/Icons";

interface Props {
  agent: Agent;
  onClick: () => void;
}

export default function AgentCard({ agent, onClick }: Props) {
  const providerColor = agent.provider === "anthropic" ? "#d97706" : "#10b981";
  return (
    <button onClick={onClick} style={card}>
      <div style={iconWrap}>{getIcon(agent.icon)}</div>
      <div style={{ flex: 1 }}>
        <div style={name}>{agent.name}</div>
        <div style={desc}>{agent.description}</div>
      </div>
      <span style={{ ...badge, background: providerColor }}>{agent.provider}</span>
    </button>
  );
}

const card: React.CSSProperties = {
  display: "flex", alignItems: "flex-start", gap: 12, padding: 16,
  background: "#1e293b", border: "1px solid #334155", borderRadius: 10,
  cursor: "pointer", textAlign: "left", width: "100%",
  transition: "border-color 0.15s",
};
const iconWrap: React.CSSProperties = {
  width: 40, height: 40, borderRadius: 8, background: "#334155",
  display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0,
};
const name: React.CSSProperties = { fontWeight: 600, fontSize: 14, color: "#f1f5f9" };
const desc: React.CSSProperties = { fontSize: 12, color: "#94a3b8", marginTop: 2 };
const badge: React.CSSProperties = {
  fontSize: 10, padding: "2px 8px", borderRadius: 12, color: "#fff", fontWeight: 600, flexShrink: 0,
};
