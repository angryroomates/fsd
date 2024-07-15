from django.shortcuts import render

def listfunction(request):
    fruits=['apple','banana','orange','mango']
    students=['jhanavi','john','vidushi','julia']
    orderedstudents=[]
    for s in students:
        if s.startswith('j'):
            orderedstudents.append(s)
    return render(request,'listapp.html',{'fruits':fruits,'stdn':orderedstudents})