# meetingRoomScheduler
Conference room scheduler -python

rooms.txt -> contains all the conference information in the following format room number, floor, how many people it can accommodate and room available timings.
(Took the example data given in test, and added number people parameter in rooms.txt file.)

functions description:
readRoomInfoFromTextFile() -> This function is to read all the contents of .txt file and load the rooms information into an 2D array. 

getAvailableRooms() -> This function look in the rooms list array and return available rooms. First it will look for number of people the room can accommodate. If the rooms capacity is greater than or equal to number of participants in meeting, then it will look for meeting start time and end times. This method will return an array of available rooms and floors they belong to.

After getting the available rooms information, if the available rooms length is more than or equal to one, will check the floor near to participants based floor number and prints the room number in console.  
