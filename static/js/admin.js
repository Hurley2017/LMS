document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission
  
    var fileInput = document.getElementById('file-input');
    var file = fileInput.files[0]; // Get the selected file
  
    if (file) {
      var reader = new FileReader();
  
      reader.onload = function(e) {
        var contents = e.target.result;
        // Process the file contents here
        console.log('File contents:', contents);
      };
      reader.readAsText(file); // Read the file as text
    }
  });
  