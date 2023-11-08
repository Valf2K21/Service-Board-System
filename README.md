# Service Board System
The Service Board System is a web application for monitoring vehicle maintenance status according to three states: counter, in progress, and completed.

## License
This project is licensed under the [GNU Affero General Public License (AGPLv3)](LICENSE)

## Tech Stack
- Python - backend programming language
- Pandas - Python-based data wrangling and analysis library
- Flask - micro web framework to develop this Python-based web application
- PostgreSQL - database creation and data storage of sample vehicle maintenance data
- Psycopg2 - adapter to connect and interact Python and PostgreSQL
- HTML - frontend markup language 
- CSS - style sheet for HTML
- JavaScript - scripts for HTML including updating plates and time

## Installation
1. Clone this repository:
```cmd
git clone https://github.com/Valf2K21/Service-Board-System.git
cd Service-Board-System
```
2. Create virtual environment
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```
3. Install dependencies
```cmd
pip install -r requirements.txt
```
4. Create new database named service_board_db in PostgreSQL 16's pgAdmin4
5. Use service_board_db_sample.sql to restore required tables in newly-created database
6. Modify database.ini by changing values of host, user, and password if needed
7. Run Service Board System
```cmd
python -m main
```

## Demo
[![Service Board System Demo](https://img.youtube.com/vi/rRLSgciMuu0/0.jpg)](https://www.youtube.com/watch?v=rRLSgciMuu0)

## Acknowledgements
The Service Board System's development was made possible thanks to the following open-source technologies and libraries:
- Python. Huge thanks to the Python Software Foundation for continuously developing the versatile programming language that served as this system's backend language.
- Pandas. I would like to thank Wes McKinney for creating an invaluable tool used for this system's data wrangling and analysis processes.
- Flask. Thanks to the Pallets Projects for providing maintenance and improvements to the Python-based micro-web framework that enabled the efficient development of this system.
- PostgreSQL. My sincere thanks to the PostgreSQL Global Development Group for developing the free and open-source relational database management system used as this system's data storage and management system.
- Psycopg2. The Psycopg Team's efforts to provide the community with a reliable PostgreSQL connection adapter are highly appreciated, and their library enabled the system's backend to seamlessly interact with the relational database.
- HTML, CSS. Thank you to the World Wide Web Consortium for providing the web development community with specifications and standards, ensuring that all developed web applications are made with the utmost quality in mind.
- JavaScript. I would like to acknowledge Ecma International for setting high standards for the scripting language utilized by this system, specifically in updating plates and time.