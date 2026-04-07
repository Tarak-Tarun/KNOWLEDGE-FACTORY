class AmazonBasic:
    movies = [
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Avatar",
    "Titanic",
    "Gladiator",
    "The Matrix",
    "Jurassic Park",
    "Avengers: Endgame",
    "Spider-Man: No Way Home"
]
    def __init__(self,name,password,email,phone_no):
        self.name=name
        self.password=password
        self.email=email
        self.phone_no=phone_no
        print( f"Free Instance for {self.name} is Created")
class AmazonPrime(AmazonBasic):
    def __init__(self,name,password,email,phone_no):
        super().__init__(name,password,email,phone_no)
        print("Prime Instance is Created for ",self.name)
obj=AmazonPrime("Tarak","amazon@123","tarak1559@gmail.com","7386891135")