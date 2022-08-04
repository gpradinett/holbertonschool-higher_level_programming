#!/usr/bin/node
// Function that return the number of ocurreces in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(elem => elem === searchElement).length);
};
