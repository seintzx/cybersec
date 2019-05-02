// link: https://www.hackerrank.com/challenges/js10-date/problem

function getDayName(dateString) {
    let dayName;
    const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    dayName = dayNames[new Date(dateString).getDay()];
    return dayName;
}
