$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  data.results.forEach(movie => {
    $('UL#list_movies').append(`<LI>${movie.title}</LI>`);
  });
});
