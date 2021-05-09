<h1 align="center"> MongoDB + Django Rest Framework </h1>

<h2 align="center">CRUD Rest API</h2>

![Postman](postman.png?raw=true)

## Introduction: 

This API interface lists the information about all the different stored pizzas, and also allows user to interact with that information (such as edit or delete). 

Following are the specifications about the API:
* A Pizza can be of multiple types: Regular or Square **only**
* A Pizza can be of multiple sizes: Small, Medium, Large, or any user defined size 
* A Pizza can consist of multiple toppings: Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno, or any user defined topping 

## Dependency Installation

The following dependencies are required to run and test this API:

1. python (version 3.x)
2. python dependencies (as listed in requirements.txt)
3. MongoDB (ensure that mongod daemon is started)

## Running the API

**Note**: The below commands assumes that MongoDB is running on port `27017`, verify by running `mongo | grep 27017` in a terminal. 

1. Clone the repository after installing the dependencies
```
git clone https://github.com/ashok-arora/mongodb-django-rest.git
```
2. cd into the api directory 
```
cd mongodb-django-rest/api
```
3. Create MongoDB table 
```
python manage.py migrate
```
3. Run 
```
python manage.py runserver 8080
```

This will start the API at `localhost:8080` server and then requests can be sent using cURL or Postman.


## API Endpoints

**Note**: Requests should be JSON formatted as:

```
{
    "ptype": shape,
    "size": size,
    "toppings": comma-seperated list of toppings
}
```
Example formatting:
```
{
    "ptype": "Rectangle",
    "size": "Medium",
    "toppings": "Tomato, Onion"
}
```

1. Create a pizza

```
Method: POST
Endpoint: /pizza/create
Request:
    1. ptype
    2. size
    3. toppings
Response:
    1. Returns 200_OK if the request is successful
    2. Returns 400_BAD_REQUEST if any of the above fields is missing
```
2. List all pizzas
```
Method: GET
Endpoint: /pizza/list

Response:
    1. Returns 200_OK if the request is successful
```

3. Filter pizzas list by size 
```
Method: GET
Endpoint: /pizza/list?size=

Response:
    1. Returns 200_OK if the request is successful
```

4. Filter pizzas list by type 
```
Method: GET
Endpoint: /pizza/list?type=

Response:
    1. Returns 200_OK if the request is successful
```

5. Edit pizza entry
```
Method: PUT
Endpoint: /pizza/edit/<id>

NOTE: substitute <id> with id from pizza list

Response:
    1. Returns 200_OK if the request is successful
    2. Returns 400_BAD_REQUEST if pizza doesn't exist
```


6. Delete pizza entry
```
Method: DELETE
Endpoint: /pizza/delete/<id>

NOTE: substitute <id> with id from pizza list

Response:
    1. Returns 200_OK if the request is successful
    2. Returns 400_BAD_REQUEST if pizza doesn't exist
```