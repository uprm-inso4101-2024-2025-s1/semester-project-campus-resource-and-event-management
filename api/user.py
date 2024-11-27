class user():
    def __init__(self, userID, username, email, password, userRole, isAdmin):
        self.__userID = userID
        self.__username = username
        self.__email = email
        self.__password = password
        self.__userRole = userRole
        self.__isAdmin = isAdmin
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
    
    def setTags(self, isAdmin):
        self.__isAdmin = isAdmin

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
    
    def getIsAdmin(self):
        return self.__isAdmin
    
    # Methods
    # Adds a room to the set of responsible rooms of a user
    def addResponsibleRooms(self, room):
        self.__responsibleRooms.add(room)

    # Removes a room from the set of responsible rooms of a user
    def removeResponsibleRooms(self, room):
        self.__responsibleRooms.remove(room)

    # Adds a tag to the set of a user
    def addTag(self, tag):
        self.__tags.add(tag)
        self.checkTagRequirement()

    # Adds a tag from the set of a user
    def removeTag(self, tag):
        self.__tags.remove(tag)
        self.checkTagRequirement()

    # New method to check if the user has selected at least 5 tags
    def checkTagRequirement(self):
        if len(self.__tags) < 5:
            print("You must select at least 5 tags (faculty, majors, associations).")
            return False
        return True

    

