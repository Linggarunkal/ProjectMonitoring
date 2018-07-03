# -*- coding: utf-8 -*-
# from [projectname] dari var yang sudah dideclare di init.py
from projectManagement import app
# flask adalah web server
from flask import render_template, request, redirect, url_for, json, jsonify
from projectManagement.models.employee import department, division, employees
from projectManagement.models.client import clients
from projectManagement.models.project import project_list, projectApp
from projectManagement.models.task import tasks
from projectManagement.models.problem_log import problem_logs
from projectManagement.models.uploaded import upload
from projectManagement.models.report import reports
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_restful import reqparse
from passlib.hash import sha256_crypt


# generate password encrypt
def generate_passwd(passwd):
    return sha256_crypt.encrypt(passwd)


@app.route('/')
def start():
    return render_template('auth/login.html')


# login route logic
@app.route("/login")
def login():
    return render_template('auth/login.html')


# login route logic
@app.route("/registration")
def registration():
    return render_template('auth/register.html')


# login route logic
@app.route("/dashboard")
def dashboard():
    return render_template('content/home.html')


# forgot password route logic
@app.route('/user/forgot')
def forgotPasswd():
    return render_template('auth/forgot-password.html')


# forgot password route logic
@app.route('/user/changepassword')
def chgPasswd():
    return render_template('content/change-password.html')

# concatString = "{0:0>4}".format(auto_increment)


# page to check emp count
@app.route('/employees/count')
def empCount():
    employee = employees()
    countEmp = employee.checkEmp()
    concatString = "{0:0>4}".format(countEmp+1)
    response = {
        'code': 200,
        'data': concatString
    }
    return json.dumps(response)


# page add employees
@app.route('/employees/add', methods=['POST'])
def empAdd():
    parse = reqparse.RequestParser()
    parse.add_argument('fname', type=str, help='fname')
    parse.add_argument('lname', type=str, help='lname')
    parse.add_argument('birth', type=str, help='birth')
    parse.add_argument('gender', type=str, help='gender')
    parse.add_argument('address', type=str, help='address')
    parse.add_argument('city', type=str, help='city')
    parse.add_argument('phone', type=str, help='phone')
    parse.add_argument('nik', type=str, help='nik')
    parse.add_argument('password', type=str, help='password')
    parse.add_argument('division', type=str, help='division')
    parse.add_argument('title', type=str, help='title')
    parse.add_argument('email', type=str, help='email')
    parse.add_argument('join_date', type=str, help='join_date')

    args = parse.parse_args()
    fname = args['fname']
    lname = args['lname']
    birth = args['birth']
    gender = args['gender']
    address = args['address']
    city = args['city']
    phone = args['phone']
    nik = args['nik']
    password = args['password']
    division = args['division']
    title = args['title']
    email = args['email']
    join_date = args['join_date']
    birthday = datetime.strptime(birth, '%d/%m/%Y').strftime('%Y-%m-%d')
    passhash = generate_passwd(password)
    joinDate = datetime.strptime(join_date, '%d/%m/%Y').strftime('%Y-%m-%d')

    employee = employees()
    addEmployee = employee.add(nik, email, passhash, fname, lname, birthday, gender, address, city, phone, division, title, joinDate)
    if addEmployee:
        response = {
            'code': 200,
            'message': 'Data Success Add to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed add to System'
        }
        return json.dumps(response)


# page all employee
@app.route('/employees/all')
def emplAll():
    div = division()
    deptName = div.all()
    emp = employees()
    titleName = emp.getJobsTitle()
    province = emp.province()
    getAllEmp = emp.all()
    return render_template('content/employee.html', deptName=deptName, titleName=titleName, province=province, getAllEmp=getAllEmp)


# page city detail
@app.route('/city/detail/<provid>')
def cityDet(provid):
    emp = employees()
    getCity = emp.city(provid)
    return json.dumps(getCity)

# page detail employee
@app.route('/employees/detail/<empno>')
def empEdtDet(empno):
    emp = employees()
    getDetEmp = emp.detail(empno)
    return render_template('content/profile.html', getDetEmp=getDetEmp)


# page edit employee
@app.route('/employees/edit/<empid>')
def empEdt(empid):
    div = division()
    deptName = div.all()
    emp = employees()
    titleName = emp.getJobsTitle()
    province = emp.province()
    city = emp.city_all()
    getDetailEmp = emp.getEmployeeDetail(empid)
    return render_template('content/edit-employee.html', deptName=deptName, titleName=titleName, province=province, city=city, getDetailEmp=json.dumps(getDetailEmp))


