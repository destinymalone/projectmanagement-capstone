from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,  include
from django.contrib.auth import views as auth_views
from polls.views import (
    RegistrationView, 
    CreateBoardView, 
    BoardDetailView,
    # BoardEditView,
    BoardDeleteView, 
    BoardListView,
    ListDetailView,
    ListEditView,
    ListDeleteView, 
    ListCardView, 
    ListDetailView,
    # CardDetailView, 
    CardEditView,
    CardDeleteView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegistrationView.as_view()),
    path("", CreateBoardView.as_view(), name="board"),
    path("board/detail/<id>/", BoardDetailView.as_view(), name="board_detail"),
    # path("board/edit<id>/", BoardEditView.as_view()),
    path("board/delete<id>/", BoardDeleteView.as_view(), name="board_delete"),
    path("list/<id>", BoardListView.as_view(), name="list_create"),
    path("list/detail/<id>/", ListDetailView.as_view(), name="list_detail"),
    path("list/edit/<id>/", ListEditView.as_view(), name="list_edit"),
    path("list/delete/<id>/", ListDeleteView.as_view(), name="list_delete"),
    path("card/<id>", ListCardView.as_view(), name="card_create"),
    # path("card/detail/<id>/", CardDetailView.as_view(), name="card_detail"),
    path("card/edit/<id>/", CardEditView.as_view(), name="card_edit"),
    path("card/delete/<id>/", CardDeleteView.as_view(), name="card_delete"),
    # path('polls/', include('polls.urls')),
]

urlpatterns += staticfiles_urlpatterns()
