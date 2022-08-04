#!/usr/bin/node
// class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return new Rectangle();
    } else if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
};
