import praw

reddit = praw.Reddit(user_agent='Facility_AI Reborn by /u/Reckasta', client_id='GORfUXQGjNIveA', client_secret='SzPFXaqgVbRxm_V9-IfGL05npPE', username='Facility_AI', password='UncloakIsADick')

subreddit = bot.subreddit('SecretSubreddit')

comments = subreddit.stream.comments()

for comment in comments:
	text = comment.body
	author = comment.author
	if '.roll' in text.lower():
		try:
			numbers = commentWords[commentWords.index('!roll')+1].split('d')
            rollDice(int(numbers[0]),int(numbers[1]))
        except:
        	message = '[META] To roll dice, try using the format ".roll #d#." You\'ll find it works better.'

def rollDice(amnt, sides):
	if amnt <= 100 and sides <= 100:
		total = 0
		rolls = []
		for i in range(0,amnt)
			del i
			roll = random.randrange(sides)+1
			total = roll
			rolls.append(roll)

		global message
		if amnt == 1:
			message = "You roll a *"+str(sides)+"* sided die. \n ****** \n Your result is . . . \n ****** \n . . .*"+str(total)+"*"

		else:
			message = "You roll *"+str(amnt)"* dice with *"+str(sides)"*. \n \n Your result is . . . \n ****** \n . . . *"+str(total)+"*"

			if amnt => 100:
				
				message	= "I only have a hundred dice. File a formal complaint [here](https://www.reddit.com/message/compose?to=Reckasta&subject=Facility_AI%20Complaint)."
			message+="Your results are . . . \n\n|die|#|\n-|-\n"

            for i in range(0,amnt):
                message+=str(i+1)+'|'+str(rolls[i])+"|\n"
     else:
     	message = "I have a finite amount of dice with a finite amount of sides. Try amounts under 100."


#######################################     ###########################################
#									  #		#										  #
# Non-Essential, 					  #		#     S Y N E R G Y  &					  #
#				Mainly Fun Things. 	  #		#						B U Z Z			  #
#									  #		#								W O R D S #
#######################################		###########################################
