# Project Title

GitHub's Gist API test with Python's requests library.

## Getting Started

This project was written in python to test Github's gist api.  
The test cases were developped using the Behavior Driven Development method.  
The requests were sent using python's 3rd party library: requests.

### 1. Prerequisites

To be able to run the tests, python and the 3rd party modules need to be installed.
Depending on your plateform, here's how to do proceed:


#### Linux 
1. Install python  
Open a terminal and execute the following:  
```
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-pip
alias pip=pip3
alias python=python3
```  

 2 . Install 3rd party libraries

After having installed python,  open a terminal in the project's root directory and execute the following
```
python -m pip install -r ./requirements.txt
```

#### Windows 
1. Install python ( **__Don't forget to add python to path__**)
```
Python 3 (https://www.python.org/downloads/)
```  
2 .Install 3rd party libraries  
After having installed python,  open a terminal in the project's root directory and execute the following
```
pip install -r ./requirements.txt
```

### 2. Running the tests

#### Note:  
Before running the tests, you need to put in your personal acces token in the config file: section "KEYS"  
Here are the steps to create a personal access token:  
https://github.blog/2013-05-16-personal-api-tokens/


To run all the test cases, open a terminal in the project's root directory and type to following command:

```
behave
```
#### 2.1. Running the tests and saving results into a result folder

If you want to run the results and save them into the results folder which is in the root directory, open a terminal in the root directory and execute the following command:
```
behave -f json -o ./results/result_file_name.json
```

#### 2.2. Running the tests and fetching results with allure
Allure Framework is a flexible multi-language test report tool  
Allure shows a very concise representation of what has been tested in a neat web report form.  

To do so, you first need to install allure on windows.
##### 2.2.1.Steps to install allure
##### Linux
``` 
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure
```
##### Note:  
You  may encounter problems when executing allure later on, if you do so, here's a workaround for the problem:  
```
curl -o allure-2.6.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.6.0/allure-2.6.0.tgz   
sudo tar -zxvf allure-2.6.0.tgz -C /opt/   
sudo ln -s /opt/allure-2.6.0/bin/allure /usr/bin/allure  
```
#### Windows
1. Install scoop (https://scoop.sh/) 
 
Scoop is a package manager for windows.
Open windows Power shell and type in the following commands:    
```
Set-ExecutionPolicy RemoteSigned -scope CurrentUser   
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
```
2. Install allure (Documentation: https://docs.qameta.io/allure/)  
```
scoop install allure
```  

#### 2.2.2. Running tests with allure
```
cd %project_root_directory%  
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder%  
allure serve %allure_result_folder%
```


### 3. Break down of the test scenarios

The following scenario tests the creation of a new gist via the api with a valid json

```
  Scenario: Create new gist with valid json
```
The following scenario tests the creation of a new gist via the api with an invlid json body

```
  Scenario: Create new gist with invalid json
```
The following scenario tests the creation of a new gist via the api with a string

```
  Scenario: Create new gist with a string
```
The following scenario tests the creation of a new gist via the api with an integer

```
  Scenario: Create new gist with an integer
```
The following scenario tests the creation of a new gist via the api with a boolean

```
  Scenario: Create new gist with a boolean
```
The following scenario tests the creation of a new gist via the api with a list

```
  Scenario: Create new gist with a list
```
The following scenario tests the creation of a new gist via the api with an invalid authentification token

```
  Scenario:Create new gist with invalid token
```
The following scenario tests the creation of a new gist via the api with no authentification token

```
  Scenario:Create new gist with no token
```
The following scenario tests the reading of an existing gist

```
 Scenario: Retrieve an existing gist by id
```
The following scenario tests the reading of an unexisting gist

```
  Scenario: Retrieve an unexisting gist by id
```
The following scenario tests the updating of an existing gist

```
  Scenario: Update an existing gist
```
The following scenario tests the updating of an unexisting gist

```
  Scenario: Update an unexisting gist
```
The following scenario tests the deletion of an existing gist

```
  Scenario: Delete an existing gist
```
The following scenario tests the deletion of an unexisting gist

```
  Scenario: Delete an unexisting gist
```






## Author

* *Amrou Bellalouna* 


