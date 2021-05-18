import random
class Songs:
    def __init__(self, song_list, list_size):
        self.song_list= song_list   #we´re going to add songs to this list which already has a first list of songs when initialized

        self.list_size= list_size #Every object in this class has a minimum list size
    
    def add_song(self):
        user_song=input("Please enter a song title: ")
        self.song_list.append(user_song)
    
    #def add_many_songs(self):
      #  user_playlist= input("Please enter a list of song titles: ")
       # self.song_list+=list(user_playlist)
   # def choose_mood(self):

      #  mood_list=["happy", "sad", "annoyed", "romantic", "hyped", "nothing special", "angry", "tired", "peaceful", "bored","anxious", "relaxed"]


       # user_mood=input("What is your mood today?")

       # if user_mood in mood_list:

       # else:
         #   print("Sorry, that mood is not in the list, why don t you try adding it?")

          #  user_mood=input("What is your mood today?")

           # mood_list.append(user_mood)
    

    def choose_prompt(self):
        
            print (random.choice(self.song_list))  #chooses a random song from the list
