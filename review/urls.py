"""djc_wcapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from review import views


urlpatterns = [
    re_path(r'^gamefile/(?P<gm_id>\w+)/enable$', views.EnableReviewGameFileDBDeatailView.as_view()),  # 增删改查
    re_path(r'^gamefile/(?P<gm_id>\w+)/disable$', views.DisableReviewGameFileDBDeatailView.as_view()),  # 增删改查
    re_path(r'^gamefile/(?P<gm_id>\w+)$', views.ReviewGameFileDBDeatailView.as_view()),  # 增删改查
    re_path(r'^gamefile$',views.ReviewGameFileDBView.as_view()), #增删改查
    # re_path(r'^gamefile$',views.ForReviewGameFileDBView.as_view()), #升级上线专用
    re_path(r'^hello$',views.HelloView.as_view()), #增删改查
]
