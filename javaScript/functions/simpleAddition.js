/*
Have the function SimpleAdding(num) add up all the numbers from 1 to num.
For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. 
*/

function simpleAdding(num) { 
    let baseNumber = 1
    let originalNumb = num
    while(baseNumber < originalNumb){
      num += baseNumber
      baseNumber ++
    }
    return num
  }