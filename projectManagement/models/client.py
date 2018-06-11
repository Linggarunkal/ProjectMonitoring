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