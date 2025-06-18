# Flask Threat Detection App (Azure Monitor)

A demo Flask web application that logs every login attempt and streams those logs to Azure Monitor (Log Analytics) for threat-detection practice.

## Features

- /login route with hard-coded credentials  
- Logs all login attempts (success and failure) to stdout  
- Azure App Service captures the logs and sends them to a Log Analytics workspace  
- Useful for practicing Kusto Query Language (KQL) queries

## Getting Started

### 1. Create a virtual environment
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run locally
python app.py

Then open http://localhost:5000/login in your browser.

## Test Credentials

- Username: student  
- Password: CollegePassword#2345

## Deploying to Azure

1. Create a Resource Group and App Service (Linux, Python 3.11).
2. Set the startup command:
   gunicorn --bind=0.0.0.0 app:app
3. Enable diagnostic settings for App Service Application Logs and Console Logs; send them to Log Analytics.
4. Push the code:
   git remote add azure https://<your-app>.scm.azurewebsites.net/<your-app>.git
   git push azure main

## Sample KQL

AppServiceAppLogs
| where TimeGenerated > ago(1h)
| where Message has "Login attempt"
| project TimeGenerated, Message
| order by TimeGenerated desc

## Key Files

- app.py – Flask application  
- requirements.txt – Python dependencies  
