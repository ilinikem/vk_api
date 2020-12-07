import requests
import os
from dotenv import load_dotenv 
load_dotenv()

def get_friends(user_id):
	data = {
	"access_token" : os.getenv('access_token'),
	"user_id": user_id,
	"v": "5.52"
	}
	url = "https://api.vk.com/method/friends.get"
	friends_list = requests.get(url, params=data)
	# ваш код здесь
	return friends_list.json()['response']
print(get_friends(os.getenv("user_id")))
# запрашиваем список друзей пользователя с ID 531301803
