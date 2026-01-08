import requests
import pywhatkit as kit
import pyautogui #for search on yt/google
import smtplib #for email

#functions 

#get my ip
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address['ip']
# ipify provides a simple public IP address API.
# We just need to make a GET request on this URL: https://api64.ipify.org/?format=json.
# It returns JSON data as: { "ip": "117.214.111.199" }


#playing yt 
def play_yt(query):
    kit.playonyt(query)

#searching on google
def search_on_google(query):
    kit.search(query)

#random jokes
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

#random advice
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']







#wattsapp
#def send_whatsapp_message(number, message):
    #kit.sendwhatmsg_instantly(f"+91{number}", message)    