# page add update employee
@app.route("/employees/update/detail", methods=['POST'])
def empUpdDetail():
    parse = reqparse.RequestParser()
    parse.add_argument('emp_id', type=str, help='emp_id')
    parse.add_argument('fname', type=str, help='fname')
    parse.add_argument('lname', type=str, help='lname')
    parse.add_argument('birth', type=str, help='birth')
    parse.add_argument('gender', type=str, help='gender')
    parse.add_argument('address', type=str, help='address')
    parse.add_argument('city', type=str, help='city')
    parse.add_argument('phone', type=str, help='phone')
    parse.add_argument('division', type=str, help='division')
    parse.add_argument('job_title', type=str, help='job_title')
    parse.add_argument('join_date', type=str, help='join_date')

    args = parse.parse_args()
    emp_id = args['emp_id']
    fname = args['fname']
    lname = args['lname']
    birth = args['birth']
    gender = args['gender']
    address = args['address']
    city = args['city']
    phone = args['phone']
    division = args['division']
    job_title = args['job_title']
    join_date = args['join_date']

    date_join = datetime.strptime(join_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    date_birth = datetime.strptime(birth, '%d/%m/%Y').strftime('%Y-%m-%d')

    emp = employees()
    updEmployees = emp.editEmp(emp_id, fname, lname, date_birth, gender, address, city, phone, division, job_title, date_join)
    if updEmployees:
        response = {
            'code': 200,
            'message': "Success Update Data to System"
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': "Failed Update Data to System"
        }
        return json.dumps(response)

# page delete detil division
@app.route('/employees/detail/delete/<empid>')
def empDelDet(empid):
    emp = employees()
    getDetEmp = emp.detail(empid)
    return render_template('content/delete-employees.html', getDetEmp=getDetEmp)


# page update detail employees
@app.route('/employees/detail/delete/', methods=['POST'])
def empDel():
    empid = request.form['employee_id']
    delEmp = employees()
    delEmp.deleted(empid)
    return redirect(url_for('emplAll'))

# page department employee
@app.route('/department/all')
def deptAll():
    allDept = department()
    getDeptAll = allDept.all()
    return render_template('content/department.html', allDeapt=getDeptAll)


# action add department employee
@app.route('/department/add', methods=['POST'])
def deptAdd():
    parse = reqparse.RequestParser()
    parse.add_argument('department_name', type=str, help='department_name')
    parse.add_argument('description', type=str, help='description')

    args = parse.parse_args()
    department_name = args['department_name']
    description = args['description']

    departemen = department()
    addDept = departemen.add(department_name, description)
    if addDept:
        response = {
            'code': 200,
            'message': 'Data Success Add to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed add to System'
        }
        return json.dumps(response)


# page show detail department
@app.route('/department/detail/edit/<deptno>')
def deptEditDet(deptno):
    detailDept = department()
    getdetDept = detailDept.detail(deptno)
    return render_template('content/edit-department.html', detailDept=json.dumps(getdetDept))


# page show detail department
@app.route('/department/detail/delete/<deptno>')
def deptDeleteDet(deptno):
    detailDept = department()
    getdetDept = detailDept.detail(deptno)
    return render_template('content/delete-department.html', detailDept=json.dumps(getdetDept))


# page update edit detail department
@app.route('/department/edit', methods=['POST'])
def deptUpdDet():
    parse = reqparse.RequestParser()
    parse.add_argument('deptId', type=str, help='deptId')
    parse.add_argument('deptName', type=str, help='deptName')
    parse.add_argument('deptDesc', type=str, help='deptDesc')

    args = parse.parse_args()
    deptId = args['deptId']
    deptName = args['deptName']
    deptDesc = args['deptDesc']
    updDept = department()
    # jika ada validasi di tambah di sini
    update_division = updDept.update(deptId, deptName, deptDesc)
    if update_division:
        response = {
            'code': 200,
            'message': 'Data Success Update to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed Update to System'
        }
        return json.dumps(response)


# page update detail department
@app.route('/department/delete', methods=['POST'])
def deptDelDet():
    deptId = request.form['deptId']
    delDept = department()
    delDept.deleted(deptId)
    return redirect(url_for('deptAll'))


# page division
@app.route('/division/all')
def divAll():
    div = division()
    divList = div.all()
    deptName = div.getDeptName()
    return render_template('content/division.html', divList=divList, deptName=deptName)


# page edit detail division
@app.route('/division/detail/edit/<divno>')
def divEditDet(divno):
    div = division()
    divDetail = div.detail(divno)
    getDept = div.getDeptName()
    return render_template('content/edit-division.html', divDetail=json.dumps(divDetail), deptName=getDept)


# page delete detil division
@app.route('/division/detail/delete/<divno>')
def divDelDet(divno):
    div = division()
    divDetail = div.detail(divno)
    getDept = div.getDeptName()
    return render_template('content/delete-division.html', divDetail=json.dumps(divDetail), deptName=getDept)


# page add division
@app.route('/division/add', methods=['POST'])
def divAdd():
    parse = reqparse.RequestParser()
    parse.add_argument('deptNo', type=str, help='deptNo')
    parse.add_argument('divName', type=str, help='divName')
    parse.add_argument('divDesc', type=str, help='divDesc')

    args = parse.parse_args()
    deptNo = args['deptNo']
    divName = args['divName']
    divDesc = args['divDesc']

    divisi = division()
    addDiv = divisi.add(deptNo, divName, divDesc)
    if addDiv:
        response = {
            'code': 200,
            'message': 'Data Success Add to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed add to System'
        }
        return json.dumps(response)


# @app.route('/department/delete', methods=['POST'])
# def deptDelDet():
#     deptId = request.form['deptId']
#     delDept = department()
#     delDept.deleted(deptId)
#     return redirect(url_for('deptAll'))


# page delete division
@app.route('/division/delete', methods=['POST'])
def divDelete():
    divno = request.form['divNo']
    div = division()
    #if add alert in this command
    div.deleted(divno)
    return redirect(url_for('divAll'))


# page update division
@app.route('/division/update', methods=['POST'])
def divUpdate():
    parse = reqparse.RequestParser()
    parse.add_argument('divNo', type=str, help='divNo')
    parse.add_argument('deptNo', type=str, help='deptNo')
    parse.add_argument('divName', type=str, help='divName')
    parse.add_argument('divDesc', type=str, help='divDesc')

    args = parse.parse_args()
    divNo = args['divNo']
    deptNo = args['deptNo']
    divName = args['divName']
    divDesc = args['divDesc']

    divisi = division()
    updDiv = divisi.updated(divNo, deptNo, divName, divDesc)
    if updDiv:
        response = {
            'code': 200,
            'message': 'Data Success Add to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed add to System'
        }
        return json.dumps(response)


# page main client
@app.route("/user/main/client", methods=['POST', 'GET'])
def userMainHome():
    client = clients()
    clientAll = client.all()
    emp = employees()
    province = emp.province()
    return render_template('content/main-client.html', pic_name=clientAll, province=province)


# page post new client
@app.route('/user/main/project/add', methods=['POST'])
def clientAddProject():
    parse = reqparse.RequestParser()
    parse.add_argument('client_name', type=str, help='client_name')
    parse.add_argument('client_email', type=str, help='client_email')
    parse.add_argument('client_address', type=str, help='client_address')
    parse.add_argument('city', type=str, help='client city')
    parse.add_argument('client_code', type=str, help='client_code')
    parse.add_argument('pic_name', type=str, help='pic_name')
    parse.add_argument('pic_email', type=str, help='pic_email')
    parse.add_argument('pic_phone', type=str, help='pic_phone')

    args = parse.parse_args()
    client_name = args['client_name']
    client_email = args['client_email']
    client_address = args['client_address']
    city = args['city']
    client_code = args['client_code']
    pic_name = args['pic_name']
    pic_email = args['pic_email']
    pic_phone = args['pic_phone']

    client = clients()
    clientAdd = client.addClient(client_name, client_email, client_address, city, pic_name, pic_phone, pic_email, client_code)
    if clientAdd == 0:
        response = {
            'code': 200,
            'message': "Succes add data to System"
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Failed add data to System'
        }
        return json.dumps(response)


# page edit client
@app.route("/user/edit/client")
def userEditClient():
    return render_template('content/edit-client.html')


# page main client
@app.route("/user/main/clientlist")
def userMainHomeList():
    return render_template('content/main-clientlist.html')


# page detail client
@app.route("/user/detail/edit/<clientid>")
def userClientDetail(clientid):
    client_customer = clients()
    getDetClient = client_customer.detail(clientid)
    getProjectClient = client_customer.listAllClient(clientid)
    return render_template('content/detail-client.html', getDetClient=getDetClient, getProjectClient=getProjectClient)


# page edit client
@app.route("/user/client/edit")
def userClientEdit():
    return render_template('content/edit-profile.html')


# page main project
@app.route("/project/main")
def mainProject():
    project = project_list()
    listProject = project.listAllProject()
    client = project.getClient()
    pm = project.getProjectManager()
    member = project.getMember()
    return render_template('content/main-project.html', client=client, pm=pm, listProject=listProject, member=member)


# page get client code
@app.route("/project/getclient/<clientcode>")
def getClient(clientcode):
    project = project_list()
    clientCode = project.getClientCode(clientcode)
    countProject = project.getCountProject(clientcode)
    code = clientCode[0]['client_code']
    auto_increment = countProject + 1
    year = datetime.now().year
    concatString = "{0:0>4}".format(auto_increment)
    pid = "7" + code + str(year) + concatString
    return json.dumps(pid)


@app.route('/project/add')
def addProject():
    project = project_list()
    client = project.getClient()
    pm = project.getProjectManager()
    return render_template('content/add-project.html', client=client, pm=pm)


# Parameter to upload file
basedir = os.path.abspath(os.curdir)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
# end parameter


@app.route("/project/add/post", methods=['POST'])
def upFile():
    pid = request.form['pid']
    client_name = request.form['client_name']
    project_name = request.form['project_name']
    project_manager = request.form['project_manager']
    start_project = request.form['start_project']
    project_start = datetime.strptime(start_project, '%d/%m/%Y').strftime('%Y-%m-%d')
    end_project = request.form['end_project']
    project_end = datetime.strptime(end_project, '%d/%m/%Y').strftime('%Y-%m-%d')
    mandays = request.form['mandays']
    priority = request.form['priority']
    files = request.files['file_doc']
    desc = request.form['desc']

    print start_project, end_project

    if files and allowed_file(files.filename) :
        filename = secure_filename(files.filename)
        fileSplit = filename.split(".")
        nama_file = pid+"_NEW_PROJECT"
        fileUpload = nama_file+"."+fileSplit[1]
        updir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        files.save(os.path.join(updir, fileUpload))
        fileFullPath = os.path.join(updir, fileUpload)
        file_size = os.path.getsize(os.path.join(updir, fileUpload))
        if os.path.exists(fileFullPath):
            addNewProject = project_list()
            newProject = addNewProject.addProject(client_name, project_name, mandays, project_start, project_end, pid, priority, project_manager, desc, fileUpload, file_size)
            if newProject == 0:
                return "Success to Database"
            else:
                os.remove(os.path.join(updir, fileUpload))
                return "Failed to Database"
    else:
        return 'Format File Not Supported'


# page edit project
@app.route("/project/edit/detail/<projectid>")
def editProject(projectid):
    proj = projectApp()
    getClientName = proj.getClientName()
    getpmName = proj.getpmName()
    getDetailProject = proj.getDetailProject(projectid)
    return render_template('content/edit-project.html', getClientName=getClientName, getpmName=getpmName, getDetailProject=json.dumps(getDetailProject))


# page view detail project
@app.route("/project/view/detail/<projectid>")
def viewDetailProject(projectid):
    project = project_list()
    titleNdesc = project.titleNdesc(projectid)
    detailProject = project.projectDetail(projectid)
    project_manager = project.getPM(projectid)
    project_team = project.getTeamProject(projectid)
    all_team = project.getAllTeamProject()
    client = clients()
    getTask = client.getTaskProject(projectid)
    getDoc = client.getDocumentProject(projectid)
    return render_template('content/detail-projectview.html', titleNdesc=titleNdesc, detailProject=detailProject, project_manager=project_manager, project_team=project_team, all_team=all_team, project_id=projectid, getTask=getTask, getDoc=getDoc)


@app.route("/project/edit/detail", methods=['POST'])
def projectEditProject():
    parse = reqparse.RequestParser()
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('project_name', type=str, help='project_name')
    parse.add_argument('pm', type=str, help="pm")
    parse.add_argument('project_start', type=str, help="project_start")
    parse.add_argument('project_end', type=str, help="project_end")
    parse.add_argument('mandays', type=str, help="mandays")
    parse.add_argument('priority', type=str, help="priority")
    parse.add_argument('desc', type=str, help="desc")
    args = parse.parse_args()

    project_id = args['project_id']
    project_name = args['project_name']
    pm = args['pm']
    project_start = args['project_start']
    project_end = args['project_end']
    mandays = args['mandays']
    priority = args['priority']
    desc = args['desc']

    date_start = datetime.strptime(str(project_start), '%d/%m/%Y').strftime('%Y-%m-%d')
    date_end = datetime.strptime(str(project_end), '%d/%m/%Y').strftime('%Y-%m-%d')

    proj = projectApp()
    updProject = proj.projectDetailUpdate(project_id, project_name, pm, date_start, date_end, mandays, priority, desc)
    if updProject:
        response = {
            'code': 200,
            'message': "Success Update to system"
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': "Failed Update to system"
        }
        return json.dumps(response)


# page to get assign_team_project
@app.route("/project/assign/members", methods=['POST'])
def projectMembers():
    parse = reqparse.RequestParser()
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('assign_user', type=str, help='assign_user')
    parse.add_argument('unassign_user', type=str, help="unassign_user")
    args = parse.parse_args()

    project_id = args['project_id']
    assign_user = args['assign_user']
    unassign_user = args['unassign_user']
    to_jsonAssignUser = json.loads(assign_user)
    to_jsonUnassignUser = json.loads(unassign_user)
    project = projectApp()
    teamProject = project.assign_teamProject(project_id, to_jsonAssignUser, to_jsonUnassignUser)
    return teamProject


# page delete team_project
@app.route("/project/remove/teamproject", methods=['POST'])
def removeTeamProject():
    parse = reqparse.RequestParser()
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('employee_id', type=str, help='employee_id')

    args = parse.parse_args()
    project_id = args['project_id']
    employee_id = args['employee_id']

    project = projectApp()
    removeUser = project.removeTeam(project_id, employee_id)
    if removeUser == 0:
        sendMail = project.mail_sending_remove(project_id, employee_id)
        return "Success"
    else:
        return "Failed"


# page add team_project
@app.route("/project/add/teamproject", methods=['POST'])
def addTeamProject():
    parse = reqparse.RequestParser()
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('employee_id', type=str, help='employee_id')

    args = parse.parse_args()
    project_id = args['project_id']
    employee_id = args['employee_id']
    project = projectApp()
    addUser = project.addTeam(project_id, employee_id)
    print project_id, employee_id
    if addUser == 0:
        sendMail = project.mail_sending(project_id, employee_id)
        return "Success"
    else:
        return "Failed"


# page approve project
@app.route("/project/approve")
def projectApprove():
    project = projectApp()
    listNewProject = project.new_project()
    return render_template('content/approve-project.html', listNewProject=listNewProject)


# page approve project Detail
@app.route("/project/approve/detail/<projectid>")
def projectApproveDet(projectid):
    project = project_list()
    client = project.getClient()
    pm = project.getProjectManager()
    detProject = projectApp()
    listDetProject = detProject.projectApproveDet(projectid)
    return render_template('content/approve-project-detail.html', listDetProject=json.dumps(listDetProject), client=client, pm=pm)


# page approval project
@app.route("/project/approve/data", methods=['POST'])
def projectApproveData():
    parse = reqparse.RequestParser()
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('startDate', type=str, help='Start Project')
    parse.add_argument('endDate', type=str, help='End Project')
    parse.add_argument('priority', type=str, help='Project Priority')
    parse.add_argument('project_status', type=str, help='project_status')
    args = parse.parse_args()

    project_id = args['project_id']
    startDate = args['startDate']
    dateStart = datetime.strptime(startDate, '%d/%m/%Y').strftime('%Y-%m-%d')
    endDate = args['endDate']
    dateEnd = datetime.strptime(endDate, '%d/%m/%Y').strftime('%Y-%m-%d')
    priority = args['priority']
    project_status = args['project_status']

    projectUpd = projectApp()
    approve = projectUpd.projectApproveUpd(project_id, dateStart, dateEnd, priority, project_status)
    if approve:
        response = {
            'code': 200,
            'Message': 'Data Updated to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'Message': 'Data Failed Update to System'
        }
        return json.dumps(response)


# page document project
@app.route("/project/document")
def projectDoc():
    project_doc = tasks()
    getData = project_doc.getDocumentproject()
    return render_template('content/doc-project.html', getData=getData)


# page task list
@app.route("/project/task/all")
def projectTaskList():
    task = tasks()
    taskAll = task.getTaskAll()
    return render_template('content/list-task.html', taskAll=taskAll)


# page task list on going
@app.route("/project/task/ongoing")
def projectTaskListOnGoing():
    task = tasks()
    taskOnGoing = task.getTaskOnGoing()
    return render_template('content/list-task-ongoing.html', taskAll=taskOnGoing)


# page task view detail
@app.route("/project/task/detail/<taskid>")
def projectTaskDetail(taskid):
    task = tasks()
    viewDetail = task.taskDetail(taskid)
    empTaskAssign = task.getTaskAssign()
    taskStatus = task.getTaskStatus()
    doc = task.getDocument(taskid)
    return render_template('content/detail-taskview.html', viewDetail=viewDetail, empTaskAssign=empTaskAssign, taskStatus=taskStatus, doc=doc)


# page update task detail desc and date
@app.route("/project/task/update/detail", methods=['POST'])
def projectTaskUpdateDetail():
    parse = reqparse.RequestParser()
    parse.add_argument('task_id', type=str, help='task_id')
    parse.add_argument('start_task', type=str, help='start_task')
    parse.add_argument('end_task', type=str, help='end_task')
    parse.add_argument('desc', type=str, help='desc')
    args = parse.parse_args()

    task_id = args['task_id']
    start_task = args['start_task']
    end_task = args['end_task']
    desc = args['desc']

    date_start = datetime.strptime(str(start_task), '%d/%m/%Y').strftime('%Y-%m-%d')
    date_end = datetime.strptime(str(end_task), '%d/%m/%Y').strftime('%Y-%m-%d')

    task = tasks()
    upData = task.updTaskDetail(task_id, date_start, date_end, desc)
    if upData:
        response = {
            'code': 200,
            'message': 'Success Update to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 200,
            'message': 'Success Update to System'
        }
        return json.dumps(response)


# page update task detail
@app.route("/project/task/update/note", methods=['POST'])
def taskNoteUpdate():
    parse = reqparse.RequestParser()
    parse.add_argument('task_id', type=str, help='task_id')
    parse.add_argument('note', type=str, help='note_task')
    args = parse.parse_args()

    task_id = args['task_id']
    note = args['note']

    task = tasks()
    noteUpdate = task.taskNote(task_id, note)
    if noteUpdate:
        response = {
            "code": 200,
            "Message": "Update Success"
        }
        return json.dumps(response)
    else:
        response = {
            "code": 500,
            "Message": "Update Failed"
        }
        return json.dumps(response)


# page to search validate employee assign task
@app.route("/project/task/getassign/<taskid>")
def projectgetAssignTask(taskid):
    task = tasks()
    getEmpAssign = task.getAssignTaskEmp(taskid)
    return json.dumps(getEmpAssign)


# page get team project
@app.route("/project/task/teamproject/<projectid>")
def projectTaskTeamproject(projectid):
    task = tasks()
    getTeamAssignProject = task.getTeamProject(projectid)
    return json.dumps(getTeamAssignProject)


# page to assign and unassign task member
@app.route("/project/task/assign", methods=['POST'])
def projectTaskAssign():
    parse = reqparse.RequestParser()
    parse.add_argument('task_id', type=str, help='task_id')
    parse.add_argument('assign', type=str, help='assign')
    parse.add_argument('unassign', type=str, help='unassign')

    args = parse.parse_args()
    task_id = args['task_id']
    assign = args['assign']
    unassign = args['unassign']

    task = tasks()
    addAssign = task.addAssignTaskEmp(task_id, assign, unassign)
    print addAssign
    if 'failed' not in addAssign:
        response = {
            'code': 200,
            'message': 'Data Success Update to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed Update to System'
        }
        return json.dumps(response)


# page to get document upload
@app.route("/project/task/getdocument/<taskid>/<mastertaskid>")
def projectTaskgetDoc(mastertaskid, taskid):
    task = tasks()
    getDocName = task.getDocTask(mastertaskid, taskid)
    return json.dumps(getDocName)


# page to update task
@app.route("/project/task/update/status", methods=['POST'])
def projectTaskUpdStatus():
    parse = reqparse.RequestParser()
    parse.add_argument('task_id', type=str, help='task_id')
    parse.add_argument('task_status', type=str, help='task_status')
    parse.add_argument('taskIncrement', type=str, help='taskIncrement')
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('master_task', type=str, help='master_task')
    args = parse.parse_args()

    task_id = args['task_id']
    task_status = args['task_status']
    taskIncrement = args['taskIncrement']
    project_id = args['project_id']
    master_task = args['master_task']


    task = tasks()
    updateTask = task.updateTaskStatus(task_id, task_status, taskIncrement, project_id, master_task)

    if updateTask == 4:
        response = {
            'code': 200,
            'Message': "Success Update to System"
        }

        return json.dumps(response)
    elif updateTask == 3:
        response = {
            'code': 204,
            'Message': 'update current task unsuccessfully'
        }
        return json.dumps(response)
    elif updateTask == 2:
        response = {
            'code': 210,
            'message': 'next task belum di input'
        }
        return json.dumps(response)
    elif updateTask == 1:
        response = {
            'code': 211,
            'message': 'document belum lengkap'
        }
        return json.dumps(response)


# page insert task to system
@app.route("/project/task/insert", methods=['POST'])
def taskInsert():
    parse = reqparse.RequestParser()
    parse.add_argument('project_id', type=str, help='project_id')
    parse.add_argument('task_startDate', type=str, help='task_startDate')
    parse.add_argument('task_endDate', type=str, help='task_endDate')
    parse.add_argument('task_target', type=str, help='task_target')
    parse.add_argument('task_id', type=str, help='task_id')
    parse.add_argument('task_description', type=str, help='task_description')
    parse.add_argument('assign_array', type=str, help='assign_array')
    parse.add_argument('incremental', type=str, help='incremental')
    args = parse.parse_args()

    project_id = args['project_id']
    task_startDate = args['task_startDate']
    task_endDate = args['task_endDate']
    task_target = args['task_target']
    task_id = args['task_id']
    task_description = args['task_description']
    assign_array = args['assign_array']
    incremental = args['incremental']
    member_split = assign_array.split(',')

    start_date = datetime.strptime(task_startDate, '%d/%m/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(task_endDate, '%d/%m/%Y').strftime('%Y-%m-%d')
    target_date = datetime.strptime(task_target, '%d/%m/%Y').strftime('%Y-%m-%d')


    task = tasks()
    addTask = task.taskAdd(project_id, start_date, end_date, target_date, task_id, task_description, incremental, member_split)
    if addTask == 0:
        response = {
            'code': 200,
            'message': "Success add to System"
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': "Failed add to System"
        }
        return json.dumps(response)


# page add task
@app.route("/project/task/add")
def projectTaskAdd():
    task = tasks()
    allClient = task.getClient()
    status = task.getProjectStatus()
    return render_template('content/add-task.html', allClient=allClient, status=status)


# page detail get pid
@app.route("/projectid/detail/<pid>")
def projectPid(pid):
    task = tasks()
    allPid = task.getPid(pid)
    return json.dumps(allPid)


# Page get detail task name
@app.route("/task/project/<projectid>/<categoryid>")
def taskProjectAdd(projectid, categoryid):
    task = tasks()
    getTask = task.getTaskName(projectid, categoryid)
    return json.dumps(getTask)


# page to get incremental task project
@app.route("/task/project/increment/<taskname>")
def taskProjectIncrement(taskname):
    task = tasks()
    getTaskCode = task.getTaskIncremental(taskname)
    return json.dumps(getTaskCode)


# page get team project assign
@app.route("/project/team/<projectid>")
def projectTeam(projectid):
    task = tasks()
    getTeamProject = task.getTeamProject(projectid)
    return json.dumps(getTeamProject)


# page detail team project
@app.route("/project/detailteam/<teamproject_id>")
def projectTeamDetail(teamproject_id):
    task = tasks()
    getTeamDetail = task.teamProjectDetail(teamproject_id)
    return json.dumps(getTeamDetail)


# page edit task
@app.route("/project/task/edit/<taskid>")
def projectTaskEdit(taskid):
    task = tasks()
    getUpdateTask = task.getDetailUpdateTask(taskid)
    return render_template('content/edit-task.html', getUpdateTask=json.dumps(getUpdateTask))


# page update task
@app.route("/task/update", methods=['POST'])
def taskUpdateDetail():
    parse = reqparse.RequestParser()
    parse.add_argument('task_id', type=str, help='task_id')
    parse.add_argument('start_date', type=str, help='start_date')
    parse.add_argument('end_date', type=str, help='end_date')
    parse.add_argument('desc', type=str, help='desc')


    args = parse.parse_args()

    task_id = args['task_id']
    start_date = args['start_date']
    end_date = args['end_date']
    desc = args['desc']

    date_start = datetime.strptime(str(start_date), '%d/%m/%Y').strftime('%Y-%m-%d')
    date_end = datetime.strptime(str(end_date), '%d/%m/%Y').strftime('%Y-%m-%d')
    task = tasks()
    updData = task.updTaskDetail(task_id, date_start, date_end, desc)
    if updData:
        response = {
            'code': 200,
            'message': 'Success Update'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Failed Update'
        }
        return json.dumps(response)

# page time sheet
@app.route("/project/timesheet")
def projectTimesheet():
    return render_template('content/time-sheet.html')


# page problem all
@app.route("/problem/all")
def problemAll():
    problem = problem_logs()
    getAllProblem = problem.getSummaryProblem()
    return render_template('content/problem-log.html', getAllProblem=getAllProblem)


# page problem add
@app.route("/problem/add")
def problemAdd():
    problemLog = problem_logs()
    getClientProject = problemLog.getClientName()
    return render_template('content/add-problem-log.html', getClientProject=getClientProject)


# page to add problem log
@app.route('/problem/add/new', methods=['POST'])
def problemAddNew():
    parse = reqparse.RequestParser()
    parse.add_argument('client_id', type=str, help='client_id')
    parse.add_argument('prl_pid', type=str, help='prl_pid')
    parse.add_argument('taskname', type=str, help='taskname')
    parse.add_argument('start_date', type=str, help='start_date')
    parse.add_argument('end_date', type=str, help='end_date')
    parse.add_argument('target_date', type=str, help='target_date')
    parse.add_argument('array_assign', type=str, help='array_assign')
    parse.add_argument('description', type=str, help='description')
    args = parse.parse_args()

    client_id = args['client_id']
    prl_pid = args['prl_pid']
    taskname = args['taskname']
    start_date = args['start_date']
    end_date = args['end_date']
    target_date = args['target_date']
    array_assign = args['array_assign']
    description = args['description']

    member_split = array_assign.split(',')

    date_start = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    date_end = datetime.strptime(end_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    date_target = datetime.strptime(target_date, '%d/%m/%Y').strftime('%Y-%m-%d')

    problem = problem_logs()
    addProblem = problem.addNewProblemLog(prl_pid, taskname, date_start, date_end, date_target, member_split, description)
    if addProblem:
        response = {
            'code': 200,
            'message': 'Success Add to system'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Failed Add to system'
        }
        return json.dumps(response)


# page get pid problem log
@app.route("/problem/getpid/<clientid>")
def problemGetpid(clientid):
    problemLog = problem_logs()
    getPidProject = problemLog.problemPid(clientid)
    return json.dumps(getPidProject)


# page to update note problem
@app.route("/problem/update/note", methods=['post'])
def problemUpdateNote():
    parse = reqparse.RequestParser()
    parse.add_argument('problem_id', type=str, help='problem_id')
    parse.add_argument('note', type=str, help='note_task')
    args = parse.parse_args()

    problem_id = args['problem_id']
    note = args['note']

    problem = problem_logs()
    noteUpdate = problem.updateNote(problem_id, note)
    if noteUpdate:
        response = {
            "code": 200,
            "Message": "Update Success"
        }
        return json.dumps(response)
    else:
        response = {
            "code": 500,
            "Message": "Update Failed"
        }
        return json.dumps(response)


# page problem assign
@app.route("/problem/getassign/problem/<problemid>")
def probleGetassignProblem(problemid):
    problem = problem_logs()
    getAssignProblem = problem.getAssignProblemEmp(problemid)
    print getAssignProblem
    
    
    return json.dumps(getAssignProblem)

# page problem detail
@app.route("/problem/detail/<problemid>")
def problemDetail(problemid):
    problem = problem_logs()
    getDetailProblem = problem.getDetailProblem(problemid)
    getAssignProblem = problem.getProblemAssign()
    getDoc = problem.getDocument(problemid)
    getUploadDoc = problem.documentProblem(problemid)
    return render_template('content/detail-problemview.html', getDetailProblem=getDetailProblem, getAssignProblem=getAssignProblem, getDoc=getDoc, getUploadDoc=getUploadDoc)


# page update problem log
@app.route("/project/problem/update/detail", methods=['POST'])
def projectProblemUpdateDetail():
    parse = reqparse.RequestParser()
    parse.add_argument('problem_id', type=str, help='problem_id')
    parse.add_argument('prl_name', type=str, help='prl_name')
    parse.add_argument('start_date', type=str, help='start_date')
    parse.add_argument('end_date', type=str, help='end_date')
    parse.add_argument('desc', type=str, help='desc')

    args = parse.parse_args()
    problem_id = args['problem_id']
    prl_name = args['prl_name']
    start_date = args['start_date']
    end_date = args['end_date']
    desc = args['desc']

    date_start = datetime.strptime(str(start_date), '%d/%m/%Y').strftime('%Y-%m-%d')
    date_end = datetime.strptime(str(end_date), '%d/%m/%Y').strftime('%Y-%m-%d')

    problem = problem_logs()
    updData = problem.updateProblemDetail(problem_id, prl_name, date_start, date_end, desc)
    if updData:
        response = {
            'code': 200,
            'message': 'Success Update to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Failed Update to System'
        }
        return json.dumps(response)


# page to assign and unassign task member
@app.route("/project/problem/assign", )
def projectProblemAssign():
    parse = reqparse.RequestParser()
    parse.add_argument('problemid', type=str, help='problemid')
    parse.add_argument('assign', type=str, help='assign')
    parse.add_argument('unassign', type=str, help='unassign')

    args = parse.parse_args()
    problemid = args['problemid']
    assign = args['assign']
    unassign = args['unassign']

    print problemid, assign, unassign
    problem = problem_logs()
    addAssign = problem.addAssignProblemEmp(problemid, assign, unassign)
    print addAssign
    if 'failed' not in addAssign:
        response = {
            'code': 200,
            'message': 'Data Success Update to System'
        }
        return json.dumps(response)
    else:
        response = {
            'code': 500,
            'message': 'Data Failed Update to System'
        }
        return json.dumps(response)


# page update problem task
@app.route("/problem/update/task", methods=['POST'])
def problemUpdateTask():
    parse = reqparse.RequestParser()
    parse.add_argument('problem_id', type=str, help='problem_id')
    parse.add_argument('increment_id', type=str, help='increment_id')
    parse.add_argument('master_problem', type=str, help='master_problem')

    args = parse.parse_args()
    problemid = args['problem_id']
    increment = args['increment_id']
    master_problem = args['master_problem']

    problem = problem_logs()
    updStatus = problem.updateTaskProblem(problemid, master_problem,increment)
    if updStatus == 0:
        response = {
            'code': 200,
            'message': 'Success Update problem Task'
        }
        return json.dumps(response)
    elif updStatus == 2:
        response = {
            'code': 210,
            'message': 'Document Not Complate Upload'
        }
        return json.dumps(response)
    elif updStatus == 1:
        response = {
            'code': 500,
            'message': 'Failed Update problem Task'
        }
        return json.dumps(response)


# page problem edit
@app.route("/problem/edit/")
def problemEdit(problemid):
    problem = problem_logs()
    getProblem = problem.getDetailProblemUpdate(problemid)
    return render_template('content/edit-problem.html', getProblem=json.dumps(getProblem))


# page report proyek
@app.route("/project/report/all")
def reportProject():
    report = reports()
    getReportProject = report.project()
    return render_template('content/report-proyek.html', getReportProject=getReportProject)


# page report task
@app.route("/project/report/task")
def reportTask():
    report = reports()
    getReportTask = report.task()
    return render_template('content/report-task.html', getReportTask=getReportTask)


# page report problem
@app.route("/project/report/problem")
def reportProblem():
    report = reports()
    getReportProblem = report.problem()
    return render_template('content/report-problem.html', getReportProblem=getReportProblem)


# page report audit trail
@app.route("/project/report/client")
def reportClient():
    report = reports()
    getReportClient = report.client()
    return render_template('content/report-client.html', getReportClient=getReportClient)


# page report employee
@app.route("/project/report/employee")
def reportEmp():
    report = reports()
    getReportEmployee = report.employee()
    return render_template('content/report-employee.html', getReportEmployee=getReportEmployee)


# problem page upload data
@app.route("/upload/doc/problemlog", methods=['POST'])
def uploadDocProblemlog():
    fileUpload = request.files['inputFile']
    problemid = request.form['problem_id']
    doc_code = request.form['docCode']
    updir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    allowFormat = app.config['ALLOWED_EXTENSIONS']
    nameFile = secure_filename(fileUpload.filename)
    uploadfileFormat = nameFile.split('.')

    if uploadfileFormat[1] in allowFormat:
        time = datetime.today()
        formattime = time.strftime('%d%m%Y_%H%M%S')
        nameFileFormat = uploadfileFormat[0]+"_"+formattime+"."+uploadfileFormat[1]
        fileUpload.save(os.path.join(updir, nameFileFormat))
        doc_url = os.path.join(updir, nameFileFormat)
        file_size = os.path.getsize(os.path.join(updir, nameFileFormat))

        problem = problem_logs()
        addDocProblem = problem.uploadDocument(nameFileFormat, problemid, doc_code, file_size, doc_url, uploadfileFormat[1])
        if addDocProblem:
            response = {
                'code': 200,
                'message': 'Success Upload Document to System'
            }
            return json.dumps(response)
        else:
            response = {
                'code': 500,
                'message': 'Failed Upload Document to System'
            }
            return json.dumps(response)
    else:
        response = {
            'code': 406,
            'message': 'Document Format not allowed'
        }
        return json.dumps(response)


# problem page upload data
@app.route("/upload/doc/task", methods=['POST'])
def uploadDocTask():
    fileUpload = request.files['inputFile']
    problemid = request.form['task_id']
    doc_code = request.form['docCode']
    updir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    allowFormat = app.config['ALLOWED_EXTENSIONS']
    nameFile = secure_filename(fileUpload.filename)
    uploadfileFormat = nameFile.split('.')

    if uploadfileFormat[1] in allowFormat:
        time = datetime.today()
        formattime = time.strftime('%d%m%Y_%H%M%S')
        nameFileFormat = uploadfileFormat[0]+"_"+formattime+"."+uploadfileFormat[1]
        fileUpload.save(os.path.join(updir, nameFileFormat))
        doc_url = os.path.join(updir, nameFileFormat)
        file_size = os.path.getsize(os.path.join(updir, nameFileFormat))

        task = tasks()
        addDocTask = task.uploadDocument(nameFileFormat, problemid, doc_code, file_size, doc_url, uploadfileFormat[1])
        if addDocTask:
            response = {
                'code': 200,
                'message': 'Success Upload Document to System'
            }
            return json.dumps(response)
        else:
            response = {
                'code': 500,
                'message': 'Failed Upload Document to System'
            }
            return json.dumps(response)
    else:
        response = {
            'code': 406,
            'message': 'Document Format not allowed'
        }
        return json.dumps(response)