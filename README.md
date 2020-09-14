# speedtest
Speedtest for a home broadband connection. Speedtest.py collects and stores the data locally; graphs.py sends it to Google Sheets for graphing and data storage. You alernatively use st.py to do both in one routine, but makes it more complicated to view and share. 

Prerequesitites:
- Python 3.5+
- A Unix-based device that is always on and where you can run things as a cron process. I use a Raspberry Pi.
- Some basic understanding of Unix/Python, but not very much.

Installation instructions:
- Load both scripts in the same folder
- Go through the Google Oauth instructions (https://developers.google.com/sheets/api/quickstart/python) so your Python script has permission to send data from your device to a Google Sheets document over which you have control
- Set up a cron process on your device to have data be collected and sent regularly. Mine is hourly, but that's up to you. 

While I haven't described it here, you can obviously do all sorts of alerting and highlight stuff, so that you find out when bandwidth drops below a certain level. That way you're not surprised when your WFH spouse, or Zoom-class kids, come running out of their rooms at the same time shouting "My Zoom call went down!".
