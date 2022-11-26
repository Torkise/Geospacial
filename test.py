import requests

url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"no","service":"hbo","type":"movie"}

headers = {
	"X-RapidAPI-Key": "edab4e7123msh8344a8f5fa69601p18c787jsnfaff8cc039db",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)