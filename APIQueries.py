import requests
import json

#End points
getObjectsURL = "https://sterlingbank-api.iserver365.com/odata/Objects"
getObjectAttributesURL = "https://sterlingbank-api.iserver365.com/odata/Objects("
patchObjectURL = "https://sterlingbank-api.iserver365.com/odata/Objects("
APMServicesURL = "http://10.0.20.196:3202/api/metrics/summary?q={%20resource.service.name%20!%3D%20%22%20%22%20}&groupBy=resource.service.name"

"""
#Simulated RESTAPI endpoints for Orbus and APM
getObjectsfakeURL = "http://127.0.0.1:5000/odata/Objects"
getObjectAttributesfakeURL = "http://127.0.0.1:5000/odata/Objects("
patchObjectfakeURL = "http://127.0.0.1:5000/odata/Objects("
APMServicesFakeURL = "http://127.0.0.1:5000/grafana/services/SLO"
"""

def getObjects():
    try:
        objectsRes = requests.get(getObjectsURL)
        if objectsRes.status_code == 200:
            return objectsRes.content.decode('utf-8')
    except Exception as e:
        print(e)


def getObjectAttributes(objectID):
    try:
        URL = getObjectAttributesURL + str(objectID) + ")/AttributeValues"
        attributes = requests.get(URL)
        if attributes.status_code == 200:
            return attributes.content.decode('utf-8')
    except Exception as e:
        print(e)
    
def patchObject(objectID, metric_val):
    try:
        URL = patchObjectURL + str(objectID) + ")"
        attributeChangePattern = { 
            "AttributeValuesFlat":
            {
                'Availability Score': 5 
            }
        }
        attributeChangePattern['AttributeValuesFlat']['Availability Score'] = metric_val

        req = requests.patch(URL, attributeChangePattern)

        return req.status_code
    except Exception as e:
        print(e)

def getServicesSLO():
    try:
        servicesSLO = requests.get(APMServicesURL)
        if servicesSLO.status_code == 200:
            return servicesSLO.content.decode('utf-8')
    except Exception as e:
        print(e)

def getObjectIDs(orbusObjects):
    objectIDs = []
    try:
        for objects in orbusObjects['value']:
            objectIDs.append((objects['ObjectId'], objects['Name']))
        return objectIDs
    except Exception as e:
        print(e)

def getServiceName(serviceObject):
    objects = {}
    try:
        for key, obj in serviceObject.items():
            for vals in obj:
                if 'errorSpanCount' in vals:
                    objects[vals['series'][0]['value']['s']] = []
                    objects[vals['series'][0]['value']['s']].append(int(vals['errorSpanCount'])/int(vals['spanCount'])*100)
        return objects
    except Exception as e:
        print(e)

#TODO:
# 1. API Authentication for both Orbus and APM -  Add Redirect URL for the server this code will be hosted on on Azure AD and grant permissions

if __name__ == "__main__":
    try:
        objectIDs = getObjectIDs(json.loads(getObjects()))
        service_names = getServiceName(json.loads(getServicesSLO()))

        for items in objectIDs:
            if items[1] in service_names:
                service_names[items[1]].append(items[0])

        for key, val in service_names.items():
            patchObject(val[1], val[0])
    except Exception as e:
        print(e)