from django.shortcuts import render
import requests
# Create your views here.
def index(request):
  url = 'https://official-joke-api.appspot.com/random_joke'

  response = requests.get(url)

  data = response.json()

  joke = data['setup']
  punchline = data['punchline']

  context = {
    'joke': joke,
    'punchline':punchline
  }
  return render(request, 'index.html', context)