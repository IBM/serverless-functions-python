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
def main(arg):

    ## Retreive cloudant credentials
    cloudantURL = arg["services.cloudant.url"]
    cloudantDB = arg["services.cloudant.database"]
    id = arg["id"]

    return read(cloudantURL, cloudantDB, id)

#
# main() will be run when you invoke this action
#
# @param The url string
# @param The database string
# @param The id of the object to retrieve
#
# @return The action response dictionary
#
def read(url, database, id):
    headers = {"Accept-type": "application/json"}
    response = requests.get(url + "/" + database + "/" + id, headers = headers)
    json_response = response.json()

    return json_response
