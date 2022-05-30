from django.shortcuts import render
from django.http import JsonResponse
import shutil
import os
import sys
import json
from django.core.wsgi import get_wsgi_application
import subprocess
from django.http import HttpResponse
import random
import shutil
#from project.reload_web import restart_server
# Create your views here.
#touch /var/www/vijayasatyad_pythonanywhere_com_wsgi.py
#{% load static %}
#<link rel="stylesheet" href="{% static 'index.css' %}">
#https://vijayasatyad.pythonanywhere.com/download_file
#project/secondapp/template_django_code/MyApp/views.py

def write_file(path,data):
    f = open(path, "w",encoding="utf8")
    f.write(data)
    f.close()

def append_file(path,data):
    f = open(path, "a",encoding="utf8")
    f.write(data)
    f.close()

def read_file(path):
    with open(path, "w",encoding="utf8") as f:
        code = f.readlines()
    code = "".join(code)
    return code

def random_key_generator():
    l = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_value = ""
    for i in range(4):
        key_value += random.choice(l)
    return key_value

def change_url_file_dynamic(url,name):
        with open('project/secondapp/demofile2.py') as f:
            lines = f.readlines()
        data = "".join(lines)
        output_data = data[:96].format(name,name,name)+data[96:97]+str(name)+",kwargs={'name':'"+str(name)+"'}))\nexcept:\n\tpass"
        f = open(url, "a")
        f.write("\n"+output_data)
        f.close()

def Remove_urls_dynamic(url,name):
        with open('project/secondapp/demofile2.py') as f:
            lines = f.readlines()
        data = "".join(lines)
        output_data = data[:96].format(name,name,name)+data[96:116]+":'"+str(name)+"'}))\nexcept:\n\tpass"
        with open(url) as f:
            lines = f.readlines()
        data = "".join(lines)
        #final_data = data.replace(output_data,"")
        try:
            final_data= data[:data.index(name)-output_data.index(name)]+data[data.index(name)+len(output_data)-output_data.index(name)+len(name)-4:]
            f = open(url, "w")
            f.write(final_data)
            f.close()
        except:
            pass

def index(request):
    if request.method=='POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user_id = body['user_id']
            Frontendhtml_code = body['frontendhtmlcode']
            Frontendcss_code = body['frontendcsscode']
            Frontendjs_code = body['frontendjscode']
            Backend_code = body['backendcode']
        except:
            Frontendhtml_code = request.POST['frontendhtmlcode']
            Frontendcss_code = request.POST['frontendcsscode']
            Frontendjs_code = request.POST['frontendjscode']
            Backend_code = request.POST['backendcode']
            user_id = request.POST['user_id']


        f = open('project/firstapp/userdata.json')
        data = json.load(f)
        L = list(data.keys())

        if str(user_id) in L:
            data[user_id]['frontendhtmlcode'] = Frontendhtml_code
            data[user_id]['frontendcsscode'] = Frontendcss_code
            data[user_id]['frontendjscode'] = Frontendjs_code
            data[user_id]['backendcode'] = Backend_code

            with open('project/firstapp/userdata.json', 'w') as f:
                json.dump(data, f, indent=2)

            #main Project
            #Frotend_code
            f = open('project/firstapp/user.json')
            data = json.load(f)
            L = list(data.keys())

            if str(user_id) in L:
                html_path = "project/secondapp/templates/{}/cross.html".format(data[user_id])
                css_path = "project/secondapp/static/{}/cross.css".format(data[user_id])
                js_path = "project/secondapp/static/{}/cross.js".format(data[user_id])

                write_file(html_path,Frontendhtml_code)
                write_file(css_path,Frontendcss_code)
                write_file(js_path,Frontendjs_code)

                #backend python
                python_path = 'project/secondapp/{}/views.py'.format(data[user_id])
                write_file(python_path,Backend_code)
                run_server()
                output = str(data[user_id])
                return JsonResponse({"output": output})
            else:
                L = list(data.values())
                generated_key = random_key_generator()
                while 1:
                    if generated_key not in L:
                        break
                    generated_key = random_key_generator()

                data[user_id] = generated_key
                with open('project/firstapp/user.json', 'w') as f:
                    json.dump(data, f, indent=2)

                os.mkdir("project/secondapp/{}".format(data[user_id]))
                os.mkdir('project/secondapp/templates/{}'.format(data[user_id]))
                os.mkdir('project/secondapp/static/{}'.format(data[user_id]))
                html_path = "project/secondapp/templates/{}/cross.html".format(data[user_id])
                css_path = "project/secondapp/static/{}/cross.css".format(data[user_id])
                js_path = "project/secondapp/static/{}/cross.js".format(data[user_id])

                change_url_file_dynamic('project/secondapp/urls.py',data[user_id])

                write_file(html_path,Frontendhtml_code)
                write_file(css_path,Frontendcss_code)
                write_file(js_path,Frontendjs_code)

                #backend python
                python_path = 'project/secondapp/{}/views.py'.format(data[user_id])
                write_file(python_path,Backend_code)
                run_server()
                output = str(data[user_id])
                run_server()
                return JsonResponse({"output": output})
        else:
            data[user_id] = {}
            data[user_id]['frontendhtmlcode'] = Frontendhtml_code
            data[user_id]['frontendcsscode'] = Frontendcss_code
            data[user_id]['frontendjscode'] = Frontendjs_code
            data[user_id]['backendcode'] = Backend_code

            with open('project/firstapp/userdata.json', 'w') as f:
                json.dump(data, f, indent=2)

            #main Project
            #Frotend_code
            f = open('project/firstapp/user.json')
            data = json.load(f)
            L = list(data.keys())

            if str(user_id) in L:
                html_path = "project/secondapp/templates/{}/cross.html".format(data[user_id])
                css_path = "project/secondapp/static/{}/cross.css".format(data[user_id])
                js_path = "project/secondapp/static/{}/cross.js".format(data[user_id])

                write_file(html_path,Frontendhtml_code)
                write_file(css_path,Frontendcss_code)
                write_file(js_path,Frontendjs_code)

                #backend python
                python_path = 'project/secondapp/{}/views.py'.format(data[user_id])
                write_file(python_path,Backend_code)
                run_server()
                output = str(data[user_id])
                return JsonResponse({"output": output})
            else:
                L = list(data.values())
                generated_key = random_key_generator()
                while 1:
                    if generated_key not in L:
                        break
                    generated_key = random_key_generator()

                data[user_id] = generated_key
                with open('project/firstapp/user.json', 'w') as f:
                    json.dump(data, f, indent=2)

                os.mkdir("project/secondapp/{}".format(data[user_id]))
                os.mkdir('project/secondapp/templates/{}'.format(data[user_id]))
                os.mkdir('project/secondapp/static/{}'.format(data[user_id]))
                html_path = "project/secondapp/templates/{}/cross.html".format(data[user_id])
                css_path = "project/secondapp/static/{}/cross.css".format(data[user_id])
                js_path = "project/secondapp/static/{}/cross.js".format(data[user_id])

                change_url_file_dynamic('project/secondapp/urls.py',data[user_id])

                write_file(html_path,Frontendhtml_code)
                write_file(css_path,Frontendcss_code)
                write_file(js_path,Frontendjs_code)

                #backend python
                python_path = 'project/secondapp/{}/views.py'.format(data[user_id])
                write_file(python_path,Backend_code)
                run_server()
                output = str(data[user_id])
                run_server()
                return JsonResponse({"output": output})


    elif request.method=='GET':
        user_id = request.GET['user_id']
        f = open('project/firstapp/userdata.json')
        data = json.load(f)
        return JsonResponse(data[user_id])

    else:
        return render(request,"index1.html")

