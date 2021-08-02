/*
Have the function OneDecremented(str) count how many times a digit appears that is exactly one less than the previous digit.
For example: if str is "5655984" then your program should return 2 because 5 appears directly after 6 and 8 appears directly after 9.
The input will always contain at least 1 digit.
*/

function OneDecremented(str) { 
    counter = 0
    index = 0
    for (n of str){
      if (parseInt(str[index+1]) +1 === parseInt(str[index])){
        counter += 1
        index +=1
      
      
      } else {
        index += 1
      }
  
      
    }
    return counter
  
  }
