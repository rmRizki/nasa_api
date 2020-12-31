import json
from urllib import request

def write_sol_data(sol, sol_obj):
	try:
		at_mn = round(sol_obj['AT']['mn'])
		at_mx = round(sol_obj['AT']['mx'])
		pre_mn = round(sol_obj['PRE']['mn'])
		pre_mx = round(sol_obj['PRE']['mx'])
		print(f"On Sol {sol} the temperatures ranged from {at_mn}॰C to {at_mx}॰C with an atmospheric pressure of {pre_mn} Pa to {pre_mx} Pa")
	except:
		pass

nama = "Masukkan Nama"
nim = "Masukkan Nim"
api_key = "Masukkan API Key"
url = "https://api.nasa.gov/insight_weather/?api_key="+api_key+"&feedtype=json&ver=1.0"

response = request.urlopen(url)
data = json.loads(response.read())

print("Tugas Sistem Paralel & Terdistribusi")
print("Nama: "+ nama)
print("NIM: "+ nim)

for sol in data['sol_keys']:
	write_sol_data(sol, data[sol])
