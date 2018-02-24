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
/post_location - POST = this api takes values in format latitude+longitude+pincode+place+address and inserts the new pincode in 
                        database.
                                    use curl command in terminal to mimic POST request
                        for example:
                                             curl -H "Content-type:text/plain" -X POST http://127.0.0.1:5000/post_location 
                         --data-ascii 28.65+77.216+IN/12345+faridabad+haryana
                         
                         
                         
                         
            
/get_using_postgres -GET = this api takes values in format latitude+longitude+radius and returns the name of places which are in 
                           the specified radius of the give latitude and longitude. this api is implemented using the earthdistance 
                           extension of postgres SQL.
                                     use curl command in terminal to mimic GET request
                           for example:
                                         curl -H "Content-type:text/plain" -X GET http://127.0.0.1:5000/get_using_postgres --data-ascii  
                           28.65+77.216+radius(in meteres)
                           
                           
                           
                           
                           
                                  
/get_using_self -GET = this api takes values in format latitude+longitude+radius and returns the name of places which are in 
                       the specified radius of the give latitude and longitude. this api is implemented by doing mathematical  
                       computations.
                                 use curl command in terminal to mimic GET request
                       for example:
                                         curl -H "Content-type:text/plain" -X GET http://127.0.0.1:5000/get_using_self --data-ascii  
                       28.65+77.216+radius(in meteres)
                       
                       
                       
                       
                       
                       
/get_city_name -GET = this api takes value in  the form of latitude+longitude and returns the name of place where the location belongs                       to.
                               use curl command in terminal to mimic GET request
                      for example:
                                         curl -H "Content-type:text/plain" -X GET http://127.0.0.1:5000/get_city_name --data-ascii  
                      28.65+77.216
