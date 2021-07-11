# Test case examples for Pet endpoint: https://petstore.swagger.io/v2/user
# Contains the following tests:
# Add new user
# Add new user without username
# Find user by username
# Update existing user details


import requests
import pytest
import unittest
import json
from requests import api

# Environment settings
userUrl = "https://petstore.swagger.io/v2/user"

#Headers
headers = {'Content-Type': 'application/json'} 

class TestUserEndpoint(unittest.TestCase):

    # Ensure that a new user can be added successfully
    def test_addNewUser(self):
        print('\nExecuting Test: Add New User...\n')
        #Body
        payload = json.dumps({
        "id": 0,
        "username": "jbond",
        "firstName": "James",
        "lastName": "Bond",
        "email": "jb@mi6.gov.uk",
        "password": "5hak3n!St1rred",
        "phone": "07007007007",
        "userStatus": 0
        })

        #Submit request and capture response
        response = requests.request("POST", userUrl, headers=headers, data=payload)
        resp = response.json()

        #print formatted response
        print(json.dumps(resp,indent=4))

        #Validate response code and check number of pets with Available status 
        self.assertEqual(response.status_code,200, "HTTP Response Code <> 200")
        self.assertEqual(resp['code'],200, "Code returned <> 200")
        self.assertEqual(resp['type'],'unknown', "Type returned <> unknown")
        print('\nFinished Test: Add New User.\n\n')


    #Ensure that adding a new user without username should results in an error
    def test_addNewUserWithoutUsername(self):
        print('\nExecuting Test: Add New User without Username...\n')
        #Body
        payload = json.dumps({
            "id": 0,
            "firstName": "Harry",
            "lastName": "Potter",
            "email": "harry@hogwarts.magic.com",
            "password": "hogw0rt5",
            "phone": "0737637493",
            "userStatus": 0
        })

        #Submit request and capture response
        response = requests.request("POST", userUrl, headers=headers, data=payload)
        resp = response.json()

        #print formatted response
        print(json.dumps(resp,indent=4))

        #Validate response code and check number of pets with Available status 

        self.assertEqual(response.status_code,200, "HTTP Response Code <> 200")
        self.assertEqual(resp['code'],200, "Code returned <> 200")
        self.assertEqual(resp['type'],'unknown', "Type returned <> unknown")
        self.assertEqual(resp['message'],'0', "message <> 0")
        print('\nFinished Test: Add New User.\n\n')


    #Ensure that user details can be retrived when requesting with a valid username
    def test_getUserByName(self):
        print('\nExecuting Test: Get User by Name...\n')

        #Body
        username = 'jbond'
        url = userUrl+ '/' + username
        #Submit request and capture response
        response = requests.request("GET", url, headers=headers, data={})
        resp = response.json()

        #print formatted response
        print(json.dumps(resp,indent=4))

        #Validate response code and user details        
        self.assertEqual(response.status_code,200, "HTTP Response Code <> 200")
        self.assertEqual(resp['username'],'jbond', "username <> jbond")
        self.assertEqual(resp['firstName'],'James', "firstName <> James")
        self.assertEqual(resp['lastName'],'Bond', "lastName <> Bond")
        self.assertEqual(resp['email'],'jb@mi6.gov.uk', "firstName <> jb@mi6.gov.uk")
        self.assertEqual(resp['password'],'5hak3n!St1rred', "password <> 5hak3n!St1rred")
        self.assertEqual(resp['phone'],'07007007007', "phone <> 07007007007")
        self.assertEqual(resp['userStatus'],0, "userStatus <> 0")
        print('\nFinished Test: Get User by Name.\n\n')


    #Ensure that request with an invalid username shoul return a meaningful error message
    def test_invalidUserName(self):
        print('\nExecuting Test: Invalid Username Returns Error Message...\n')

        #Body
        username = 'nosuchperson'
        url = userUrl+ '/' + username
        #Submit request and capture response
        response = requests.request("GET", url, headers=headers, data={})
        resp = response.json()

        #print formatted response
        print(json.dumps(resp,indent=4))

        #Validate response code and error message    
        self.assertEqual(response.status_code,404, "HTTP Response Code <> 404")
        self.assertEqual(resp['code'],1, "code <> 1")
        self.assertEqual(resp['type'],'error', "type <> error")
        self.assertEqual(resp['message'],'User not found', "message <> User not found")
        print('\nFinished Test: Invalid Username Returns Error Message.\n\n')


    #Ensure that existing user details can be updated successfully
    def test_updateUserDetails(self):
        print('\nExecuting Test: Update details of an existing user...\n')

        #Body
        username = 'hpotter'
        url = userUrl+ '/' + username
        payload = json.dumps({
            "id": 3527858756895,
            "username": "hpotter",
            "firstName": "Harry",
            "lastName": "Potter",
            "email": "harryp@hogwards.edu",
            "password": "mugg1e5mag1c",
            "phone": "0793747264728",
            "userStatus": 0
        })

        #Submit request and capture response
        response = requests.request("PUT", url, headers=headers, data=payload)
        resp = response.json()

        #print formatted response
        print(json.dumps(resp,indent=4))

        #Validate response code and message  
        self.assertEqual(response.status_code,200, "HTTP Response Code <> 200")
        self.assertEqual(resp['code'],200, "code <> 200")
        self.assertEqual(resp['type'],'unknown', "type <> unknown")
        self.assertEqual(resp['message'],'3527858756895', "message <> 3527858756895")
        print('\nFinished Test: Update details of an existing user.\n\n')
        

if __name__ == '__main__':
    # Run the main unittest code
    unittest.main()