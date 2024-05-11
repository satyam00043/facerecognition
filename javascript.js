console.log("satyam");
function foo(x){
    const a=10;
    return a+x+10;
}
function bar(b){
    const y=12;
    return foo(b*y);
}
console.log(bar(10));