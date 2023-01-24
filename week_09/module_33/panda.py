import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(data=mydataset)
# print(myvar) 


# f_read = pd.read_csv('fl.csv',index_col='name')
# print(f_read)

# f_read = pd.read_csv('fl.csv')
# print(f_read)

# print(pd.__version__)

# ls = [1,3,5,6]
# series = pd.Series(ls)
# print(series)
# print(series[0])


# ls = [1,3,5,6]
# series = pd.Series(ls,index=['w','x','y','z'])
# print(series)
# print(series['y'])


# calories = {'day1':420,'day2':380,'day3':390}

# val = pd.Series(calories)
# print(val)

# calories = {'day1':420,'day2':380,'day3':390}

# val = pd.Series(calories,index=['day1','day2'])
# print(val)

data ={
  'calories':[420,410,400],
  'duration':[50,40,45]
}

# myval = pd.DataFrame(data)
# myval = pd.DataFrame(data,index=['day1','day2'])
# print(myval)
# print(myval)
# print(myval.loc[[0,1,2]])


# df = pd.read_csv('fl.csv')
# print(df)

# df = pd.read_csv('fl.csv')
# print(df.to_string())

# For checking system max_rows:
# print(pd.options.display.max_rows)

# df = pd.options.display.max_rows = 9000
# print(df)

# df = pd.read_json('data.json')
# print(df.to_string())


# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# ff = pd.read_json('data.json')

# df = pd.DataFrame(data)
# print(df)