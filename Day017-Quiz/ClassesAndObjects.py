class User:
    def __init__(self,id,username):
        """Constructor is always called when a new object is created """
        self.id=id
        self.username=username
        self.followers=0 #We can create attributes with default values
        self.following=0
    
    def follow(self,user):
        user.followers+=1
        self.following+=1
        
    
user_1=User("001","Alisha")
user_2=User("002","Angela")

print(user_1.username)
print(user_1.id)
print(user_1.followers)

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
