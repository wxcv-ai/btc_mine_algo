import requests
# https://campeonbet.com/sports
url = "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLivenow?timezoneOffset=-60&langId=8&skinName=campeonbet&configId=12&culture=en-GB&countryCode=TN&deviceType=Mobile&numformat=en&integration=campeonbet&sportId=68&showAllEvents=false&count=10"

payload={}
headers = {
  'authority': 'sb2frontend-altenar2.biahosted.com',
  'accept': '*/*',
  'accept-language': 'en,en-US;q=0.9,fr;q=0.8',
  'origin': 'https://campeonbet.com',
  'referer': 'https://campeonbet.com/',
  'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
