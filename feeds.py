import subprocess
import time
import json
import re
import MySQLdb
proc = subprocess.Popen(["curl", "http://194.47.151.126:4000/emoncms/feed/list.json?userid=1&apikey=bcf2edbe8c6d528bcf914759af63a253"],   stdout=subprocess.PIPE)
(out, err) = proc.communicate()
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
j=json.loads(out)

for i in j:
 

  id1 = i['id']
  userid = i['userid']
  name = i['name']
  public = i['public']
  size = i['size']
  engine = i['engine']
  time = i['time']
  value = i['value']
  
  a.append(id1)
  b.append(userid)
  c.append(name)
  d.append(public)
  e.append(size)
  f.append(engine)
  g.append(time)
  h.append(value)
  conn = MySQLdb.connect(host="localhost",user="root",passwd="adil",db="anm")
  x = conn.cursor()
  for app1,app2,app3,app4,app5,app6,app7,app8 in zip(a,b,c,d,e,f,g,h):
     name1 = re.findall("tx\d_ws\d",app3) 
     
     if len(name1) ==0:
      try:
       x.execute("""INSERT INTO new(name,time,value) VALUES(%s,%s,%s)""",(app3,app7,app8))
       conn.commit()
      except:
       conn.rollback()
       conn.close()
print ('checkdb')
