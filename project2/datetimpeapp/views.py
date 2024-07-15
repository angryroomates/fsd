from django.shortcuts import render
from datetime import datetime,timedelta

def dateoffset(request):
    now = datetime.now()
    offset_day= timedelta(days=4)
    offset_hours= timedelta(hours=4)
    p_day=now+offset_day
    m_day=now-offset_day
    p_hours=now+offset_hours
    m_hours=now-offset_hours
    context={"dd":now.date,"cc":now.time,"p_day":p_day,"m_day":m_day,"p_hours":p_hours,"m_hours":m_hours}
    return render(request,"dateoffset.html",context)
