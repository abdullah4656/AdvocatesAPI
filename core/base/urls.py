from django.urls import path
from . import views
urlpatterns = [
    path("list/",views.AdvocateList.as_view()),
    path("list/<str:username>/",views.AdvocateDetail.as_view()),
       path("clist/",views.CompanyList.as_view()),
          path("clist/<str:name>/",views.CompanyDetail.as_view()),
              path('list/search/', views.SearchAdvocates.as_view(), name='advocate-search'),
#  path("list/",views.Query)
    # path("search/",views.Query)
]
