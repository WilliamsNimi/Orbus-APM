# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
import re
import json

app = Flask(__name__)

sampleObjects = {
  "@odata.context": "string",
  "value": [
    {
      "ObjectId": "2bde59d2-3cf3-4ac7-aace-6017ea7f92b4",
      "ModelId": "a25b2257-d8a1-48e1-80ab-96a32bb87f7c",
      "ObjectTypeId": "f92298e9-c6d3-4de4-9e1a-127d0e2266e0",
      "Name": "Test object name",
      "LockedOn": "2024-08-20T12:29:28.2407448Z",
      "LockedById": "9ffbfa78-da28-4405-b790-79f1042f3276",
      "LockedBy": {
        "UserId": "9ffbfa78-da28-4405-b790-79f1042f3276",
        "Name": "Example User",
        "EmailAddress": "Example@example.com",
        "IsInactive": False
      }
    },
    {
      "ObjectId": "2bde59d2-3cf3-4ac7-aace-6017ea7f93e5",
      "ModelId": "a25b2257-d8a1-48e1-80ab-96a32bb87f7c",
      "ObjectTypeId": "f92298e9-c6d3-4de4-9e1a-127d0e2266e0",
      "Name": "Test object name",
      "LockedOn": "2024-08-20T12:29:28.2407448Z",
      "LockedById": "9ffbfa78-da28-4405-b790-79f1042f3276",
      "LockedBy": {
        "UserId": "9ffbfa78-da28-4405-b790-79f1042f3276",
        "Name": "Example User",
        "EmailAddress": "Example@example.com",
        "IsInactive": False
      }
    },
    {
      "ObjectId": "2bde59d2-3cf3-4ac7-aace-6017ea7f94f6",
      "ModelId": "a25b2257-d8a1-48e1-80ab-96a32bb87f7c",
      "ObjectTypeId": "f92298e9-c6d3-4de4-9e1a-127d0e2266e0",
      "Name": "Test object name",
      "LockedOn": "2024-08-20T12:29:28.2407448Z",
      "LockedById": "9ffbfa78-da28-4405-b790-79f1042f3276",
      "LockedBy": {
        "UserId": "9ffbfa78-da28-4405-b790-79f1042f3276",
        "Name": "Example User",
        "EmailAddress": "Example@example.com",
        "IsInactive": False
      }
    }
  ],
  "@odata.nextLink": "string",
  "@odata.count": 0
}

sampleObjectAttributes = {
  "@odata.context": "https://sterlingbank-api.iserver365.com/odata/$metadata#AttributeValues",
  "value": [
    {
      "@odata.type": "#OfficeArchitect.Contracts.OData.Model.AttributeValue.AttributeValueText",
      "StringValue": "NIPOutwardsDB",
      "AttributeValueId": 848429,
      "AttributeCategoryId": 1,
      "AttributeId": "611a7fe0-26ef-e811-9f2b-00155d26bcf8",
      "AttributeName": "Name",
      "AttributeAlias": "null",
      "Value": "NIPOutwardsDB"
    }
  ]
}

metricsObjects = {
  "vals":
  [
    {
  
  "spanCount": "123456",
  "errorSpanCount": "1234",
  "series": [
    {
      "key": "resource.service.name",
      "value": {
        "type": 5,
        "s": "sterling.ussd.Api"
      }
    }
  ],
  "p99": "1234566",
  "p95": "12344556",
  "p90": "122222",
  "p50": "122222"
},
{
  
  "spanCount": "126",
  "errorSpanCount": "14",
  "series": [
    {
      "key": "resource.service.name",
      "value": {
        "type": 5,
        "s": "sterling.onboarding.Api"
      }
    }
  ],
  "p99": "1234566",
  "p95": "12344556",
  "p90": "122222",
  "p50": "122222"
}
]
}

#print(sampleObjectAttributes['value'][0]['AttributeName'])

@app.route('/odata/Objects')
def getObjects():
	return json.dumps(sampleObjects)

@app.route('/odata/Objects(<id>)/AttributeValues')
def getObjectAttributes(id):
	return json.dumps(sampleObjectAttributes)

@app.route('/odata/Objects(<id>)', methods=['PATCH'])
def patchObject(id):
	new_list = {}
	new_list = request.get_data().decode('utf-8')
	print(new_list)
	return json.dumps(new_list)

@app.route('/grafana/services/SLO')
def getServiceSLO():
	return json.dumps(metricsObjects)
