// Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:
// tips: https://stackoverflow.com/questions/2941679/change-text-color-using-jquery
// Defino $ para que no haya problemas con el semistandard
const $ = window.$;

$(document).ready(function () {
  const button = $('#red_header');
  button.click(function () {
    button.css('color', '#FF0000');
  });
});
