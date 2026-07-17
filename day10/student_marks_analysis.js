let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49]

let passed = 0
let failed = 0
let max = 0

for(let i = 0; i<marks.length; i++)
{
    if(marks[i] >= 50)
    {
        console.log("student " + (i+1) +": - Passed")
        passed++
    }
    else
    {
        console.log("Student " + (i+1) + ": - Failed") 
        failed++
    }
}

ma = 0
mi = marks[0]

for(let i=0;i<marks.length;i++)
{
    if(marks[i]>ma)
    {
        ma=marks[i]
    }
}

for(let i=0; i<marks.length;i++)
{
    if(marks[i]<mi)
    {
        mi=marks[i]
    }
}

console.log("The Maximum marks achieved by a student is " + ma)
console.log("The minimum marks achieved by a student is "+mi)
console.log("Total Passed: " + passed)
console.log("Total Failed: " + failed)