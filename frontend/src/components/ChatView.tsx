import { useState, useRef, useEffect } from "react";
import { useChat } from "@/hooks/useChat";
import type { Agent } from "@/types";
import { getIcon } from "@/components/Icons";

interface Props {
  agent: Agent;
  onBack: () => void;
}

export default function ChatView({ agent, onBack }: Props) {
  const { messages, loading, send, clear } = useChat(agent.id);
  const [input, setInput] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = () => {
    if (!input.trim() && !file) return;
    send(input.trim(), file || undefined);
    setInput("");
    setFile(null);
  };

  return (
    <div style={container}>
      <div style={header}>
        <button onClick={onBack} style={backBtn}>&larr;</button>
        <div style={iconWrap}>{getIcon(agent.icon, 18)}</div>
        <span style={{ fontWeight: 600 }}>{agent.name}</span>
        <button onClick={clear} style={clearBtn}>Clear</button>
      </div>

      <div style={msgArea}>
        {messages.length === 0 && (
          <div style={empty}>Start a conversation with {agent.name}</div>
        )}
        {messages.map((m, i) => (
          <div key={i} style={{ ...msgBubble, alignSelf: m.role === "user" ? "flex-end" : "flex-start", background: m.role === "user" ? "#3b82f6" : "#334155" }}>
            <div style={{ whiteSpace: "pre-wrap", fontSize: 14, lineHeight: 1.6 }}>{m.content}</div>
          </div>
        ))}
        {loading && <div style={{ ...msgBubble, background: "#334155", alignSelf: "flex-start" }}>
          <span style={dots}>Thinking...</span>
        </div>}
        <div ref={endRef} />
      </div>

      <div style={inputArea}>
        {agent.supports_file && (
          <label style={fileLabel}>
            {file ? file.name.slice(0, 15) : "Attach"}
            <input type="file" style={{ display: "none" }} onChange={(e) => setFile(e.target.files?.[0] || null)} />
          </label>
        )}
        <input
          style={inputBox}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && handleSend()}
          placeholder="Type a message..."
        />
        <button onClick={handleSend} disabled={loading} style={sendBtn}>Send</button>
      </div>
    </div>
  );
}

const container: React.CSSProperties = { display: "flex", flexDirection: "column", height: "100vh", background: "#0f172a" };
const header: React.CSSProperties = { display: "flex", alignItems: "center", gap: 10, padding: "12px 16px", borderBottom: "1px solid #1e293b", color: "#f1f5f9" };
const backBtn: React.CSSProperties = { background: "none", border: "none", color: "#94a3b8", fontSize: 20, cursor: "pointer", padding: "4px 8px" };
const clearBtn: React.CSSProperties = { marginLeft: "auto", background: "none", border: "1px solid #334155", color: "#94a3b8", fontSize: 12, padding: "4px 12px", borderRadius: 6, cursor: "pointer" };
const iconWrap: React.CSSProperties = { width: 32, height: 32, borderRadius: 6, background: "#1e293b", display: "flex", alignItems: "center", justifyContent: "center" };
const msgArea: React.CSSProperties = { flex: 1, overflowY: "auto", padding: 16, display: "flex", flexDirection: "column", gap: 10 };
const msgBubble: React.CSSProperties = { maxWidth: "75%", padding: "10px 14px", borderRadius: 12, color: "#f1f5f9" };
const empty: React.CSSProperties = { color: "#475569", textAlign: "center", marginTop: 60, fontSize: 14 };
const dots: React.CSSProperties = { color: "#94a3b8", fontSize: 13 };
const inputArea: React.CSSProperties = { display: "flex", gap: 8, padding: 12, borderTop: "1px solid #1e293b" };
const inputBox: React.CSSProperties = { flex: 1, padding: "10px 14px", borderRadius: 8, border: "1px solid #334155", background: "#1e293b", color: "#f1f5f9", fontSize: 14, outline: "none" };
const sendBtn: React.CSSProperties = { padding: "10px 20px", borderRadius: 8, border: "none", background: "#3b82f6", color: "#fff", fontWeight: 600, cursor: "pointer", fontSize: 14 };
const fileLabel: React.CSSProperties = { padding: "10px 14px", borderRadius: 8, border: "1px solid #334155", background: "#1e293b", color: "#94a3b8", cursor: "pointer", fontSize: 12, display: "flex", alignItems: "center" };
