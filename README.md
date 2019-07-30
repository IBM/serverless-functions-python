<p align="center">
    <a href="https://cloud.ibm.com">
        <img src="https://landscape.cncf.io/logos/ibm-cloud-kcsp.svg" height="100" alt="IBM Cloud">
    </a>
</p>


<p align="center">
    <a href="https://cloud.ibm.com">
    <img src="https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg" alt="IBM Cloud">
    </a>
    <img src="https://img.shields.io/badge/platform-python-lightgrey.svg?style=flat" alt="platform">
    <img src="https://img.shields.io/badge/license-Apache2-blue.svg?style=flat" alt="Apache 2">
</p>

# Create a serverless Python application

> We have similar applications available for [Swift](https://github.com/IBM/serverless-functions-swift) and [Node.js](https://github.com/IBM/serverless-functions-nodejs).

This repository has code to create a serverless Backend for Frontend (BFF) using Python and IBM Cloud Functions, backed by a NoSQL database. Cloud Functions supplies basic Create, Read, Update, and Delete operations in a serverless environment. These functions can be mapped to an API gateway, then integrated into an iOS app for example, to enable persistence of data into a Cloudant NoSQL Database. 

Cloudant NoSQL DB provides access to a fully managed NoSQL JSON data layer that's always-on. This service is compatible with CouchDB, and accessible through a simple to use HTTP interface for mobile and web application models.

## Included Components

* [Cloudant NoSQL DB](https://cloud.ibm.com/catalog/services/cloudant): A fully managed data layer designed for modern web and mobile applications that leverages a flexible JSON schema.
* [Continuous Delivery](https://cloud.ibm.com/catalog/services/continuous-delivery): Enable tool integrations that support your development, deployment, and operation tasks.
* [GitLab](https://about.gitlab.com/): GitLab unifies issues, code review, CI, and CD into a single UI.

## Featured Technologies

* [IBM Cloud Functions](https://cloud.ibm.com/openwhisk): An event-action platform that allows you to execute code in response to an event.
* [Python](https://www.python.org/): A general purpose programming language.

## Steps

While you can use the individual actions locally, this collection of endpoints is meant to be deployed to IBM Cloud Functions. You can [deploy this application to IBM Cloud](https://cloud.ibm.com/developer/appservice/create-app?starterKit=8707985f-4ffc-3ac1-ae4f-54eea4f1a3ae) or [deploy it manually](#deploying-manually) by cloning this repo first.  

You can then review the [Actions](https://cloud.ibm.com/openwhisk/actions) in the IBM Cloud Console interface, along with your [Cloud Functions APIs](https://cloud.ibm.com/openwhisk/apimanagement).
<table>
  <thead>
      <tr>
        <th>Method</th>
        <th>HTTP request</th>
        <th>Description</th>
      </tr>
  </thead>
  <tbody>
    <tr>
      <td>Create</td>
      <td>POST /database</td>
      <td>Inserts an object</td>
    </tr>
    <tr>
      <td>Read</td>
      <td>GET /database/<font color="#ec407a">objectId</font></td>
      <td>Retrieves an object</td>
    </tr>
    <tr>
      <td>ReadAll</td>
      <td>GET /database</td>
      <td>Retrieves all objects</td>
    </tr>
    <tr>
      <td>Delete </td>
      <td>DELETE /database/<font color="#ec407a">objectId</font></td>
      <td>Deletes an object</td>
    </tr>
    <tr>
      <td>DeleteAll</td>
      <td>DELETE /database</td>
      <td>Deletes all objects</td>
    </tr>
    <tr>
      <td>update</td>
      <td>PUT /database/<font color="#ec407a">objectId</font></td>
      <td>Updates content of an object</td>
    </tr>
  </tbody>
</table>

### Deploying to IBM Cloud

<p align="center">
    <a href="https://cloud.ibm.com/developer/appservice/create-app?starterKit=8707985f-4ffc-3ac1-ae4f-54eea4f1a3ae">
    <img src="https://cloud.ibm.com/devops/setup/deploy/button_x2.png" alt="Deploy to IBM Cloud">
    </a>
</p>

Use the button above to deploy this same application to IBM Cloud. This option will create a deployment pipeline, complete with a hosted Git lab project and DevOps toolchain. [IBM Cloud DevOps](https://www.ibm.com/cloud/devops) services provides toolchains as a set of tool integrations that support development and deployment to IBM Cloud Functions. 


### Deploying Manually 

To deploy this application to IBM Cloud using the command line, you can leverage IBM Cloud Developer Tools. You will need to have the credentials for a Cloudant or CouchDB service, and need to update the feilds in the `localdev-config.json` file

* Install the [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) on your machine by running the following command:
  ```
  curl -sL https://ibm.biz/idt-installer | bash
  ```

* Install the [Whisk Deploy CLI](https://github.com/apache/incubator-openwhisk-wskdeploy/releases).

  If on a Mac or Linux, ensure the `deploy.sh` script is executable and run it:
  ```
  chmod +x deploy.sh
  ./deploy.sh
  ```

  Alternatively, you can run the `wskdeploy` command directly, you use the `--param` command line flags to provide values for the `services.cloudant.database` and `services.cloudant.url` values.

  ```bash
  /wskdeploy -m "manifest.yml" --param "services.cloudant.url" "<url>" --param "services.cloudant.database" "products"
  ```

  Where `<url>` is the URL value from your Cloudant service credentials.

## Next Steps
* Explore other [sample applications](https://cloud.ibm.com/developer/appservice/starter-kits) on IBM Cloud.

## License

[Apache 2.0](LICENSE)
