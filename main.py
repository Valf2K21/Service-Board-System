'''
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
'''

# import dependencies
import logging
from flask import Flask, render_template, jsonify

# import user-created dependencies
from functions.get_time import get_time
from functions.plate_updater import plate_updater

# configure logging to only show error level messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# create a Flask web application instance
app = Flask(__name__)

# define path to activate time_grab() function below
@app.route('/time', methods = ['POST'])

# create user-defined function for current time grabber
def time_grab():
    # call get_time() function to get current time
    time = get_time()

    # convert result into json so javascript can accesss them properly
    return jsonify(result = time)

# define path to activate plates_grab() function below
@app.route('/plates', methods = ['POST'])

# create user-defined function for current all_plates grabber
def plates_grab():
    # call plate_updater function to get current all_plates
    all_plates = plate_updater()

    # convert result into json so javascript can access them properly
    return jsonify(all_plates)

# define path to activate main system's function below
@app.route('/', methods = ['GET'])

# create user-defined function for service board gui
def service_board():
    # use render_template() function to grab filled HTML template and return to display it
    return render_template('base.html')

# if-statement to run Flask web application instance
if __name__ == '__main__':
    print('Service Board System Link: http://127.0.0.1:5000/')
    app.run()