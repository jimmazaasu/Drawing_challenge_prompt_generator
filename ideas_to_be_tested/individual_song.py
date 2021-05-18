class Individual_song:

    def __init__(self, song_title,song_lyrics):

        self.song_title= song_title
        self.song_lyrics=song_lyrics

shes_american=Individual_song("she´s american", """A big town               
Synthetic apparitions of *NOT being lonely
Look, he's having a breakdown
Oh what a let down, a shame, I think he might die
Oh, she's dancing enthralling, I guess I gotta wait my turn
I said, don't fall in love with the moment
She said I've got a lot to learn
You know I'm in love with this city
But the green IS turning brown
And I just look pathetic now
If she likes it 'cause we just don't eat
And we're so intelligent, she's American
If she says I've got to fix my teeth
Then she's so American (she's American)
And if she likes it 'cause we just don't eat
And we're socially relevant, she's American
If she says I've got to fix my teeth
Then she's so American (she's American)
She's inducing sleep to avoid pain
And I think she's got a gun divinely decreed and custom made
She calls on the phone like the old days, expecting the world
Don't fall in love with the moment
And think you're in love with the girl
There's no more water in this city
But be careful OR you'll drown
You think you've got it figured out
If she likes it 'cause we just don't eat
And we're so intelligent, she's American
If she says I've got to fix my teeth
Then she's so American (she's American)
And if she likes it 'cause we just don't eat
And we're socially relevant, she's American
If she says I've got to fix my teeth
Then she's so American (she's American)
Well, your face has got a hold on me
But your brain IS proper weird
Are you feeling the same?
You just keep nodding at me looking vacant
She's American
She's American
If she likes it 'cause we just don't eat
And we're so intelligent, she's American
If she says I've got to fix my teeth
Then she's so American (she's American)
If she likes it 'cause we just don't eat
And we're socially relevant, she's American
If she says I've got to fix my teeth
Then she's so American (she's American)""")

#previous line instantiates a song

#remember to include function that converts any words that may also be python keywords into all caps in order to avoid problems

print(shes_american.song_title) #this line´s purpose is to test that the constructor and the song instantiation (title) are working properly 
print(shes_american.song_lyrics) #this line´s purpose is to test that the constructor and the song instantiation (lyrics) are working properly 