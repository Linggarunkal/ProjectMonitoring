from projectManagement.library.connection import mysqlconnection
from projectManagement.library.config import HOST, USERNAME, PASSWORD, DATABASE
from passlib.hash import sha256_crypt


class login_user(object):
    def verify_login(self, username, password):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            usercheck = conn.execquery('select * from employees where nik="'+username+'"')
            if usercheck == 0:
                return 2
            else:
                checkPassword = conn.customquery('select nik, password from employees where nik = "'+username+'"')
                passwordHash = checkPassword[0][1]
                decryp = sha256_crypt.verify(password, passwordHash)
                if decryp:
                    return 0
                else:
                    return 1
        except Exception as e:
            return "Error Database: %s" % str(e)

    def check_name(self, nik):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond = 'nik = %s'
            getData = conn.select('employees', cond, 'firstname, lastname', nik=nik)
            name_emp = getData[0][0]+" "+getData[0][1]
            return name_emp
        except Exception as e:
            return "Error Database: %s" % str(e)
