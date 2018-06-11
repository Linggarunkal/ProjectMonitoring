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