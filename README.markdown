Usage
-----
./ical-to-gcal.py <source file> [<destination file>]

Purpose
-------
Cleans iCal .ics backups to be imported in Google Calendar. If VALARM and VTODO tags don't get stripped from the .ics file, Google will fail an import with the following error message:

"Failed to import events: Unable to process your iCal/CSV file"

(see http://mccammon.org/keith/2009/07/14/errors-importing-ical-data-icalendar-into-google-calendar/ )

Step by step
------------

iCal
----
1. iCal
2. Export > Export
3. ~/Desktop/<source file>.ics
4. Export

Shell
-----
1. ./ical-to-gcal.py ~/Desktop/<source file>.ics

Google Calendar
---------------
1. http://www.google.com/calendar
2. Calendar-Settings
3. Calendar
4. Import calendar
5. Choose
6. ~/Desktop/<source file>.gcal.ics
7. Import 
