from django.shortcuts import render


def index2(request,name=None):
    #commentsb added 12345
    dict_error = name
    msg = "Sorry backend code is not working getting the error "
    dict_error['msg'] = msg
    my_dic = dict_error
    return render(request,'error.html',context=my_dic)
