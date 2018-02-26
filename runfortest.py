import requests

def post():
    url = 'http://127.0.0.1:5000/post_location'
    data=["56.88+63.75+IN/45645+vijay nagar+tamil nadu","28.6333+77.2167+IN/110001+Cannught place+New Delhi"]
    for i in data:
        response = requests.post(url, data=i,headers=headers)
        print(response.text)

def get_postgres():
    url = 'http://127.0.0.1:5000/get_using_postgres'
    data=["28.6488+77.1726+5000","28.6333+77.2167+3000"]
    for i in data:
        response = requests.post(url, data=i,headers=headers)
        print(response.text)

def get_self():
    url = 'http://127.0.0.1:5000/get_using_self'
    data=["28.6488+77.1726+5000","28.6333+77.2167+3000"]
    for i in data:
        response = requests.post(url, data=i,headers=headers)
        print(response.text)

def get_cityname():
    url = 'http://127.0.0.1:5000/get_using_postgres'
    data=["28.6488+77.1726","28.6333+77.2167"]
    for i in data:
        response = requests.post(url, data=i,headers=headers)
        print(response.text)