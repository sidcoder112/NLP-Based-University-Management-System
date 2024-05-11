import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from NLP.models import *


def login(request):
    return render(request,"index.html")

def login_post(request):
    usn = request.POST['textfield']
    psw = request.POST['textfield2']
    res = Login.objects.filter(username=usn, password=psw)
    if res.exists():
        request.session['lid'] = res[0].id
        request.session['log'] = "lo"
        if res[0].usertype == 'admin':
            return redirect('/admin_home')
        if res[0].usertype == 'college':
            return redirect('/clg_home')
        if res[0].usertype == 'student':
            return redirect('/student_home')
    else:
        return HttpResponse("<script>alert('Invalid details');window.location='/';</script>")


def admin_home(request):
    return render(request, "ADMIN/index.html")
def student_home(request):
    return render(request, "student/index.html")

def Reg_collages(request):
    return render(request,"ADMIN/Reg_collage.html")

def View_collage(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=collage.objects.filter(LOGIN__usertype="pending")
    return render(request,"ADMIN/view_regcollage.html",{'data':res})

def admin_approve_college(request, id):
    Login.objects.filter(id=id).update(usertype="college")
    return HttpResponse("<script>alert('College approved');window.location='/View_collage';</script>")

def admin_reject_college(request, id):
    Login.objects.filter(id=id).update(usertype="rejected")
    return HttpResponse("<script>alert('College approved');window.location='/View_collage#admin';</script>")

def View_approved_collage(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=collage.objects.filter(LOGIN__usertype="college")
    return render(request,"ADMIN/view_appr_collage.html",{'data':res})


def Courses(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    return render(request,"ADMIN/Course.html")
def course_post(request):
    course_name = request.POST['textfield']
    course_code = request.POST['textfield2']
    select = request.POST['select']
    i=Course.objects.filter(Course_code=course_code)
    if i.exists():
        return HttpResponse("<script>alert('Alredy Added');window.location='/Courses'</script>")
    else:
        obj = Course()
        obj.Course_Name = course_name
        obj.Course_code = course_code
        obj.Stream = select
        obj.save()
        return redirect("/View_Course")


def View_Course(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Course.objects.all()
    return render(request,"ADMIN/view_course.html",{'data':res})

def delete_Course(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/View_Course")

def edit_course(request, id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Course.objects.get(id=id)
    return render(request, "ADMIN/edit_Course.html", {'data':res})
def ed_course_post(request, id):
    cname=request.POST['textfield']
    ccode=request.POST['textfield2']
    stream=request.POST['select']
    obj=Course.objects.get(id=id)
    obj.Course_Name=cname
    obj.Course_code=ccode
    obj.Stream=stream
    obj.save()
    return redirect("/View_Course")


def Subjects(request, id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    return render(request,"ADMIN/Subject.html", {'id':id})
def Sub(request, id):
    sub_name = request.POST['textfield']
    semester = request.POST['select']
    credit = request.POST['textfield2']
    c_code = request.POST['textfield3']
    i=subject.objects.filter(subject_name=sub_name,semester=semester,COURSE_id=id)
    if i.exists():
        return HttpResponse("<script>alert('Alredy Added');window.location='/Courses'</script>")
    else:
        j = subject.objects.filter(coursecode=c_code)
        if j.exists():
            return HttpResponse("<script>alert('Course code should be unique');window.location='/Courses'</script>")
        else:
            obj = subject()
            obj.subject_name = sub_name
            obj.semester = semester
            obj.credit = credit
            obj.COURSE_id = id
            obj.coursecode=c_code
            obj.save()
            return HttpResponse("<script>alert('Subject added');window.location='/View_Course';</script>")

def View_subject(request, id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=subject.objects.filter(COURSE_id=id)
    request.session['cid']=id
    return render(request,"ADMIN/View_Subject.html",{'data':res})

def delete_sub(request, id):
    subject.objects.filter(id=id).delete()
    cid=request.session['cid']
    return redirect("/View_subject/"+cid)

def edit_sub(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=subject.objects.get(id=id)
    return render(request, "ADMIN/edit_Subject.html", {'data':res})
def edit_sub_post(request, id):
    sname=request.POST['textfield']
    sem=request.POST['select']
    credit=request.POST['textfield2']
    subject.objects.filter(id=id).update(subject_name=sname, semester=sem, credit=credit)
    cid=request.session['cid']
    return redirect("/View_subject/"+cid)

def Notifications(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    return render(request,"ADMIN/Notification.html")

def Nf(request):
    notification = request.POST['textarea']
    type = request.POST['select']
    i=Notification.objects.filter(Notification=notification)
    if i.exists():
        return HttpResponse("<script>alert('Alredy Added');window.location='/Notifications'</script>")
    else:
        obj = Notification()
        obj.Notification = notification
        obj.type = type
        obj.date = datetime.datetime.now().date()
        obj.save()
        return HttpResponse("<script>alert('Notification added');window.location='/Notifications';</script>")


def View_Notification(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Notification.objects.all()
    return render(request,"ADMIN/View_Notification.html",{'data':res})

def delete_nof(request, id):
    Notification.objects.get(id=id).delete()
    return redirect(request, "/View_Notification")


def View_Student(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=student.objects.all()
    return render(request,"ADMIN/View_Student.html",{'data':res})

def View_Student_post(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    reg=request.POST['reg']
    res=student.objects.filter(reg_no=reg)
    return render(request,"ADMIN/View_Student.html",{'data':res})

def view_internalmark(request, id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=internal_mark.objects.filter(STUDENT_id=id)
    return render(request, "ADMIN/view_internalmark.html", {'data':res})



def External_Marks(request, id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    stud=student.objects.get(id=id)
    sub=subject.objects.filter(COURSE=stud.COURSE, semester=stud.semester)
    print(sub, "sub")
    return render(request,"ADMIN/External Mark.html", {'id':id, 'data':sub})

def Ext_Mark(request, id):
    mark = request.POST['textfield']
    subject = request.POST['select']
    i=External_Mark.objects.filter(max_mark=mark,SUBJECT_id=subject,STUDENT_id=id)
    if i.exists():
        return HttpResponse("<script>alert('Already added');window.location='/View_Student';</script>")
    else:
        obj = External_Mark()
        obj.max_mark = mark
        obj.SUBJECT_id = subject
        obj.STUDENT_id = id
        obj.save()
        return HttpResponse("<script>alert('External mark added');window.location='/View_Student';</script>")



def View_External_Mark(request, id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    request.session['stid']=id
    res=External_Mark.objects.filter(STUDENT_id=id)
    return render(request,"ADMIN/view_exernalmark.html",{'data':res})

def delete_exnmark(request, id):
    External_Mark.objects.get(id=id).delete()
    stid=request.session['stid']
    return redirect("/View_External_Mark"+stid)




def Academic_Calender(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Course.objects.all()
    return render(request,"ADMIN/Academic Calendar.html", {'data':res})

def AC_post(request):
    cid = request.POST['select']
    year = request.POST['textarea']
    file = request.FILES['filefield']
    d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\HP\PycharmProjects\NLP_web_search\NLP\static\proj_files\\" + d + ".xls", file)
    path="/static/proj_files/" + d + ".xls"
    i=Academic_Calendar.objects.filter(Year=year,COURSE_id=cid)
    if i.exists():
        return HttpResponse("<script>alert('Already added');window.location='/Academic_Calender';</script>")
    else:
        obj = Academic_Calendar()
        obj.COURSE_id = cid
        obj.Year = year
        obj.Calendar = path
        obj.save()
        return HttpResponse("<script>alert('Academic calendar added');window.location='/Academic_Calender';</script>")


def admin_view_academic_calendar(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Academic_Calendar.objects.all()
    return render(request, "ADMIN/view_academic_calendar.html", {'data':res})

def delete_calender(request, id):
    Academic_Calendar.objects.get(id=id).delete()
    return redirect("/admin_view_academic_calendar")

def Exan_timetablee(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=subject.objects.all()
    return render(request,"ADMIN/Exan_timetable.html", {'data':res})

def exam_tb(request):
    subject= request.POST['select']
    date = request.POST['textfield2']
    time = request.POST['textfield3']
    i=Exan_timetable.objects.filter(SUBJECT_id=subject,date=date)

    dt_lst=date.split("-")
    tm_lst=time.split(":")
    print(dt_lst, "date")
    print(tm_lst, "time")
    exam_datetime = datetime.datetime(int(dt_lst[0]), int(dt_lst[1]), int(dt_lst[2]), int(tm_lst[0]), int(tm_lst[1]))   #   exam time
    exam_hr_start = datetime.datetime(int(dt_lst[0]), int(dt_lst[1]), int(dt_lst[2]), 9, 0)   #   exam starting min time (9am)
    exam_hr_end = datetime.datetime(int(dt_lst[0]), int(dt_lst[1]), int(dt_lst[2]), 13, 0)   #   exam starting max time (1pm)
    print(exam_hr_start, exam_datetime, exam_hr_end)


    if i.exists():
        return HttpResponse("<script>alert('Already  added');window.location='/Exan_timetablee';</script>")

    else:
        if exam_datetime >= exam_hr_start and exam_datetime <=exam_hr_end:
            obj = Exan_timetable()
            obj.SUBJECT_id = subject
            obj.date = date
            obj.time = time
            obj.save()
            return HttpResponse("<script>alert('Exam timetable added');window.location='/Exan_timetablee';</script>")
        else:
            return HttpResponse("<script>alert('Exam should be conducted in working hours!!!');window.location='/Exan_timetablee';</script>")



def View_Exan_timetable(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Exan_timetable.objects.all()
    return render(request,"ADMIN/view_timetable.html",{'data':res})

def delete_tb_(request, id):
    Exan_timetable.objects.get(id=id).delete()
    return redirect("/View_Exan_timetable")

def Research_articles(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    return render(request,"ADMIN/Research_article.html")

def Research_art(request):
    fl = request.FILES['fileField']
    author = request.POST['textfield']
    date = request.POST['textfield2']
    abst = request.POST['textarea']

    d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\HP\PycharmProjects\NLP_web_search\NLP\static\proj_files\\" + d + ".pdf", fl)
    path="/static/proj_files/" + d + ".pdf"

    i=Research_article.objects.filter(Author=author,date=date,Article=path)
    if i.exists():
        return HttpResponse("<script>alert('Already added');window.location='/Research_articles';</script>")

    else:
        obj = Research_article()
        obj.Author = author
        obj.date = date
        obj.Article = path
        obj.Abstract=abst
        obj.save()
        return HttpResponse("<script>alert('Research article added');window.location='/Research_articles';</script>")


def View_Research_article(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Research_article.objects.all()
    return render(request,"ADMIN/View_research_ar.html",{'data':res})

def delete_rech(request, id):
    Research_article.objects.get(id=id).delete()
    return redirect("/View_Research_article")



def clg_reg(request):
    return render(request, "college/Register.html")
def clg_reg_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    psw=request.POST['textfield7']

    i=Login.objects.filter(username=email)
    if i.exists():
        return HttpResponse("<script>alert('Alredy Registered');window.location='/clg_reg';</script>")

    else:
        obj = Login()
        obj.username = email
        obj.password = psw
        obj.usertype = "pending"
        obj.save()

        obj1 = collage()
        obj1.name = name
        obj1.email = email
        obj1.phone = phone
        obj1.place = place
        obj1.post = post
        obj1.pin = pin
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('Registered');window.location='/';</script>")

def clg_home(request):
    return render(request, "college/index.html")

def view_profile(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=collage.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "college/view_profile.html", {'data':res})

def view_prof_update(request,id):
    name = request.POST['textfield']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    collage.objects.filter(id=id).update(name=name,phone=phone,place=place,post=post,pin=pin)
    return HttpResponse("<script>alert('Updated');window.location='/view_profile#admin';</script>")



def clg_view_course(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Course.objects.all()
    return render(request, "college/view_course.html", {'data':res})

def clg_Add_tolist(request, id):
    return render(request, "college/add_own_list.html", {'id':id})
def clg_Add_tolist_post(request, id):
    fee=request.POST['textfield6']
    i=own_list.objects.filter(COURSE_id=id,COLLEGE__LOGIN=request.session['lid'])
    if i.exists():
        return HttpResponse("<script>alert('Already Added to list');window.location='/clg_view_course';</script>")
    else:
        obj = own_list()
        obj.COURSE_id = id
        obj.fee=fee
        obj.COLLEGE = collage.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Added to list');window.location='/clg_view_course';</script>")



def clg_View_Notification(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Notification.objects.filter(type="college")
    return render(request,"college/View_Notification.html",{'data':res})

def clg_view_academic_calendar(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Academic_Calendar.objects.all()
    return render(request, "college/view_academic_calendar.html", {'data':res})


def clg_View_Exan_timetable(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Exan_timetable.objects.all()
    return render(request,"college/view_timetable.html",{'data':res})

def add_student(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=own_list.objects.filter(COLLEGE__LOGIN=request.session['lid'])
    return render(request,"college/add_stud.html",{"data":res})

def add_student_post(request):
    nm=request.POST['textfield']
    em=request.POST['textfield2']
    ph=request.POST['textfield3']
    pl=request.POST['textfield4']
    age=request.POST['textfield5']
    reg=request.POST['textfield6']
    crse=request.POST['crse']
    sem=request.POST['sem']

    i=Login.objects.filter(username=em)
    if i.exists():
        return HttpResponse("<script>alert('Already Registered');window.location='/add_student_post';</script>")

    else:
        obj = Login()
        obj.usertype = "student"
        obj.username = em
        obj.password = random.randint(11111, 99999)
        obj.save()

        obj1 = student()
        obj1.name = nm
        obj1.email = em
        obj1.place = pl
        obj1.phone = ph
        obj1.age = age
        obj1.reg_no = reg
        obj1.COURSE_id = crse
        obj1.semester = sem
        obj1.LOGIN = obj
        obj1.COLLAGE = collage.objects.get(LOGIN=request.session['lid'])
        obj1.save()
        return HttpResponse("<script>alert('Registered');window.location='/view_students_clg';</script>")



def view_students_clg(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=student.objects.filter(COLLAGE__LOGIN=request.session['lid'])
    return render(request,"college/view_students.html",{"data":res})
def view_students_clg_post(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    stream=request.POST['select']
    res=student.objects.filter(COLLAGE__LOGIN=request.session['lid'], COURSE__Stream=stream)
    return render(request,"college/view_students.html",{"data":res})

def add_internal_mark(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    cid=student.objects.get(id=id).COURSE_id
    sid=subject.objects.filter(COURSE_id=cid)
    return render(request,"college/add_internl.html",{'data':sid,"id":id})

def add_internal_mark_post(request,id):
    mark=request.POST['textfield6']
    sub=request.POST['sub']
    i=internal_mark.objects.filter(max_mark=mark,SUBJECT_id=sub,STUDENT_id=id)
    if i.exists():
        return HttpResponse("<script>alert('Already Added');window.location='/view_students_clg';</script>")
    else:
        obj = internal_mark()
        obj.max_mark = mark
        obj.SUBJECT_id = sub
        obj.STUDENT_id = id
        obj.save()
        return HttpResponse("<script>alert('Added');window.location='/view_students_clg';</script>")


def view_internal_mark(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=internal_mark.objects.filter(STUDENT_id=id)
    return render(request,"college/view_internal.html",{"data":res})

def delete_internal_mark(request,id):
    internal_mark.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_students_clg';</script>")


def update_student(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=student.objects.get(id=id)
    res1=own_list.objects.filter(COLLEGE__LOGIN=request.session['lid'])
    return render(request,"college/update_stud.html",{'data':res,"data1":res1})

def update_student_post(request,id):
    nm = request.POST['textfield']
    ph = request.POST['textfield3']
    pl = request.POST['textfield4']
    age = request.POST['textfield5']
    reg = request.POST['textfield6']
    crse = request.POST['crse']
    sem = request.POST['sem']
    student.objects.filter(id=id).update(name=nm,phone=ph,age=age,place=pl,reg_no=reg,COURSE_id=crse,semester=sem)
    return HttpResponse("<script>alert('Updated');window.location='/view_students_clg';</script>")


def delete_student(request,id):
    student.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_students_clg';</script>")


###################################################################################################

def view_profile_student(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=student.objects.get(LOGIN=request.session['lid'])
    sid=student.objects.get(LOGIN=request.session['lid']).COURSE_id
    res1=own_list.objects.filter(COURSE_id=sid)
    return render(request,"student/view_profile.html",{"data":res,"data1":res1})

def view_profile_update(request,id):
    nm = request.POST['textfield']
    ph = request.POST['textfield3']
    pl = request.POST['textfield4']
    age = request.POST['textfield5']
    reg = request.POST['textfield6']
    crse = request.POST['crse']
    sem = request.POST['sem']
    student.objects.filter(id=id).update(name=nm, phone=ph, age=age, place=pl, reg_no=reg, COURSE_id=crse, semester=sem)
    return HttpResponse("<script>alert('Updated');window.location='/view_profile_student';</script>")

def view_subjectes_stud(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    sid=student.objects.get(LOGIN=request.session['lid'])
    cid=sid.COURSE_id
    res=subject.objects.filter(COURSE_id=cid)
    return render(request,"student/View_Subject.html",{'data':res})

def view_internal_marks_stud(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=internal_mark.objects.filter(STUDENT__LOGIN=request.session['lid'])
    return render(request,"student/view_internalmark.html",{"data":res})

def view_notification_stud(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Notification.objects.filter(type="student")
    return render(request,"student/View_Notification.html",{'data':res})

def view_external_stud(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=External_Mark.objects.filter(STUDENT__LOGIN=request.session['lid'])
    return render(request,"student/view_exernalmark.html",{'data':res})

def view_academic_calender_stud(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    sid = student.objects.get(LOGIN=request.session['lid'])
    cid = sid.COURSE_id
    res=Academic_Calendar.objects.filter(COURSE_id=cid)
    return render(request,"student/view_academic_calendar.html",{"data":res})

def view_timetable_stud(request,id):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Exan_timetable.objects.filter(id=id)
    return render(request,"student/view_timetable.html",{"data":res})

def view_articles_stud(request):
    if request.session['log']!='lo':
        return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")
    res=Research_article.objects.all()
    return render(request,"student/View_research_ar.html",{'data':res})

def logout(request):
    request.session['log']=""
    request.session.clear()
    return HttpResponse("<script>alert('Logout Succesfully');window.location='/';</script>")

def user_search_post(request):
    qry=request.POST['qry']

    res=Research_article.objects.all()
    arr_res=[]
    for i in res:
        arr_res.append(i.Abstract)
    from .text_Compare import rank_texts
    ranked_texts = rank_texts(arr_res, qry)
    print("R1 ", ranked_texts)
    new_res=[]
    for i in ranked_texts:
        # print(i)
        if(float(i[0])>0.1):
            txt=i[1]
            print(txt)
            idx=arr_res.index(txt)
            new_res.append(res[idx])
    # print(new_res)


    res_noti=Notification.objects.filter(type="student")
    arr_res_noti=[]
    for i in res_noti:
        arr_res_noti.append(i.Notification)
    from .text_Compare import rank_texts
    ranked_texts_noti = rank_texts(arr_res_noti, qry)
    # print(ranked_texts_noti)
    new_res_noti=[]
    for i in ranked_texts_noti:
        # print(i)
        if(float(i[0])>0.1):
            txt=i[1]
            # print(txt)
            idx=arr_res_noti.index(txt)
            new_res_noti.append(res_noti[idx])
    # print(new_res_noti)

    res_course=own_list.objects.all()
    arr_res_course=[]
    for i in res_course:
        arr_res_course.append(i.COURSE.Course_Name + " course is provided by " + i.COLLEGE.name)
    from .text_Compare import rank_texts
    ranked_texts_course = rank_texts(arr_res_course, qry)
    # print(ranked_texts_course)
    new_res_course=[]
    for i in ranked_texts_course:
        # print(i)
        if(float(i[0])>0.1):
            txt=i[1]
            # print(txt)
            idx=arr_res_course.index(txt)
            new_res_course.append(res_course[idx])
    # print(new_res_course)

    sid = student.objects.get(LOGIN=request.session['lid'])
    cid = sid.COURSE_id
    res_cal = Academic_Calendar.objects.filter(COURSE_id=cid)
    arr_res_cal=[]
    for i in res_cal:
        arr_res_cal.append(i.Year)
    print("Acad Cal :" , arr_res_cal)
    from .text_Compare import rank_texts
    ranked_texts_cal = rank_texts(arr_res_cal, qry)
    # print(ranked_texts_cal)
    new_res_cal=[]
    for i in ranked_texts_cal:
        # print(i)
        if(float(i[0])>0.1):
            txt=i[1]
            # print(txt)
            idx=arr_res_cal.index(txt)
            new_res_cal.append(res_cal[idx])
    # print(new_res_cal)



    return render(request, "student/index.html", {'data':new_res, 'noti':new_res_noti, 'course':new_res_course, 'cal':new_res_cal})
