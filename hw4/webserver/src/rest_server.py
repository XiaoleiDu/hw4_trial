from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render_to_response

import requests
import json
import mysql.connector as mysql
import os
import datetime

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] 

USERS_FILE_PATH = "users.txt"
jetbotid = "jetbotid"

## File Utility methods
def read_file(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

def write_to_file(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
        
# Save data in Data Store
def save_user_details(userid, pwd, status, created_at):
  users = read_file(USERS_FILE_PATH)

  newUser = {}
  newUser['userid'] = userid
  newUser['pwd'] = pwd
  newUser['status'] = status
  newUser['created_at'] = created_at

  users.append(newUser)

  write_to_file(USERS_FILE_PATH, users)
  
# # update the txt file to data base info
def refresh_users_file():
  lines = []
  # connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from TUsers;")
  records = cursor.fetchall()
  # cursor.execute("select userid from TUsers where id = 1;")
  # userid = cursor.fetchall()
  # userid = str(userid)
  # fixuserid = userid[3:]#remove first two chars
  # userid = fixuserid[:-4]#remove last four chars
  for record in records:
    #print(str(record[0])) #id
    #print(str(record[1])) #firstname
    #print(str(record[2])) #lastname
    #print(str(record[3])) #email
    #print(str(record[4])) #created_at
    tempstr = ''
    for x in range(0, 5):
      tempstr += str(record[x])
      tempstr += ' '
    tempstr += '\n'
    print(tempstr)
    lines.append(tempstr)
  file2 = open('templates/public/users.txt', 'w') 
  file2.writelines(lines)
  file2.close()
  # file3 = open('templates/public/user.txt', 'w') 
  # file3.writelines(userid)
  # file3.close()
    
# def manipulateDataBase(req):
  # changeLineNumber = int(req.params['submit_button'])
  # file1 = open('templates/public/users.txt', 'r') 
  # Lines = file1.readlines() 
  # file1.close()
  # count = 0
  # # Strips the newline character 
  
  # for line in Lines: 
    # if len(line.split()) >= 5:
      # print(count)
      # print(changeLineNumber)
      # if line.split()[3] == "pending" and count == changeLineNumber:
        # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
        # cursor = db.cursor()
        # # Updating Records
        # cursor.execute("update TUsers set status='verified' where userid='%s' and status = 'pending';" % line.split()[1])
        # db.commit()
        # print('---------- UPDATE ----------')
        # print(cursor.rowcount, "record(s) updated.")
        # refresh_users_file()
        # return render_to_response('templates/did_login.html', {}, request=req)
      
      
      # if line.split()[3] == "verified" and count == changeLineNumber: 
        # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
        # cursor = db.cursor()      
        # # Deleting Records
        # cursor.execute("delete from TUsers where userid = '%s' and status = 'verified';" % line.split()[1])
        # db.commit()

        # print('---------- DELETE ----------')
        # print(cursor.rowcount, "record(s) deleted.")
        # refresh_users_file()
        # return render_to_response('templates/did_login.html', {}, request=req)
    # count = count + 1
  # return render_to_response('templates/did_login.html', {}, request=req)

# def refresh_users_file2():
  # Lines = []
  # # Connect to the database and retrieve the student
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # cursor.execute("select * from Moves;")
  # records = cursor.fetchall()
  # for record in records:
    # #print(str(record[0])) #id
    # #print(str(record[1])) #user_id
    # #print(str(record[2])) #pwd
    # #print(str(record[3])) #status
    # #print(str(record[4])) #created_at
    # tempStr = ''
    # for x in range(0, 7):
      # tempStr += str(record[x])
      # tempStr += ' '
    # tempStr += '\n'
    # print(tempStr)
    # Lines.append(tempStr)
  # file2 = open('templates/public/moves.txt', 'w') 
  # file2.writelines(Lines)
  # file2.close()

# def control_jetbot(req):
  # print('control_jetbot')
  # global jetbotid
  # buttonnumber = int(req.params['submit_button'])
  # print(buttonnumber)
  # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # cursor.execute("select userid from tcuser where id = 1;")
  # userid = cursor.fetchall()
  # userid = str(userid)
  # fixuserid = userid[3:]#remove first three chars
  # userid = fixuserid[:-4]#remove last four chars
  # # insert records
  # if buttonnumber == 0:
    # query = "insert into moves (direction, initialtime, starttime, endtime, userid, jetbotid, status) values (%s, %s, %s, %s, %s, %s, %s)"
    # values = [
      # ('forward', x, x, x, userid, jetbotid, 'pending')
    # ]
    # cursor.executemany(query, values)
    # db.commit()
    # db.close()
  # elif buttonnumber == 1:
    # query = "insert into moves (direction, initialtime, starttime, endtime, userid, jetbotid, status) values (%s, %s, %s, %s, %s, %s, %s)"
    # values = [
      # ('backward', x, x, x, userid, jetbotid,'pending')
    # ]
    # cursor.executemany(query, values)
    # db.commit()
    # db.close()
  # elif buttonnumber == 2:
    # query = "insert into moves (direction, initialtime, starttime, endtime, userid, jetbotid, status) values (%s, %s, %s, %s, %s, %s, %s)"
    # values = [
      # ('left', x, x, x, userid, jetbotid,'pending')
    # ]
    # cursor.executemany(query, values)
    # db.commit()
    # db.close()
  # elif buttonnumber == 3:
    # query = "insert into moves (direction, initialtime, starttime, endtime, userid, jetbotid, status) values (%s, %s, %s, %s, %s, %s, %s)"
    # values = [
      # ('right', x, x, x, userid, jetbotid,'pending')
    # ]
    # cursor.executemany(query, values)
    # db.commit()
    # db.close()
  # elif buttonnumber == 4:
    # query = "insert into moves (direction, initialtime, starttime, endtime, userid, jetbotid, status) values (%s, %s, %s, %s, %s, %s, %s)"
    # values = [
      # ('stop', x, x, x, userid, jetbotid,'pending')
    # ]
    # cursor.executemany(query, values)
    # db.commit()
    # db.close()
  # else:
    # query = "insert into moves (direction, initialtime, starttime, endtime, userid, jetbotid, status) values (%s, %s, %s, %s, %s, %s, %s)"
    # values = [
      # ('nothing', x, x, x, userid, jetbotid,'pending')
    # ]
    # cursor.executemany(query, values)
    # db.commit()
    # db.close()
  # return render_to_response('templates/j_controller.html', {}, request=req)
  
def manipulateUsersData(req):
  changeLineNumber = int(req.params['submit_button'])
  file1 = open('templates/public/users.txt', 'r') 
  Lines = file1.readlines() 
  file1.close()
  count = 0
  # Strips the newline character 
  for line in Lines: 
    if len(line.split()) >= 6:
      print(count)
      print(changeLineNumber)
      if line.split()[5] == "\"pending\"}," and count == changeLineNumber:
        tempStr = ''
        for x in range(0, 5):
          tempStr += Lines[count].split()[x]
          tempStr += ' '
        tempStr += "\"verified\"},\n"
    
        Lines[count] = tempStr
        file2 = open('templates/public/users.txt', 'w') 
        file2.writelines(Lines)
        file2.close()
        return render_to_response('templates/did_login.html', {}, request=req)
      
      
      if line.split()[5] == "\"verified\"}," and count == changeLineNumber:  
        print('poping here')
        print(count)
        Lines.pop(count)
        file2 = open('templates/public/users.txt', 'w') 
        file2.writelines(Lines)
        file2.close()
        return render_to_response('templates/did_login.html', {}, request=req)
    count = count + 1
  return render_to_response('templates/did_login.html', {}, request=req)

#check login info
# def gotoadminportal(req):
  # userid = req.params['userid']
  # password = req.params['pwd']
  # # connect to the database and retrieve the student
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # cursor.execute("select * from tstudentststudents where userid='%s' and status = 'verified';" % userid) 
  # record = cursor.fetchone()
  # db.close()
  # if record is none:
    # return render_to_response('templates/invalid_credentials.html', {'error':'invalid credentials'}, request=req)
  # else: # userid exists and is verified
    # if str(record[2]) == password: # password is correct    
      # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
      # db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
      # cursor = db.cursor()
      # # insert records
      # query = "insert into tcuser (userid, pwd, status, created_at) values (%s, %s, %s,%s)"
      # values = [
        # (userid,password, 'verified', x)
      # ]
      # cursor.executemany(query, values)
      # db.commit()
      # db.close()
      # return render_to_response('templates/gotoadminportal.html', {}, request=req)
    # else:
      # return render_to_response('templates/invalid_credentials.html', {'error':'invalid credentials'}, request=req)

# def check(test_str):
  # import re
    # #http://docs.python.org/library/re.html
    # #re.search returns none if no position in the string matches the pattern
    # #pattern to search for any character other then . a-z 0-9
  # pattern = r'[^\.a-z0-9a-z]'
  # if re.search(pattern, test_str):
        # #character other then . a-z 0-9 was found
        # #print 'invalid : %r' % (test_str,)
        # return false
  # else:
        # #no character other then . a-z 0-9 was found
        # #print 'valid   : %r' % (test_str,)
      # return true

# #--- this is called to compare credentials to the value
# def is_valid_user(req):
  # return true

#--- this route will validate login credentials...
# def did_login(req):
  # print("post_login")
  # if is_valid_user(req):   
    # return render_to_response('templates/did_login.html', {}, request=req)
  # else:
    # return render_to_response('templates/show_login.html', {'error':'invalid credentials'}, request=req)

#--- this route will lead to jetbot tracker page
# def j_tracker(req):
  # refresh_users_file2()
  # return render_to_response('templates/j_tracker.html', {}, request=req)

#--- this route will lead to jetbot controller page
# def j_controller(req):
  # print('j_controller, creating the moves table')
  # # connect to the database and retrieve the student
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # # create a moves table (wrapping it in a try-except is good practice)
  # try:
    # cursor.execute("""
      # create table moves (
        # moveid integer  auto_increment primary key,
        # direction      varchar(30) not null,
        # initialtime    timestamp,
        # starttime      timestamp,
        # endtime        timestamp,
        # userid         varchar(30) not null,
        # jetbotid       varchar(30) not null,
        # status         varchar(30) not null
      # );
    # """)
  # except:
    # print("table already exists. not recreating it.")
  # print('getting user info')
  # refresh_users_file()
  # print('finish')
  # return render_to_response('templates/j_controller.html', {}, request=req)


#--- this route will register
def get_register(req):
  print("get_register")
  return render_to_response('templates/register.html', {}, request=req)
  
#--- this route finish register
def finished_register(req):
  print("finished_register")
  return render_to_response('templates/login.html', {}, request=req)  

def signUp(req):
  x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # get user info
  firstname = req.params['firstname']
  lastname = req.params['lastname']
  email = req.params['email']
  # print(check(userId))
  # print(check(password))
  tempStr = ''
  # if check(userId) and check(password) and userId != tempStr and password != tempStr:
    # Insert Records
  query = "insert into TUsers (firstname, lastname, email, created_at) values (%s, %s, %s,%s)"
  values = [
    (firstname,lastname,email, x)
  ]
  cursor.executemany(query, values)
  db.commit()
  
  
  refresh_users_file()
  return render_to_response('templates/show_login.html', {}, request=req)
  # else:
    # return render_to_response('templates/try_again.html', {}, request=req)

# def get_jetbotid(req):
  # # get user info
  # global jetbotid 
  # jetbotid = req.params['jetbotid']
  # print(jetbotid)
  # return render_to_response('templates/redriectjetbotcontroller.html', {}, request=req)

# def redirect_jetbotsumbit(req):
  # return render_to_response('templates/submitjetbotid.html', {}, request=req)

def GO_back(req):
  return render_to_response('templates/gotoAdminPortal.html', {}, request=req)

#--- this route log out
# def log_out(req):
  # print("log_out")
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # cursor.execute("drop table if exists tcuser;")
  # try:
    # cursor.execute("""
      # create table tcuser (
        # id integer  auto_increment primary key,
        # userid      varchar(30) not null,
        # pwd         varchar(30) not null,
        # status       varchar(30) not null,
        # created_at  timestamp
      # );
    # """)
  # except:
    # print("table already exists. not recreating it.")
  # return render_to_response('templates/show_login.html', {}, request=req)

#--- this route will show a login form
def get_login(req):
  x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  cursor.execute("select COUNT(*) FROM TUsers")
  count = cursor.fetchall()
  file = open('templates/public/count.json','w',encoding='utf-8')
  data1 = {'count':count}
  json.dump(data1,file,ensure_ascii=False)
  
  # cursor.execute("select COUNT(*) FROM News")
  # newscount = cursor.fetchall()
  # file = open('templates/public/newscount.json','w',encoding='utf-8')
  # data1 = {'newscount':newscount}
  # json.dump(data1,file,ensure_ascii=False)
  
  cursor.execute("SELECT * FROM News")
  row = cursor.fetchall()
  file = open('templates/public/news.json','w',encoding='utf-8')
  data1 = {'news':row}
  json.dump(data1,file,ensure_ascii=False)
  # while row is not None:
        # file = open('templates/public/news.json','w',encoding='utf-8')
        # data1 = {'news':row}
        # json.dump(data1,file,ensure_ascii=False)
        # row = cursor.fetchone()
  cursor.execute("SELECT * FROM Progress")
  progress = cursor.fetchall()  
  file = open('templates/public/parameter.json','w',encoding='utf-8')
  data1 = {'parameter':progress}
  json.dump(data1,file,ensure_ascii=False)
  refresh_users_file()
  return render_to_response('templates/show_login.html', {}, request=req)

def about(req):
  return render_to_response('templates/about.html', {}, request=req)
  
def features(req):
  return render_to_response('templates/features.html', {}, request=req)
  
def try_again(req):
  return render_to_response('templates/try_again.html', {}, request=req)
  
def price(req):
  return render_to_response('templates/price.html', {}, request=req)

def news(req):
  return render_to_response('templates/news.html', {}, request=req)  
  
def parameter(req):
  return render_to_response('templates/parameter.html', {}, request=req)
# def count(req):
  # return render_to_response('templates/count.html', {}, request=req)
  
# def get_moves(req):
  # # Connect to the database and retrieve the student
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # cursor.execute("select * from Moves where status = 'pending';")
  # records = cursor.fetchall()
  # #print(records[0])
  # #print(records[1])
  # print(len(records))
  # if len(records) == 0:
    # print("giving nothing to jetbot")
    # return json.dumps("nothing in Moves table")
  # else:
    # return json.dumps(str(records[0]))
  
# def finished_top_pending_move(req):
  # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # print("finished_top_pending_move")
  # moveId = req.params['finished_move_id']
  # print(moveId)
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # tempString = "update Moves set status='complete' where moveId = '{}';".format(moveId)
  # print(tempString)
  # cursor.execute(tempString)
  # db.commit()
  # tempString = "update Moves set endTime='{}' where moveId = '{}';".format(x, moveId)
  # print(tempString)
  # cursor.execute(tempString)
  # db.commit()
  
# def update_start_time(req):
  # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # print("updating start time")
  # moveId = req.params['starting_move_id']
  # print(moveId)
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # tempString = "update Moves set startTime='{}' where moveId = '{}';".format(x, moveId)
  # print(tempString)
  # cursor.execute(tempString)
  # db.commit()

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('v2', '/')
  config.add_view(get_login, route_name='v2')
  
  config.add_route('login', '/login')
  config.add_view(get_login, route_name='login')
  # config.add_view(gotoAdminPortal, route_name='login', request_method='POST')
  
  # config.add_route('did_login', '/did_login')
  # config.add_view(did_login, route_name='did_login')
  # config.add_view(manipulateDataBase, route_name='did_login', request_method='POST')

  # config.add_route('log_out', '/log_out')
  # config.add_view(log_out, route_name='log_out')
  # config.add_view(log_out, route_name='log_out', request_method='POST')

  config.add_route('Go_back', '/Go_back')
  config.add_view(GO_back, route_name='Go_back')

  # config.add_route('Get_jetbotid', '/Get_jetbotid')
  # config.add_view(redirect_jetbotsumbit, route_name='Get_jetbotid')
  # config.add_view(Get_jetbotid, route_name='Get_jetbotid', request_method='POST')

  # config.add_route('j_tracker', '/j_tracker')
  # config.add_view(j_tracker, route_name='j_tracker')
  
  # config.add_route('j_controller', '/j_controller')
  # config.add_view(j_controller, route_name='j_controller')
  # config.add_view(control_jetbot, route_name='j_controller', request_method='POST')
  
  config.add_route('register', '/register')
  config.add_view(get_register, route_name='register')
  config.add_view(signUp, route_name='register', request_method='POST')
  
  config.add_route('try_again', '/try_again')
  config.add_view(try_again, route_name='try_again')
  
  # config.add_route('instruct_jetbot', '/moves')
  # config.add_view(get_moves, route_name='instruct_jetbot', renderer='json')
  
  # config.add_route('jetbot_return_back_one_finished_move', '/finished_top_pending_move')
  # config.add_view(finished_top_pending_move, route_name='jetbot_return_back_one_finished_move', renderer='json')
  
  # config.add_route('update_start_time', '/update_start_time')
  # config.add_view(update_start_time, route_name='update_start_time', renderer='json')
  
  config.add_route('about', '/about')
  config.add_view(about, route_name='about')
  
  config.add_route('features', '/features')
  config.add_view(features, route_name='features')
  
  # config.add_route('count','/count')
  # config.add_view(count, route_name='count')
  
  config.add_route('price', '/price')
  config.add_view(price, route_name='price')
  
  config.add_route('news','/news')
  config.add_view(news, route_name='news')
  
  config.add_route('parameter','/parameter')
  config.add_view(parameter, route_name='parameter')
  
  config.add_static_view(name='/', path='./templates/public', cache_max_age=3600) #expose the public folder for the CSS file

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()