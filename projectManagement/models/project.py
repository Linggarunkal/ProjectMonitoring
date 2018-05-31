from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE


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