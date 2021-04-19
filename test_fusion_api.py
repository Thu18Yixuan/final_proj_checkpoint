import requests
import json

API_KEY = "6CDPBSQ9LNshy9YK-_QJ0ePT28fnyUjCzoGdRjBzroNGeB9FlE85vmfBnFt5U2Xrd43cHbrbj2DLYng-CfpT7jeFllLeoJLj_4YkqMUtzQ-g5oNxngIRBFfI0iFmYHYx"

# I do this as the instructions on the webpage but I received a VALIDATION_ERROR, PLEASE HELP!
url = 'https://api.yelp.com/v3/businesses/north-india-restaurant-san-francisco'
headers = {'Authorization': 'Bearer 6CDPBSQ9LNshy9YK-_QJ0ePT28fnyUjCzoGdRjBzroNGeB9FlE85vmfBnFt5U2Xrd43cHbrbj2DLYng-CfpT7jeFllLeoJLj_4YkqMUtzQ-g5oNxngIRBFfI0iFmYHYx'}
response = requests.get(url, headers=headers)
json_response = response.json()
# json_res = json.loads(json_response)
print (json_response)
