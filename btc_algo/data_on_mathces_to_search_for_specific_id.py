import requests
import json

url = "https://guest.api.arcadia.pinnacle.com/0.1/sports/33/matchups/live?withSpecials=false"

payload={}
headers = {
  'Host': 'guest.api.arcadia.pinnacle.com',
  'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'X-Device-Uuid': '824649d5-bd265640-748dda63-41e89823',
  'Sec-Ch-Ua-Mobile': '?1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Api-Key': 'CmX2KcMrXuFmNg6YFbmTxE0y9CIrOi0R',
  'Sec-Ch-Ua-Platform': '"Android"',
  'Origin': 'https://www.pinnacle.com',
  'Sec-Fetch-Site': 'same-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.pinnacle.com/',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'fr-FR,fr;q=0.9,ar-TN;q=0.8,ar;q=0.7,en-US;q=0.6,en;q=0.5',
  'If-Modified-Since': 'Fri, 03 Feb 2023 21:28:42 GMT'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
