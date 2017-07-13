class user:
    #initiation
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.friend = ""
        self.friends = []
        self.bio = ""
        self.num_friends = 0
        self.post = ("",(0,0,0))
        self.posts = {}
        self.post_date =(0,0,0)
        self.profile_pic = ""

    #fields
    def friend_list(self, friends):
        self.friends = friends
    def Bio(self, bio):
        self.bio = bio
    def numfriends(self, num_friends):
        self.num_friends = num_friends
    def user_posts(self, posts):
        self.posts = posts
    def profilePic(self, profile_pic):
        self.profile_pic = profile_pic

    #methods
    def add_friend(self, friend):
        self.friends.append(friend)
    def update(self, post_date, post):
        self.posts[post_date] = post

class Network:
    def __init__(self):

        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def printbios(self):
        for i in self.users:
            print(i.bio)
    def printbio(self, user):
        print(user.bio)
    def printdateposts(self, date):
        for i in self.users:
            print(i.posts[date])
    def printpost(self, date, user):
        print(user.posts[date])
    def print_friends(self, user):
        print(user.friends)
    def how_popular(self, user):
        print(user.num_friends)
    def print_name(self, user):
        print(user.username)
    def hide_password(self, user):
        x = []
        for i in range(0, len(user.password)):
            x.append("*")
        str = "".join(x)
        print(str)
#Gabe's profile
my_network = Network()
Gabe = user("Angel_Gabriel", "password")
Gabe.friend_list(["His mom", "Python"])
Gabe.Bio("I am a boy who is going to bake cookies for his favorite girls")
Gabe.add_friend("Doggo")
Gabe.numfriends(len(Gabe.friends))
Gabe.user_posts({(7,13,17):"Promise to make cookies not going to do it."})
Gabe.update((7,14,17), "Sitting not making cookies. B)")
my_network.add_user(Gabe)
#Mellissa's profile
Mellissa = user("invisible_bunny", "password")
Mellissa.friend_list(["Sarah", "Ambar", "Allison", "Allison", "Han Wen", "Melanie", "Julie", "Kaitlyn", "Anyssa", "Pryanka", "Sanyoni", "Betsebeth", "Cassie", "Sevilay", "Angelica", "Zelda", "Marisole", "Anna", "Jamie"])
Mellissa.Bio("This is an AB coversation, so C your way out of it.P.S I have no birthday. P.P.S I have more friends than Gabe")
Mellissa.add_friend("Facebook")
Mellissa.numfriends(len(Mellissa.friends))
Mellissa.user_posts({(7,13,17):"Didn't get any older today."})
Mellissa.update((7,14,17), "NORTHWESTERN ! B)")

#Using the network
my_network.add_user(Mellissa)
#my_network.printbios()
#my_network.printpost((7,14,17), Gabe)
#my_network.print_friends(Mellissa)
#my_network.how_popular(Gabe)
P = False
User = user(input("What will be your username?"), input("What password do you want?"))
while P == False:
    if len(User.password) > 9:
        P = False
        User = user(User.username, input("Password cannot be more than 9 characters. Try again."))
    else:
        P = True
User.friend_list(["His mom", "Python"])
User.Bio(input("Write your bio!"))
User.add_friend("Doggo")
User.numfriends(len(Gabe.friends))
User.user_posts({(7,13,17):"Promise to make cookies not going to do it."})
User.update((7,14,17), "Sitting not making cookies. B)")
my_network.add_user(User)
print("Cool, here is your profile!")
print("Username:")
my_network.print_name(User)
print("Password:")
my_network.hide_password(User)
print("Bio:")
my_network.printbio(User)
