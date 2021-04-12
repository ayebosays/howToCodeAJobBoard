import requests

# Adzuna API Status Codes
#
# Adzuna API URL: https://developer.adzuna.com/
#
# 200: Everything went okay, and the result has been returned (if any)
# 301: The server is redirecting you to a different endpoint.
#      This can happen when a company switches domain names, or an endpoint name is changed.
# 400: The server thinks you made a bad request. This can happen when you don't send along
#      The rigth data, among other things.
# 401: The server thinks you're not authenticated. Many APIs require login credentials,
#      so this happens when you don't send the right credentials to access an API
# 403: The resource you're trying to access is forbidden: You don't have the right
#      permissions to see it.
# 404: The resource you tried to access wasn't found on the server.
# 503: The server is not ready to handle the request.
#
# /api/version?app_id=9fe38888&app_key=f625066fd57c72fc852be0a6c018d27c


# Querying the API
# The root URL of the API is located at: https://api.adzuna.com/v1/api
# Suppose you want to query: https://api.adzuna.com/v1/api/jobs/gb/search/1
#
# You will have to pass two obligatory parameters:
# - app_id
# - app_key
#
# Putting it all together, the call will look like this:
#
# https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={YOUR_APP_ID}&app_key={YOUR_APP_KEY}


# JSON
#
# To receive JSON, set your Accept header to application/json
# The data will be then returned as UTF-8 JSON
# Some characters may be escaped as \uXXXX, as described in the JSON specification: http://www.json.org/

#appId = '9fe38888'
#appKey = 'f625066fd57c72fc852be0a6c018d27c'

try:
    url = "https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=9fe38888&app_key=f625066fd57c72fc852be0a6c018d27c"
    r = requests.get(url)
    print("Entire JSON response\n")
    print(r.json())

except r.status_code == 200:
    print("An error occured:")

