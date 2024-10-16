class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am a cat.my name is {self.name}.i am {self.age} year old")
    def make_sound(self):
        print("meow")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"iam a dog.my name is {self.name}.iam {self.age} year old")
    def make_sound(self):
            print("bask")

class cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cow.my name is {self.name}.I am {self.age} years old.")
    def make_sound(self):
        print("mmaa")


cat1=cat("kitty",2)
dog1=dog("fluffy",3)
cow1=cow("pinkyy",3)

for animal in(cat1,dog1,cow1):
  animal.make_sound()    
  animal.info()