from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE


class clients(object):
    def all(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getClientAll = conn.select('v_client_detail', None, 'client_id, name, email, address, pic_name')
            detClientAll = []
            for index, list in enumerate(getClientAll):
                i = {
                    'client_id': list[0],
                    'name': list[1],
                    'email': list[2],
                    'address': list[3],
                    'pic_name': list[4]
                }
                detClientAll.append(i)
            return detClientAll
        except Exception as e:
            return "Error Database: %s" % str(e)

    def detail(self, clientid):
        self.clientid = clientid
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condClient = 'client_id = %s'
            getClient = conn.select('v_client_detail', condClient, '*', client_id = self.clientid)
            detClient = []
            for index, list in enumerate(getClient):
                i = {
                    'client_id': list[0],
                    'name': list[1],
                    'email': list[2],
                    'address': list[3],
                    'city_code': list[4],
                    'city_name': list[5],
                    'pic_name': list[6],
                    'pic_number': list[7],
                    'pic_email': list[8],
                    'client_code': list[9]
                }
                detClient.append(i)
            return detClient
        except Exception as e:
            return "Error Database: %s" % str(e)

    def addClient(self, name, email, address, city_code, pic_name, pic_number, pic_email, client_code):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            add = conn.insert('client', name=name, email=email, address=address, city_code=city_code, pic_name=pic_name, pic_number=pic_number, pic_email=pic_email, client_code=client_code)
            if add == 0:
                return 0
            else:
                return 1
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getTaskProject(self, projectid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            getData = conn.select('v_task_project', cond, '*', project_id=projectid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'project_id': list[0],
                    'master_task_id': list[1],
                    'task_name': list[2],
                    'taskstatus_id': list[3],
                    'status_name': list[4]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDocumentProject(self, projectid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'project_id = %s'
            getData = conn.select('v_document_project', cond, '*', project_id=projectid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'document_type_id': list[0],
                    'document_name': list[1],
                    'task_id': list[2],
                    'project_id': list[3],
                    'document_size': list[4],
                    'document_filename': list[5],
                    'document_extention': list[6]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def listAllClient(self, clientid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'client_id = %s'
            getAllProject = conn.select('v_project_detail', cond, 'left(project_name, 15), client_name, status_name, left(description, 40), enddate, firstname, lastname, project_id', client_id=clientid)
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