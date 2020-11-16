'use strict'


//navbar responsive
const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})

//mostrar info pizza
//revisar bien esta parte
//solucionar tiempo de visibilidad


var btn = document.getElementById("mostrar");

var span = document.getElementById("close")[0];

function mostrar(){
  var pizza = document.getElementById("pizza");
  pizza.style.display = "block";
}

span.onclick = function(){
  pizza.style.display = "none";
}

window.onclick = function(event){
  if(event.target == modal){
    modal.style.display = "none";
  }
}

