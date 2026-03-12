import { useState } from "react";
import Dashboard from "@/components/Dashboard";
import ChatView from "@/components/ChatView";
import type { Agent } from "@/types";

export default function App() {
  const [selected, setSelected] = useState<Agent | null>(null);

  if (selected) {
    return <ChatView agent={selected} onBack={() => setSelected(null)} />;
  }
  return <Dashboard onSelect={setSelected} />;
}
