from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE
import json


class problem_logs(object):
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

    def problemPid(self, clientid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'client_id = %s'
            getData = conn.select('v_project_status_position', cond, '*', client_id=clientid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'task_id': list[0],
                    'project_id': list[1],
                    'client_id': list[2],
                    'name': list[3],
                    'pid': list[4],
                    'master_task_id': list[5],
                    'task_name': list[6],
                    'taskstatus_id': list[7]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)
