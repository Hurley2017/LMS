function clearCookies(vr) {
    document.cookie = vr + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  }
  function logout()
  {
    clearCookies("email");
    clearCookies("session");
    window.location = "/" 
  }
   