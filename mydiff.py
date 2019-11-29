
import webbrowser
# import izip
f = open('helloworld.html','w')
import sqlite3
conn = sqlite3.connect("mydb.db")
curr = conn.cursor()
data = curr.execute("""SELECT websitecontent,website FROM poc_work""").fetchall()
# import ipdb;ipdb.set_trace()
message = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {
      box-sizing: border-box;
    }
    /* Create two equal columns that floats next to each other */
    .column {
      float: left;
      width: 50%;
      padding: 10px;
      # height: 100%; /* Should be removed. Only for demonstration */
      border: 1px solid #FFFFFF;
    }
    /* Clear floats after the columns */
    .row:after {
      content: "";
      display: table;
      clear: both;
    }
    </style>
    </head>
    <body>
    <div class="row">
    """
def diffsend(mstr1,mstr2):
  mlsre2 = mstr2.split()
  print(type(mlsre2))
  diffrencestring = []
  for data2 in mlsre2:
    if data2 not in mstr1:
      diffrencestring.append(data2)
  return diffrencestring
i = 0
strdiffrance = None
for Webdata in data:
    try:  
      if data[i][1] == data[i+1][1]:
        mdict = {data[i][1]:[data[i][0],data[i+1][0]]}
    except IndexError:
      print("index not found")
      pass
    if len(mdict[Webdata[1]])==2:
        x = mdict[Webdata[1]][0]
        y = mdict[Webdata[1]][1]
        strdiffrance = diffsend(x,y)
        print(strdiffrance)
    i+=1
    message+="""
    <div class="column" style="background-color:#bbb;">
      """+str(Webdata[0])+"""</div>"""

message+="""
</div>
</body>
</html>
"""
mdict = {}
if strdiffrance:
  words = [w.replace(w, '<mark>'+w+'</mark>') for w in strdiffrance]
  mdict = {k:v for (k,v) in zip( strdiffrance,words) }
# print(mdict)
# import ipdb;ipdb.set_trace()
for i in mdict.keys():
    # print(i)
    message = message.replace(str(i),str(mdict[i]))
# print(message)
f.write(message)
f.close()
conn.close()
webbrowser.open_new_tab('helloworld.html')
