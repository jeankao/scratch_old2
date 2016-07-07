# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from teacher.views import ClassroomListView, ClassroomCreateView, AnnounceListView, AnnounceCreateView
#, ClassroomDetails

urlpatterns = [
    # post views
    url(r'^classroom/$', login_required(ClassroomListView.as_view()), name='classroom-list'),
    url(r'^classroom/add/$', login_required(ClassroomCreateView.as_view()), name='classroom-add'),
    url(r'^classroom/edit/(?P<classroom_id>\d+)/$', views.classroom_edit, name='classroom-edit'),
    # 退選
    url(r'^unenroll/(?P<enroll_id>\d+)/(?P<classroom_id>\d+)/$', views.unenroll),  	
    
    #作業
    url(r'^work/(?P<classroom_id>\d+)/$', views.work),    
    url(r'^assistant/(?P<classroom_id>\d+)/(?P<user_id>\d+)/(?P<lesson>\d+)/$', views.assistant), 
    url(r'^assistant_cancle/(?P<classroom_id>\d+)/(?P<user_id>\d+)/(?P<lesson>\d+)/$', views.assistant_cancle),  
    url(r'^score_peer/(?P<index>\d+)/(?P<classroom_id>\d+)/(?P<group>\d+)/$', views.score_peer),     
    url(r'^scoring/(?P<classroom_id>[^/]+)/(?P<user_id>\d+)/(?P<index>\d+)/$', views.scoring),     
    url(r'^score/(?P<classroom_id>\d+)/(?P<index>\d+)/$', views.score),   
    url(r'^work/group/(?P<lesson>\d+)/(?P<classroom_id>\d+)/$', views.work_group),   	

    #測驗卷
    url(r'^exam/(?P<classroom_id>\d+)/$', views.exam_list),
	url(r'^exam_detail/(?P<classroom_id>\d+)/(?P<student_id>\d+)/(?P<exam_id>\d+)/$', views.exam_detail), 
    
    # 心得
    url(r'^memo/(?P<classroom_id>\d+)/$', views.memo),	
	url(r'^check/(?P<user_id>[^/]+)/(?P<unit>[^/]+)/(?P<classroom_id>\d+)/$', views.check), 	
	
	#結算成績
    url(r'^grade/(?P<classroom_id>\d+)/$', views.grade),
    url(r'^grade1/(?P<classroom_id>\d+)/$', views.grade_unit1),
    url(r'^grade2/(?P<classroom_id>\d+)/$', views.grade_unit2),
    url(r'^grade3/(?P<classroom_id>\d+)/$', views.grade_unit3),
    url(r'^grade4/(?P<classroom_id>\d+)/$', views.grade_unit4),	
    
    #公告
    url(r'^announce/(?P<classroom_id>\d+)/$', login_required(AnnounceListView.as_view()), name='announce-list'),
    url(r'^announce/add/(?P<classroom_id>\d+)/$', login_required(AnnounceCreateView.as_view()), name='announce-add'),  
    url(r'^announce/detail/(?P<message_id>\d+)/$', views.announce_detail),

    #系統事件記錄
    url(r'^event/(?P<classroom_id>\d+)/(?P<user_id>\d+)/$', views.EventListView.as_view()),
    url(r'^event/clear/(?P<classroom_id>\d+)/$', views.clear),
    url(r'^event/excel/(?P<classroom_id>\d+)/$', views.event_excel),
    url(r'^event/make/$', views.event_make),    
    url(r'^event/video/make/$', views.event_video_make),
    
    
    #教學筆記
    url(r'^note/(?P<classroom_id>\d+)/$', views.NoteListView.as_view()),	
]