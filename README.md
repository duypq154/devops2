# devops2
# Overview
- This is a "Building CI/CD pipeline project"
- In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.
- You will build and learn following capacibility:
 1. Connect to your Github Repo using ssh key from Azure
 2. (CI) Deploy Github Action to automate testing and verify your code after commit
 3. (CD) Deploy the application in Azure CloudShell.
 4. (CD) Deploy Azure App Service via CLI
 5. Azure DevOps pipeline: A pipeline has been set up in Azure DevOps to automatically test and deploy the updated code to the Azure App Service.

# Plan
- Trello plan: https://trello.com/b/tnGwokZy/devops
- Project Management Template: https://github.com/duypq154/devops2/blob/main/Project_plan/Project%20Management%20Template.xlsx

# Instructions
1. Setup Azure Cloud Shell:
    - Create a GubHub Repo (https://github.com/duypq154/devops2)
    - Launch Azure Cloud Shell environment and create ssh key using command:
         ssh-keygen -t rsa
    - Access to your ssh key using command:
         cat /home/odl_user/.ssh/id_rsa.pub
    - Add created ssh key to your GitHub:
         Go to Settings => SSH and GPG keys => New SSH Key
    - Clone your GitHub Repo from Azure CLI using command:
         git clone git@github.com:duypq154/devops2.git
    - Change directory to your repo after cloned using command:
	    cd devops2
	- Create a Python virtual environment using command:
	    python -m venv devops2
	- Access to your virtual environment using command:
	    source devops2/bin/activate
    - Create Makefile, requirements.txt, Python Virtual Environment, script and test script files
    - Run make all to install dependency, test and lint your code using command:
         make all
    - Result of clone actions: https://github.com/duypq154/devops2/blob/main/output/clone_project_powershell.png
    - Result of "make all" actions: https://github.com/duypq154/devops2/blob/main/output/Makeall_result_in_Makefile.png

2. CI Configure Github Action:
    - Go to your Github Account and enable Github Actions
    - Replace .yml file with your code to make CI when any push actions perform
    - Push the changes to GitHub and verify that both lint and test steps pass in your project
    - Result of GitHub Actions: https://github.com/duypq154/devops2/blob/main/output/Passing%20of%20GitHub%20Action.png

3. CD on Azure:
    - Get your app from GitHub: https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/tree/master/C2-AgileDevelopmentwithAzure/project/starter_files
    - Run your app using command:
        python app.py
    - Create Azure WebApp Service using command:
        az webapp up --name flaskappduypq5 --resource-group Azuredevops --sku B1 --logs --runtime PYTHON:3.9
        result: https://flaskappduypq5.azurewebsites.net/
    - Run prediction against a working devloyed Azure Application using command:
        chmod +xr make_predict_azure_app.sh
        ./make_predict_azure_app.sh
    - Trace streamed log files from deployed application
	    az webapp log tail -g Azuredevops --name flaskappduypq5
    - Result of created Azure WebApp Service: https://github.com/duypq154/devops2/blob/main/output/Deploy_WebAppService_Result.png
    - Result of make prediction: https://github.com/duypq154/devops2/blob/main/output/Make_prediction_azure_app_result.png
    - Result of log tail: https://github.com/duypq154/devops2/blob/main/output/Webapp_LogTail_Result.png

    - Logged into the https://portal.azure.com/
    - Created a DevOps org at https://dev.azure.com/
    - Created a DevOps publish project: GO to Organization setting => Policies => Allow public project => create your public project
    - Create Service Connection on DevOps project: Go to the Project settings >> Service connection settings, and ensure you set up a new service connection via Azure Resource Manager and Service principal
    - Create personal access token: From your devops project, go to User settings => Personal access tokens => save your PAT
    - Create your self-hosted Agent Pool: Go to the Project Settings => Agent pools and add a new agent pool, say myAgentPool
    - Create an Agent (VM): Using Azure UI to create a default VM quickly
    - Connect to your VM using command:
        ssh myagent@(Your VM public IP)
    - Install docker in your VM using command:
        sudo snap install docker
    - Upgrade your python using command:
        sudo apt update
    - Configure the your user to run Docker using command:
        sudo groupadd docker
        sudo usermod -aG docker $USER
        exit
        restart your VM to apply new setting
    - Create Agent Service:
        Go to Project settings => Agent pools => New Agent
        ReConnect to your VM using command:
        ssh myagent@(Your VM public IP)
        Download your agent pool to VM by command:
             curl -O https://vstsagentpackage.azureedge.net/agent/3.220.5/vsts-agent-linux-x64-3.220.5.tar.gz
             pwd
             ls
        Create a new folder and cd to it: 
            mkdir myagent && cd myagent
        Extract agent:
             tar zxvf ~/vsts-agent-linux-x64-3.220.5.tar.gz
        Run config agent by command:
             ./config.sh
        Provide your organization devops link
        Provide your PAT
        Provide your AgentPool Name
        Provide your agent name created in VM
        Start the azure pipeline agent service by command:
            sudo ./svc.sh install
            sudo ./svc.sh start
    - Application Specific Configuration:
        sudo apt-get install python3.9-venv
        sudo apt-get install python3-pip
        pip install pylint==2.13.7
        Update the Path for Pylint.
            export PATH=$HOME/.local/bin:$PATH
            echo $PATH
            which pylint
        Result of agent service: https://github.com/duypq154/devops2/blob/main/output/Agent_Pool.png
    - Create a PipeLine: 
        Go back to your devops project => Pipeline => Create Pipeline => GitHub ==> Choose your Repo
        Result of Pipeline run: https://github.com/duypq154/devops2/blob/main/output/Pipeline_result.png
    - Add more Jobs to the Pipeline:
        Install zip into your VM to run pipeline Archive file:
            sudo apt-get -y install zip
        Result of multiple job in Pipeline:https://github.com/duypq154/devops2/blob/main/output/Pipeline_multiple_step_result.png
    - Add Deployment Stages to the Pipeline:
        Result of deployment stage in Pipeline: https://github.com/duypq154/devops2/blob/main/output/Deployment_Stage_in_Pipeline_Result.png
    
hello github repo test
[![Python application test with Github Actions](https://github.com/duypq154/devops2/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/duypq154/devops2/actions/workflows/pythonapp.yml)
