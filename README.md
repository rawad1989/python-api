# python-api

This is a simple RESTful API for storing and tracking the running distances and times that users wants to store.

It consists from the following functions:

1. login function: login function it will returns an access token if user is authenticated
2. Userrun function: returns the list of runs for a user or add a user run. 
3. totalrun function: returns the total run distance .
4. avgspeed function: returns the avgerage speed for customer speed.
5. avgsessionspeed function: returns the averge speed for a specific session.

# Function Description:

notice all function uses json format in request and response

# Login Function:
This function is used to autheticate  

- method: POST
- Url: http:127.0.0.1:8000/api/login/
- paraments: username, password
- returned values: authentication token 

Example:

curl  -X POST -H 'Content-Type: application/json' -d '{"username":"test1","password":"me@123123"}' http://127.0.0.1:8000/api/login/ 

On success it will return the token
{"token":"28e8aeebb47715b903c02b95318a425b01f91a3a"}
other wise it will return an error with message

# userrun Function:

This function uses the POST and the GET methods

Using the GET method:

It will return a list for all user runs as a json object consists from distance and runtime for each run

- method: GET
- Url:http://127.0.0.1:8000/api/userrun/
- parameters: authentication token
- returned values: a list of user run as a json object

Example:

curl -X GET http://127.0.0.1:8000/api/userrun/ -H 'Authorization: Token 46c060801e8f801b601abc39d19078848677659b' -H "Content-Type: application/json"  

On success it will return json object as follow:
[{"id":12,"distance":100,"runtime":3600},{"id":13,"distance":50,"runtime":3000},{"id":14,"distance":30,"runtime":8000},{"id":15,"distance":100,"runtime":100},{"id":16,"distance":100,"runtime":100},{"id":17,"distance":100,"runtime":100}][

Using the POST method:
The function will insert a new user run for the specified user.

- method:POST
- Url: http://127.0.0.1:8000/api/userrun/
- parameters: distance, runtime
- returned values: json object with data and return 201 http request

Example: 

curl -X POST http://127.0.0.1:8000/api/userrun/ -H 'Authorization: Token 46c060801e8f801b601abc39d19078848677659b' -H "Content-Type: application/json"   -d '{"distance":"100","runtime":"100"}'

returned values:
{"distance":"100","runtime":"100"}

# Totalrun funcation:

This function will return the sum of all distance for the user 

- method: GET
- Url:http://127.0.0.1:8000/api/totalrun/
- parameters: authentication token
- returned values: json object containg the total run 

Example:

curl  http://127.0.0.1:8000/api/totalrun/ -H 'Authorization: Token 46c060801e8f801b601abc39d19078848677659b'

return respose:

{"total_distance":"580"}

# Average speed function:

This function will return the average speed for all run session

- method: GET
- Url:http://127.0.0.1:8000/api/avgspeed/
- parameters: authentication token
- returned values: json object containg the average speed

Example:

curl  http://127.0.0.1:8000/api/avgspeed/ -H 'Authorization: Token 46c060801e8f801b601abc39d19078848677659b'

returned response:

{"AvgSpeed": "139.2"}

# Average Session Speed function:

This function will return the average speed for a specific user run

- method: GET
- Url:http://127.0.0.1:8000/api/avgsessionspeed/[run-session-id]
- parameters: authentication token , run-session-id
- returned values: json object with average session speed

Example:

curl  http://127.0.0.1:8000/api/avgsessionspeed/13 -H 'Authorization: Token 46c060801e8f801b601abc39d19078848677659b'

returned values:

{"AvgSessionSpeed": 60.0}










