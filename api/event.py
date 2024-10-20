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

