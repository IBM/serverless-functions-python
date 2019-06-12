##
 # Copyright 2018 IBM Corp. All Rights Reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the “License”);
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #  https://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an “AS IS” BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
#

import sys
import json
import requests

def main(dict):

    ## Retreive cloudant credentials
    cloudantURL = dict["services.cloudant.url"]
    cloudantDB = dict["services.cloudant.database"]

    ## Sanitize database object
    del dict["services.cloudant.url"]
    del dict["services.cloudant.database"]

    return create(cloudantURL, cloudantDB, dict)

def create(url, database, data):
    headers = {"Content-type": "application/json"}
    response = requests.post(url + "/" + database, headers = headers, data = json.dumps(data))
    json_response = response.json()

    return json_response
