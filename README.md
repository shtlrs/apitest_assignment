# Project Title

GitHub's Gist API test

## Getting Started

This project was written in python to test Github's gist api.
The test cases were developped using the Behavior Driven Development method.
The requests were sent using python's 3rd party library: request.

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

To run all the test cases, open a terminal in the project's root directory and type to following command:

```
behave
```

If you want to run the results and save them into the results folder which is in the root directory, open a terminal in the root directory and execute the following command:
```
behave -f json -o ./results/result_file_name.json
```

## Running the tests and fetching results with allure

If you want to see the results in a more presentable way than a json file, you could use allure.
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


### Break down into end to end tests

This tests the creation of a new gist via the api with a valid json

```
  Scenario: Create new gist with valid json
```
This tests the creation of a new gist via the api with an invlid json body

```
  Scenario: Create new gist with invalid json
```
This tests the creation of a new gist via the api with a string

```
  Scenario: Create new gist with a string
```
This tests the creation of a new gist via the api with an integer

```
  Scenario: Create new gist with an integer
```
This tests the creation of a new gist via the api with a boolean

```
  Scenario: Create new gist with a boolean
```
This tests the creation of a new gist via the api with a list

```
  Scenario: Create new gist with a list
```
This tests the creation of a new gist via the api with an invalid authentification token

```
  Scenario:Create new gist with invalid token
```
This tests the creation of a new gist via the api with no authentification token

```
  Scenario:Create new gist with no token
```
This tests the reading of an existing gist

```
 Scenario: Retrieve an existing gist by id
```
This tests the reading of an unexisting gist

```
  Scenario: Retrieve an unexisting gist by id
```
This tests the updating of an existing gist

```
  Scenario: Update an existing gist
```
This tests the updating of an unexisting gist

```
  Scenario: Update an unexisting gist
```
This tests the deletion of an existing gist

```
  Scenario: Delete an existing gist
```
This tests the deletion of an unexisting gist

```
  Scenario: Delete an unexisting gist
```






## Authors

* *Amrou Bellalouna* 


