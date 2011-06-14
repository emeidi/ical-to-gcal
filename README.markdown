Usage
=====
`./ical-to-gcal.py <source file> [<destination file>]`

Purpose
=======
Cleans iCal .ics backups to be imported in Google Calendar. If VALARM and VTODO tags don't get stripped from the .ics file, Google will fail an import with the following error message:

"Failed to import events: Unable to process your iCal/CSV file"

(see <http://mccammon.org/keith/2009/07/14/errors-importing-ical-data-icalendar-into-google-calendar/> )

Step by step
============

iCal
----
1. iCal
1. Export > Export
1. `~/Desktop/<calendar>.ics`
1. Export

Shell
-----
1. `./ical-to-gcal.py ~/Desktop/<calendar>.ics`

Google Calendar
---------------
1. http://www.google.com/calendar
1. Calendar-Settings
1. Calendar
1. Import calendar
1. Choose
1. `~/Desktop/<calendar>.gcal.ics`
1. Import 
