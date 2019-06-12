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

#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
def main(dict):

    ## Retreive cloudant credentials
    cloudantURL = dict["services.cloudant.url"]
    cloudantDB = dict["services.cloudant.database"]

    ## Sanitize database object
    del dict["services.cloudant.url"]
    del dict["services.cloudant.database"]

    if dict.get("id") is None:
        print("Error: An Id was not provided in the request object")
        return { "ok": False }

    original = read(cloudantURL, cloudantDB, dict.get("id"))

    if original is None:
        return { "ok": False }
    else:
        return update(cloudantURL, cloudantDB, original, dict)

#
# read() reads an entry from the database
#
# @param The url string
# @param The database string
# @param The id of the object to retrieve
#
# @return The Cloudant document
#
def read(url, database, id):
    headers = {"Accept-type": "application/json"}
    response = requests.get(url + "/" + database + "/" + id, headers = headers)
    json_response = response.json()

    if json_response.get("error"):
        print("Error: ", json_response.get("error"))
        return None
    else:
        return json_response

#
# update() reads an entry from the database
#
# @param The url string
# @param The database string
# @param The original object from the database
# @param The updated object from the client
#
# @return The action response dictionary
#
def update(url, database, original, updated):
    merged = {**original, **updated}
    del merged["id"]


    headers = {"Accept-type": "application/json"}
    response = requests.put(url + "/" + database + "/" + merged.get("_id"), headers = headers, data = json.dumps(merged))
    json_response = response.json()

    if json_response.get("ok"):
        return json_response
    else:
        print("Error: ", json_response.get("error"))
        return json_response
