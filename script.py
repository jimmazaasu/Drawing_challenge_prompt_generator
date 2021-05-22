from song import Songs

#The program itself

song_database=Songs(["She s american","Red dress","Teenage dirtbag","Somebody Else", "El Duelo", "Rude", "F for you","Rose colored boy", "Cake pop", "Little Red Corvette", "Like I Love You","Love It If We Made It","Purple Rain","Girlfriend","If You re Too Shy (Let me know)","It´s Not Living (If It´s Not With You)", "Nice For What","Time After Time","Last Stardust","Thinking of You (I Drive Myself Crazy)"],21)




print("This program will choose a random prompt for your artistic inspiration")


print("Your prompt for today is: ")


song_database.choose_prompt()

while len(song_database.song_list)<(song_database.list_size):
  print("Help the list grow by adding more songs")

  song_database.add_song()
print("Your song database is now:")

print(song_database.song_list)

new_song_database=Songs(song_database.song_list,30)

print("Here,  an extra prompt just for you")

new_song_database.choose_prompt()


print("Now do me a favor and go to script.py to add more songs")
