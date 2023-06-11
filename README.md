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
        az webapp up --name flaskappduypq5 --resource-group Azuredevops --sku B1 --logs --runtime "PYTHON:3.9"
    - Run prediction against a working devloyed Azure Application using command:
        vim ./make_predict_azure_app.sh

[![Python application test with Github Actions](https://github.com/duypq154/devops2/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/duypq154/devops2/actions/workflows/pythonapp.yml)
