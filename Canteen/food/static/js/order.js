var bcart = document.querySelector("#bcart");
var btotal = document.querySelector("#btotal");

function addBreakfast(bid)
{
    let x = document.getElementById("login").innerHTML
    
    if(x == "Login")
    {
        alert("must Login");
        window.location.href="login";
    }
    else
    {
    breakfastId = '#brea' + bid;
    var name = document.querySelector(breakfastId).innerHTML;
    
    var radio = 'breakfast'+bid;
    var price = document.getElementsByName(radio).value;
    
   
    bcart.innerHTML += '<li>' + name +' - '+ price + '</li>';
    }

}

