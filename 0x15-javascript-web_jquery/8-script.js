// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

// Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
// GET jquery: https://jquery-tutorial.net/ajax/the-get-and-post-methods/
const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, element) {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  });
});
