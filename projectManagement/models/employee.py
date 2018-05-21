from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE


class department(object):
    def add(self, deptname):
        self.deptname = deptname

        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addDept = conn.insert('department', department_name=self.deptname)
            if len(addDept) == 0:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def all(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDept = 'status = %s'
            getDept = conn.select('department', condDept, 'department_id, department_name, description', status='added')
            detailDept = []
            for index, list in enumerate(getDept):
                i = {
                    'department_id': list[0],
                    'department_name': list[1],
                    'department_desc': list[2]
                }
                detailDept.append(i)
            return detailDept
        except Exception as e:
            return "Error Database: %s" % str(e)

    def detail(self, departmentid):
        self.departmentid = departmentid
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDetail = 'department_id = %s'
            getDetail = conn.select('department', condDetail, 'department_id, department_name, description', department_id=self.departmentid)
            detailDept = []
            for index, list in enumerate(getDetail):
                i = {
                    'department_id': list[0],
                    'department_name': list[1],
                    'department_desc': list[2]
                }
                detailDept.append(i)
            return detailDept
        except Exception as e:
            return "Error Database: %s" % str(e)

    def update(self, departmentid, departmentname, departmentdesc):
        self.departmentid = departmentid
        self.departmentname = departmentname
        self.deptmentdesc = departmentdesc

        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condUpdDept = 'department_id = %s'
            updDept = conn.update('department', condUpdDept, self.departmentid, department_name=self.departmentname, description=self.deptmentdesc)
            if updDept:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def deleted(self, departmentid):
        self.departmentid = departmentid
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDelDept = 'department_id = %s'
            updDept = conn.update('department', condDelDept, self.departmentid, status='deleted')
            if updDept:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)


class division(object):
    def all(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            allDiv = conn.select('v_division_detail', None, '*')
            detailAllDiv = []
            for index, list in enumerate(allDiv):
                i = {
                    'division_id': list[0],
                    'division_name': list[1],
                    'department_name': list[2],
                    'description': list[3]
                }
                detailAllDiv.append(i)
            return detailAllDiv
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getDeptName(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getDept = conn.select('department', None, 'department_id, department_name')
            detDept = []
            for index, list in enumerate(getDept):
                i = {
                    'department_id': list[0],
                    'department_name': list[1]
                }
                detDept.append(i)
            return detDept
        except Exception as e:
            return "Error Database: %s" % str(e)

    def add(self, deptNo, divName):
        self.deptNo = deptNo
        self.divName = divName
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)

            return "testing"
        except Exception as e:
            return "Error Database: %s" % str(e)

    def detail(self, divNo):
        self.divNo = divNo
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDiv = 'division_id = %s'
            detDiv = conn.select('v_division_detail', condDiv, '*', division_id=self.divNo)
            detailDiv = []
            for index, list in enumerate(detDiv):
                i = {
                    'division_id': list[0],
                    'division_name': list[1],
                    'department_id': list[2],
                    'description': list[4]
                }
                detailDiv.append(i)
            return detailDiv
        except Exception as e:
            return "Error Database: %s" % str(e)