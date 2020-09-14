# speedtest
Speedtest for a home broadband connection. The speedtest.py script collects and stores the data locally; uploadtosheets.py sends it to Google Sheets for graphing and data storage. You alternatively use st.py to do both in one routine, but makes it more complicated to view, share, and alert. 

Prerequesitites:
- Python 3.5+
- A Unix-based device that is always on and where you can run things as a cron process. I use a Raspberry Pi.
- Some basic understanding of Unix/Python, but not very much.
- A Google Sheets account

Installation instructions:
- Load speedtest.py and uploadtosheets.py scripts in the same folder
- Go through the Google Oauth instructions (https://developers.google.com/sheets/api/quickstart/python) so your Python script has permission to send data from your device to a Google Sheets document over which you have control
- Set up a cron process on your device to have data be collected and sent regularly. Mine is hourly, but that's up to you. 

Notes:
- While I haven't described it here, you can obviously do all sorts of alerting and highlighting of stuff, so that you find out when bandwidth drops below a certain level. That way you're not surprised when your WFH spouse, or Zoom-class kids, come running out of their rooms at the same time shouting "My Zoom call went down!".
- Please no questions on how to install, deal with Unix, or deal with scripts, or cron, etc. 
