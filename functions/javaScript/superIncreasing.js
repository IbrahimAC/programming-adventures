/*
Have the function Superincreasing(arr) take the array of numbers stored in arr 
and determine if the array forms a superincreasing sequence where each element in the array is greater than the sum of all previous elements.
The array will only consist of positive integers. For example: if arr is [1, 3, 6, 13, 54] then your program should return the string "true" because it forms a superincreasing sequence.
If a superincreasing sequence isn't formed, then your program should return the string "false"
*/

//Attempt 1 - forget to consider cases where the given values are the same e.g. [3,3]
function Superincreasing(arr) { 
    let totalSum = 0
      for (let i = 0; i < arr.length; i++) {
          sum += arr[i];
          if(arr[i+1] < totalSum){
            return false
          }
      }
    
      return true 
    
    }

    
//Attempt 2
function Superincreasing(arr) { 
    let totalSum = 0
      for (let i = 0; i < arr.length; i++) {
          sum += arr[i];
          if(arr[i+1] <= totalSum){
            return false
          }
      }
    
      return true 
    
    }
