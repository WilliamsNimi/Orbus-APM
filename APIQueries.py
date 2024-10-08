import requests
import json

""" End points
getObjectsURL = "https://sterlingbank-api.iserver365.com/odata/Objects"
getObjectAttributes = "https://sterlingbank-api.iserver365.com/odata/Objects("#{key})/AttributeValues
patchObject = "https://sterlingbank-api.iserver365.com/odata/Objects("#{key})
apmServices = ""
"""

#Simulated RESTAPI endpoints for Orbus and APM
getObjectsfakeURL = "http://127.0.0.1:5000/odata/Objects"
getObjectAttributesfakeURL = "http://127.0.0.1:5000/odata/Objects("
patchObjectfakeURL = "http://127.0.0.1:5000/odata/Objects("
APMServicesFakeURL = "http://127.0.0.1:5000/grafana/services/SLO"

attributeChangePattern = { 
    "AttributeValuesFlat":
    {
        'RiskRating': 5 
    }
}

objectIds = []

def getObjects():
    #TODO: Replace URL with correct URL from ORbus
    objectsRes = requests.get(getObjectsfakeURL)
    if objectsRes.status_code == 200:
        return objectsRes.content.decode('utf-8')


def getObjectAttributes(objectID):
    #TODO: Replace URL with correct URL from ORbus
    URL = getObjectAttributesfakeURL + str(objectID) + ")/AttributeValues"
    attributes = requests.get(URL)
    if attributes.status_code == 200:
        return attributes.content.decode('utf-8')
    
def patchObject(objectID):
    #TODO: replace URL with correct Orbus Patch URL
    URL = patchObjectfakeURL + str(objectID) + ")"
    patch = requests.patch(URL, data=json.dumps(attributeChangePattern))
    if patch.status_code == 200:
        return patch.content.decode('utf-8')

def getServicesSLO():
    #TODO: replace URL with correct endpoint from APM
    servicesSLO = requests.get(APMServicesFakeURL)
    if servicesSLO.status_code == 200:
        return servicesSLO.content.decode('utf-8')

def getObjectIDs(orbusObjects):
    objectIDs = []
    for objects in orbusObjects['value']:
        objectIDs.append((objects['ObjectId'], objects['Name']))
    return objectIDs

def getServiceName(serviceObject):
    objects = []
    for key, obj in serviceObject.items():
        for vals in obj:
            objects.append((vals['series'][0]['value']['s'], (int(vals['errorSpanCount'])/int(vals['spanCount']))*100))
    return objects

#TODO: 1. Process Data gotten from APM and Orbus then Patch to Orbus with the patchObject(objectID) function
# 2. API Authentication for both Orbus and APM -  Add Redirect URL for the server this code will be hosted on on Azure AD and grant permissions

if __name__ == "__main__":
    print(type(getObjects()))
    print(getObjectIDs(json.loads(getObjects())))
    print(getServiceName(json.loads(getServicesSLO())))

