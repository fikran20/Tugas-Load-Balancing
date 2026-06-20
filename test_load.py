import requests
import concurrent.futures

url = "http://localhost:8099/api/v1/status"

def send_request(req_id):
    try:
        response = requests.get(url)
        if "SERVER 1" in response.text:
            server = "SERVER 1"
        elif "SERVER 2" in response.text:
            server = "SERVER 2"
        elif "SERVER 3" in response.text:
            server = "SERVER 3"
        else:
            server = "UNKNOWN"
        print(f"Request ke-{req_id:02d} berhasil -> Dilayani oleh {server}")
    except Exception as e:
        print(f"Request ke-{req_id:02d} gagal!")

print("Mengirim 30 request sekaligus...")
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(1, 31):
        executor.submit(send_request, i)