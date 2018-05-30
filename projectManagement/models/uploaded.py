import os
from werkzeug.utils import secure_filename


class upload(object):
    def __init__(self, raw, filedir):
        self.raw = raw
        self.filedir = filedir

    def photo(self, photoName, photoExtention):
        self.photoName = photoName
        self.photoExtention = photoExtention
        try:
            self.raw.filename = self.photoName+'.'+self.photoExtention
            files = secure_filename(self.raw.filename)
            self.raw.save(os.path.join(self.filedir, files))
            return True
        except Exception:
            return False

    def document(self, docName, docExtention):
        self.docName = docName
        self.docExtention = docExtention
        try:
            self.raw.filename = self.docName+'.'+self.docExtention
            files = secure_filename(self.raw.filename)
            self.raw.save(os.path.join(self.filedir, files))
            return True
        except Exception:
            return False



