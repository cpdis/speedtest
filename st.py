# All-in-1 speed test, but without the integration into Google Sheets, which is a handicap for people to share the data, create alerting, etc.

import re
import sqlite3 as lite
import sys
import time    
import sqlite3 as lite
import plotly
from plotly.graph_objs import *
import pandas as pd

time.strftime('%Y-%m-%d %H:%M:%S')

# Read latest speed data from .txt file

lines = open('/home/paul/speed.txt').read().splitlines()

p = re.match("Ping: (.*?) ms", lines[0])
d = re.match("Download: (.*?) Mbit/s", lines[1])
u = re.match("Upload: (.*?) Mbit/s", lines[2])

con = lite.connect('/home/paul/tw-speed.db')

# Update database

with con:
	cur = con.cursor()  
	cur.execute('''INSERT INTO data(ping,download,upload) VALUES(?,?,?)''',(p.group(1),d.group(1),u.group(1)))

# Get data from database and update graph

with con:
    cur = con.cursor()  
    cur.execute('SELECT * FROM data')
    rows = cur.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'id', 1: 'Ping', 2: 'Download', 3: 'Upload', 4:'Date'}, inplace=True);
df = df.sort(['Date'], ascending=[1]);

trace1 = Scatter(
     x=df['Date'],
     y=df['Download'],
     name='Download',
)
trace2 = Scatter(
    x=df['Date'],
    y=df['Upload'],
    name='Upload',
    yaxis='y2'
)
layout = Layout(
    title="Time Warner Broadband Speed",
    xaxis=XAxis( title='Date' ),
    yaxis=YAxis( 
        title='Download speed (mb/s)', 
        range=[0,35]
    ),
    yaxis2=YAxis(
        title='Upload speed (mb/s)',
        range=[0,6],
        titlefont=Font(
            color='rgb(148, 103, 189)'
        ),
        tickfont=Font(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)

# Update graph
data = Data([trace1,trace2])
fig = Figure(data=data, layout=layout)
py.plot(fig, filename='broadband speeds',world_readable=False)
