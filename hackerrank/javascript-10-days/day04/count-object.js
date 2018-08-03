// link: https://www.hackerrank.com/challenges/js10-count-objects/problem

function getCount(objects) {
    return objects.filter(function(o){
        return o.x == o.y;
    }).length;
}
