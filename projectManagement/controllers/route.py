# -*- coding: utf-8 -*-
# from [projectname] dari var yang sudah dideclare di init.py
from projectManagement import app
# flask adalah web server
from flask import render_template



@app.route('/')
def start():
    return render_template('auth/login.html')


#login route logic
@app.route("/login")
def login():
    return render_template('auth/login.html')


#login route logic
@app.route("/dashboard")
def dashboard():
    return render_template('content/home.html')


#registration route logic
@app.route("/user/registration")
def registration():
    return render_template('auth/register.html')


#forgot password route logic
@app.route('/user/forgot')
def forgotPasswd():
    return render_template('auth/forgot-password.html')


#forgot password route logic
@app.route('/user/changepassword')
def chgPasswd():
    return render_template('content/change-password.html')


#page all employee
@app.route('/employees/all')
def emplAll():
    return render_template('content/employee.html')


#page edit detail employee
@app.route('/employees/edit/detail')
def empEdtDet():
    return render_template('content/edit-employee.html')


#page department employee
@app.route('/department/all')
def deptAll():
    return render_template('content/department.html')


#page edit detail department
@app.route('/department/edit/detail')
def deptEditDet():
    return render_template('content/edit-department.html')


#page division
@app.route('/division/all')
def divAll():
    return render_template('content/division.html')


#page edit detail division
@app.route('/division/edit/detail')
def divEditDet():
    return render_template('content/edit-division.html')


#page main client
@app.route("/user/main/client")
def userMainHome():
    return render_template('content/main-client.html')


#page edit client
@app.route("/user/edit/client")
def userEditClient():
    return render_template('content/edit-client.html')


#page main client
@app.route("/user/main/clientlist")
def userMainHomeList():
    return render_template('content/main-clientlist.html')


#page detail client
@app.route("/user/client/detail")
def userClientDetail():
    return render_template('content/detail-client.html')


#page edit client
@app.route("/user/client/edit")
def userClientEdit():
    return render_template('content/edit-profile.html')


#page main project
@app.route("/project/main")
def mainProject():
    return render_template('content/main-project.html')


#page edit project
@app.route("/project/edit/detail")
def editProject():
    return render_template('content/edit-project.html')


#page view detail project
@app.route("/project/view/detail")
def viewDetailProject():
    return render_template('content/detail-projectview.html')


#page approve project
@app.route("/project/approve")
def projectApprove():
    return render_template('content/approve-project.html')


#page document project
@app.route("/project/document")
def projectDoc():
    return render_template('content/doc-project.html')


#page task list
@app.route("/project/task/all")
def projectTaskList():
    return render_template('content/list-task.html')


#page edit task
@app.route("/project/task/edit")
def projectTaskEdit():
    return render_template('content/edit-task.html')


#page detail task
@app.route("/project/task/detail")
def projectTaskDetail():
    return render_template('content/detail-task.html')


#page time sheet
@app.route("/project/timesheet")
def projectTimesheet():
    return render_template('content/time-sheet.html')


#page problem all
@app.route("/problem/all")
def problemAll():
    return render_template('content/problem-log.html')


#page problem detail
@app.route("/problem/detail")
def problemDetail():
    return render_template('content/detail-problem.html')


#page problem edit
@app.route("/problem/edit")
def problemEdit():
    return render_template('content/edit-problem.html')


#page report proyek
@app.route("/project/report/all")
def reportProject():
    return render_template('content/report-proyek.html')


#page report task
@app.route("/project/report/task")
def reportTask():
    return render_template('content/report-task.html')


#page report problem
@app.route("/project/report/problem")
def reportProblem():
    return render_template('content/report-problem.html')


#page report audit trail
@app.route("/project/report/audit")
def reportAudit():
    return render_template('content/report-audit.html')