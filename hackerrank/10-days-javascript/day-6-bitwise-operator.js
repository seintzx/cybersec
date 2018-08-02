function toBinary(x){
    var prepend;
    if(x>0) prepend="0"; else prepend=""; 
    return prepend+((x>>>0)).toString(2);
}
function getMaxLessThanK(n, k){
    var max = 0;
    var arr = [];
    arr = Array.from({length: n}, (v, k) => k+1);  
    for (var j=0; j< arr.length -1; j++){
        for(var l=j+1; l< arr.length; l++){
            var digit = parseInt((toBinary(arr[j]) & toBinary(arr[l])), 2)
            max = (digit > max && digit < k) ? digit : max;
        }
    }
    return max;
}
