// link: https://www.hackerrank.com/challenges/js10-arrays/problem

function getSecondLargest(nums) {
    var max = Math.max.apply(null, nums);
    var maxI = nums.indexOf(max);
    nums[maxI] = -Infinity;
    while(max == Math.max.apply(null, nums)){
        var max = Math.max.apply(null, nums);
        var maxI = nums.indexOf(max);
        nums[maxI] = -Infinity;
    }
    return Math.max.apply(null, nums);
}
