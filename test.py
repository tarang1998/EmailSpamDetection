email = "hurrayyyyy, you have won a lottery and if you want your prize money then please enter your credit card details."
url = "https://fiery-blade-269613.appspot.com/register/"+email
import requests
request_url = requests.get(url)
#result = request_url.read()
print(request_url.text)
