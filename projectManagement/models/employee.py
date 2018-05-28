from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE


class department(object):
    def add(self, deptname, deptdesc):
        self.deptname = deptname
        self.deptdesc = deptdesc
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addDept = conn.insert('department', department_name=self.deptname, description=self.deptdesc)
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
            allDiv = conn.select('v_division_detail', None, 'division_id, division_name, department_name, description')
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
            condDept = 'status = %s'
            getDept = conn.select('department', condDept, 'department_id, department_name', status='added')
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

    def add(self, deptNo, divName, divDesc):
        self.deptNo = deptNo
        self.divName = divName
        self.divDesc = divDesc
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            addDiv = conn.insert('division', department_id=self.deptNo, division_name=self.divName, description=self.divDesc)
            if len(addDiv) == 0:
                return True
            else:
                return False
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

    def deleted(self, divno):
        self.divno = divno
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDelDiv = 'division_id = %s'
            divDelUpd = conn.update('division', condDelDiv, self.divno, status='deleted')
            if divDelUpd:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

    def updated(self, divNo, deptName, divName, divDesc):
        self.divNo = divNo
        self.deptName = deptName
        self.divName = divName
        self.divDesc = divDesc

        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condUpd = 'division_id = %s'
            updDiv = conn.update('division', condUpd, self.divNo, department_id=self.deptName, division_name=self.divName, description=self.divDesc)
            if updDiv:
                return True
            else:
                return False
        except Exception as e:
            return "Error Database: %s" % str(e)

class employees(object):
    def all(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getEmpAll = conn.select('v_employees_detail', None, 'initial ,firstname, lastname, division_name ,title_name, employee_id')
            detEmpAll = []
            for index, list in enumerate(getEmpAll):
                i = {
                    'initial': list[0],
                    'fistname': list[1],
                    'lastname': list[2],
                    'division_name': list[3],
                    'position': list[4],
                    'employee_id':list[5]
                }
                detEmpAll.append(i)
            return detEmpAll
        except Exception as e:
            return "Error Database: %s" % str(e)

    def getJobsTitle(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getTitle = conn.select('emptitle', None, 'empTitle_id,title_name')
            detailTitle = []
            for index, list in enumerate(getTitle):
                i = {
                    'empTitle_id': list[0],
                    'title_name': list[1]
                }
                detailTitle.append(i)
            return detailTitle
        except Exception as e:
            return "Error Database: %s" % str(e)

    def school(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getSchool = conn.select('school_level', None, '*')
            detSchool = []
            for index, list in enumerate(getSchool):
                i = {
                    'school_code': list[0],
                    'school_level': list[1]
                }
                detSchool.append(i)
            return detSchool
        except Exception as e:
            return "Error Database: %s" % str(e)

    def province(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getProvince = conn.select('province', None, '*')
            detProvince = []
            for index, list in enumerate(getProvince):
                i = {
                    'province_id': list[0],
                    'province_name': list[1]
                }
                detProvince.append(i)
            return detProvince
        except Exception as e:
            return "Error Database: %s" % str(e)

    def city(self, prov_id):
        self.prov_id = prov_id
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condCity = 'province_id = %s'
            getCity = conn.select('city', condCity, 'city_code, city_name', province_id=self.prov_id)
            detCity = []
            for index, list in enumerate(getCity):
                i = {
                    'city_code': list[0],
                    'city_name': list[1]
                }
                detCity.append(i)
            return detCity
        except Exception as e:
            return "Error Database: %s" % str(e)

    def detail(self, empid):
        self.empid = empid
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condEmp = 'employee_id = %s'
            getEmp = conn.select('v_employees_detail', condEmp, 'employee_id, NIK, email, firstname, lastname, birthday, gender, address, city_name, phone, division_name, title_name, join_date, school, institusi_name, start_school, completed_school, degree, grade, experience_comp, experience_location, experience_position, experience_report, experience_start, experience_completed', employee_id=self.empid)
            detEmp = []
            for index, list in enumerate(getEmp):
                i = {
                    'employee_id': list[0],
                    'NIK': list[1],
                    'email': list[2],
                    'firstname': list[3],
                    'lastname': list[4],
                    'birtday': list[5],
                    'gender': list[6],
                    'address': list[7],
                    'city_name': list[8],
                    'phone': list[9],
                    'division_name': list[10],
                    'title_name': list[11],
                    'join_date': list[12],
                    'school': list[13],
                    'institusi_name': list[14],
                    'start_school': list[15],
                    'completed_school': list[16],
                    'degree': list[17],
                    'grade': list[18],
                    'experience_comp': list[19],
                    'experience_location': list[20],
                    'experience_position': list[21],
                    'experience_report': list[22],
                    'experience_start': list[23],
                    'experience_completed': list[24]
                }
                detEmp.append(i)
            return detEmp
        except Exception as e:
            return "Error Database: %s" % str(e)