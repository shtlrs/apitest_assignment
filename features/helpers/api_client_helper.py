# Package imports
import requests
import json



class ApiClient:
    """
    Create a client that will communicate with an API's endpoint
    """

    def __init__(self, endpoint):
        """
        Initialize the api client
        
        :param endpoint: the api's endpoint that will be tested
        :type endpoint: string

        """

        self.endpoint = endpoint

    def create_gist(self, body, access_token):
        """
        Create a gist.
        
        :param body: the content that will be used to create the gist
        :type body: json
        :param access_token: the authentication token to allow access to gists
        :type access_token: string

        """
        self.response = requests.post(url=self.endpoint,
                                      headers={'Content-Type': 'application/json',
                                               'Authorization': 'bearer ' + access_token},
                                      json=json.loads(json.dumps(body)))
        return self

    def get_gist_id(self):
        """
        Retrieve the id of last made gist
        :return: id: The id of the last made gist
        :rtype id: string
        """
        id = self.response.json()["id"]

        return id

    def get_status_code(self):
        """
        Retrieve the status code of the last request made

        :return: status_code: the status code of the last request
        :rtype status_code: int
        """
        status_code = self.response.status_code

        return status_code

    def get_description(self):
        """
        Returns the gist's description
        :return: desciption: the gist's description
        :rtype: string
        """
        description = self.response.json()["description"]

        return description

    def get_gist(self, id, access_token):
        """
        Retrieve a specific gist by it's id
        :param id: id of the gist to be read
        :type id: int
        :param access_token: the authentication token to allow access to gists
        :type access_token: string
        """
        self.response = requests.get(url=self.endpoint + '/' + id,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'bearer ' + access_token}
                                     )
        # print(self.response.content)

    def delete_gist(self, id, access_token):
        """
        Deletes a specific gist by id
        :param id: id of the gist to be deleted
        :type id: int
        :param access_token: the authentication token to allow access to gists
        :type access_token: string
        """
        self.response = requests.delete(url=self.endpoint + '/' + id,
                                        headers={'Content-Type': 'application/json',
                                                 'Authorization': 'bearer ' + access_token})

    def update_gist(self, id, body, access_token):
        """
        Updates a specific gist by id


        :param id: id of the gist to be updated
        :type id: int
        :param body: the content that will be used to create the gist
        :type body: json
        :param access_token: the authentication token to allow access to gists
        :type access_token: string

        """
        self.response = requests.post(url=self.endpoint + '/' + id,
                                      headers={'Content-Type': 'application/json',
                                               'Authorization': 'bearer ' + access_token},
                                      json=json.loads(json.dumps(body)))
        return self

    def get_content(self, ):
        """
        Returns the url, files, description, id and the gist's type(public or secret),
        :return: url: gist's url
        :rtype: string
        :return: files: the gist's files
        :rtype:  dict
        :return: public: the gist type: public or secret
        :rtype: boolean
        :return: id: the gist's id
        :rtype: string
        :return: description: the gist's description
        :rtype: string
        """
        url = self.response.url
        files = self.response.json()["files"]
        public = self.response.json()["public"]
        id = self.response.json()["id"]
        description = self.response.json()["description"]

        return url, files, public, id, description
