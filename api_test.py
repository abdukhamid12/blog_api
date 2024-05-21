import requests
import json

url = "https://blog-api-1-e1yr.onrender.com/api/v1/posts/"
url_for_users = "https://blog-api-1-e1yr.onrender.com/api/v1/users/"

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic eG9taWQ6MTIzNA=='
}



def get_all_posts():
  try:
    response = requests.request("GET", url, headers=headers, data=payload)
    my_json = json.loads(response.text)
    return my_json
  except Exception as e:
    return [{"title": "Nice Try!", "content": "Ma'lumot qo'shing"}]

def get_all_users():
    response = requests.request("GET", url_for_users, headers=headers, data=payload)
    my_json = json.loads(response.text)
    return my_json

# def put_post():
#   response = requests.request("PUT", put_url, headers=headers, data=payload)
#   put_data = json.loads(response.text)
#
#   return put_data
#
# def delete_post():
#   response = requests.request("DELETE", delete_url, headers=headers, data=payload)
#   delete_data = json.loads(response.text)
#
#   return delete_data
#
# def create_post():
#   response = requests.request("POST", url, headers=headers, data=payload)
#   create_data = json.loads(response.text)
#
#   return create_data
#
# def patch_post():
#   response = requests.request("PATCH", patch_url, headers=headers, data=payload)
#   patch_data = json.loads(response.text)
#
#   return patch_data
#
#
# if __name__ == '__main__':
#   data = patch_post()
#   pp(data)