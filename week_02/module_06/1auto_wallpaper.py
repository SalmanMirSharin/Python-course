'''problem:
Download and change desktop wallpaper:

'''

# from numpy import imag
# import requests
# import json
# import PyWallpaper

# api_url ="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# responce = requests.get(api_url)
# content = responce.content.decode('UTF-8')

# #convert to json

# dict_content = json.loads(content)
# image_url = dict_content['url']

# #image download:

# res = requests.get(image_url)

# #save the image:
# with open('apod.png','wb') as image:
#     image.write(res.content)

# #set as wallpaper:

# PyWallpaper.change_wallpaper("apod.png")





from curses.ascii import isdigit


ls =[12,35,56]

def lis(ls):
    for i in ls:
        return i
print(lis(ls))



# val = "111"

# isdigit(val)



# i =0
# while i<len(ls):
#     result = lis(ls)
#     print(next(result))
#     i+=1

