/* ═══════════════════════════════════════════════════════
   AI CHATBOT — JavaScript Controller
   Features: Toggle, Send, Typing indicator, Suggestions
   ═══════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
    const chatBtn = document.getElementById('chatbot-button');
    const chatWindow = document.getElementById('chatbot-window');
    const closeChat = document.getElementById('close-chat');
    const chatBody = document.getElementById('chat-body');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const suggestionBtns = document.querySelectorAll('.suggestion-btn');

    // ═══════ Toggle Chat Window ═══════
    chatBtn.addEventListener('click', () => {
        chatWindow.classList.toggle('hidden');
        if (!chatWindow.classList.contains('hidden')) {
            chatInput.focus();
        }
    });

    closeChat.addEventListener('click', () => {
        chatWindow.classList.add('hidden');
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !chatWindow.classList.contains('hidden')) {
            chatWindow.classList.add('hidden');
        }
    });

    // ═══════ Add Message to Chat ═══════
    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `chat-message ${sender}`;

        const content = document.createElement('div');
        content.className = 'chat-msg-content';
        content.innerHTML = text;

        msgDiv.appendChild(content);
        chatBody.appendChild(msgDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        requestAnimationFrame(() => {
            chatBody.scrollTop = chatBody.scrollHeight;
        });
    }

    // ═══════ Show Typing Indicator ═══════
    function showTyping() {
        const indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.id = 'typing-indicator';
        indicator.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;
        chatBody.appendChild(indicator);
        scrollToBottom();
        return indicator;
    }

    function removeTyping() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) indicator.remove();
    }

    // ═══════ Send Message ═══════
    function sendMessage(text) {
        if (!text.trim()) return;

        addMessage(text, 'user');
        chatInput.value = '';
        chatInput.focus();

        // Show typing indicator
        showTyping();

        // Send to backend
        fetch('/api/chat/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text }),
        })
        .then(res => res.json())
        .then(data => {
            removeTyping();
            const response = data.bot_response || data.error || 'Sorry, something went wrong.';
            // Simulate slight typing delay for natural feel
            setTimeout(() => {
                addMessage(response, 'bot');
            }, 300);
        })
        .catch(err => {
            removeTyping();
            setTimeout(() => {
                addMessage('⚠️ Connection error. The AI assistant is currently offline. Try asking about <strong>skills</strong>, <strong>projects</strong>, or <strong>contact info</strong>!', 'bot');
            }, 300);
        });
    }

    // ═══════ Event Listeners ═══════
    sendBtn.addEventListener('click', () => sendMessage(chatInput.value));

    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage(chatInput.value);
    });

    // Suggestion buttons
    suggestionBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            sendMessage(btn.getAttribute('data-text'));
        });
    });
});
