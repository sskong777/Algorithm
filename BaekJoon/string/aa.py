import random 
class ClassHelper:
    
    def __init__(self,students):
        self.students = students
    
    # def pick(self, num):
    #     res = []
    #     for i in range(num):
    #         res.append(random.choice(self.students))
    #     return res

    def pick(self, num):
        return random.sample(self.students, num)
    
    def match_pair(self):
        res_match = []
        for i in range(len(self.students)//2):

            if i == len(self.students)//2 -1:
                res_match.append(self.pick(3))
            else:
                res_match.append(self.pick(2))
            
            
        print(res_match)

ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

print(ch.pick(2))
ch.match_pair()