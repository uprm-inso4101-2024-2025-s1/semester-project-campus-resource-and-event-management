class user():
    def __init__(self, userID, username, email, password, userRole):
        self.__userID = userID
        self.__username = username
        self.__email = email
        self.__password = password
        self.__userRole = userRole
        self.__responsibleRooms = set()
        self.__tags = set()
    
    # Setter Methods
    def setUserID(self, userID):
        self.__userID = userID
        
    def setUsername(self, username):
        self.__username = username

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password
        
    def setUserRole(self, userRole):
        self.__userRole = userRole

    def setResponsibleRooms(self, responsibleRooms):
        self.__responsibleRooms = responsibleRooms

    def setTags(self, tags):
        self.__tags = tags

    # Getter Methods
    def getUserID(self):
        return self.__userID 
        
    def getUsername(self):
        return self.__username

    def getEmail(self):
        return self.__email 

    def getPassword(self):
        return self.__password 
        
    def getUserRole(self):
        return self.__userRole 

    def getResponsibleRooms(self):
        return self.__responsibleRooms 

    def getTags(self):
        return self.__tags

