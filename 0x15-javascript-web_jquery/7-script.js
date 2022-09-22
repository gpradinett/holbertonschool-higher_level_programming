// Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
// GET jquery: https://jquery-tutorial.net/ajax/the-get-and-post-methods/
const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
  // el ID "character"
  $('#character').text(data.name);
}
);
