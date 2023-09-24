import requests as req
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        res =  req.get(self.url)
        return res.content

    def load_json(self):

        return json.loads(self.get_response_body())


# import requests
# import json

# class GetRequester:

#     def __init__(self, url):
#         self.url = url

#     def get_response_body(self):

#         response = requests.get(self.url)
#         return response.content

#     def load_json(self):
#         return json.loads(self.get_response_body())
    
# requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
# print(requester.load_json())