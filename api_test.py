import json
from pprint import pp

import requests

url = 'http://127.0.0.1:8000/api/v1/posts/'
put_url = "http://127.0.0.1:8000/api/v1/posts/11/"
delete_url = "http://127.0.0.1:8000/api/v1/posts/4/"
patch_url = "http://127.0.0.1:8000/api/v1/posts/11/"

payload = {
    "title": "Smoke_BackEnd",
    "content": "Abdukhamid1",
    "created": "2024-05-02T12:47:55.214779Z",
    "updated": "2024-05-02T12:47:55.214779Z",
    "is_published": True,
}
headers = {
  'Authorization': 'Basic cm9vdDoxMjM0',
  'Cookie': 'csrftoken=7JtGQzRdCnwS5tFFqeMNspVoGpyaVPZF'
}

def get_all_posts():
  response = requests.request("GET", url, headers=headers, data=payload)
  data = json.loads(response.text)
  return data

def put_post():
  response = requests.request("PUT", put_url, headers=headers, data=payload)
  put_data = json.loads(response.text)

  return put_data

def delete_post():
  response = requests.request("DELETE", delete_url, headers=headers, data=payload)
  delete_data = json.loads(response.text)

  return delete_data

def create_post():
  response = requests.request("POST", url, headers=headers, data=payload)
  create_data = json.loads(response.text)

  return create_data

def patch_post():
  response = requests.request("PATCH", patch_url, headers=headers, data=payload)
  patch_data = json.loads(response.text)

  return patch_data


if __name__ == '__main__':
  data = patch_post()
  pp(data)