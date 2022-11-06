import random
class BRTA:
    def __init__(self) -> None:
        self.__license = {}

    def take_driving_test(self,email):
        score = random.randint(0,100)
        
        if score>=33:
            print('Congrats, You passed!',score)
            license_number = random.randint(5000,9999)
            self.__license[email] = license_number
            print('License No:',license_number)
            return license_number
        else:
            print('You failed!',score)
            return False

    def validate_license(self,email,license):
        
        for key,val in self.__license.items():
            if key==email and val==license:
                return True
        return False

        
        
# br = BRTA()

# br.take_driving_test('random@gmail.com')

# br.validate_license('djff',333455)


