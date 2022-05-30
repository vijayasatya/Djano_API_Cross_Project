from django.shortcuts import render


# Create your views here.
def cross(request,name):
    #Write your code here dont change function name, and try except block happy coding


    msg = "hI LOVE TO CODE THIS"
    my_dic = {'msg' :msg}
    path = '{}/cross.html'.format(name)
    return render(request,path,context=my_dic)