document.getElementById("sendButton").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") {
        return;
    }

    appendMessage(userInput, "user-message");
    document.getElementById("userInput").value = "";

    fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        appendMessage(data.response, "bot-message");
    })
    .catch((error) => {
        console.error('Erro detalhado:', error);
        appendMessage("Desculpe, ocorreu um erro.", "bot-message");
    });
}

function appendMessage(message, className) {
    var chatbox = document.getElementById("chatbox");
    var messageElement = document.createElement("div");
    messageElement.className = "message " + className;
    messageElement.textContent = message;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}
