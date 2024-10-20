class event():
    def __init__(self, eventID, name, roomID, organizer, date, duration, status, capacity, description, tags):
        self.__event_id = eventID
        self.__name = name
        self.__roomID = roomID
        self.__organizer = organizer
        self.__attendees = set()
        self.__date = date
        self.__duration = duration
        self.__status = status
        self.__capacity = capacity
        self.__description = description
        self.__tags = set()

    # Setter Methods
    def setEventID(self, eventID):
        self.__event_id = eventID

    def setName(self, name):
        self.__name = name

    def setRoomID(self, roomID):
        self.__roomID = roomID

    def setOrganizer(self, organizer):
        self.__organizer = organizer

    def setAttendees(self, attendees):
        self.__attendees = attendees

    def setDate(self, date):
        self.__date = date

    def setDuration(self, duration):
        self.__duration = duration

    def setStatus(self, status):
        self.__status = status

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setDescription(self, description):
        self.__description = description

    def setTags(self, tags):
        self.__tags = tags

    # Getter Methods
    def getEventID(self):
        return self.__event_id
    
    def getName(self):
        return self.__name
    
    def getRoomID(self):
        return self.__roomID
    
    def getOrganizer(self):
        return self.__organizer
    
    def getAttendees(self):
        return self.__attendees
    
    def getDate(self):
        return self.__date
    
    def getDuration(self):
        return self.__duration

    def getStatus(self):
        return self.__status
    
    def getCapacity(self):
        return self.__capacity
    
    def getDescription(self):
        return self.__description
    
    def getTags(self):
        return self.__tags
    
    # Methods
    # Adds user to attendees set to event
    def addAttendee(self, user):
        self.__attendees.add(user)

    # Removes user from attendees set to event
    def removeAttendee(self, user):
        self.__attendees.remove(user)

    # Get remaining capacity
    def remainingCapacity(self):
        return self.__capacity - len(self.__attendees)
    
    # Returns true if event is over capacity
    def isFull(self):
        return len(self.__attendees) >= self.__capacity
    
    # Check if 2 events start at the same time
    def checkConflict(self, event):
        return self.__date == event.getDate()
    
    # Adds a tag to the set of an event
    def addTag(self, tag):
        self.__tags.add(tag)

    # Removes a tag from the set of an event
    def removeTag(self, tag):
        self.__tags.remove(tag)
    