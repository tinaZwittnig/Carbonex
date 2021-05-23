$(document).ready(function(){
    $('.collapsible').collapsible();
  });


function dodajTocke(e) {
    console.log(e.target.value)
    let dodatek = parseInt(e.target.value);
    let trenutne = parseInt(document.querySelector('#tocke').innerText);
    let nove = dodatek + trenutne;
    document.querySelector('#tocke').innerText = nove;
}

//DOM listeners
//added in api.js