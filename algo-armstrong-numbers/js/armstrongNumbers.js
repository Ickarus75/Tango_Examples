// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(number) {
    let solution=[]
    for (let num = 0; num<number.length; num++){
        let numsToAdd=[]
        numStr=String(number[num]).split('')
        for (let i =0 ; i< numStr.length; i++){
            numsToAdd.push(Number(numStr[i])**numStr.length)
        }
        let sumToAdd= numsToAdd.reduce((a,b)=>a+b,0)
        if(num=== sumToAdd){
            solution.push(number[num])
        }
    }
    return solution;
};
// console.log(findArmstrongNumbers())