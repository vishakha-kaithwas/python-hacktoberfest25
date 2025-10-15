class Movie:
    def __init__(self,name,timing):
        self.name = name 
        self.timing = timing 

class User:
    def __init__(self,user_name,ID):
        self.user_name = user_name
        self.ID = ID 

class Booking(Movie,User):
    count = 0
    def __init__(self,name,timing,user_name,ID):
        Movie.__init__(self,name,timing)
        User.__init__(self,user_name,ID)
        Booking.count += 1 
        self.Movie_id = f"MOV{Booking.count:03d}"

    def show(self):
        print(f"Movie: {self.name}")
        print(f"Timings: {self.timing}")
        print(f"User Name: {self.user_name}")
        print(f"User ID: {self.ID}")
        print(f"Movie ID: {self.Movie_id}")

    def saving_entries(self):
        with open("Movies.txt","a") as f:
            f.writelines(f"Movie: {self.name} | Timings: {self.timing} | User Name: {self.user_name} | User ID: {self.ID} | Movie ID: {self.Movie_id}" )

User1 = Booking("Marvel","10 am", "Vishakha","101")
User1.show()
User1.saving_entries()
Footer
