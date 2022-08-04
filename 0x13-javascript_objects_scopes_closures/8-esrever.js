#!/usr/bin/node

exports.esrever = function (list) {
  const num = [];
  for (let i = list.length - 1; i >= 0; i--) {
    num.push(list[i]);
  }
  return (num);
};
