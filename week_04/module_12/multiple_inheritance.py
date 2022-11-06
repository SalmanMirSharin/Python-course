class School:
    def __init__(self,school_name):
        self.school_name = school_name
        print('School init called')

class Grade:
    def __init__(self,grade_name):
        self.grade_name = grade_name
        print('Grade Class init called')
        
class SportsTeam:
    def __init__(self,sport_name):
        self.sport = sport_name
        self.team = []

    def add_player(self,player_name):
        self.team.append(player_name)

class Student(School,Grade,SportsTeam):
    def __init__(self, name,grade_name,school,sports_name):
        self.name = name
        print('Student init clled')
        Grade.__init__(self,grade_name)
        School.__init__(self,school)
        SportsTeam.__init__(self,sports_name)


ananta_j = Student('Aj','MBA','Uk','Chess') 
print(ananta_j.name)
print(ananta_j.grade_name)
print(ananta_j.school_name)

ananta_j.add_player('Borsha')
ananta_j.add_player('Aj')
print(ananta_j.team)
