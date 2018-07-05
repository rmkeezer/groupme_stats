import requests

msg = "test"
response = requests.post(
    url="http://127.0.0.1:80/post?text=testing")
print(response.status_code, response.reason)