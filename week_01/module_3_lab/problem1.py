
#Clean the Dirty data:


data = "aNtEriOur\n\n>>"

new_data = data.lower()
output_data = ''
for character in new_data:
    if(character=='a') or (character=='e') or (character=='i') or (character=='o') or (character=='u'):
        #print(f"{character} found")
        output_data+=character +'-'

print(output_data[:-1])

        
   