def run_server():
        os.chdir("project")
        from reload_web import restart_server
        #subprocess.call([r"project/reload_web.sh"])
        restart_server
        #return JsonResponse({"output": "Saved"})

def download_file(request):

    if request.method=='GET':
        user_id = request.GET['user_id']
        f = open('project/firstapp/userdata.json')
        data = json.load(f)

        html_path = "project/secondapp/template_django_code/MyApp/templates/cross.html"
        css_path = "project/secondapp/template_django_code/MyApp/static/cross.css"
        js_path = "project/secondapp/template_django_code/MyApp/static/cross.js"
        python_path = 'project/secondapp/template_django_code/MyApp/views.py'

        write_file(html_path,data[user_id]["frontendhtmlcode"])
        write_file(css_path,data[user_id]["frontendcsscode"])
        write_file(js_path,data[user_id]["frontendjscode"])
        write_file(python_path,data[user_id]["backendcode"])

        #from pathlib import Path
        #downloads_path = str(Path.home() / "Downloads")
        shutil.make_archive("Demo_download_test", 'zip',"project/secondapp/template_django_code")
        zip_file = open("Demo_download_test.zip", 'rb')
        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % 'foo.zip'
        #os.remove(zip_file)
        return response



def main(request):
    return render(request,"index1.html")


def add_user_data(request):
    if request.method=='POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            tid = body['tid']
            usid = body['uid']
        except:
            tid = request.POST["tid"]
            usid = request.POST["uid"]

        f = open("project/firstapp/All_Mainserver_userdata.json")
        data = json.load(f)
        data[usid] = tid

        with open("project/firstapp/All_Mainserver_userdata.json", "w",encoding="utf8") as f:
                    json.dump(data, f, indent=2)
        run_server()
        return JsonResponse({"output": "Saved"})

def delete_folder(request):
    if request.method =='POST':
        user_id = request.POST['user_id']
        f = open('project/firstapp/user.json')
        data = json.load(f)

        #temp
        f_temp = open ('project/firstapp/user.json')
        data_temp = json.load(f_temp)
        try:
            del data_temp[user_id]
        except:
            return JsonResponse({"output": "No folder exists"})

        with open("project/firstapp/user.json", "w",encoding="utf8") as f:
                json.dump(data_temp, f, indent=2)

        name = data[user_id]
        url = 'project/secondapp/urls.py'
        Remove_urls_dynamic(url,name)
        path1 = "project/secondapp/{}".format(data[user_id])
        path2 = 'project/secondapp/templates/{}'.format(data[user_id])
        path3 = 'project/secondapp/static/{}'.format(data[user_id])
        shutil.rmtree(path1)
        shutil.rmtree(path2)
        shutil.rmtree(path3)
        run_server()
        return JsonResponse({"output": "Project deleted successfully"})
    else:
        return JsonResponse({"output": "Nothing happens"})



















