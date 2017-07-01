import praw
import config

	def bot_login():
		r = praw.Reddit(username = config.username,
					password = config.password,
					client_id = config.client_id,
					client_secret = config.client_secret,
					user_agent = "FacilityAI Reborne by /u/Reckasta")

		return r
