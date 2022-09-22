// Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
// tips: https://api.jquery.com/text/
const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#update_header');
  button.click(function () {
    $('header').text('New Header!!!');
  });
});
