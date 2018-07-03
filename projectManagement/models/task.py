from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE
import json
from datetime import datetime

class tasks(object):
    def getClient(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            clientAll = conn.select('client', None, 'client_id, name')
            detClient = []
            for index, list in enumerate(clientAll):
                i = {
                    'client_id': list[0],
                    'client_name': list[1]
                }
                detClient.append(i)
            return detClient
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getPid(self, client_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'client_id = %s'
            pid = conn.select('project', cond, 'project_id, client_id, pid', client_id=client_id)
            detailPid = []
            for index, list in enumerate(pid):
                i = {
                    'project_id': list[0],
                    'client_id': list[1],
                    'pid': list[2]
                }
                detailPid.append(i)
            return detailPid
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getProjectStatus(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getStatus = conn.customquery("select status_id, status_name from project_status where status_id not in ('PRST00001','PRST00002','PRST00003','PRST00009','PRST00010')")
            detail = []
            for index, list in enumerate(getStatus):
                i = {
                    "status_id": list[0],
                    "status_name": list[1]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskName(self, project_id, category_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getTask = conn.customquery("select master_task_id, task_name, increment_task from master_task where master_task_id not in (select master_task_id from task where project_id='"+project_id+"') and project_status_id = '"+category_id+"';")
            detail = []
            for index, list in enumerate(getTask):
                i = {
                    'master_task_id': list[0],
                    'task_name': list[1],
                    'increment_task': list[2]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskIncremental(self, taskname):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'master_task_id = %s'
            getData = conn.select('master_task', cond, 'master_task_id, task_name, increment_task', master_task_id=taskname)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'master_task_id': list[0],
                    'task_name': list[1],
                    'increment_task': list[2]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTeamProject(self, project_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            getTeam = conn.select('v_employee_assign_project', cond, '*', project_id=project_id)
            detail = []
            for index, list in enumerate(getTeam):
                i = {
                    'teamproject_id': list[0],
                    'employee_id': list[1],
                    'email': list[2],
                    'firstname': list[3],
                    'lastname': list[4],
                    'title_name': list[5],
                    'project_id': list[6],
                    'initial': list[7]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def teamProjectDetail(self, teamproject_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'teamproject_id = %s'
            getTeamDetail = conn.select('v_employee_assign_project', cond, '*', teamproject_id=teamproject_id)
            detail = []
            for index, list in enumerate(getTeamDetail):
                i = {
                    'teamproject_id': list[0],
                    'employee_id': list[1],
                    'email': list[2],
                    'firstname': list[3],
                    'lastname': list[4],
                    'title_name': list[5],
                    'project_id': list[6],
                    'initial': list[7]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def taskAdd(self, project_id, task_startDate, task_endDate, task_target, task_id, task_description, incremental, member_split):
        taskstatus = 'STAT00001'
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addTask = conn.customquery("call sp_add_task('"+project_id+"','"+task_startDate+"','"+task_endDate+"','"+task_target+"','"+task_id+"','"+taskstatus+"','"+task_description+"','"+incremental+"')")

            if len(addTask) > 0:
                start = 0
                taskCode = addTask[0][0]
                insertStatus = []
                while (start < len(member_split)):
                    taskAssign = member_split[start]
                    addAssignTask = conn.insert('task_assign', task_id=taskCode, teamproject_id=taskAssign)
                    insertStatus.append(addAssignTask)
                    start += 1
                if 0 in insertStatus:
                    return 0
            else:
                return 1
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskAll(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_task_detail', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'task_id': list[0],
                    'project_id': list[1],
                    'pid': list[2],
                    'client_id': list[3],
                    'name_client': list[4],
                    'task_startdate': list[5],
                    'task_enddate': list[6],
                    'master_task_id': list[7],
                    'task_name': list[8],
                    'project_status_id': list[9],
                    'status_project': list[10],
                    'taskstatus_id': list[11],
                    'status_task': list[12]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskOnGoing(self):
        task_status = 'STAT00002'
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'taskstatus_id = %s'
            getData = conn.select('v_task_detail', cond, '*', taskstatus_id=task_status)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'task_id': list[0],
                    'project_id': list[1],
                    'pid': list[2],
                    'client_id': list[3],
                    'name_client': list[4],
                    'task_startdate': list[5],
                    'task_enddate': list[6],
                    'master_task_id': list[7],
                    'task_name': list[8],
                    'project_status_id': list[9],
                    'status_project': list[10],
                    'taskstatus_id': list[11],
                    'status_task': list[12]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def taskDetail(self, taskid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'task_id = %s'
            getData = conn.select('v_task_detail_view', cond, '*', task_id=taskid)
            detail = []
            for index, list in enumerate(getData):
                dateStart = list[11].strftime('%d/%m/%Y')
                dateEnd = list[12].strftime('%d/%m/%Y')
                i = {
                    'task_id': list[0],
                    'master_task_id': list[1],
                    'task_name': list[2],
                    'project_status_id': list[3],
                    'category_task': list[4],
                    'task_description': list[5],
                    'project_id': list[6],
                    'client_id': list[7],
                    'client_name': list[8],
                    'project_name': list[9],
                    'pid': list[10],
                    'task_startDate': dateStart,
                    'task_enddate': dateEnd,
                    'taskstatus_id': list[13],
                    'task_status': list[14],
                    'task_notes': list[15],
                    'task_proses_increment': list[16]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskAssign(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_task_assign_employee', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'taskassign_id': list[0],
                    'task_id': list[1],
                    'teamproject_id': list[2],
                    'employee_id': list[3],
                    'nik': list[4],
                    'firstname': list[5],
                    'lastname': list[6],
                    'emptitle_id': list[7],
                    'title_name': list[8],
                    'initial': list[9]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def taskNote(self, taskid, note):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'task_id = %s'
            updData = conn.update('task', cond, taskid, task_notes=note)
            if updData:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getAssignTaskEmp(self, taskid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = "task_id = %s"
            getData = conn.select("task_assign", cond, '*', task_id=taskid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'taskassign_id': list[0],
                    'task_id': list[1],
                    'teamproject_id': list[2]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def addAssignTaskEmp(self, taskid, assign, unassign):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            validate = []
            data = json.loads(assign)
            data_unassign = json.loads(unassign)
            start = 0
            # for assign new task
            # process assign new employee
            while start < len(data):
                getRowExist = conn.execquery("select * from task_assign where task_id ='"+taskid+"' and teamproject_id = '" +data[start]+"'")
                if getRowExist == 0:
                    # insert assign user
                    addNewAssign = conn.insert('task_assign', task_id=taskid, teamproject_id=data[start])
                    if addNewAssign == 0:
                        # send send email
                        # get email
                        condEmail = 'teamproject_id = %s'
                        getEmail = conn.select('v_email_assign_project', condEmail, 'firstname, lastname, email, name, pid', teamproject_id=data[start])
                        name = getEmail[0][0]+" "+getEmail[0][1]
                        email = getEmail[0][2]
                        project_name = getEmail[0][3]
                        pid = getEmail[0][4]
                        link = 'http://localhost:14045/dashboard'
                        status = 'Assign Task'
                        from email_sending import send_email

                        mail = send_email(email)
                        send = mail.nofitication(name, pid, project_name, status, link)

                        validate.append('success')
                    else:
                        validate.append('failed')
                start += 1
            # for unassign user
            # process unassign
            count = 0
            while count < len(data_unassign):
                getAssignExist = conn.execquery("select * from task_assign where task_id ='"+taskid+"' and teamproject_id='"+data_unassign[count]+"'")
                if getAssignExist == 1:
                    delAssign = conn.execquery("delete from task_assign where task_id = '"+taskid+"' and teamproject_id='"+data_unassign[count]+"'")
                    if delAssign == 1:

                        condEmail = 'teamproject_id = %s'
                        getEmail = conn.select('v_email_assign_project', condEmail,'firstname, lastname, email, name, pid', teamproject_id=data_unassign[count])
                        name = getEmail[0][0] + " " + getEmail[0][1]
                        email = getEmail[0][2]
                        project_name = getEmail[0][3]
                        pid = getEmail[0][4]
                        link = 'http://localhost:14045/dashboard'
                        status = 'Unassign Task'
                        from email_sending import send_email

                        mail = send_email(email)
                        send = mail.nofitication(name, pid, project_name, status, link)
                        validate.append('success')
                    else:
                        validate.append('failed')
                count += 1
            return validate
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDocTask(self, mastertaskid, taskid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.customquery('select ta.task_id, ta.master_task_id, dt.document_type_id, dt.document_name from task ta left join document_type dt on ta.master_task_id = dt.master_task_id where ta.task_id = "'+taskid+'" and ta.master_task_id = "'+mastertaskid+'" and dt.document_type_id not in (select document_type_id from document where task_id = "'+taskid+'");')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'task_id': list[0],
                    'master_task_id': list[1],
                    'document_type_id': list[2],
                    'document_name': list[3]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskStatus(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('status', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'taskstatus_id': list[0],
                    'Status_Name': list[1],
                    'Status_Desc': list[2]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def updateTaskStatus(self, taskid, taskStatus, taskIncrement, project_id, master_task):
        try:
            nextCountTask = int(taskIncrement)+1
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getValidation = conn.execquery('SELECT ta.task_id, ta.master_task_id, dt.document_type_id, dt.document_name FROM task ta LEFT JOIN document_type dt ON ta.master_task_id = dt.master_task_id WHERE ta.task_id = "'+taskid+'" AND ta.master_task_id = "'+master_task+'" AND dt.document_type_id NOT IN (SELECT  document_type_id FROM document WHERE task_id = "'+ taskid +'");')
            if getValidation == 0:
                checkNextTask = conn.execquery('select * from task where project_id="' + project_id + '" and task_proses_increment="' + str(nextCountTask) + '"')
                if checkNextTask == 1:
                    cond = 'task_id = %s'
                    updData = conn.update('task', cond, taskid, taskstatus_id=taskStatus)
                    if updData:
                        updNextTask = conn.execquery('update task set taskstatus_id="STAT00002" where project_id="' + project_id + '" and task_proses_increment="' + str(nextCountTask) + '"')
                        if updNextTask == 1:
                            return 4
                        else:
                            return 3
                else:
                    return 2
            else:
                return 1

        except Exception as e:
            return "Error Database: %s" % str(e)

    def uploadDocument(self, doc_name, problemid, doc_code, doc_size, doc_url, doc_extention):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addDoc = conn.insert('document', document_filename=doc_name, document_type_id=doc_code, Document_URL=doc_url, task_id=problemid, document_size=doc_size, document_extention=doc_extention)
            if addDoc == 0:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDocument(self, taskid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'task_id = %s'
            getData = conn.select('v_document_task_detail', cond, '*', task_id=taskid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'document_no': list[0],
                    'document_type_id': list[1],
                    'document_name': list[2],
                    'document_url': list[3],
                    'task_id': list[4],
                    'document_size': list[5],
                    'document_filename': list[6],
                    'document_extention': list[7]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDetailUpdateTask(self, taskid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'task_id = %s'
            getData = conn.select('v_detail_update_task', cond, '*', task_id=taskid)
            detail = []
            for index, list in enumerate(getData):
                start_date = datetime.strptime(str(list[4]), '%Y-%m-%d').strftime('%d/%m/%Y')
                end_date = datetime.strptime(str(list[5]), '%Y-%m-%d').strftime('%d/%m/%Y')
                i = {
                    'task_id': list[0],
                    'project_id': list[1],
                    'name': list[2],
                    'pid': list[3],
                    'Task_StartDate': start_date,
                    'Task_EndDate': end_date,
                    'master_task_id': list[6],
                    'task_name': list[7],
                    'task_description': list[8]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def updTaskDetail(self, task_id, start_date, end_date, desc):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'task_id = %s'
            updData = conn.update('task', cond, task_id, Task_StartDate=start_date, Task_EndDate=end_date, task_description=desc)
            if updData:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDocumentproject(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_document_detail_project', None, 'document_no, name, document_name, pid, status, client_name')
            print getData
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'document_no': list[0],
                    'project_name': list[1],
                    'document_name': list[2],
                    'pid': list[3],
                    'status': list[4],
                    'client_name': list[5]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)