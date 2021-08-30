# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 08:05:24 2021

@author: megha
"""

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('-pbEZDCbeErs3bVhh95asn4d7PKmIxvnF_VwvRLo-z-c')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')
response = assistant.create_session(
    assistant_id='61ab5168-213e-4a59-a00d-a7743c0317c2'
).get_result()
session_id = response
session_id = session_id["session_id"]
print(type(session_id))
print(session_id)

while True:
    input_text = input("enter the text")
    
    response = assistant.message(
    assistant_id='61ab5168-213e-4a59-a00d-a7743c0317c2',
    session_id=session_id,
    input={
        'message_type': 'text',
        'text': input_text
    }
    ).get_result()

#print(json.dumps(response, indent=2))
   
    print(response)
    print(response["output"]["generic"][0]["text"])