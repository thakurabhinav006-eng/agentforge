import { useState, useEffect } from "react";
import { fetchAgents } from "@/api/agents";
import type { Agent } from "@/types";

export function useAgents() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAgents()
      .then(setAgents)
      .catch(() => setAgents([]))
      .finally(() => setLoading(false));
  }, []);

  const categories = [...new Set(agents.map((a) => a.category))];

  return { agents, categories, loading };
}
