# Project Title

GitHub's Gist API test with Python's requests library.

## Getting Started

This project was written in python to test Github's gist api.  
The test cases were developped using the Behavior Driven Development method.  
The requests were sent using python's 3rd party library: requests.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3 (https://www.python.org/downloads/)
```
```
3rd party libraries that will be listed in the installing section
```

### Installing

This section lists the third party python modules that need to be installed for this test to be run

```
pip install behave
```

```
pip install compare
```
```
pip install requests
```
```
pip install allure-behave
```


## Running the tests

###Note:  
Before running the tests, you need to put in your personal acces token in the config file: section "KEYS"  
Here are the steps to create a personal access token:  
https://github.blog/2013-05-16-personal-api-tokens/


To run all the test cases, open a terminal in the project's root directory and type to following command:

```
behave
```
## Running the tests and saving results into a result folder

If you want to run the results and save them into the results folder which is in the root directory, open a terminal in the root directory and execute the following command:
```
behave -f json -o ./results/result_file_name.json
```

## Running the tests and fetching results with allure
Allure Framework is a flexible multi-language test report tool  
Allure shows a very concise representation of what has been tested in a neat web report form.  

To do so, you first need to install allure on windows.
### Steps to install allure
#### Install scoop 
Scoop 
1. Install scoop (https://scoop.sh/) 
Scoop is a package manager for windows.
Open windows Power shell and type in the following commands:  
```Set-ExecutionPolicy RemoteSigned -scope CurrentUser```  
then:  
```iex (new-object net.webclient).downloadstring('https://get.scoop.sh')```
2. Install allure (Documentation: https://docs.qameta.io/allure/)
```scoop install allure```
3. Run tests with allure-behave  
3.1. Go to the project's root directory   
3.2. Run the following command : ```behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ```  
This will generate JSON report to ```%allure_result_folder% ```   
3.3. Run the command: ```allure serve %allure_result_folder%```
    This will allow you to view HTML report.


### Break down of the test scenarios

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






## Authors

* *Amrou Bellalouna* 


