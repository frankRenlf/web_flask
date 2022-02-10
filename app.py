from flask import Flask, request, render_template, session
# import sys
# sys.path.append("/database")
from database.sqlalchemyDemo import login as lg, register as reg, findEvent, delAffair, editAffair, addAffair, \
    adminLogin as adminLg, findAllEvents as finAllAffair
from common.CommonResponse import CommonResponse
# from common.RedisConfig import ifExistUsername,ifFindPasswordByUsername
# from bean.Menu import menulist
import json

# from common.RedisConfig import ifExistPerInf,storgeProfile

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'


@app.route('/account/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if lg(username, password):
        session['username'] = username
        return render_template("account/account_main.html")
    else:
        return render_template("index.html", errorMsg='用户名或密码不正确')


@app.route('/account/mainPage')
def mainPage():
    return render_template("account/account_main.html")


@app.route('/admin/mainPage')
def adminMainPage():
    return render_template("admin/admin_main.html")


@app.route('/account/register', methods=['POST'])
def register():
    usern = request.form.get('username')
    passw = request.form.get('password')
    print(usern + passw)
    res = reg(usern, passw)
    if res['status'] == 0:
        return render_template("index.html", msg='注册成功')
    else:
        return render_template("index.html", msg='由于某些原因，注册失败')


@app.route('/account/undoneAffair', methods=['GET'])
def copeUnDoneAffair():
    return render_template('account/undoneAffair.html')


@app.route('/account/doneAffair', methods=['GET'])
def copeDoneAffair():
    return render_template('account/doneAffair.html')


# 根据用户名找到所有符合类型的事务
@app.route('/account/findEvents', methods=['GET'])
def findEvents():
    flag = request.args['flag']
    username = session['username']

    affairList = findEvent(username, flag)
    print(affairList)
    return affairList


# 管理员事务查找界面
@app.route('/admin/allAffairs', methods=['GET'])
def findAllAffairs():
    return render_template('admin/allAffair.html')


# 管理员查看所有事务
@app.route('/admin/findAllEvents', methods=['GET'])
def findAllEvent():
    # username = session['username']
    affairList = finAllAffair()
    print(affairList)
    return affairList


# 删除事务接口
@app.route('/account/delEvent', methods=['GET'])
def delEvent():
    title = request.args['title']
    username = session['username']
    # username = '2507062649'
    delAffair(username, title)
    return render_template('account/undoneAffair.html')


# 更改事务接口
@app.route('/account/editEvent', methods=['GET'])
def editEvent():
    title = request.args['title']
    field = request.args['field']
    value = request.args['value']
    category = request.args['category']
    username = session['username']
    # username = '2507062649'
    editAffair(username, title, field, value)
    if category == 'undone':
        return render_template('account/undoneAffair.html')
    else:
        return render_template('account/doneAffair.html')


# 增加事务
@app.route('/account/addEvent', methods=['POST'])
def addEvent():
    title = request.form.get('title')
    username = session['username']
    # username = '2507062649'
    description = request.form.get('description')
    deadline = request.form.get('deadline')
    mask = request.form.get('mask')
    flag = request.form.get('flag')
    addAffair(username, title, description, deadline, mask, flag)
    return render_template('account/undoneAffair.html')


# 进入管理员登陆界面
@app.route('/account/admin')
def adminLoginPage():
    return render_template('admin/adminLogin.html')


@app.route('/admin/login', methods=['POST'])
def adminLogin():
    username = request.form.get('username')
    password = request.form.get('password')
    if adminLg(username, password):
        session['adminUsername'] = username
        return render_template("admin/admin_main.html")
    else:
        return render_template("admin/adminLogin.html", errorMsg='用户名或密码不正确')


# app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'
# @app.route('/student/login',methods=['POST'])
# def login():
#     student_id=request.form.get('student_id')
#     password=request.form.get('password')
#     flag = stucdent_login(student_id, password)
#     if flag == True:
#         #session['username'] = student_id  session中存取用户名，此处替代为在redis中存储
#         # return render_template('common/main.html')
#         response = CommonResponse(200, "账号密码正确")
#         return json.dumps(response.__dict__, ensure_ascii=False)  # ensure_ascii=False 表示不会用ASCII编码，使中文正常显示
#     else:
#         # return render_template('index.html', errorMsg='用户名或密码不正确')
#         response = CommonResponse(200, "账号或密码错误")
#         return json.dumps(response.__dict__, ensure_ascii=False)
#     # flag=ifExistUsername(username)
#     # if flag == True:
#     #     tem_password_flag=ifFindPasswordByUsername(username)
#     #     if tem_password_flag==password:
#     #         response = CommonResponse(200,"账号密码正确",{})
#     #         return json.dumps(response.__dict__,ensure_ascii=False) #ensure_ascii=False 表示不会用ASCII编码，使中文正常显示
#     #     else:
#     #         response = CommonResponse(200,"账号或密码错误",{})
#     #         return json.dumps(response.__dict__,ensure_ascii=False)
#
# @app.route('/student/perInf',methods=['POST'])
# def getStudentProfileByStudent_id():
#     student_id=request.form.get('student_id')
#     IfInRedis=ifExistPerInf(student_id)
#     if IfInRedis != False:
#         profile = {'student_id': IfInRedis[0],
#                    'username': IfInRedis[1],
#                    'building_name': IfInRedis[2],
#                    'phone': IfInRedis[3],
#                    'room_name': IfInRedis[4],
#                    'userface': IfInRedis[5],
#                    'sex': IfInRedis[6],
#                    'major': IfInRedis[7],
#                    'grade': IfInRedis[8],
#                    'class_': IfInRedis[9]
#                    }
#     else:
#         studentProfile =getStudentProfile(student_id)
#         if studentProfile==None:
#             response=CommonResponse(404,"不存在该student_id的信息")
#             return json.dumps(response.__dict__,ensure_ascii=False)
#         else:
#             profile = {'student_id': studentProfile.student_id,
#                        'username': studentProfile.username,
#                        'building_name': studentProfile.building_name,
#                        'phone': studentProfile.phone,
#                        'room_name': studentProfile.room_name,
#                        'userface': studentProfile.userface,
#                        'sex':studentProfile.sex,
#                        'major':studentProfile.major,
#                        'grade':studentProfile.grade,
#                        'class_':studentProfile.class_
#
#                        }
# #            storgeProfile(profile)
#     response=CommonResponse(200,"学生信息查询成功",**profile)
#     return json.dumps(response.__dict__,ensure_ascii=False)
#
# @app.route('/student/rmInf',methods=['GET'])
# def getRoomMateInf():
#     student_id=request.args.get('student_id')
#     building_name=request.args.get('building_name')
#     room_name=request.args.get('room_name')
#     result=getAllRoomMatesInf(student_id,building_name,room_name)
#     if(result==False):
#         response = CommonResponse(404, "不存在该学生舍友信息")
#         return json.dumps(response.__dict__, ensure_ascii=False)
#     else:
#         return result
#
# @app.route('/getAllMembers',methods=['POST'])
# def getAllMembers():
#     username=request.form.get('username')
#     allMembers=getMembers(username)
#     if allMembers==False:
#         response = CommonResponse(404,"查不到其余成员信息")
#     else:
#         resultFormat=formatMembers(allMembers)
#         return resultFormat
#
#
#
# @app.route('/config/sysmenu',methods=['GET'])
# def getMenu():
#     menuListJson=json.dumps(menulist)
#     return menuListJson
#
# # # @app.route('/student/personInf',methods=['GET'])
# # # def showPersonInf():
# # #     student_id=session['student_id']
# # #     print(student_id)
#


if __name__ == '__main__':
    app.run(debug=True, port=8085)
