// tips: https://api.jquery.com/append/
// Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:
const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#add_item');
  button.click(function () {
    $('ul').append('<li>Item</li>');
  });
});
