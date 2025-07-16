function formatRelativeTime(date) {
  const now = new Date();
  const diffMs = now - date;
  const diffMin = Math.floor(diffMs / 60000);

  if (diffMin === 0) return "Just now";
  if (diffMin === 1) return "1 minute ago";
  if (diffMin < 10) return `${diffMin} minutes ago`;

  let hours = date.getHours();
  const minutes = date.getMinutes().toString().padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12 || 12;
  return `${hours}:${minutes} ${ampm}`;
}

// Αποθήκευση μηνυμάτων με την αρχική ώρα
const sentMessages = [];

function addUserMessage(text) {
  const chatBody = document.querySelector('.chat-body');
  const now = new Date();

  const msgDiv = document.createElement('div');
  msgDiv.className = 'user-message';

  const messageId = `msg-${Date.now()}`;
  msgDiv.innerHTML = `
    <div class="bubble">${text}</div>
    <div class="timestamp" id="${messageId}">${formatRelativeTime(now)}</div>
  `;

  chatBody.appendChild(msgDiv);
  chatBody.scrollTop = chatBody.scrollHeight;

  // Αποθήκευση της ώρας του μηνύματος
  sentMessages.push({ id: messageId, timestamp: now });
}

// Ενημέρωση όλων των χρονικών stamps κάθε λεπτό
setInterval(() => {
  sentMessages.forEach(({ id, timestamp }) => {
    const el = document.getElementById(id);
    if (el) {
      el.textContent = formatRelativeTime(timestamp);
    }
  });
}, 60000); // κάθε 1 λεπτό

// Προσθήκη του πρώτου timestamp για την εκκίνηση του chat
document.addEventListener("DOMContentLoaded", () => {
  const timeElement = document.getElementById("chat-start-time");
  const now = new Date();

  let hours = now.getHours();
  const minutes = now.getMinutes().toString().padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12 || 12;

  timeElement.textContent = `Chat Started: ${hours}:${minutes} ${ampm}`;
});

// Χειρισμός αποστολής μηνύματος
document.querySelector('.send-btn').addEventListener('click', () => {
  const input = document.querySelector('textarea');
  const message = input.value.trim();
  if (message !== '') {
    addUserMessage(message);
    input.value = '';
  }
});

 document.querySelectorAll('.quick-replies button').forEach(button => {
    button.addEventListener('click', () => {
      const message = button.getAttribute('data-msg');
      addUserMessage(message);
    });
  }); 