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

    def addNewProblemLog(self, prl_pid, taskname, start_date, end_date, target_date, array_assign, description):
        try:
            master_problem = 'MSPR00001'
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addData = conn.customquery("call sp_add_problemlog('"+prl_pid+"','"+taskname+"','"+start_date+"','"+end_date+"','"+target_date+"','"+master_problem+"','"+description+"')")
            if addData > 0:
                start = 0
                problemeCode = addData[0][0]
                insertStatus = []
                while (start < len(array_assign)):
                    problemAssign = array_assign[start]
                    addAssignProblem = conn.insert('problem_assign', problem_log_id=problemeCode, teamproject_id=problemAssign)
                    insertStatus.append(addAssignProblem)
                    start += 1
                if 0 in insertStatus:
                    return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getSummaryProblem(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_problemlog_summary', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'problem_log_id': list[0],
                    'project_id': list[1],
                    'client_id': list[2],
                    'client_name': list[3],
                    'pid': list[4],
                    'problem_name': list[5],
                    'start_date': list[6],
                    'end_date': list[7],
                    'master_problem_id': list[8],
                    'status': list[9]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDetailProblem(self, problemid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'problem_log_id = %s'
            getData = conn.select('v_problemlog_detail', cond, '*', problem_log_id=problemid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'problem_log_id': list[0],
                    'project_id': list[1],
                    'project_name': list[2],
                    'client_id': list[3],
                    'client_name': list[4],
                    'pid': list[5],
                    'problem_name': list[6],
                    'start_date': list[7],
                    'end_date': list[8],
                    'target_date': list[9],
                    'master_problem_id': list[10],
                    'status_problem': list[11],
                    'description': list[12],
                    'increment_process': list[13],
                    'problem_note': list[14]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def updateNote(self, problemid, note):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'problem_log_id = %s'
            updData = conn.update('problem_log', cond, problemid, problem_note=note)
            if updData:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getAssignProblemEmp(self, problemid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = "problem_log_id = %s"
            getData = conn.select("problem_assign", cond, '*', problem_log_id=problemid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'problemassign_id': list[0],
                    'problem_log_id': list[1],
                    'teamproject_id': list[2]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getProblemAssign(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.select('v_problem_assign_employee', None, '*')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'problemassign_id': list[0],
                    'problem_log_id': list[1],
                    'teamproject_id': list[2],
                    'employee_id': list[3],
                    'email': list[4],
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

    def addAssignProblemEmp(self, problemid, assign, unassign):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            validate = []
            data = json.loads(assign)
            data_unassign = json.loads(unassign)
            start = 0
            # for assign new task
            while start < len(data):
                getRowExist = conn.execquery("select * from problem_assign where problem_log_id ='"+problemid+"' and teamproject_id = '" +data[start]+"'")
                if getRowExist == 0:
                    # insert assign user
                    addNewAssign = conn.insert('problem_assign', problem_log_id=problemid, teamproject_id=data[start])
                    if addNewAssign == 0:
                        validate.append('success')
                    else:
                        validate.append('failed')
                start += 1
            # for unassign user
            count = 0
            while count < len(data_unassign):
                print data_unassign[count]
                getAssignExist = conn.execquery("select * from problem_assign where problem_log_id ='"+problemid+"' and teamproject_id='"+data_unassign[count]+"'")

                if getAssignExist == 1:
                    delAssign = conn.execquery("delete from problem_assign where problem_log_id = '"+problemid+"' and teamproject_id='"+data_unassign[count]+"'")
                    if delAssign == 1:
                        validate.append('success')
                    else:
                        validate.append('failed')
                count += 1
            return validate
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDocument(self, problemid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getData = conn.customquery('select * from doc_type_problemlog where document_type_problemlog_id not in (select document_type_problemlog_id from document_problemlog where problem_log_id="'+problemid+'");')
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'document_type_problemlog_id': list[0],
                    'document_name': list[1],
                    'master_problem_id': list[2]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def documentProblem(self, problemid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'problem_log_id = %s'
            getData = conn.select('v_document_problem_detail', cond, '*', problem_log_id=problemid)
            detail = []
            for index, list in enumerate(getData):
                i = {
                    'document_problemlog_id': list[0],
                    'document_type_problemlog_id': list[1],
                    'document_name': list[2],
                    'document_url': list[3],
                    'problem_log_id': list[4],
                    'document_size':list[5],
                    'document_filename': list[6],
                    'document_extention': list[7]
                }
                detail.append(i)
            return detail
        except Exception as e:
            return "Error Database: %s" % str(e)

    def uploadDocument(self, doc_name, problemid, doc_code, doc_size, doc_url, doc_extention):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addDoc = conn.insert('document_problemlog', document_filename=doc_name, document_type_problemlog_id=doc_code, document_url=doc_url, problem_log_id=problemid, document_size=doc_size, document_extention=doc_extention)
            if addDoc == 0:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def updateTaskProblem(self, problemid, problem_master, increment_id):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getValueMaster = 'master_problem_id = %s'
            getMasterId = conn.select('master_problem', getValueMaster, 'master_problem_id, increment_problem', master_problem_id=problem_master)

            nextIncrement = int(getMasterId[0][1]) + 1
            statusIncrement = "{0:0>5}".format(str(nextIncrement))
            master_problem = "MSPR"+statusIncrement

            validateDocument = conn.execquery('SELECT * FROM doc_type_problemlog WHERE master_problem_id = "'+problem_master+'" and document_type_problemlog_id NOT IN (SELECT document_type_problemlog_id FROM document_problemlog WHERE problem_log_id = "'+problemid+'");')
            if validateDocument == 0:
                cond = 'problem_log_id = %s'
                updTaskProblem = conn.update('problem_log', cond, problemid, master_problem_id=master_problem)
                if updTaskProblem:
                    return 0
                else:
                    return 1
            else:
                return 2
        except Exception as e:
            return "Error Database: %s" % str(e)