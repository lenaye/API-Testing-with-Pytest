# API-Testing-with-Pytest

# Introduction

This repository contains automated Python API tests for a free and open Petstore API https://petstore.swagger.io/v2/ 

The info on the endpoints as well as input/output parameters and schema for the Petstore API can be found here: https://petstore.swagger.io

There are two Pytest scripts in this folder: 
* test_pet_endpoint.py 
* test_user_endpoint.py
* test_pet_endpoint_with_dataload.py
	
## Purpose
To demonstate the use pytest (Python testing framework), requests (a popular Python libarary for making HTTP requests) and unittest libraries.

More info can be found here:
* Pytest test framework (https://docs.pytest.org/en/6.2.x/index.html)
* Requests library (https://docs.python-requests.org/en/master/)
* unittest library (https://docs.python.org/3/library/unittest.html)

## Installation and Set Up
1. Install Python from https://www.python.org/downloads/
2. Clone the repo.
3. Install pytest framework, i.e. ```pip install -U pytest```
4. Install requests library, i.e. ```python -m pip install requests``` or simply ```pip install requests```
6. There's no need to install unittest library as it comes with Python 3.x installation.

## Descriptions of the Postman test case Collection

The test ```test_pet_endpoint.py``` demonstrates the use of pytest and request libraries and used Python's native assertion methods for verification of reponses.
The test ```test_user_endpoint.py``` demonstrates the use of unittest library and the assertion methods provided by unittest.

The last test ```test_pet_entpoint_with_dataload.py``` demonstrates the use of fixture and initial test data injection into the endpoint in order to guarantee the subsequent tests passes. 


## A few issues wit the API
Since this is an open and publi API without authentication, the data that it returns is not always of the best quality. A few points to note:

1. The data appears to be unstable and changing quite frequently. This makes run reliable and repeatable automated tests difficult as they tend to fail now and then.

2. There appeared to be duplicate record IDs with different data in the system, i.e. querying using one Id returned different pet info at different times , so when calling a GET request for a particular pet with an Id, the expected result is not always guaranteed to be returned.

3. In the case of status field, when calling the request for a Store inventory, there appear to be many more statuses of pets than what's listed in the Swagger UI.  According to the model, the only acceptable status values are `[ available, pending, sold ]`
It is possible to add new pets using POST /pet endpoint using a status of 'happy' and 'missing' and were both accepted. This indicates that there's no validation of this status on the back-end.

4. Likewise, when you submti a request for GET /pet/{petId} where the {petId} is a long numeric number, i.e. > 200 digits the API throws an error "java.lang.NumberFormatException:". This kind of error should be handled properly by the API.

5. The Swagger UI showed different response codes for each endpoint, i.e. 200, 400, and 404, but it will return a 400 response in most cases when you supply an invalid Id in the request. In such cases only 404 (Pet not found or User not found) is returned.
