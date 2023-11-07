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

// use setInterval() function to call update_plates() function every 5 minutes
let plates_interval = setInterval(() => { update_plates();}, 300000);

// create a function to update plates of each service state
function update_plates(event = null) {
    // if-statement to check if event is null
    if (event !== null) {
        // prevent the default form submission behavior of refreshing webpage
        event.preventDefault();
    }

    // create a function that is the actual plates grabber
    function execute_plates_grabber() {
        // use fetch() function to call Flask's plates_grab() function
        fetch('/plates', {
            // notify Flask that the request being made uses POST method
            method: 'POST',
        })

            // receive the returned json result by Flask
            .then(response => response.json())

            // extract the values of said json result
            .then(data => {
                // store plates json result in a variable
                const counter_list = data['counter'];
                const progress_list = data['progress'];
                const completed_list = data['completed'];

                // call execute_updater() function to update each service state's plates
                execute_updater('counter', counter_list);
                execute_updater('progress', progress_list);
                execute_updater('completed', completed_list);
            });
    }

    // create a function that is the actual plates updater
    function execute_updater(state, state_list) {
        // store state-determined container in a variaable
        let state_element = document.getElementById(state);
        
        // create an empty array to store generated plates later
        let generated = [];
        
        // clear old data from passed state's container
        state_element.innerHTML = '';
        
        // for-loop to loop through each list of state_list
        for (let i = 0; i < state_list.length; i++) {
            // put currently-iterated list and its contents in their respective variables
            let current_list = state_list[i];
            let plate_no = current_list[0];
            let appoint = current_list[2];
            
            // if-statement to check if plate_no is empty or N/A
            if (!plate_no || plate_no === 'N/A') {
                // use sticker_no as plate_no instead
                plate_no = current_list[1];
            }
            
            // if-elif statement to determine what plate color to use according to its appointment type
            if (appoint === 1 && !generated.includes(plate_no)) {
                // create a new paragraph and break elements for the new plate to be generated
                let new_plate = document.createElement('p');
                let line_break = document.createElement('br');
                
                // set the class to be used by the new element
                new_plate.className = 'walk-in_plate';
                
                // use final value of plate_no as the new element's text
                new_plate.textContent = plate_no;
                
                // use appendChild() function to append the new plate and its break element to the passed state's container
                state_element.appendChild(new_plate);
                state_element.appendChild(line_break);
                
                // use push() function to add used plate_no in generated list
                generated.push(plate_no);
            }
            
            else if (appoint >= 1 && appoint <= 5 && !generated.includes(plate_no)) {
                // create a new paragraph and break elements for the new plate to be generated
                let new_plate = document.createElement('p');
                let line_break = document.createElement('br');
                
                // set the class to be used by the new element
                new_plate.className = 'booking_plate';
                
                // use final value of plate_no as the new element's text
                new_plate.textContent = plate_no;
                
                // use appendChild() function to append the new plate and its break element to the passed state's container
                state_element.appendChild(new_plate);
                state_element.appendChild(line_break);
                
                // use push() function to add used plate_no in generated list
                generated.push(plate_no);
            }
        }
    }
    
    // call execute_plates_grabber() function to get plates json result
    execute_plates_grabber();
}