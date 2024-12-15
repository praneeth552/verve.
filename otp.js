function sendOtpData() {
    // Collect all input fields with class 'input'
    const inputs = document.querySelectorAll('.input');
    let otp = '';

    // Concatenate values of all input fields
    inputs.forEach(input => {
        otp += input.value;
    });

    // Get CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Prepare the data to send
    const data = { otp: otp };

    // Send data to the backend using Fetch API
    fetch('/verify-otp/', {
        method: 'POST',  // Method type
        headers: {
            'Content-Type': 'application/json',  // Set content type to JSON
            'X-CSRFToken': csrfToken,  // Add CSRF token for security
        },
        body: JSON.stringify(data),  // Convert the data object to JSON and send it in the request body
    })
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
        console.log(data);  // Handle the response
        if (data.status === 'success') {
            alert('OTP verified successfully');
            window.location.href = '/change/';  // Redirect on success
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error('Error:', error));  // Handle any errors
}
