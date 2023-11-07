/*
    The Service Board System is a web application for monitoring vehicle maintenance status according to three states: counter, in progress, and completed.
    Copyright (C) 2023 Valfrid Galinato
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

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