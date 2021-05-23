
// scan config
const SCAN_OPTIONS = {
    acceptAllAdvertisements: true,
    keepRepeatedDevices: true
};


// function to scan for devices
async function scanForAdvertisements() {
    console.log("dela")
    try {
        const scan = await navigator.bluetooth.requestLEScan(SCAN_OPTIONS);
        let numberOfEvents = 0;

        navigator.bluetooth.addEventListener('advertisementreceived', event => {
            handleScanEvent(event);
            numberOfEvents++;
        });

    }
    catch(error)  {
        alert(error)
    }
}


// handler za najdene naprave
function handleScanEvent(event) {
    if (event.device.name === "Avto") {
        document.querySelector('#rssi').textContent = `${event.rssi}`;
        if (event.rssi > -60) {
            alert("Premisli, ali do cilja lahko prides kako drugace?");
        }
    }
}

//DOM za start
document.querySelector('#init_ble').addEventListener('click', scanForAdvertisements);
