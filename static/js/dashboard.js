function search()
{
  const data_package = {
    content : document.getElementById("search").value,
  };
  fetch('/search_res')  

}