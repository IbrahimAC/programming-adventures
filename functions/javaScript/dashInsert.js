/*
Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3. 
Don't count zero as an odd number.
*/

function dashInsert(str) { 
    array = []
    x = 0
    y = 1
    while(y < str.length ){
      if(parseInt(str[x]) % 2 !== 0 && parseInt(str[y]) % 2 !== 0){
        array.push(str[x])
        array.push('-')
        x += 1
        y+= 1
      } else {
        array.push(str[x])
        
        x += 1
        y+= 1
      }
      
    }
    array.push(str[str.length -1])
    return array.join('')
  }