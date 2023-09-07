
function add(n){
    let display = document.getElementById('display')
    display.value = display.value+n
}

function reset(){
     document.getElementById('display').value="";
     document.getElementById('result').value="";
     }

     function calculate(){
        let display = document.getElementById('display');
        let result = eval(display.value);
        document.getElementById('result').value=result;
    }