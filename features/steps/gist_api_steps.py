from behave import *
import requests
import json
import os
from configparser import ConfigParser
from features.helpers.api_client_helper import apiClient
from ast import literal_eval
from compare import expect

#----------Preconfiguration---------------#
parser = ConfigParser()
path = os.path.join(os.getcwd(),"config\\config.ini")
parser.read(path)

url = parser.get("URLS","base_url")
gists_endpoint = parser.get("URLS","gists_endpoint")
access_token = parser.get("KEYS","access_token")
gist_1 = literal_eval(parser.get("BODY","gist_1"))
gist_2 = literal_eval(parser.get("BODY","gist_2"))
gist_3 = literal_eval(parser.get("BODY","gist_3"))
gist_4 = literal_eval(parser.get("BODY","gist_4"))
gist_5 = literal_eval(parser.get("BODY","gist_5"))
string_gist = literal_eval(parser.get("BODY","string_gist"))
int_gist = literal_eval(parser.get("BODY","int_gist"))
boolean_gist = literal_eval(parser.get("BODY","boolean_gist"))
list_gist = literal_eval(parser.get("BODY","list_gist"))
improper_dict_gist = literal_eval(parser.get("BODY","improper_dict_gist"))


#----------Creating an instance of the api Client class-----------#

client = apiClient(url+gists_endpoint)

@given('user creates a new gist with {state}')
def step_create_new_gist(context,state):
    """
    Create gists with valid and invalid json body
    This function is fired when parsing the feature file to test the Scenario of creating gists

    :param context: object used to hold contextual information during the running of tests
    :param state: State of the json body used to create the gist ( valid or invalid )
    :type state: string
    """

    if state =="valid_json_body":
        client.create_gist(gist_1,access_token)
    elif state == "invalid_json_body":
        client.create_gist(improper_dict_gist,access_token)
    elif state ==  "a_string":
        client.create_gist(string_gist,access_token)
    elif state == "an_int":
        client.create_gist(int_gist,access_token)
    elif state == "a_boolean":
        client.create_gist(boolean_gist,access_token)
    elif state == "a_list":
        client.create_gist(list_gist,access_token)

@given('user authenticates with {token}')
def step_authentication(context,token):
    """

    Authentication with wrong credentials

    :param context: object used to hold contextual information during the running of tests

    :param token: type of token used for authentication
    :type token: string
    """
    if token == "invalid_token":
        client.create_gist(gist_1,"wrongacesstoken")
    elif token =="no_token":
        client.create_gist(gist_1, '')


@given('user searches for an {state} gist by id')
def step_search_for_gist(context,state):
    """
    Retrieves gists with existing and unexisting ids (e.g gists)
    This function is fired when parsing the feature file to test the Scenario of retrieving gists

    :param context: object used to hold contextual information during the running of tests
    :param state: State of the gist that will be retrieved (existant of unexistant)
    :type state: string
    """
    if state == "existing":
        client.create_gist(gist_2,access_token)
        id = client.get_gist_id()
        client.get_gist(id,access_token)
    elif state =="unexisting":
        client.get_gist("blabliblou",access_token)



@given('user updates an {state} gist by id')
def step_update_gist(context,state):
    """
    Update gists with existing and unexisting ids (e.g gists)
    This function is fired when parsing the feature file to test the Scenario of updating gists

    :param context: object used to hold contextual information during the running of tests
    :param state: State of the gist that will be updated (existant of unexistant)
    :type state: string
    """
    if state == "existing":
        client.create_gist(gist_3,access_token)
        id = client.get_gist_id()
        print("HAW EL ID YA ZEBBI:", id)
        client.update_gist(id,gist_5,access_token)
    elif state =="unexisting":
        client.update_gist("blabliblou",gist_5,access_token)


@given('user deletes an {state} gist by id')
def step_delete_gist(context,state):
    """
    Delete gists with existing and unexisting ids (e.g gists)
    This function is fired when parsing the feature file to test the Scenario of deleting gists

    :param context: object used to hold contextual information during the running of tests
    :param state: State of the gist that will be deleted (existant of unexistant)
    :type state: string
    """
    if state == "existing":
        client.create_gist(gist_3,access_token)
        id = client.get_gist_id()
        print("HAW EL ID YA ZEBBI:", id)
        client.delete_gist(id,access_token)
    elif state =="unexisting":
        client.delete_gist("blabliblou",access_token)


@then('response code should be {code}')
def step_assert_response_code(context,code):
    """
    Compare the request's actual status code with the expected one
    This function is fired when parsing the feature file to compare actual response codes to expected ones
    :param context: object used to hold contextual information during the running of tests
    :param code: expected status code
    :type code: string
    """
    status_code = client.get_status_code()
    expect(status_code).to_equal(int(code))

@then('the description of gist {gist_number} should be correct')
def step_assert_gist_description(context,gist_number):
    """
    Compare the created or updated gist's description with the initial description
    This function is fired when parsing the feature file to validate that the gists have the correct description
    :param context: object used to hold contextual information during the running of tests
    :param gist_number: number of the gist that was  created/ read or updated
    :type code: string
    """

    description = client.get_description()
    if gist_number == 1:
        expect(description).to_equal(gist_1["description"])
    elif gist_number == 2:
        expect(description).to_equal(gist_2["description"])
    elif gist_number == 5:
        expect(description).to_equal(gist_5["description"])