
from django.urls import path
from .views import index,run_server,main,download_file,add_user_data,delete_folder

urlpatterns = [
    path('backend_request', index),
    path('Run_Server', run_server),
    path('download_file', download_file),
    path('add_user_data', add_user_data),
    path('delete_folder_data', delete_folder),
    path('', main),
]