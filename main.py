# Request and Response
# As you very briefly read above, all interactions
# between a
# client—in this case your Python console—and an API are split into
# a request and a response:

# Requests contain relevant data regarding your API request call,
# such as the base URL,
# the endpoint, the method used, the headers, and so on.
# Responses contain relevant data returned by the server,
# including the data or content, the status code, and the headers.


import requests
# response = requests.get("https://api.thedogapi.com/")
# print(response.text)
# '{"message":"The Dog API"}'

# RESOURCE

# response = requests.get("https://api.thedogapi.com/v1/breeds")


# REQUEST RESPONSE Cycle
# response = requests.get("https://api.thedogapi.com/v1/breeds")
# print(response)



# REQUEST
# print(response.request)
# print(response.request.url)
#
# print(response.request.path_url)
# print(response.request.method)
# print(response.request.headers)

# RESPONSE
# print(response)
# text returns the response contents in Unicode format.
# print(response.text)
# print(response.content)

# the requests library includes a specific .json()
# method that you can use to immediately convert the API bytes response into a Python data structure:
# print(response.json())
# print(response.status_code)
# print(response.reason)
# print(response.headers)


# EXAMPLE FAILED
# response = requests.get("https://api.thedogapi.com/v1/breedzz")
#
# print(response.status_code)
# print(response.reason)




# response = requests.get("https://api.thedogapi.com/v1/breeds?limit=3&page=1")
# print(response.request.path_url)
#
#
# url = "https://api.thedogapi.com/v1/breeds"
# params= {"limit":3, "page":1}
# response = requests.get(url=url, params=params)
# print(response.request.url)
# print(response.request.path_url)

#test test

#What are the most common reactions for every breed

response = requests.get("https://api.fda.gov/drug/event.json?limit=1")
print(response.text)


# url = 'https://api.fda.gov/drug/event.json?search=reactionmeddrapt:"headache"&limit=5'
# params= {"limit":5, "page":1}
# response = requests.get(url=url, params=params)
# print(response.request.url)
# print(response.request.path_url)


