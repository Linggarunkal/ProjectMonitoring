from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE


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
            getStatus = conn.customquery("select status_id, status_name from project_status where status_id not in ('PRST00001','PRST00002','PRST00003','PRST00008','PRST00009')")
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
            getTask = conn.customquery("select master_task_id, task_name from master_task where master_task_id not in (select master_task_id from task where project_id='"+project_id+"') and project_status_id = '"+category_id+"';")
            detail = []
            for index, list in enumerate(getTask):
                i = {
                    'master_task_id': list[0],
                    'task_name': list[1]
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

    def taskAdd(self, project_id, task_startDate, task_endDate, task_target, task_id, task_description, member_split):
        taskstatus = 'STAT00001'
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addTask = conn.customquery("call sp_add_task('"+project_id+"','"+task_startDate+"','"+task_endDate+"','"+task_target+"','"+task_id+"','"+taskstatus+"','"+task_description+"')")

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