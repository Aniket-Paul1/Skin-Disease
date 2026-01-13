import requests

url = "http://127.0.0.1:8000/predict"
image_path = r"C:\Users\ANIKET\OneDrive\Desktop\Adi\Skin disease\d1.jpg"

with open(image_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Status:", response.status_code)
print("Response:", response.text)
