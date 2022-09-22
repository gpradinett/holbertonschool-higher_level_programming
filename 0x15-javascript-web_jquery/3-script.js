// Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header
// tips: https://api.jquery.com/addClass/

const $ = window.$;

$(document).ready(function () {
  const button = $('DIV#red_header');
  button.click(function () {
    $('header').addClass('red');
  });
});
