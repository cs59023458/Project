var P = document.getElementById("protein");
    var C = document.getElementById("carbohydrate");
    var F = document.getElementById("fat");
    
    var outputP = document.getElementById("p");
    var outputC = document.getElementById("c");
    var outputF = document.getElementById("f");
    
    outputP.innerHTML = P.value;
    outputC.innerHTML = C.value;
    outputF.innerHTML = F.value;
    
    P.oninput = function () {
        outputP.innerHTML = this.value;
    }
    C.oninput = function () {
        outputC.innerHTML = this.value;
    }
    F.oninput = function () {
        outputF.innerHTML = this.value;
    }