// Function to send form data to API endpoint
function sendData(formData) {
    fetch('http://127.0.0.1:5000/send_reginfo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => {
      if (response.status) {
        // Request succeeded
        return response.json();
      } else {
        // Request failed
        throw new Error('Error: ' + response.status);
      }
    })
    .then(data => {
      // Handle the API response
      console.log(data);
      // Do something with the response data
    })
    .catch(error => {
      // Handle any errors
      console.error(error);
    });
  }
  
  // Event listener for form submission
  document.getElementById('register').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
  
    // Create an object with the form data
    const formData = {
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      password2: document.getElementById('password2').value,
      fname: document.getElementById('fname').value,
      lname: document.getElementById('lname').value,
      address: document.getElementById('address').value
    };
    // Send the data to the API endpoint
    sendData(formData);
  });
  