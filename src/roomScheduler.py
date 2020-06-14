import os
import datetime

#Function to read rooms information from a text file and return an array
def readRoomInfoFromTextFile():
        current_working_directory = os.path.abspath('.')
        for filename in os.listdir(current_working_directory):
            if filename.endswith('.txt'):

                # Ensuring that if something goes wrong during read, that the program exits gracefully.
                try:
                    with open(filename, 'r') as current_file:
                        roomsInfo = []

                        # Reads each line of the file, and creates a 1d list of each point: e.g. [1,2].
                        for line in current_file.readlines():
                            point = line.split(' ')
                            for i in [line.split(',') for line in point]:
                                  roomsInfo.append(i)
                except IOError:
                    print("Something went wrong when attempting to read file.")
        return roomsInfo

#Function to convert string to time
def convertToTime(timeToConvert):
    date_time_obj = datetime.datetime.strptime(timeToConvert, '%H:%M')
    return date_time_obj.time()


#Function to return available rooms by taking meeting start and end time as input
def getAvailableRooms(roomsInfo, meetingStartTime, meetingEndTime):
    availableRooms = []
    for i in roomsInfo:
        for j in range(3, len(i)-1):
            if (j % 2 == 1):
                roomAvailableFrom = convertToTime(i[j])
                roomAvailableTill = convertToTime(i[j+1])
                #Checking the number of participants a meeting room can hold
                if i[2] <= noofParticipants:
                    #condition to check meeting room is available in the given time slot
                    if roomAvailableFrom <= meetingStartTime:
                         if roomAvailableTill >= meetingEndTime:
                               availableRooms.append([i[0],i[1]])
    return availableRooms

#find closest floor
def getClosestFloor(floors, participantsFloor):
    return min(floors, key = lambda x:abs(x - int(participantsFloor)))

#Get input from user
print("Enter number of participants")
noofParticipants = input()
print("Enter floor in which participants are located")
participantsFloor = input()
print("Enter desired meeting start time in the format HH:MM")
meetingStartTime = input()
print("Enter expected meeting end time in the format HH:MM")
meetingEndTime = input()
print("Values entered in the format number of participants floor meeting start time meeting end time")
print(noofParticipants , participantsFloor , meetingStartTime , meetingEndTime)

#Read rooms information from text file and insert the values into an array
roomsInfo = readRoomInfoFromTextFile()

meetingStartTime = convertToTime(meetingStartTime)
meetingEndTime = convertToTime(meetingEndTime)
#Get list of rooms available during the given time period
availableRooms = getAvailableRooms(roomsInfo,meetingStartTime, meetingEndTime)

#Get nearest room based on floor number
if len(availableRooms) >= 1:
   floors = []
   for room in availableRooms:
       floors.append(int(room[1]))
   closestFloor = getClosestFloor(floors, participantsFloor)

   for room in availableRooms:
       if int(room[1]) == closestFloor:
          finalMeetingRoom = room[0]
          print("Following room in available:")
          print(finalMeetingRoom)
else:
   print("Didn't find any room available in given time slot, please try considering another time slot.")



