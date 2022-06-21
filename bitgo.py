function OptimalAssignments(strArr) {

 var len = strArr.length;
//1. get list of permutations
 var cmdLines = orderStrings(len);
//2. convert the array of strings to an array of number arrays.
 var workArray = convertArray(strArr);
//3. attach to each item in the cmdLine permutation a score
 var cmdLinesScores = cmdLines.map(function(val){
 return [val, scoreMaker(val)];
 })
//4. sort the scores from greatest to least, and return the most efficient
//in string form
 cmdLinesScores.sort(function(a, b) {return(b[1] - a[1])});
 var rawAnswer = cmdLinesScores.pop()[0];
//5. convert the answer into the required format, and return
 return (ansConvert(rawAnswer));
//---------------------helper functions--------------------
 function orderStrings(num){
 var numArr = [];
 for (var i = 0; i < num; i++){
 numArr[i] = i + 1;
 }
 var result = allPerms(numArr).map(function(val) {
 return val.join('');
 });
 return result;
 }
 function allPerms(inputArray) {
 var data = inputArray;
 var resultArray = [];
 var len = data.length;
 if (len === 0) {
 return [[]];
 }
 else {
 var first = data.shift();
 var words = allPerms(data);
 words.forEach(function(word) {
 for (var i = 0; i < len; ++i) {
 var tmp = word.slice();
 tmp.splice(i, 0, first)
 resultArray.push(tmp);
 }
 });
 }
 return resultArray;
 }
 function convertArray(arr) {
 pattern = /(d+)/g;
 newArr = [];
 var newArr = arr.map(function(val, ind){
 pattern = /(d+)/g;
 holdArr = [];
 do {
 var test = pattern.exec(val);
 if (test) {
 holdArr.push(parseInt(test[1]));
 }
 }
 while (pattern.lastIndex > 0);
 return holdArr;
 });
 return newArr;
 }
 function scoreMaker(orderString) {
 var orderArr = orderString.split('');
 var holdArr = workArray.map(function(val, ind) {
 return val[orderArr[ind] - 1];
 });
 var score = holdArr.reduce(function(first, last){
 return first + last;
 });
 return score;
 }
 function ansConvert(str) {
 var res = '';
 for (var i = 0; i < len; i++) {
 res = res + '(' + (i+1) + '-' + rawAnswer[i] + ')';
 }
 return res;
 }
}

// keep this function call here
// to see how to enter arguments in JavaScript scroll down
OptimalAssignments(readline());
