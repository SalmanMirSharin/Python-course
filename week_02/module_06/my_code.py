import requests

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_response(url):
    return requests.get(url)

if __name__=="__main__":
    #print("hey dear")
    res = get_request(api_url)
    print(res)