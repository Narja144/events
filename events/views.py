from django.shortcuts import render # origin line
from django.http import HttpResponse
from .models import Event

def index(request):
    return render(request, 'events/index.html')
    # html = '''
    # <h1>Hey Client, my app is running!</h1>
    # <p>Check out our <a href="/events">offerings</a></p>
    # '''
    # return HttpResponse(html)

def event_listing(request):
    events = Event.objects.all()
    return render(request, 'events/event_listing.html', {'events': events})
    # html = '''
    # <ul>
    #     <li>Chill on the beach <a href="/event/Chill">detail</a></li>
    #     <li>Camping in the woods <a href="/event/Camping">detail</a></li>
    #     <li>Flying into the space <a href="/event/Flying">detail</a></li>
    # </ul>
    # '''
    # return HttpResponse(html)

def event_detail(request, name):
    data = {'Chill' : '<h2>Chill on the beach just for $400</h2>',
            'Camping' : '<h2>Camp with us for $50</h2>',
            'Flying' : '<h2>Fly for free</h2>'}
    selection = data.get(name)
    if selection:
        return HttpResponse(selection)
    else:
        return HttpResponse('No such event in offering for now')
