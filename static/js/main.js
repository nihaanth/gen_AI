// static/js/main.js
async function searchTools() {
    const query = document.getElementById('searchInput').value;
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query })
        });
        const data = await response.json();
        displaySearchResults(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

function displaySearchResults(results) {
    // Update UI with search results
    console.log(results);
}