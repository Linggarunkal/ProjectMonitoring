from pertaminaAPI.library.connection import mysqlconnection
from pertaminaAPI.library.config import HOST, USERNAME, PASSWORD, DATABASE
from pertaminaAPI.library.response_message import messages
from passlib.hash import sha256_crypt
from flask import jsonify
import MySQLdb


class signin(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def passwdVerify(self, secret, passwd):
        return sha256_crypt.verify(secret, passwd)

    def login(self):
        try:
            __email = self.email
            __password = self.password
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond_email = 'email = %s'
            checkUser = conn.select('users', cond_email, 'email, password', email=__email)
            if (len(checkUser) > 0):
                verify = self.passwdVerify(__password, checkUser[0][1])
                if verify:
                    condUser = 'email = %s'
                    getUserid = conn.select('users', condUser, '*', email=__email)

                    userid = []
                    for index, list in enumerate(getUserid):
                        getid = (list[0])

                        i = {
                            "userid": getid
                        }
                        userid.append(i)

                    message = messages(200)
                    msg = message.resp(userid)
                    return msg
                else:
                    message = messages(401)
                    msg = message.resp(None)
                    return msg
            else:
                message = messages(204)
                msg = message.resp(None)
                return msg

        except Exception as e:
            message = messages(500)
            msg = message.resp(str(e))
            return msg


class signup(object):
    def __init__(self, email, password, telp):
        self.email = email
        self.password = password
        self.telp = telp



    def registration(self):
        try:
            hashPasswd = passwdHash()
            resHashPasswd = hashPasswd.passwdEncrypt(self.password)
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            reg = conn.insert('users', email=self.email, password=resHashPasswd, tlp=self.telp)
            if reg == 0:
                message = messages(200)
                msg = message.resp(None)
                return msg
            else:
                message = messages(500)
                msg = message.resp(None)
                return msg

        except Exception as e:
            message = messages(500)
            msg = message.resp(str(e))
            return msg


class passwdHash(object):
    def passwdEncrypt(self, passwd):
        return sha256_crypt.encrypt(passwd)