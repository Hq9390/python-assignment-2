import random
import string

index=1
arrayofjokes = ['I used to have a handle on life, but then it broke.',
            ' Don’t you hate it when someone answers their own questions? I do.',
            ' I told him to be himself; that was pretty mean, I guess.',
            'I know they say that money talks, but all mine says is ‘Goodbye.’',
            'Two fish are in a tank. One says, ‘How do you drive this thing?',
            'I don’t suffer from insanity—I enjoy every minute of it.',
            ' reading a book about anti-gravity. It’s impossible to put down.',
            ' People who take care of chickens are literally chicken tenders.',
            'It was an emotional wedding. Even the cake was in tiers.',
            'Despite the high cost of living, it remains popular.',
            'I can’t believe I got fired from the calendar factory. All I did was take a day off!.',
            'Money talks. Mine always says goodbye.',
            'I went to see the doctor about my short-term memory problems — the first thing he did was make me pay in advance',
                'You have two parts of the brain, “left” and “right”. On the left side, there’s nothing right and on the right side, there’s nothing left.',
                'Why do bees hum? They don’t remember the lyrics!.',
                'Don’t spell part backward. It’s a trap.',
                'Thanks for explaining the word “many” to me, it means a lot.',
                'I’m reading a book about anti-gravity. It’s impossible to put down.',
                'R.I.P boiled water. You will be mist.',
                'At what age is it appropriate to tell my dog that he’s adopted?',
                'I started out with nothing, and I still have most of it.',
                'Did Noah include termites on the ark?',
                'Where there’s a will, there’s a relative.',
                'Women should not have children after 35, but 35 kids are enough!',
                'My first job was working in an orange juice factory, but I got canned. I just couldn’t concentrate.',
                'I doubt, therefore, I might be.',
                'I used to have a handle on life, but then it broke.'
           ]

randomSubJokes =[]
for i in random.sample(range(1, 27), 10):
    # get random string of length 6 without repeating letters
    # randomNumber = random.randint(0,len(arrayofjokes)-1)
    # joke = arrayofjokes[randomNumber]
    randomSubJokes.append(arrayofjokes[i])
    # print(i)
    # index += 1


# random.sample(range(1, 2), 10)
#print(*enumerate(joke), sep='\n')
