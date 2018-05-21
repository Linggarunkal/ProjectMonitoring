# -*- coding: utf-8 -*-
# from [projectname] dari var yang sudah dideclare di init.py
from projectManagement import app
# flask adalah web server
from flask import render_template, request, redirect, url_for, json
from projectManagement.models.employee import department, division


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
    allDept = department()
    getDeptAll = allDept.all()
    return render_template('content/department.html', allDeapt=getDeptAll)


#action add department employee
@app.route('/department/add', methods=['POST'])
def deptAdd():
    deptName = request.form['department_name']
    addDept = department()
    getAddDept = addDept.add(deptName)
    if getAddDept:
        return redirect(url_for('deptAll'))


#page show detail department
@app.route('/department/detail/edit/<deptno>')
def deptEditDet(deptno):
    detailDept = department()
    getdetDept = detailDept.detail(deptno)
    return render_template('content/edit-department.html', detailDept=json.dumps(getdetDept))


#page show detail department
@app.route('/department/detail/delete/<deptno>')
def deptDeleteDet(deptno):
    detailDept = department()
    getdetDept = detailDept.detail(deptno)
    return render_template('content/delete-department.html', detailDept=json.dumps(getdetDept))


#page update edit detail department
@app.route('/department/edit', methods=['POST'])
def deptUpdDet():
    deptId = request.form['deptId']
    deptName = request.form['deptName']
    deptDesc = request.form['deptDesc']
    updDept = department()
    # jika ada validasi di tambah di sini
    updDept.update(deptId, deptName, deptDesc)
    return redirect(url_for('deptAll'))


#page update detail department
@app.route('/department/delete', methods=['POST'])
def deptDelDet():
    deptId = request.form['deptId']
    delDept = department()
    delDept.deleted(deptId)
    return redirect(url_for('deptAll'))


#page division
@app.route('/division/all')
def divAll():
    div = division()
    divList = div.all()
    deptName = div.getDeptName()
    return render_template('content/division.html', divList=divList, deptName=deptName)


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