const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, (response) => {
  $.each(response.results, (i, film) => {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
