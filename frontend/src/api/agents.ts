const API = import.meta.env.VITE_API_URL || "/api/v1";

export async function fetchAgents() {
  const res = await fetch(`${API}/agents`);
  if (!res.ok) throw new Error("Failed to load agents");
  return res.json();
}

export async function sendMessage(agentId: string, message: string, sessionId?: string | null) {
  const res = await fetch(`${API}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ agent_id: agentId, message, session_id: sessionId }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Request failed" }));
    throw new Error(err.detail);
  }
  return res.json();
}

export async function sendMessageWithFile(
  agentId: string,
  message: string,
  file: File,
  sessionId?: string | null
) {
  const form = new FormData();
  form.append("agent_id", agentId);
  form.append("message", message);
  form.append("file", file);
  if (sessionId) form.append("session_id", sessionId);
  const res = await fetch(`${API}/chat/file`, { method: "POST", body: form });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Request failed" }));
    throw new Error(err.detail);
  }
  return res.json();
}
