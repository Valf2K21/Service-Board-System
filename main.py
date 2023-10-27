# import dependencies
import logging
from flask import Flask, render_template, jsonify

# import user-created dependencies
from functions.get_time import get_time
from functions.plate_updater import plate_updater

# configure logging to only show error level messages
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

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
    print('plates_grab called successfully')
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