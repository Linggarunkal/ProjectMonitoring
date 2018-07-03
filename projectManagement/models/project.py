from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE
from datetime import datetime


class project_list(object):
    def getClient(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getAllClient = conn.select('client', None, 'client_id, name')
            detailAllClient = []
            for index, list in enumerate(getAllClient):
                i = {
                    'client_id': list[0],
                    'client_name': list[1]
                }
                detailAllClient.append(i)
            return detailAllClient
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getProjectManager(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condPM = 'empTitle_id = %s'
            getAllPM = conn.select('employees', condPM, 'employee_id, firstname, lastname', empTitle_id='EMTL00003')
            detailAllPM = []
            for index, list in enumerate(getAllPM):
                i = {
                    'employee_id': list[0],
                    'firstname': list[1],
                    'lastname': list[2]
                }
                detailAllPM.append(i)
            return detailAllPM
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getClientCode(self, client_code):
        self.client_code = client_code
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condClient = 'client_id = %s'
            getClientCode = conn.select('v_client_detail', condClient, 'client_id, client_code', client_id=self.client_code)
            detailClientCode = []
            for index, list in enumerate(getClientCode):
                i = {
                    'client_id': list[0],
                    'client_code': list[1]
                }
                detailClientCode.append(i)
            return detailClientCode
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getCountProject(self, clientid):
        self.clientid = clientid
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condClientid = 'client_id = %s'
            getCount = conn.select('project', condClientid, 'client_id, project_id', client_id=self.clientid)
            return len(getCount)
        except Exception as e:
            return "Error Database: %s" % str(e)

    def addProject(self, client_id, name, mandays, startDate, endDate, pid, priority, employee_id, description, doc_project, doc_size):
        self.client_id = client_id
        self.name = name
        self.mandays = mandays
        self.startDate = startDate
        self.endDate = endDate
        self.pid = pid
        self.priority = priority
        self.employee_id = employee_id
        self.description = description
        self.doc_project = doc_project
        self.doc_size = doc_size
        print self.startDate
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            projectAdd = conn.insert('project', client_id=self.client_id, name=self.name, mandays=self.mandays, startDate=self.startDate, endDate=self.endDate, pid=self.pid, priority=self.priority, employee_id=self.employee_id, description=self.description, doc_project=self.doc_project, doc_size=self.doc_size)
            print projectAdd
            if projectAdd == 0:
                return 0
            else:
                return 1
        except Exception as e:
            return "Error Database: %s" % str(e)

    def listAllProject(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getAllProject = conn.select('v_project_detail', None, 'left(project_name, 15), client_name, status_name, left(description, 40), enddate, firstname, lastname, project_id')
            detAllProject = []
            for index, list in enumerate(getAllProject):
                i = {
                    'project_name': list[0],
                    'client_name': list[1],
                    'status_name': list[2],
                    'desc': list[3],
                    'deadline': list[4],
                    'firstname': list[5],
                    'lastname': list[6],
                    'project_id': list[7]
                }
                detAllProject.append(i)
            return detAllProject
        except Exception as e:
            return "Error Database: %s" % str(e)

    def titleNdesc(self, project_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            detail = conn.select('v_project_detail', cond, 'project_name, description', project_id=project_id)
            getDetail = []
            for index, list in enumerate(detail):
                i = {
                    'project_name': list[0],
                    'desc': list[1]
                }
                getDetail.append(i)
                return getDetail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def projectDetail(self, project_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            detail = conn.select('v_project_detail', cond, 'client_name, pid, mandays, startDate, endDate, priority, project_id', project_id=project_id)
            getDetail = []
            for index, list in enumerate(detail):
                i = {
                    'client_name': list[0],
                    'pid': list[1],
                    'mandays': list[2],
                    'startDate': list[3],
                    'endDate': list[4],
                    'priotiry': list[5],
                    'project_id': list[6]
                }
                getDetail.append(i)
            return getDetail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getPM(self, project_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            detail = conn.select('v_project_detail', cond, 'project_manager, firstname, lastname', project_id=project_id)
            getDetail = []
            for index, list in enumerate(detail):
                i = {
                    'project_manager': list[0],
                    'firstname': list[1],
                    'lastname': list[2]
                }
                getDetail.append(i)
            return getDetail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getMember(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            detail = conn.select('v_employee_team_project', None, 'initial, employee_id, email, firstname, lastname, project_id')
            getDetail = []
            for index, list in enumerate(detail):
                i = {
                    'initial': list[0],
                    'employee_id': list[1],
                    'email': list[2],
                    'firstname': list[3],
                    'lastname': list[4],
                    'project_id': list[5]
                }
                getDetail.append(i)
            return getDetail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTeamProject(self, project_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            detail = conn.select('v_employee_team_project', cond, 'employee_id, firstname, lastname, email, title_name, initial', project_id=project_id)
            getDetail = []
            for index, list in enumerate(detail):
                i = {
                    'employee_id': list[0],
                    'firstname': list[1],
                    'lastname': list[2],
                    'email': list[3],
                    'title_name': list[4],
                    'initial': list[5]
                }
                getDetail.append(i)
            return getDetail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getAllTeamProject(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            detail = conn.select('v_employee_team_project', None, 'employee_id, firstname, lastname, email, title_name, initial, assign_project_user, project_id')
            getDetail = []
            for index, list in enumerate(detail):
                i = {
                    'employee_id': list[0],
                    'firstname': list[1],
                    'lastname': list[2],
                    'email': list[3],
                    'title_name': list[4],
                    'initial': list[5],
                    'assign_project_user': list[6],
                    'project_id': list[7]
                }
                getDetail.append(i)
            return getDetail
        except Exception as e:
            return "Error Database: %s" % str(e)

class projectApp(object):
    def new_project(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            status_code = 'PRST00001'
            condNewProject = 'status_id = %s'
            getNewProject = conn.select('v_project_detail', condNewProject, 'project_id, client_name, project_name, pid, startDate, endDate, mandays, status_name', status_id=status_code)
            detNewProject = []
            for index, list in enumerate(getNewProject):
                i = {
                    'project_id': list[0],
                    'client_name': list[1],
                    'project_name': list[2],
                    'pid': list[3],
                    'startDate': list[4],
                    'endDate': list[5],
                    'mandays': list[6],
                    'status_name': list[7]
                }
                detNewProject.append(i)
            return detNewProject
        except Exception as e:
            return "Error Database: %s" % str(e)

    def projectApproveDet(self, project_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condProject = 'project_id = %s'
            getDetProject = conn.select('v_project_detail', condProject, '*', project_id=project_id)
            detProject = []
            for index, list in enumerate(getDetProject):

                i = {
                    'project_id': list[0],
                    'client_id': list[1],
                    'client_name': list[2],
                    'project_name': list[3],
                    'mandays': list[4],
                    'startDate': list[5],
                    'endDate': list[6],
                    'status_id': list[7],
                    'status_name': list[8],
                    'pid': list[10],
                    'project_manager': list[11],
                    'description': list[16],
                    'doc_project': list[17],
                    'doc_size': list[18],
                    'priority': list[19]
                }
                detProject.append(i)
            return detProject
        except Exception as e:
            return "Error Database: %s" % str(e)

    def projectApproveUpd(self, project_id, startDate, endDate, priority, status_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condProject = 'project_id = %s'
            updProject = conn.update('project', condProject, project_id, startDate=startDate, endDate=endDate, priority=priority, status_id=status_id)
            if updProject:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def assign_teamProject(self, project_id, assign_user, unassign_user):
        try:
            add = self.addTeamProject(project_id, assign_user)
            remove = self.decreaseTeamProject(project_id, assign_user)
            print add, remove
            return "testing"
        except Exception as e:
            return "Error Database: %s" % str(e)

    def decreaseTeamProject(self, project_id, unassign_user):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condProject = 'project_id = %s'
            getListExisting = conn.select('v_employee_team_project', condProject, 'employee_id, TeamProject_ID', project_id=project_id)

            # from assign to unassign
            x = 0
            while (x < len(getListExisting)):
                if getListExisting[x][0] not in unassign_user:
                    decrease = conn.execquery('delete from team_project where project_id = "'+project_id+'" and employee_id = "'+getListExisting[x][0]+'"')
                    print decrease
                    if decrease > 0:
                        return 0
                    else:
                        return 1
                x += 1
        except Exception:
            return 1
    # ini process assign employee to project
    def addTeamProject(self, project_id, assign_user):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condProject = 'project_id = %s'
            getListExisting = conn.select('v_employee_team_project', condProject, 'employee_id, TeamProject_ID',project_id=project_id)
            # from unasign to assign
            y = 0
            while (y < len(assign_user)):
                x = 0
                userinSystem = []
                while (x < len(getListExisting)):
                    userinSystem.append(getListExisting[x][0])
                    x += 1
                if assign_user[y] not in userinSystem:
                    addMember = conn.insert('team_project', project_id=project_id, employee_id=assign_user[y])
                    if addMember == 0:
                        return 0
                    else:
                        return 1
                y += 1
        except Exception:
            return 1

    def removeTeam(self, project_id, employee_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            delete = conn.execquery('delete from team_project where project_id = "'+project_id+'" and employee_id="'+employee_id+'";')
            if delete > 0:
                return 0
            else:
                return 1
        except Exception as e:
            return "Error Database: %s" % str(e)

    def addTeam(self, project_id, employee_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            checkUser = conn.execquery('select project_id, employee_id from team_project where project_id = "'+project_id+'" and employee_id = "'+employee_id+'";')
            print checkUser
            if checkUser == 0:
                add = conn.insert('team_project', project_id=project_id, employee_id=employee_id)
                if add == 0:
                    return 0
                else:
                    return 1
            else:
                return 1
        except Exception as e:
            return "Error Database: %s" % str(e)

    # for edit project
    def getClientName(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('client', None, 'client_id, name')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'client_id': list[0],
                    'name': list[1]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getpmName(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = "empTitle_id = %s"
            getData = conn.select('employees', cond, 'employee_id, firstname, lastname, emptitle_id', emptitle_id='EMTL00003')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'employee_id': list[0],
                    'firstname': list[1],
                    'lastname': list[2],
                    'emptitle_id': list[3]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDetailProject(self, projectid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            getData = conn.select('project', cond, 'project_id, client_id, name, mandays, startDate, endDate, pid, priority, employee_id, description', project_id=projectid)
            detail = []
            for index, list in enumerate(getData):
                date_start = datetime.strptime(str(list[4]), '%Y-%m-%d').strftime('%d/%m/%Y')
                date_end = datetime.strptime(str(list[5]), '%Y-%m-%d').strftime('%d/%m/%Y')
                i = {
                    'project_id': list[0],
                    'client_id': list[1],
                    'name': list[2],
                    'mandays': list[3],
                    'startDate': date_start,
                    'endDate': date_end,
                    'pid': list[6],
                    'priority': list[7],
                    'employee_id': list[8],
                    'description': list[9]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def projectDetailUpdate(self, project_id, project_name, pm, project_start, project_end, mandays, priority, desc):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = "project_id = %s"
            updData = conn.update('project', cond, project_id, name=project_name, mandays=mandays, startDate=project_start, endDate=project_end, priority=priority, employee_id=pm, description=desc)
            if updData:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)