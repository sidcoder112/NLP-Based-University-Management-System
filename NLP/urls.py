"""NLP_web_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from NLP import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.login),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('View_approved_collage',views.View_approved_collage),
    path('View_collage',views.View_collage),
    path('admin_approve_college/<id>',views.admin_approve_college),
    path('admin_reject_college/<id>',views.admin_reject_college),
    path('Courses',views.Courses),
    path('course_post',views.course_post),
    path('View_Course',views.View_Course),
    path('delete_Course/<id>',views.delete_Course),
    path('edit_course/<id>',views.edit_course),
    path('ed_course_post/<id>',views.ed_course_post),
    path('Subject/<id>',views.Subjects),
    path('Sub/<id>',views.Sub),
    path('View_subject/<id>',views.View_subject),
    path('delete_sub/<id>',views.delete_sub),
    path('edit_sub_post/<id>',views.edit_sub_post),
    path('edit_sub/<id>',views.edit_sub),

    path('Notifications',views.Notifications),
    path('Nf',views.Nf),
    path('View_Notification',views.View_Notification),
    path('delete_nof/<id>',views.delete_nof),

    path('View_Student', views.View_Student),
    path('view_internalmark/<id>', views.view_internalmark),
    path('External_Marks/<id>',views.External_Marks),
    path('Ext_Mark/<id>',views.Ext_Mark),
    path('View_External_Mark/<id>',views.View_External_Mark),


    path('Academic_Calender',views.Academic_Calender),
    path('AC_post',views.AC_post),
    path('admin_view_academic_calendar',views.admin_view_academic_calendar),
    path('delete_calender/<id>',views.delete_calender),

    path('Exan_timetablee',views.Exan_timetablee),
    path('exam_tb',views.exam_tb),
    path('View_Exan_timetable',views.View_Exan_timetable),
    path('delete_tb_/<id>',views.delete_tb_),
    path('Research_articles',views.Research_articles),
    path('Research_art',views.Research_art),
    path('View_Research_article',views.View_Research_article),
    path('delete_rech/<id>',views.delete_rech),

    path('student_home',views.student_home),


    path('clg_reg',views.clg_reg),
    path('clg_reg_post',views.clg_reg_post),
    path('clg_home',views.clg_home),
    path('view_profile',views.view_profile),
    path('clg_view_course',views.clg_view_course),
    path('clg_Add_tolist/<id>',views.clg_Add_tolist),
    path('clg_Add_tolist_post/<id>',views.clg_Add_tolist_post),
    path('clg_Add_tolist',views.clg_Add_tolist),
    path('clg_View_Notification',views.clg_View_Notification),
    path('clg_view_academic_calendar',views.clg_view_academic_calendar),
    path('clg_View_Exan_timetable',views.clg_View_Exan_timetable),
    path('add_student',views.add_student),
    path('add_student_post',views.add_student_post),
    path('view_students_clg',views.view_students_clg),
    path('view_students_clg_post',views.view_students_clg_post),

    path('update_student/<id>',views.update_student),
    path('update_student_post/<id>',views.update_student_post),
    path('delete_student/<id>',views.delete_student),
    path('add_internal_mark/<id>',views.add_internal_mark),
    path('add_internal_mark_post/<id>',views.add_internal_mark_post),
    path('view_internal_mark/<id>',views.view_internal_mark),
    path('delete_internal_mark/<id>',views.delete_internal_mark),
    path('view_prof_update/<id>',views.view_prof_update),




    path('view_profile_student',views.view_profile_student),
    path('view_profile_update/<id>',views.view_profile_update),
    path('view_subjectes_stud',views.view_subjectes_stud),
    path('view_internal_marks_stud',views.view_internal_marks_stud),
    path('view_notification_stud',views.view_notification_stud),
    path('view_external_stud',views.view_external_stud),
    path('view_academic_calender_stud',views.view_academic_calender_stud),
    path('view_timetable_stud/<id>',views.view_timetable_stud),
    path('view_articles_stud',views.view_articles_stud),
    path('logout',views.logout),

    path('user_search_post',views.user_search_post),





]
