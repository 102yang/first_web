let num = document.getElementById("num")
let increse = document.getElementById("increse")
let decrese = document.getElementById("decrese")
let clear = document.getElementById("clear")

increse .onclick=()=>{
    let cnt = parseInt(num.innerText, 10);
    num.innerText = cnt+1;
}
decrese .onclick=()=>{
    let cnt = parseInt(num.innerText, 10);
    num.innerText = cnt-1;
}
clear .onclick=()=>{
    let cnt = parseInt(num.innerText, 10);
    num.innerText = 0;
}
