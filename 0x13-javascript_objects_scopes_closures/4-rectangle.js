#!/usr/bin/node
// class Rectangle that defines a rectangle:

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print (c = "X") {
    // print rectangle
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }

  rotate () {
    // swap width and length values
    const auxWidth = this.width;
    this.width = this.height;
    this.height = auxWidth;
  }

  double () {
    // double width and length values
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
