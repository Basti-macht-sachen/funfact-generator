document.getElementById('newFactButton').addEventListener('click', async function() {
    try {
        // Fetch a new fact from the Flask API
        const response = await fetch('/api/fact');
        
        // Check if the response is successful (status code 200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        // Update the fact on the page
        document.getElementById('fact').textContent = data.fact;
    } catch (error) {
        // Log any errors to the console for debugging
        console.error('Error fetching new fact:', error);
        document.getElementById('fact').textContent = "Oops! Couldn't load a new fact. Please try again.";
    }
});
