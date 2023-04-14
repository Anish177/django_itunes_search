from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def search(request):

    return render(request, 'song_search/search.html')

def results(request):
    search_term = request.POST['search bar']
    media_type = request.POST['media choice']
    api_response = requests.get(f'https://itunes.apple.com/search?term={search_term}&media=music&entity={media_type}&limit=10')
    response = api_response.json()['results']
    context = {
        'search_term': search_term,
        'results': response,
        'media_type': media_type,
        'number_of_results': api_response.json()['resultCount']
    }

    return render(request, 'song_search/results.html', context)