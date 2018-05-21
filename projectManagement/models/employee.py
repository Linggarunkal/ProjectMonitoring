from projectManagement.library.connection import mysqlconnection
from projectManagemeny.library.config import HOST, USERNAME, PASSWORD, DATABASE


class employees(object):
    def __init__(self, name):
        self.name = name
        return name