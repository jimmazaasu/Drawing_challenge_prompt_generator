
from songs import Songs



#The program itself

song_database=Songs(["She´s american","Red dress","Teenage dirtbag","Somebody Else", "El Duelo", "Rude", "F for you","Rose colored boy"],10)


print("This program will choose a random prompt for your artistic inspiration")


print("Your prompt for today is: ")


song_database.choose_prompt()

while len(song_database.song_list)<(song_database.list_size):
  print("Help the list grow by adding more songs")

  song_database.add_song()
print("Your song database is now:")

print(song_database.song_list)

new_song_database=Songs(song_database.song_list,12)

new_song_database.choose_prompt()

