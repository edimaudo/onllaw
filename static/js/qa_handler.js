document.addEventListener('DOMContentLoaded', () => {
    const qaForm = document.getElementById('qaForm');
    const submitBtn = document.getElementById('submitBtn');
    const resultContainer = document.getElementById('resultContainer');
    const answerArea = document.getElementById('answerArea');

    if (qaForm) {
        qaForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Prepare UI for loading
            submitBtn.disabled = true;
            submitBtn.innerText = "PROCESSING...";
            resultContainer.classList.add('hidden');

            const formData = new FormData(qaForm);
            
            try {
                // We send the request to the POST route in main.py
                const response = await fetch('/api/qa', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) throw new Error('Network response was not ok');

                const data = await response.json();
                
                // Update the UI with the agent's response
                answerArea.innerText = data.answer || data.error || "No response received.";
                resultContainer.classList.remove('hidden');

            } catch (error) {
                answerArea.innerText = "An error occurred while contacting the Statute Sentinel.";
                resultContainer.classList.remove('hidden');
                console.error('Error:', error);
            } finally {
                // Restore button state
                submitBtn.disabled = false;
                submitBtn.innerText = "SUBMIT INQUIRY";
            }
        });
    }
});
