// Function to send form data to API endpoint
function setCookie(name, value) {
  localStorage.setItem(name, value);
} 
function redirect1()
{
  window.location = "/admin";
}
function redirect2()
{
  window.location = "/dashboard";
}
function sendData(formData) {
    fetch('/send_loginfo', {
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
      if(data.status == false)
      {
        document.getElementById("message").innerHTML = data.message;
      }
      else
      {
        if(data.message.role == "ADMIN")
        {
            document.getElementById("message").innerHTML = "Successfull login... Redirecting to Admin Panel...";
            setCookie("email", data.message.avatar, 7);
            setCookie("session", data.message.key, 7);
            setTimeout(redirect1, 2500);
        }
        else
        {
            document.getElementById("message").innerHTML = "Successfull login... Redirecting to dashboard...";
            setCookie(data.message);
            setTimeout(redirect2, 2500);
        }
      }
    })
    .catch(error => {
      // Handle any errors
      console.error(error);
    });
  }
  
  // Event listener for form submission
  document.getElementById('login').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
  
    // Create an object with the form data
    const formData = {
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
    };
    // Send the data to the API endpoint
    sendData(formData);
  });
  