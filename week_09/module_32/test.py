# from pyautogui import sleep
# import requests
# import json
 
# api_url ="https://api.openweathermap.org/data/2.5/weather?q=dhaka&appid=93bebef1e163a20cc27448fb1181b755"


# def weather_data(api_url):
#     response = requests.get(api_url)
#     # print(response)
    
#     # get the json
#     content = response.content.decode('UTF-8')
#     # print(content)

#     # convert string to json:
#     dict_cont = json.loads(content)
#     # print(dict_content)

#     res = dict_cont['main']['temp']

#     Formula = res-273.15
#     cel = '{:.2f}'.format(Formula)
#     # cel = f'{Formula:.2f}'
 
#     while True:
#         sleep(2)
#         print(f'{cel} celsius')

# weather_data(api_url)










