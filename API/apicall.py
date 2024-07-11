import requests as r

response = r.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())

"""# Status codes
1xx-informational

2xx-successful
    200 OK success

3xx-redirection

4xx-client error
    400 Bad request
    401 Unauthorized
    404 Not found
5xx-server error
    500 internal server error
    503 service unavailable """


