# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from student.views import RankListView, BugListClassView, BugCreateView

urlpatterns = [
    # 作業進度查詢
    url(r'^progress/(?P<classroom_id>\d+)/(?P<unit>\d+)$', views.progress),   

    # 作業上傳
    url(r'^work/(?P<classroom_id>\d+)/$', views.work),       
    url(r'^submit/(?P<index>\d+)/$', views.submit),       
    url(r'^submitall/(?P<index>\d+)/$', views.submitall),      
    # 同學
    url(r'^classmate/(?P<classroom_id>\d+)/$', views.classmate), 
    url(r'^loginlog/(?P<user_id>\d+)/$', views.LoginLogListView.as_view()),     
    # 分組
    url(r'^group/enroll/(?P<classroom_id>[^/]+)/(?P<group_id>[^/]+)/$', views.group_enroll),    
    url(r'^group/add/(?P<classroom_id>[^/]+)/$', views.group_add),     
    url(r'^group/(?P<classroom_id>[^/]+)/$', views.group),   
    url(r'^group/size/(?P<classroom_id>[^/]+)/$', views.group_size),      
    url(r'^group/open/(?P<classroom_id>[^/]+)/(?P<action>[^/]+)/$', views.group_open),     
	url(r'^group/delete/(?P<group_id>[^/]+)/(?P<classroom_id>[^/]+)/$', views.group_delete), 
    # 選課
    url(r'^classroom/enroll/(?P<classroom_id>[^/]+)/$', views.classroom_enroll),      
    url(r'^classroom/add/$', views.classroom_add),  
    url(r'^classroom/$', views.classroom),
	url(r'^classroom/seat/(?P<enroll_id>\d+)/(?P<classroom_id>\d+)/$', views.seat_edit, name='seat_edit'),
   
    # 課程  
    url(r'^lesson/(?P<lesson>[^/]+)/$', views.lesson),    
    url(r'^lessons/(?P<unit>[^/]+)/$', views.lessons),   
    url(r'^lesson/log/(?P<lesson>[^/]+)/$', views.lesson_log),    
    #查詢該作業分組小老師
    url(r'^group/work/(?P<lesson>[^/]+)/(?P<classroom_id>[^/]+)$', views.work_group),  
    #查詢該作業所有同學心得
    url(r'^memo/(?P<classroom_id>[^/]+)/(?P<index>[^/]+)/$', views.memo),   
    
    #測驗
    url(r'^exam/$', views.exam),      
    url(r'^exam_check/$', views.exam_check),     
    url(r'^exam/score/$', views.exam_score),  	

    #積分排行榜
    url(r'^rank/(?P<kind>[^/]+)/(?P<classroom_id>[^/]+)/$', views.RankListView.as_view(), name='rank'), 
    
    #查詢某班級所有同學心得		
    url(r'^memo_all/(?P<classroom_id>[^/]+)$', views.memo_all),  	
    url(r'^memo_show/(?P<user_id>\d+)/(?P<unit>\d+)/(?P<classroom_id>[^/]+)/(?P<score>[^/]+)/$', views.memo_show),
    
    # bug
    url(r'^bug/class/(?P<classroom_id>[^/]+)/$', login_required(views.BugListClassView.as_view()), name='bug_class_list'),	
    url(r'^bug/(?P<bug_id>[^/]+)/$',views.bug_detail, name='bug_detail'),
	url(r'^bug/add/(?P<classroom_id>[^/]+)/$', login_required(BugCreateView.as_view()), name='bug-add'),    
	url(r'^bug/value/(?P<bug_id>[^/]+)/$', views.debug_value, name='bug-add'),    
	
	#作品編號
	url(r'^work_help/$', views.work_help), 
	
	#學習筆記
	url(r'^note/$', views.NoteListView.as_view(), name='note'), 
	url(r'^note/doc/$', views.doc_download), 
		
]
