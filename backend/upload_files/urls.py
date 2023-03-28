from django.contrib import admin
from django.urls import path
from . import views as upload_files_views

# import mysite.views

urlpatterns = [
    # path('upload/', upload_files_views.upload_statments, name="upload_statements"),
    path('shubham/<str:text>/', upload_files_views.upload_statements, name="upload_statements"),
    path('bankstatements/', upload_files_views.uploadBankStatments, name="uploadBankStatments"),
]
