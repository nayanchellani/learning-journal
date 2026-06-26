import { useState, useEffect, useRef } from 'react';

const API_BASE = 'http://127.0.0.1:8000/api';

const generateThreadId = () => {
  return `thread_${Math.random().toString(36).substring(2, 11)}`;
};

function App() {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [threadId, setThreadId] = useState('');
  const [error, setError] = useState('');
  
  const messagesEndRef = useRef(null);

  useEffect(() => {
    let savedThreadId = localStorage.getItem('chatbot_thread_id');
    if (!savedThreadId) {
      savedThreadId = generateThreadId();
      localStorage.setItem('chatbot_thread_id', savedThreadId);
    }
    setThreadId(savedThreadId);
    loadHistory(savedThreadId);
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const loadHistory = async (id) => {
    setIsLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_BASE}/history/${id}`);
      if (response.ok) {
        const data = await response.json();
        setMessages(data.messages || []);
      } else {
        throw new Error('Failed to fetch history');
      }
    } catch (err) {
      setError('Could not connect to the backend server.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSend = async (e) => {
    e.preventDefault();
    if (!inputText.trim() || isLoading) return;

    const userMessage = inputText.trim();
    setInputText('');
    setError('');
    setIsLoading(true);

    const tempMessages = [...messages, { role: 'user', content: userMessage }];
    setMessages(tempMessages);

    try {
      const response = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage,
          thread_id: threadId,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setMessages(data.messages);
      } else {
        throw new Error('API Error');
      }
    } catch (err) {
      setError('Failed to send message. Is backend running?');
    } finally {
      setIsLoading(false);
    }
  };

  const handleNewChat = () => {
    const newId = generateThreadId();
    localStorage.setItem('chatbot_thread_id', newId);
    setThreadId(newId);
    setMessages([]);
    setError('');
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>AI Chatbot</h2>
        <button onClick={handleNewChat} className="reset-btn">Clear Chat</button>
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="messages-list">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <p>Welcome! Type a message below to start chatting.</p>
          </div>
        ) : (
          messages.map((msg, index) => (
            <div key={index} className={`message-row ${msg.role}`}>
              <div className="message-sender">
                {msg.role === 'user' ? 'You' : 'Bot'}
              </div>
              <div className="message-text">
                {msg.content}
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className="message-row assistant">
            <div className="message-sender">Bot</div>
            <div className="message-text typing">Typing...</div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSend} className="input-form">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Type your message..."
          disabled={isLoading}
        />
        <button type="submit" disabled={!inputText.trim() || isLoading}>
          Send
        </button>
      </form>
    </div>
  );
}

export default App;
