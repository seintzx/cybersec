// link: https://www.hackerrank.com/challenges/js10-inheritance/problem

Rectangle.prototype.area = function(){
    return this.w * this.h;
};

class Square extends Rectangle {
    constructor(l) {
        super(l,l);
    }
}
