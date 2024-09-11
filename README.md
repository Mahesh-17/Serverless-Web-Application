# CMPE 272 - Assignment 2 : 

Building a serverless web application using AWS Lambda and DynamoDB and to get familiarity with CRUD operations on cloud.

## Prerequisites:

Create an AWS cloud free tier account and set the preferred region

## Creating Table Using DynamoDB :

Navigate to DynamoDB in AWS Management Console and click on create table

- Table Name  : StudentRecords
- Primary Key : student_id(string)

<img width="1195" alt="TableCreation" src="https://github.com/user-attachments/assets/d16d8543-0b71-4b2e-9f4d-845a9210615a">

## Setting up AWS Lambda Function :

- Navigate to Lambda in AWS Management Console and click on create function
- Set the function name as StudentRecordHandler and choose the runtime as Python 3.12


<img width="1440" alt="FuncCreation" src="https://github.com/user-attachments/assets/488d32b1-4504-4d4c-9ade-35efbc6a1eed">


## Attching the Policies :

- Navigate to IAM Dashboard and go to the roles and select the role named StudentRecordHandler
- Attach the policy named AmazonDynamoDBFullAccess, which grants full access to DynamoDB resources to perform CRUD operations.

<img width="1440" alt="PolicyAttach" src="https://github.com/user-attachments/assets/41e15821-6f77-4349-ba1c-c1251a5f0082">

## Adding the code :

- Once setting up the policy, navigate to lambda function and select the created function
- Go to code source and write the code for CRUD operations and deploy it

##  Creating an API Gateway :

- Navigate to API Gateway in the AWS Management Console and click on create API
- Choose the API type as REST api and create an API named StudentAPI

## Setting up Resources :

- Once the API is created go the StudentAPI and click on create resources
- Choose the resource-name as /students(endpoint) and create resource

## Creating Methods for the resources :

- Once the endpoint got created click on the create method by clicking the created end point
- Choose the method name as POST, integration type as lambda function and choose the lambda function by placing the correcting region   and create the method
- Follow the same process for GET method as well.

<img width="1440" alt="GetResource" src="https://github.com/user-attachments/assets/e18c2ca5-81a9-46b2-ac86-844073054c6b">

- Screenshot of API Gateway once the methods were created :
  
<img width="1440" alt="ApiGateway" src="https://github.com/user-attachments/assets/39b1375b-eb26-43e6-91d3-13983372c45b">


## Deploy API :

Once the methods created, Click on Deploy API button and choose stage name as UAT/Dev/Prod(Choosen staging as Dev) and deploy it by adding description(optional).

<img width="1440" alt="DevDeploy" src="https://github.com/user-attachments/assets/98f65aa0-bb0b-44fe-a09d-0f0266cd66d7">


## Testing the Application :

Testing the application using the below curl command

 1. Create :
            curl -X POST \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students \
  -H 'Content-Type: application/json' \
  -d '{"action": "create", "student_id": "123", "name": "John Do", "course": "Enterprise Software Platforms"}'

  <img width="835" alt="Create" src="https://github.com/user-attachments/assets/bfac4cb7-fceb-4353-a8e3-c49073d93f8d">
  
 
 2. Update :
            curl -X POST \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students \
  -H 'Content-Type: application/json' \
  -d '{"action": "update", "student_id": "123", "name": "John Doe", "course": "Enterprise Software Platforms"}'

    <img width="835" alt="Update" src="https://github.com/user-attachments/assets/bdc4ff29-bbcd-4f00-a326-c8cb92ce2e13">
    

    Initial Table :

      <img width="1440" alt="IntitialTable" src="https://github.com/user-attachments/assets/2e3f7598-5946-4d5e-8811-7b8b8a0ad56d">

    Updated Table :

      <img width="1440" alt="UpdatedTable" src="https://github.com/user-attachments/assets/c5cd7a25-8734-4d5f-b570-5604dc4689cf">

      Updated the name to "John Doe" from "John Do"   

 
 3. Delete :
            curl -X POST \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students \
  -H 'Content-Type: application/json' \
  -d '{"action": "delete", "student_id": "111"}'

    
    <img width="836" alt="Delete" src="https://github.com/user-attachments/assets/d92ed003-e99c-4f24-a709-f63b8b015a78">

  - Record Deleted from the table

    <img width="1440" alt="FinalTable" src="https://github.com/user-attachments/assets/a21913ea-e669-4e59-aa1f-2c6632893276">

    
 4. Read :
             curl -X POST \
  https://<your-api-id>.execute-api.<region>.amazonaws.com/dev/students \
  -H 'Content-Type: application/json' \
  -d '{"action": "read", "student_id": "123"}'

  <img width="840" alt="Read" src="https://github.com/user-attachments/assets/ba181710-cb53-4597-88fa-2ddc85b2132c">


  ## Reflection - Challenges I faced & What I learnt :

  - Understanding serverless architecture is essential for modern cloud computing, with AWS Lambda functions leading this shift. By learning to develop and deploy Lambda functions, developers can build scalable, event-driven applications without the need for server management. 
  - This serverless model pairs effectively with NoSQL databases like Amazon DynamoDB, which features a flexible key-value data model. Proficiency in DynamoDB's query syntax, including operations such as put_item and get_item, is crucial for effective data management.
  - To turn Lambda functions into RESTful APIs, configuring Amazon API Gateway is a vital skill. Additionally, using AWS SDKs like boto3 facilitates smooth interaction with DynamoDB within Lambda functions, creating a robust, serverless backend system.

    
## This README.md file provides clear overview on how to build and test the serverless application using AWS on cloud

