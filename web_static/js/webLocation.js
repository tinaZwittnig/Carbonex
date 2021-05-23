// funkcija za lokacijo
function getLocation() {
    const mapLink = document.querySelector('#map-link');
    //ce je vse ok
    function success(position) {
        const latitude  = position.coords.latitude;
        const longitude = position.coords.longitude;
        return {lat: latitude, lon: longitude}
    }
    //ce mamo probleme
    function error() {
        console.log("error")
    }
    //browser ne podpira geolokacije
    if(!navigator.geolocation) {
        console.log("Geolocation not working")
    } else {
        navigator.geolocation.getCurrentPosition(success, error);
    }
    return {lat:46.0569, lon:14.5058}
}
