function getCookie(name) {
    const cookieName = name + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
  
    for (let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
      }
      if (cookie.indexOf(cookieName) === 0) {
        const cookieValue = cookie.substring(cookieName.length, cookie.length);
        return JSON.parse(decodeURIComponent(cookieValue));
      }
    }
  
    return null;
  }
   //check if logged-in
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
        window.location = "/";
      }
      else
      {
        if(data.message.role == "ADMIN")
        {
            document.getElementById("message").innerHTML = "Successfull login... Redirecting to Admin Panel...";
            setTimeout(redirect1, 2500);
        }
        else
        {
            document.getElementById("message").innerHTML = "Successfull login... Redirecting to dashboard...";
            setTimeout(redirect2, 2500);
        }
        document.getElementById("greet").innerHTML = data.message.fname + " " + data.message.lname;
      }
    })
    .catch(error => {
      // Handle any errors
      console.error(error);
    });
function redirect1()
{
  window.location = "/admin";
}
function redirect2()
{
  window.location = "/dashboard";
}