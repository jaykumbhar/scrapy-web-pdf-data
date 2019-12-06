import os
import webbrowser
import sqlite3
from datetime import datetime
import lxml
from lxml.html.clean import Cleaner
cleaner =Cleaner()
cleaner.javascript = True
# cleaner.style = True

conn = sqlite3.connect("mydb.db")
curr = conn.cursor()
def diffsend(mstr2,mstr1):
  # import ipdb;ipdb.set_trace()
  mlsre2 = mstr2.split()
  diffrencestring = []
  for data2 in mlsre2:
    if data2 not in mstr1:
      diffrencestring.append(data2)
  return diffrencestring
mtestMainWeb = """<!DOCTYPE html> <html> <head> <script type="text/javascript" src="https://code.jquery.com/jquery-1.10.2.js"></script><meta name="viewport" content="width=device-width, initial-scale=1"> <style> * { box-sizing: border-box; } /* Create two equal columns that floats next to each other */ .column { float: left; width: 50%; padding: 10px; # height: 100%; /* Should be removed. Only for demonstration */ border: 1px solid #FFFFFF; } /* Clear floats after the columns */ .row:after { content: ""; display: table; clear: both; } .button{ padding: 10px; position: fixed; top: 10px; float: right; background-color: red; color: #fff; font-weight: bold; right: 17px; } </style> </head> <body> 
    <h2> Please find below the updates for the websites/sources <i></h2><h3>(Please click on the links displayed below)</i></h3>
<div class="row">"""
mywebsites = curr.execute("SELECT website FROM poc_work GROUP by website").fetchall()
outWebsites = [item for t in mywebsites for item in t] 
for num,myweb in enumerate(outWebsites):
    print("SELECT websitecontent FROM poc_work WHERE website='{}' order by date desc limit 2".format(myweb))
    data11 = curr.execute("SELECT websitecontent FROM poc_work WHERE website='{}' order by date desc limit 2".format(myweb)).fetchall()
    outwebContent = [item for t in data11 for item in t]
    strdiffrance = []
    if len(outwebContent) == 2:
        x= outwebContent[0]
        y= outwebContent[1]
        strdiffrance = diffsend(x,y)
    else:
        print("No Entry fro diffrance")
    mdict = {}
    message = ''
    message+="""<!DOCTYPE html> <html> <head> <script type="text/javascript" src="https://code.jquery.com/jquery-1.10.2.js"></script> 
        <meta name="viewport" content="width=device-width, initial-scale=1"/> <style> * { box-sizing: border-box; } /* Create two equal columns that floats next to each other */ .column { float: left; width: 50%; padding: 10px; # height: 100%; /* Should be removed. Only for demonstration */ border: 1px solid #FFFFFF; } /* Clear floats after the columns */ .row:after { content: ""; display: table; clear: both; } .button{ padding: 10px; position: fixed; top: 10px; float: right; background-color: red; color: #fff; font-weight: bold; right: 17px; } </style>   </head> <body> <div class="row">
        <script type="text/javascript">

            var i=0; function increase(){
           
            var t = "test"+i;
            if($('#test'+i).length!=0){
               window.location.href="#"+t;
              $('#test' +(i-1)).removeAttr('style');
              $('#test' +i).css('background-color','red');
              i++;
             }else{
               console.log(i)
                $('#test' +(i-1)).removeAttr('style');
                i=0;   
                window.location.href="#"+t;            
                $('#test' +i).css('background-color','red');
             }
            return(t); }
            </script> 
          
        """
    for Webdata in outwebContent:
        # Webdata = re.sub(r'\<script>.+</script>',' ',Webdata)
        # import ipdb;ipdb.set_trace()
        Webdata = cleaner.clean_html(Webdata)
        message+="""<div class="column" style="background-color:#bbb;">
          <div class="button">
          <input type="button" value="NEXT" onclick="increase();">
          </div>
          """+str(Webdata)+"""</div>"""
    message+="""</div></body></html>"""
    mdict = {}
    if strdiffrance:
      words = [w.replace(w, '<mark id="test'+str(num)+'">'+str(w)+'</mark>') for num,w in enumerate(strdiffrance)]
      print(words)
      mdict = {k:v for (k,v) in zip( strdiffrance,words) }
    # import ipdb;ipdb.set_trace()
    for i in mdict.keys():
        # print("I am replaceing ",i," to ",mdict[i] )
        message = message.replace(str(i),str(mdict[i]))
    dirName = 'POC_Extracted_WEBSITES-'+str(datetime.now().date())
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    filename = dirName+'/POCWORK'+myweb.replace('/','').replace(':','')+'__.html'
    mtestMainWeb+="""<div class="column"> Sr.No: {2} <a href="{0}"> {1}</a></div></div>""".format(filename,myweb,num+1)
    f = open(filename,'w')
    if message:
      f.write(message)
    f.close()
    # webbrowser.open_new_tab(filename)
mtestMainWeb+="""</div></body></html>"""
f = open('index.html','w')
if message:
  f.write(mtestMainWeb)
f.close()
webbrowser.open_new_tab('index.html')
conn.close()
