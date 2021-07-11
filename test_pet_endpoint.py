# Test case examples for Pet endpoint: https://petstore.swagger.io/v2/pet
# Contains the following tests:
# Find pet by Status - Available
# Find pet by Status - Sold
# Find pet by Status - Pending)
# Add a new pet
# Find Pet by Id

#Imports
import requests
import pytest
import json
from requests import api
from requests.models import Response

# Environment settings
petUrl = "https://petstore.swagger.io/v2/pet"
petFindByStatusUrl= petUrl + "/findByStatus"

#Constants
code200 = 200
code404 = 404
sold_count = 5
pending_count = 5
available_count = 500

#Headers
headers = {'Content-Type': 'application/json'} 

#Check through all pets for a particular status
def matching_status(resp,status):
    #Iterate respoonse and collate details
    msg="Status <> " + status

    for pet in resp:
        try:
            assert(pet['status']) == status, msg
        except:
            continue

#Compares elements from response against payload
def find_matching_elements(resp,payload):
    assert resp['category']['name'] == payload['category']['name'], "category{name} does not match" 
    assert resp['name'] == payload['name'], "name does not match"
    assert resp['photoUrls'][0] == payload['photoUrls'][0], "photoUrls does not match"
    assert resp['tags'][0]['name'] == payload['tags'][0]['name'], "tags{name} does not match"
    assert resp['status'] == payload['status'], "status does not match"


#Ensure that pets with Avaliable status can be retrieved   
def test_findByStatusIdAvailable():
    #Body
    payload= {'status': 'available'}

    #Submit request and capture response
    response = requests.request("GET",petFindByStatusUrl,params=payload)
    resp = response.json()

    #Validate response code and check number of pets with Available status    
    assert response.status_code == code200, "HTTP Response Code <> 200"
    assert len(resp) >= available_count ,"Too few Available pets"
    matching_status(resp,payload['status'])


#Ensure that pets with Sold status can be retrieved  
def test_findByStatusIdSold():
    #Body
    payload= {'status': 'sold'}

    #Submit request and capture response
    response = requests.request("GET",petFindByStatusUrl,params=payload)
    resp = response.json()
    
    #Validate response code and check number of pets with Sold status
    assert response.status_code == code200, "HTTP Response Code <> 200"
    assert len(resp) >= sold_count ,"Too few Sold pets"
    matching_status(resp,payload['status'])


#Ensure that pets with Pending status can be retrieved  
def test_findByStatusIdPending():
    #Body
    payload= {'status': 'pending'}

    #Submit request and capture response
    response = requests.request("GET",petFindByStatusUrl,params=payload)
    resp = response.json()

    #Validate response code and check number of pets with Pending status
    assert response.status_code == code200, "HTTP Response Code <> 200"
    assert len(resp) >= pending_count ,"Too few Pending pets"
    matching_status(resp,payload['status'])


#Ensure that a nwe pet can be added successfully
def test_addNewPet():
    global saved_pet
    #Body
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "Terrier"
        },
        "name": "Mini",
        "photoUrls": [
            "https://www.thesprucepets.com/littedoggie.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Mini"
            }
        ],
        "status": "available"
    }

    response = requests.request("POST", petUrl, headers=headers, data=json.dumps(payload))
    resp = response.json()
    saved_pet = resp # save response of newly added pet for searching in test_findPetById

    #print formatted response
    print(json.dumps(resp,indent=4))

    #Validate response code and matching elements
    assert response.status_code == code200, "HTTP Response Code <> 200"
    find_matching_elements(resp,payload)


#Ensure that existing pet can be retrieved with a valid pet Id
def test_findPetById():
    #Body - extract the Id from the newly added pet from test_addNewPet
    payload = str(saved_pet['id'])

    newUrl = petUrl +'/'+ payload
    #Submit request and capture response
    response = requests.request("GET",newUrl,params={})
    resp = response.json()

    #print formatted response
    print(json.dumps(resp,indent=4))

    #Validate response code and matching elements
    assert response.status_code == code200, "HTTP Response Code <> 200"
    find_matching_elements(resp,saved_pet)