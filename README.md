# apitest
DEPENDENCIES
-----------------------
1 python 3.5
2 numpy
3 pandas
4 sqlalchemy
5 flask
6 math
7 psycopg2
8 shapely
9 postgres SQL 10
10 curl

STEPS TO RUN
------------------------
1) get your cmd/terminal to the "apitest" directory using cd
2) in the cmd/terminal run the command "python runmefordatabasesetup.py"
3) then run the command "python ./server.py"

APIs MADE IN THIS PROJECT
--------------------------
/post_location - POST = this api takes values in format latitude+longitude+pincode+place+address and inserts the new pincode in database
                 use curl command in terminal to mimic POST request
                 for example
                 curl -H "Content-type:text/plain" -X POST http://127.0.0.1:5000/post_location --data-ascii 28.65+77.216+IN/12345+extension+gurugram
            
/get_using_postgres -GET = 
/get_using_self -GET
/get_city_name -GET
