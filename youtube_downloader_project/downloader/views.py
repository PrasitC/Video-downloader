

from django.shortcuts import render
from pytube import YouTube

def index(request):
    return render(request, 'index.html')  
def download(request):
    if request.method == 'POST':
        link = request.POST['link']
        resolution = request.POST['resolution']
        yt = YouTube(link)
        if resolution == 'highest':
            video = yt.streams.get_highest_resolution()
        else:
            video = yt.streams.get_lowest_resolution()
        video.download()
        return render(request, 'success.html')  
    return render(request, 'index.html')  
