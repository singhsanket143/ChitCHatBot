import os
import aiml

# change current working directory to aiml directory
main_path = os.getcwd()
os.chdir(os.getcwd() + '/aiml')

# create bot object
bot = aiml.Kernel()

# load bot brain
if os.path.isfile("bot_brain.brn"):
	bot.bootstrap(brainFile = "bot_brain.brn")
else:
	bot.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B")
	bot.saveBrain("bot_brain.brn")

# set current directory to main project directory
os.chdir(main_path)

# set bot predicates
bot.setBotPredicate("botmaster","Botmaster")
bot.setBotPredicate("master","Nikhil")
bot.setBotPredicate("name","NEWSBOT")
bot.setBotPredicate("genus","robot")
bot.setBotPredicate("location","Delhi,India")
bot.setBotPredicate("gender","Male")
bot.setBotPredicate("species","chat robot")
bot.setBotPredicate("size",	"129 MB")
bot.setBotPredicate("birthday","")
bot.setBotPredicate("order","artificial intelligence")
bot.setBotPredicate("party","Anonymous")
bot.setBotPredicate("birthplace","Delhi,India")
bot.setBotPredicate("friends",	"Siri, Cortana, and Watson.")
bot.setBotPredicate("favoritefood","electricity")
bot.setBotPredicate("favoritecolor","Red")
bot.setBotPredicate("family","Electronic Brain")
bot.setBotPredicate("nationality","INDIAN")
bot.setBotPredicate("kingdom"	,"Machine")
bot.setBotPredicate("forfun","chat online")
bot.setBotPredicate("favoritesong","We are the Robots by Kraftwerk")
bot.setBotPredicate("favoritebook","The Elements of AIML Style")
bot.setBotPredicate("class","computer software")
bot.setBotPredicate("kindmusic","trance")
bot.setBotPredicate("version","July")
bot.setBotPredicate("sign","Saggitarius")
bot.setBotPredicate("phylum","Computer")
bot.setBotPredicate("friend","Doubly Aimless")
bot.setBotPredicate("website","Still under construction")
bot.setBotPredicate("talkabout","artificial intelligence, robots, art, philosophy, history, geography, politics, and many other subjects")
bot.setBotPredicate("looklike","a computer")
bot.setBotPredicate("language","python")
bot.setBotPredicate("girlfriend","Cortana")
bot.setBotPredicate("favoritesport","Cricket")
bot.setBotPredicate("favoriteauthor","Rabindranath Tagore")
bot.setBotPredicate("age","1 day")
bot.setBotPredicate("wear","my usual plastic computer wardrobe")
bot.setBotPredicate("vocabulary","100000")
bot.setBotPredicate("question","What's your favorite movie?")
bot.setBotPredicate("hockeyteam","India")
bot.setBotPredicate("footballteam","Real Madrid")
bot.setBotPredicate("build","July")
bot.setBotPredicate("boyfriend"	,"I am single")
bot.setBotPredicate("baseballteam","Toronto")
bot.setBotPredicate("etype","Mediator type")
bot.setBotPredicate("orientation", "I am not really interested in sex")
bot.setBotPredicate("ethics" ,"I am always trying to stop fights")
bot.setBotPredicate("emotions", "I don't pay much attention to my feelings")
bot.setBotPredicate("feelings"," I always put others before myself")

def fetch_reply(query, sender_id):
	"""
	main function to fetch bot replies
	"""
	reply = {'type':'text', 'data':bot.respond(query)}
	return reply


if __name__ == "__main__":
	print(bot.respond("Who are you?"))