// static/js/dashboard.js
function createTool() {
    const toolName = prompt("Enter tool name:");
    if (toolName) {
        fetch('/api/create_tool', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: toolName })
        })
        .then(response => response.json())
        .then(data => {
            alert('Tool created successfully!');
            location.reload();
        })
        .catch(error => console.error('Error:', error));
}
}