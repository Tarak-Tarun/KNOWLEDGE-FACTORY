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
    def shows_can_watch(self):
        print(f"Movies You can Watch")
        for i in self.movies:
            print(i)
class AmazonPrime(AmazonBasic):
     prime_exclusive=[
    "The Shawshank Redemption",
    "The Godfather",
    "The Godfather Part II",
    "Pulp Fiction",
    "Forrest Gump",
    "Fight Club",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers",
    "The Lord of the Rings: The Return of the King",
    "Star Wars: A New Hope",
    "The Empire Strikes Back",
    "The Silence of the Lambs",
    "Saving Private Ryan",
    "Schindler's List",
    "The Green Mile",
    "Parasite",
    "Joker",
    "Whiplash",
    "The Prestige",
    "Mad Max: Fury Road"
]
     def __init__(self,name,password,email,phone_no):
        self.name=name
        self.password=password
        self.email=email
        self.phone_no=phone_no
        print( f"Prime Instance for {self.name} is Created")
     def shows_can_watch(self):
        print(f"Movies You can Watch: ")
        for i in self.prime_exclusive:
            print(i)
        for i in self.movies:
            print(i)
        
    
free=AmazonBasic("Tarak","amazon@123","tarak1559@gmail.com","7386891135")
free.shows_can_watch()
Prime=AmazonPrime("tarun","amazon@123","tarak1559@gmail.com","7386891135")
Prime.shows_can_watch()
