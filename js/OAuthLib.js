  var clientId    = '914958245698';
  var apiKey      = 'AIzaSyDniwD4xBZEtyIG4a3EZLsSscN7eYI7-kw';
  var authUrlBase = 'https://accounts.google.com/o/oauth2/auth';
  var scopes      = 'https://www.googleapis.com/auth/plus.me';

    <!-- Sets ApiKey y verifica si está logueado  -->
  function init() {
    console.log("INIT!");
    gapi.client.setApiKey(apiKey);
    window.setTimeout(checkAuth,1);
  }

  function checkAuth() {
    gapi.auth.authorize({
      client_id: clientId, 
      scope: scopes, 
      immediate: true}, handleAuthResult);
  }

    <!-- Acción del Botón que Autoriza  -->
  function handleAuthClick(event) {
    gapi.auth.authorize({
      client_id: clientId, 
      scope: scopes, 
      immediate: false}, handleAuthResult);
    return false;
  }

  function handleAuthResult(authResult) {
    if (authResult && !authResult.error) {
      console.log( "handleAuthResult" );
      getUserInfo(); 
    }
  }

  function getUserInfo() {
    console.log("..");
    gapi.client.load('plus', 'v1', function() {
      var request = gapi.client.request({
        'path': '/plus/v1/people/me',
        'method' : 'get'
      });
      request.execute(function(resp) {
        document.getElementById('userID').value = resp.id;
        document.getElementById('userName').innerHTML = resp.displayName;
        document.getElementById('userFoto').src = resp.image.url;
      });
    });
  }