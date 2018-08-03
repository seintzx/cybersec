// link: https://www.hackerrank.com/challenges/js10-class/problem

class Polygon{
    constructor(lengths){
        this.lengths = lengths;
    }
    perimeter(){
        let sum = 0;
        this.lengths.forEach(function(len){
            sum += len;
        });
        return sum;
    }
}
