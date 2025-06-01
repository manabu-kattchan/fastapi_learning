import requests
import json

def main():
    url = 'https://fastapi-learning-test.onrender.com'
    data = {
        'x': 3,
        'y': 4
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())

if __name__ == '__main__':
    main()
