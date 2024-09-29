import requests

url = 'http://127.0.0.1:5000/'

data = {
    "x1": 5,
    "y1": 9,
    "x2": 7,
    "y2": 4
}

response = requests.post(url, json=data)

if response.status_code == 200:
    try:
        print(response.json())
    except ValueError:
        print("Відповідь не є дійсним JSON:", response.text)
else:
    print(f"Помилка! Статус-код: {response.status_code}, відповідь: {response.text}")

