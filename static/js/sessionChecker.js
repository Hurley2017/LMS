function getCookie(name) {
    return localStorage.getItem(name);
  } //check if logged-in
    const Data = 
    {
      email : getCookie("email"),
      key : getCookie("session"),
    }
    fetch('/checkSession', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(Data)
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
        window.location = "/login";
      }
      else
      {
        document.getElementById("greet").innerHTML = data.message.fname + " " + data.message.lname;
      }
    })
    .catch(error => {
      // Handle any errors
      console.error(error);
    });