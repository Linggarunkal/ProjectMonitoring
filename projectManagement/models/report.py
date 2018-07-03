from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE


class reports(object):
    def project(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_detail_project_report', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'project_id': list[0],
                    'client_id': list[1],
                    'client_name': list[2],
                    'project_name': list[3],
                    'startDate': list[4],
                    'endDate': list[5],
                    'pid': list[6],
                    'status_project': list[7],
                    'task_name': list[8],
                    'project_status_id': list[9],
                    'status_name': list[10]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def task(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_detail_project_task', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'task_id': list[0],
                    'project_id': list[1],
                    'project_name': list[2],
                    'task_startDate': list[3],
                    'task_enddate': list[4],
                    'master_task_id': list[5],
                    'task_name': list[6],
                    'taskstatus_id': list[7],
                    'status_name': list[8],
                    'project_status_id': list[9],
                    'category': list[10]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def problem(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_detail_project_problem', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'problem_log_id': list[0],
                    'project_id': list[1],
                    'client_id': list[2],
                    'client_name': list[3],
                    'project_name': list[4],
                    'problem_name': list[5],
                    'start_date': list[6],
                    'end_date': list[7],
                    'master_problem_id': list[8],
                    'problem_task': list[9]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def employee(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_detail_project_employee', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'nik': list[0],
                    'firstname': list[1],
                    'lastname': list[2],
                    'division_id': list[3],
                    'division_name': list[4],
                    'department_id': list[5],
                    'department_name': list[6],
                    'emptitle_id': list[7],
                    'title_name': list[8],
                    'join_date': list[9]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def client(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('client', None, 'name, client_code, email, pic_name, pic_email')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'client_name': list[0],
                    'client_code': list[1],
                    'client_email': list[2],
                    'pic_name': list[3],
                    'pic_email': list[4]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def homeProject(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getProject = conn.execquery('select * from project')
            return getProject
        except Exception as e:
            return "Error Database: %s" % str(e)

    def homeClient(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getClient = conn.execquery('select * from client')
            return getClient
        except Exception as e:
            return "Error Database: %s" % str(e)

    def homeTask(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getTask = conn.execquery('select * from task')
            return getTask
        except Exception as e:
            return "Error Database: %s" % str(e)

    def homeTaskPending(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getTaskPending = conn.execquery('select * from task where taskstatus_id not in ("STAT00004")')
            return getTaskPending
        except Exception as e:
            return "Error Database: %s" % str(e)

    def homeEmployee(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getEmployee = conn.execquery('select * from employees')
            return getEmployee
        except Exception as e:
            return "Error Database: %s" % str(e)