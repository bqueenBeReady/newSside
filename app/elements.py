
class User():
    def __init__(self, elem):
        self.user = elem['user']
        self.id = elem['id']
        self.location = elem['location']
        self.ppic = elem['profilePicture']

    def toJson(self):
        return {'user':self.user, 'id':self.id,'location':self.location,'profilePicture':self.ppic}



class WorkOut():
    def __init__(self, elem):
        self.type = elem['wtype']
        self.id = elem['wid']
        self.location = elem['location']
        self.creator = elem['wcreator']
        self.pictures = elem['pics']
        self.timeCreated = elem['ctime']
        self.startTime = elem['stime']

    def toJson(self):
        return {'wtype': self.type, 'id': self.id, 'location': self.location, 'wcreator': self.creator, 'pics':self.pictures, 'stime':self.startTime, 'ctime':self.timeCreated}



class picturePost():
    def __init__(self, elem):
        self.href = elem['href']
        self.pid = elem['pictureId']
        self.cid = elem['creatorId']
        self.timeCreated = elem['ctime']

    def toJson(self):
        return {'href':self.href, 'pictureId':self.pid, 'creatorId':self.cid, 'ctime':self.timeCreated}



