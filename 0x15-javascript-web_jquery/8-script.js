$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (resp) {
  for (let i = 0; i < resp.results.length; i++) { $('#list_movies').append('<li>' + resp.results[i].title + '</li>'); }
});
