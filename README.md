<h1>Pyglot</h1><br>

***REFERENCES***

**Python Virtual Environment** (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)<br>
  1. (In CLI or code editor e.g. Visual Studio Code), go to (i.e. cd for Windows) project directory, run "py -m venv env"
  2. In project directory, run ".\env\Scripts\activate"
  3. Install modules using pip/pip3
  4. Run "deactivate" to leave virtual environment

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
<font size="8">*Variables Setup, for personal use:* set PROJECT_ID=hello-315713 \ set PROJECT_NAME=pyglot \ set DOCKER_IMG=gcr.io/%PROJECT_ID%/%PROJECT_NAME% \ set REGION="us-central1"</font>

***PROBLEM:***<br>
Traditionally, investments are calculated using **average** prices and are not managed/realized **per transaction**.<br>
However, an **average** approach might not be as effective for cryptocurrency investment. Because cryptocurrency is highly volatile, the **average** approach may present psychological barriers. A scenario - you buy 1 Bitcoin (BTC) at USD 50000. It drops to USD 40000, and you buy 1 more. Your average buy price is between USD 45000, but BTC drops further to USD 30000. Psychological barriers include:
1. **BIG DIP** - The current price is way below your **average** price, so you may be psychologically paralyzed from "buying the dip" or psychologically pressured to sell at a loss, only to regret/FOMO when it bounces back up. HOWEVER, a **per transaction** approach may help you temporarily ignore your previous purchases, and perceive the current dip as new territory to invest in.
2. **BOUNCING BEAR** - You may "buy the dip" and buy 1 BTC at USD 30000. Now your average price is USD 40000. But BTC moves sideways over time, hovering between USD 30000 and USD 35000, never reaching USD 40000. During this sideway movement, you may be psychologically paralyzed from selling at USD 35000 and buying back at USD 30000 because it's all below your **average price** of USD 40000. HOWEVER, a **per transaction** approach may help you focus on "riding the waves" of BTC's bounce. Selling at USD 35000 and buying back at USD 30000 may not produce great profits, but is USD 0.01 profit insignificant?

***SOLUTION:***

<h1>BULLSHEET</h1><br/>
Python, SQL on Google Cloud Platform (Compute Engine, Cloud Storage, Cloud Functions, BigQuery) and Google Data Studio<br>
- Live at https://datastudio.google.com/reporting/43c0182a-33b4-42ab-823d-3515366f6e90<br>
- Reference: "How to automate financial data collection with Python using APIs and Google Cloud" at https://towardsdatascience.com/how-to-automate-financial-data-collection-with-python-using-tiingo-api-and-google-cloud-platform-b11d8c9afaa1<br>
- DAG: <br>
<img src="https://github.com/artc95/Bullsheet/blob/master/Bullsheet_DAG.PNG?raw=true" width="70%" height="70%"><br>
- Compute Engine User Interface: <br>
  
