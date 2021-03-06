from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from main.views import *
from users.views import *

urlpatterns = [
    path('main/', Main.as_view(), name = 'main'),
    path('admin/', admin.site.urls),

    path('main/register/', Register.as_view(), name = 'register'),
    path('main/login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('main/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('main/profile/', Profile.as_view(), name = 'profile'),
    path('main/ask_question/', Ask_Question.as_view(), name = 'ask_question'),

    path('main/all_votes/', All_Votes.as_view(), name = 'all_votes'),
    path('main/view_all_my_votes/', View_All_My_Votes.as_view(), name = 'view_all_my_votes'),

    path('main/set_all_my_questions/', Set_All_My_Questions.as_view(), name = 'set_all_my_questions'),
    path('main/set_all_my_questions/get_all_my_questions/', Get_All_My_Questions.as_view(), name = 'get_all_my_questions'),
    path('main/set_all_my_questions/<int:question_id>/<int:vote_a>/<int:vote_b>/<int:vote_c>/', Edit_All_My_Questions.as_view(), name = 'edit_all_my_questions'),
    path('main/set_all_my_questions/<int:question_id>/<int:vote_a>/<int:vote_b>/<int:vote_c>/get_edit_all_my_questions', Get_Edit_All_My_Questions.as_view(), name = 'get_edit_all_my_questions'),
    
    path('main/bookmark/<int:question_id>/', Bookmark.as_view(), name = 'bookmark'),
    path('main/get_bookmarks/', Get_Bookmarks.as_view(), name = 'get_bookmarks'),
    path('main/delete_bookmark/<int:question_id>', Delete_Bookmark.as_view(), name = 'delete_bookmark'),
    path('main/get_bookmarks/view_my_bookmarks/', View_My_Bookmarks.as_view(), name = 'view_my_bookmarks'),

    path('main/answer_vote/', Answer_Vote.as_view(), name = 'answer_vote'),
    path('main/answer_vote/<slug:question_id>/<slug:vote_type>/<slug:vote>/', Answer_Vote.as_view(), name = 'answer_vote'),
    
    path('main/delete/<int:answer_id>/', Delete.as_view(), name = 'delete'),
    
    path('main/edit/', Edit.as_view(), name = 'edit'),
    path('main/edit/<int:answer_id>/', Edit.as_view(), name = 'edit'),

    path('main/view_all_my_votes/get_all_user_qs_vs', Get_All_My_Votes.as_view(), name = 'get_all_user_qs_vs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
