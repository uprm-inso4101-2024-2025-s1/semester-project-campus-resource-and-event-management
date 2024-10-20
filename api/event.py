class event():
    def __init__(self, eventID, name, roomID, organizer, attendees, date, duration, status, capacity, description, tags):
        self.__event_id = eventID
        self.__name = name
        self.__roomID = roomID
        self.__organizer = organizer
        self.__attendees = attendees
        self.__date = date
        self.__duration = duration
        self.__status = status
        self.__capacity = capacity
        self.__description = description
        self.__tags = tags

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
    def setData(self, data):
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

