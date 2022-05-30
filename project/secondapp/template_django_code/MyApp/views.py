from django.shortcuts import render 
# Create your views here.
def cross(request,name):
    #commentsb added 12345
    msg = "No issues code is working fine"
    my_dic = {'msg' : msg}
    path = '{}/cross.html'.format(name)
    print(path)
    return render(request,path,context=my_dic)