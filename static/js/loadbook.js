function loadbooks()
{
    fetch('/getBooks', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
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
            var incomingData = data.message;
            var constructTable = "<h2>Borrowed Books</h2><div class='borrowed-books'>";
            for(var i = 0; i < incomingData.length; i++)
            {
                constructTable = constructTable + "<div class='book-card'><img src='{{url_for('static', filename='./img/unnamed.jpg')}}' alt='Book 1'>";
                constructTable = constructTable + "<h3>" + incomingData[i].title + "</h3>";
                constructTable = constructTable + "<p>" + incomingData[i].author + "</p>";
                constructTable = constructTable + "<p>" + incomingData[i].category + "</p>";
                constructTable = constructTable + "<p>" + incomingData[i].borrowed + "</p>";
                constructTable = constructTable + "<br>";
                constructTable = constructTable + "<button class='return-button'>Return</button>";
                constructTable = constructTable + "</div>";
            }
            constructTable = constructTable + "</div>";
            document.getElementById("borrowed").innerHTML = constructTable;
        }
      })
      .catch(error => {
        // Handle any errors
        console.error(error);
      });
}