import requests
import json

API_KEY = "6CDPBSQ9LNshy9YK-_QJ0ePT28fnyUjCzoGdRjBzroNGeB9FlE85vmfBnFt5U2Xrd43cHbrbj2DLYng-CfpT7jeFllLeoJLj_4YkqMUtzQ-g5oNxngIRBFfI0iFmYHYx"


test_url_1 = 'https://api.yelp.com/v3/businesses/north-india-restaurant-san-francisco'
test_url_2 = 'https://api.yelp.com/v3/businesses/search?term=restaurants&location=New_York'
headers = {'Authorization': 'Bearer 6CDPBSQ9LNshy9YK-_QJ0ePT28fnyUjCzoGdRjBzroNGeB9FlE85vmfBnFt5U2Xrd43cHbrbj2DLYng-CfpT7jeFllLeoJLj_4YkqMUtzQ-g5oNxngIRBFfI0iFmYHYx'}
response = requests.get(test_url_2, headers=headers)
json_response = response.json()
# json_res = json.loads(json_response)
print (json_response)

