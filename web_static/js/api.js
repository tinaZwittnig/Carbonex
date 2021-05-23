

function getResult() {
   var dest = document.querySelector('#search').value;
   var loc = getLocation()

   $.getJSON( "data/v1/route",{location: loc.lat + "," + loc.lon, destination:dest}, function( data ) {
      console.log(data);
      document.querySelector('#away').innerText = data.kilometers;
      document.querySelector('#location_info').classList.remove("hidden")
      data.options.forEach(function (option) {
         if (option.name === "bus"){
            document.querySelector('#fromBus').innerText = option.vstopna;
            document.querySelector('#toBus').innerText = option.izstopna;
            document.querySelector('#numberBus').innerText = option.number;
            document.querySelector('#departureBus').innerText = option.leaving_time;
            document.querySelector('#arrivalBus').innerText = option.arriving_time;
            document.querySelector('#timeBus').innerText = option.time;
            document.querySelector('#treesBus').innerText = "TBD";
            document.querySelector('#busRezultat').classList.remove("hidden")
         } else if (option.name === "bike"){
            document.querySelector('#toBike').innerText = data.destination;
            document.querySelector('#timeBike').innerText = option.time;
            document.querySelector('#distBike').innerText = option.kilometers;
            document.querySelector('#caloriesBike').innerText = option.cal;
            document.querySelector('#treesBike').innerText = option.trees;
            document.querySelector('#bikeRezultat').classList.remove("hidden")
         } else if (option.name === "walk"){
            document.querySelector('#toFoot').innerText = data.destination;
            document.querySelector('#timeFoot').innerText = option.time;
            document.querySelector('#distFoot').innerText = option.kilometers;
            document.querySelector('#caloriesFoot').innerText = option.cal;
            document.querySelector('#treesFoot').innerText = option.trees;
            document.querySelector('#footRezultat').classList.remove("hidden")
         } else if (option.name === "car"){
            document.querySelector('#toCar').innerText = data.destination;
            document.querySelector('#timeCar').innerText = option.time;
            document.querySelector('#distCar').innerText = option.kilometers;
            document.querySelector('#treesCar').innerText = option.trees;
            document.querySelector('#carRezultat').classList.remove("hidden")
         }
      });
      document.querySelectorAll('.tockeGumb').forEach(item => {
         item.addEventListener('click', dodajTocke)
      })
   });

}

//DOM za search
document.querySelector('#search_button').addEventListener('click', getResult);
