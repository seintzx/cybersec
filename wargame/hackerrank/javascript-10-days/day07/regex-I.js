// link: https://www.hackerrank.com/challenges/js10-regexp-1/problem

function regexVar() {
    var re = new RegExp(/(^[aeiou]).*\1/i);
    // var re = new RegExp(/^(a|e|i|o|u)\w*\1$/);
    return re;
}
