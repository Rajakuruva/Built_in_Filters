from django.shortcuts import render
import datetime
# Create your views here.
def Builtin_filters(request):
    d={"a":"Hi I aM fiLTeRs iN DjaNGo","dt":datetime.datetime.now,'c':1,'x':2}
    return render(request,'Builtin_filters.html',d)