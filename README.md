# CDTM MPD Prostate IoT Button

Welcome to the CDTM MDP PROSTATE - Prostate / Procare IoT Button code repository.

This Code was written in the context of 
the Managing Product Development Course 
at the Center for Digital Technology and Management. 

## Disclaimer
This is a prototype. Do not use it in a production setting!

This project gives an outlook what you could do. 
It was not meant to run anywhere in production.

## Abstract 
Cancer is a widespread disease in modern world. 
Prostate cancer is a cancer type which affects only men and the onset happens around the age of 65 in majority of the cases. 
This disease accompanies a wide array of symptoms which are often not reported routinely due to multitude of reasons. 
Studies have found that routine reporting of symptoms leads to several clinical benefits in terms of combating the disease progression. 
Procare is a solution aimed at connecting the patient with the doctor digitally in order to enable the doctor to more easily keep track of the disease progression in the patient and take preventive measures to prolong the patients life expectancy. 
It is a digital ecosystem which offers facilities of symptom reporting, medication tracking, a knowledge network, and a chat feature for the patient to talk with the doctor. 
A patient can interact with the ecosystem easily using the web/mobile interface or smart devices such as Amazon Alexa or Amazon IoT Button.

# Team
* Saad
* Ibrar
* Afrida
* Sebastian

# Project Description

# Set-Up

1. Clone the Git Repository (https://github.com/SbstnErhrdt/cdtm-mpd-prostate-iot-button). You can do that by executing the following command on your system in the Terminal / Command Line Interface
`$ git clone https://github.com/SbstnErhrdt/cdtm-mpd-prostate-iot-button  


2. Make sure you have installed nodejs and the node package manager. See frontend installation:
You have to install NodeJS on your system.
Go to the node website (https://nodejs.org/en/) and download the latest version and install it.
By default it should also install the Node Package Manager (NPM)

3. Install the necessary dependencies of the application. 
Go to the root folder of the app and execute the following command. \
`$ npm install`

4. Adapt the handle in the handler.py file with the specific endpoint of you production backend instance. \ 
`r = requests.post('XXX/api/1/iot/medication', json=event)`
(line 13)
E.g. replace `XXX with` `https://PRODUCTION.MYURL.TLD:PORT/` so that the final output looks like 
`https://PRODUCTION.MYURL.TLD:PORT/api/1/iot/medication`

5. Follow the serverless guide with regards to Amazon Web Services:
https://serverless.com/framework/docs/providers/aws/guide/credentials/ 
   
6. Deploy the skill by executing \
`$ sls deploy production` \
You will get an URL of the endpoint. Save the url you will need it in step.

7. Use the app of your AWS IoT Button and connect to the specific button

8. Log in with your AWS credentials and set the endpoint to the specific lambda function you just deployed with the serverless framework.


# Codebase

This repository basically just consist out of one file. 

The `handler.py` file. Within this file the request of the IoT device is just forwarded to and endpoint of the backend.	
In the `serverless.yml the specifications to the deployment of the function can be made			 	