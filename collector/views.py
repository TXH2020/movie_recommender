from django.http import HttpResponse
import decimal
from collector.models import Log
from analytics.models import Rating
import datetime
import random
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def log(request):
    c=Log.objects.all().count()+1
    r=Rating.objects.all().count()+1
    if request.method == 'POST':
        date = request.GET.get('date', datetime.datetime.now())

        user_id = request.POST['user_id']
        content_id = request.POST['content_id']
        event = request.POST['event_type']
        session_id = request.POST['session_id']

        l = Log(
            id=c,
            created=date,
            user_id=user_id,
            content_id=str(content_id),
            event=event,
            session_id=str(session_id))
        l.save()
        rt = Rating(
            id=r,
            user_id=user_id,
            movie_id=str(content_id),
            rating=decimal.Decimal(round(random.random()*10,2)),
            rating_timestamp=date)
        rt.save()
            
    else:
        HttpResponse('log only works with POST')

    return HttpResponse('ok')
