
import keyboard

with open("File.txt", "r") as f:
    page = f.read()
 
page = page.split("--")


i = 0
print(page[i])
i += 1
 
while True:
    print()
    print("1.Press 'Enter' to read more:")
    print("1.Press 'q' to quit:")
 
    k = input()
    try:
        if len(page) <= i:
            i = 0
        
        if keyboard.read_key()=='q':
            break

        elif k =='':
            
            print(page[i])
            keyboard.read_key()
           
            i += 1
        elif k =='-1':
      
            print(page[i-1])
            i -= 1

        else:
            num = int(k)
            if len(page) <= num:
                print(page[i])
                i += 1
            else:
                i = num
                print(page[i])
    except:
        pass