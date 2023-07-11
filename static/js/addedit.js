function getCookie(name)
{
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
function redirect()
{
  window.location = "/";
}
function redirect1()
{
  window.location = "/admin";
}
if(getCookie("role") != "ADMIN")
{
    redirect();
}
 // Event listener for form submission
 document.getElementById('addbook').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
  
    // Create an object with the form data
    const Data = 
    {
        bookid: document.getElementById("bookid").value,
        title: document.getElementById("title").value,
        authorid: document.getElementById("authorid").value,
        edition: document.getElementById("edition").value,
        categoryid: document.getElementById("categoryid").value,
        publisherid: document.getElementById("publisherid").value,
        copies: document.getElementById("copies").value,
        publicationyear: document.getElementById("publicationyear").value,
    }
    // Send the data to the API endpoint
    add(Data);
  });
// send data package from add.html form element to server
function add(Data)
{
    fetch('/add_book', {
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
        if(data.status == true)
        {
            document.getElementById("status").innerHTML = data.message;
            setTimeout(redirect1, 5000);
        }
        else
        {
            document.getElementById("status").innerHTML = "User not added";
        }
      })
        .catch(error => {
        // Handle any errors
        console.error(error);
        });
}