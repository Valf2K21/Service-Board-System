// use setInterval() function to call update_time() function every 5 minutes
let plates_interval = setInterval(update_plates, 300000);

// create a function to update plates of each service state
function update_plates(event) {
    // create a function that is the actual plates updater
    function execute_updater(state) {
        // prevent the default form submission behavior of refreshing webpage
        event.preventDefault();
        
        // use fetch() function to call Flask's plates_grab() function
        fetch('/plates', {
            // notify Flask that the request being made uses POST method
            method: 'POST',
        })

            // receive the returned json result by Flask
            .then(response => response.json())
        
            // extract the values of said json result
            .then(data => {
                // store state-determined container and list of lists in a variaable
                let state_element = document.getElementById(state);
                let plates_list = data[state];

                // create an empty array to store generated plates later
                let generated = [];

                // clear old data from passed state's container
                state_element.innerHTML = '';

                // for-loop to loop through each list of plates_list
                for (let i = 0; i < plates_list.length; i++) {
                    // put currently-iterated list and its contents in their respective variables
                    let current_list = plates_list[i];
                    let plate_no = current_list[0];
                    let appoint = current_list[2];

                    // if-statement to check if plate_no is empty or N/A
                    if (!plate_no || plate_no === 'N/A') {
                        // use sticker_no as plate_no instead
                        plate_no = current_list[1];
                    }

                    // if-elif statement to determine what plate color to use according to its appointment type
                    if (appoint === '1' && !generated.includes(plate_no)) {
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
                        generated.pust(plate_no);
                    }

                    else if (appoint >= '1' && appoint <= '5' && !generated.includes(plate_no)) {
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
                        generated.pust(plate_no);
                    }
                }
            });
    }

    // call execute_updater() function to update each service state's plates
    execute_updater('counter');
    execute_updater('progress');
    execute_updater('completed');
}