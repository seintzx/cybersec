// link: https://www.hackerrank.com/challenges/js10-arrows/problem

function modifyArray(nums) {
    nums = nums.map((num) => (num%2==1? 3:2) * num);
    return nums;
}
