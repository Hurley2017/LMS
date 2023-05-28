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
    session : getCookie("session"),
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
      document.getElementById("message").innerHTML = data.message;
    }
    else
    {
      if(data.message.role == "ADMIN")
      {
          document.getElementById("message").innerHTML = "Successfull login... Redirecting to Admin Panel...";
          setCookie(data.message);
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