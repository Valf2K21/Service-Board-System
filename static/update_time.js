// use setInterval() function to call update_time() function every 1000ms
let time_interval = setInterval(update_time, 1000);

// create a function to update time
function update_time() {
    // use fetch() function to call Flask's time_grab() function
    fetch('/time', {
        // notify Flask that the request being made uses POST method
        method: 'POST',
    })
        
        // receive the returned json result by Flask
        .then(response => response.json())
        
        // extract the values of said json result
        .then(data => {
            // update currently displayed time using its element id
            document.getElementById('result').textContent = data.result;
        });
}