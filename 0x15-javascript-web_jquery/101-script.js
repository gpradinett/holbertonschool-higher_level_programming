const $ = window.$;

$(document).ready(function () {
  const buttonAdd = $('DIV#add_item');
  buttonAdd.click(function () {
    $('ul.my_list').append($('<li>Item</li>'));
  });
  const buttonRemove = $('DIV#remove_item');
  buttonRemove.click(function () {
    const items = $('ul.my_list li');
    if (items.length > 0) {
      items[items.length - 1].remove();
    }
  });
  const buttonEmpty = $('DIV#clear_list');
  buttonEmpty.click(function () {
    $('ul.my_list').empty();
  });
});