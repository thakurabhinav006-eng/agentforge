import { useState, useCallback } from "react";
import { sendMessage, sendMessageWithFile } from "@/api/agents";
import type { ChatMessage } from "@/types";

export function useChat(agentId: string) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const send = useCallback(
    async (text: string, file?: File) => {
      setMessages((m) => [...m, { role: "user", content: text }]);
      setLoading(true);
      try {
        const res = file
          ? await sendMessageWithFile(agentId, text, file, sessionId)
          : await sendMessage(agentId, text, sessionId);
        setSessionId(res.session_id);
        setMessages((m) => [...m, { role: "assistant", content: res.reply }]);
      } catch (e: any) {
        setMessages((m) => [...m, { role: "assistant", content: `Error: ${e.message}` }]);
      } finally {
        setLoading(false);
      }
    },
    [agentId, sessionId]
  );

  const clear = useCallback(() => {
    setMessages([]);
    setSessionId(null);
  }, []);

  return { messages, loading, send, clear };
}
