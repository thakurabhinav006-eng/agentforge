export interface Agent {
  id: string;
  name: string;
  description: string;
  category: string;
  icon: string;
  provider: string;
  input_type: string;
  supports_file: boolean;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface ChatState {
  messages: ChatMessage[];
  sessionId: string | null;
  loading: boolean;
}
