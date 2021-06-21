<h1>Pyglot</h1><br>
Interactive Python web application using Flask and pywebio. Tests users (who are learning English) on when to use the definite article "the".<br>
Input: Any English text.<br>
Output: Produces input text but with "the"s replaced by blanks, and corresponding questions on whether or not to use "the".<br>
<br>

***REFERENCES***

**Python Virtual Environment** (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)<br>
  1. (In CLI or code editor e.g. Visual Studio Code), go to (i.e. cd for Windows) project directory, run "py -m venv env"
  2. In project directory, run ".\env\Scripts\activate"
  3. Install modules using pip/pip3
  4. Run "deactivate" to leave virtual environment

**GCP in Python Virtual Environment**
1. Ensure virtual environment is activated with (env) at the start of command line
2. Install necessary GCP modules (e.g. run "pip install --upgrade google-cloud-language")
3. Before running .py scripts:
  - Use virtual environment's interpreter (in Visual Studio Code, interpreter option is at the bottom)
  - Set Google Application Credentials e.g. run "set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\artc\Desktop\xxx.json" (instructions on creating Service Account, getting account key as .json file and setting Credentials as .json file https://cloud.google.com/docs/authentication/getting-started)


**Set and See Environment Variables in Windows**
- set VARIABLE=string
- echo %VARIABLE%

**PyWebIO, Flask**
- PyWebIO Documentation and Integration with Flask https://pywebio.readthedocs.io/en/latest/guide.html#integration-with-web-framework
- Flask quickstart guide https://flask.palletsprojects.com/en/1.1.x/quickstart/

**Containerize (a.k.a. Create Docker image), Upload image to Container Registry, Deploy to Cloud Run** (https://codelabs.developers.google.com/codelabs/cloud-run-hello-python3#4, https://towardsdatascience.com/how-to-deploy-docker-containers-to-the-cloud-b4d89b2c6c31 app.py deploy failed but consider Dockerfile line "RUN pip install -r requirements.txt" which iterates through requirements.txt to install modules)<br>
1. In project directory, create app.py and Dockerfile (and requirements.txt if needed)
2. In project directory, run "gcloud auth login" and log into Google Cloud Platform (GCP) using web browswer
3. *Containerize and Upload image to Container Registry*: In project directory, run "gcloud builds submit --tag gcr.io/%PROJECT_ID%/%PROJECT_NAME%", variables are:
  - set PROJECT_ID=string...ID generated by GCP for your project (usually project_name-number_sequence)
  - set PROJECT_NAME=string...name of your choice (usually project name)
  - set DOCKER_IMG=gcr.io/%PROJECT_ID%/%PROJECT_NAME%
and confirm that image successfully created with STATUS "SUCCESS"<br>
4. *Deploy to Cloud Run*: In project directory, run "gcloud run deploy %PROJECT_NAME% --image %DOCKER_IMG% --platform managed --region %REGION% --allow-unauthenticated", variables are:
  - REGION="string"...usually "us-central1"<br>

*Variables Setup in Windows Powershell, for personal use:* set PROJECT_ID=hello-315713<br>
set PROJECT_NAME=pyglot<br>
set DOCKER_IMG=gcr.io/%PROJECT_ID%/%PROJECT_NAME%<br>
set REGION="us-central1"
  
