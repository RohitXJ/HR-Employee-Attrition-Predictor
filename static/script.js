document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('attritionForm');
    const submitButton = document.getElementById('submitButton');
    const messageBox = document.getElementById('messageBox');
    const predictionResultBox = document.getElementById('predictionResultBox');
    const predictionTitle = document.getElementById('predictionTitle');
    const predictionMessage = document.getElementById('predictionMessage');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Hide previous messages and results
        hideMessageBox();
        hidePredictionResult();

        // Show loading message
        showMessage('Predicting attrition...', 'loading');
        submitButton.disabled = true; // Disable button during prediction
        submitButton.textContent = 'Predicting...';

        const formData = new FormData(form);
        const data = {};
        for (const [key, value] of formData.entries()) {
            // Convert numerical inputs to numbers if they are intended as such
            // You might need more sophisticated type checking based on your inputs
            if (!isNaN(value) && value !== '') {
                data[key] = parseFloat(value);
            } else {
                data[key] = value;
            }
        }

        console.log('Sending data to backend:', data);

        try {
            // Replace '/predict' with the actual endpoint of your Flask backend
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                // If the response is not OK (e.g., 404, 500), throw an error
                const errorData = await response.json(); // Try to parse error message from backend
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            console.log('Prediction Result:', result);

            if (result.status === 'success') {
                displayPrediction(result.attrition_status, result.prediction_message);
                showMessage('Prediction successful!', 'success');
            } else {
                showMessage(result.message || 'Prediction failed. Please try again.', 'error');
            }

        } catch (error) {
            console.error('Error during prediction:', error);
            showMessage(`Error: ${error.message}. Please check console for details.`, 'error');
        } finally {
            submitButton.disabled = false; // Re-enable button
            submitButton.textContent = 'Predict Attrition';
        }
    });

    /**
     * Displays a message in the message box.
     * @param {string} message - The message to display.
     * @param {'success'|'error'|'loading'} type - The type of message (determines styling).
     */
    function showMessage(message, type) {
        messageBox.textContent = message;
        // Remove all previous type classes
        messageBox.classList.remove('hidden', 'success', 'error', 'loading');
        // Add the current type class
        messageBox.classList.add(type);
        messageBox.classList.remove('hidden');
    }

    /**
     * Hides the message box.
     */
    function hideMessageBox() {
        messageBox.classList.add('hidden');
        messageBox.textContent = '';
        messageBox.classList.remove('success', 'error', 'loading');
    }

    /**
     * Displays the prediction result.
     * @param {'Yes'|'No'} attritionStatus - The raw attrition status from the backend.
     * @param {string} message - The detailed prediction message.
     */
    function displayPrediction(attritionStatus, message) {
        predictionTitle.textContent = `Attrition Prediction: ${attritionStatus}`;
        predictionMessage.textContent = message;

        // Apply dynamic styling based on prediction
        predictionResultBox.classList.remove('positive', 'negative');
        if (attritionStatus === 'Yes') { // Assuming 'Yes' means employee will leave
            predictionResultBox.classList.add('negative');
        } else if (attritionStatus === 'No') { // Assuming 'No' means employee will stay
            predictionResultBox.classList.add('positive');
        }
        predictionResultBox.classList.remove('hidden');
    }

    /**
     * Hides the prediction result box.
     */
    function hidePredictionResult() {
        predictionResultBox.classList.add('hidden');
        predictionTitle.textContent = '';
        predictionMessage.textContent = '';
        predictionResultBox.classList.remove('positive', 'negative');
    }
});
