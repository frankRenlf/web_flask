from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
import json

# 创建对象的基类
Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'
    username = Column(String(30), primary_key=True)
    password = Column(String(30))


# admin类
class Admin(Base):
    __tablename__ = 'admin'
    username = Column(String(30), primary_key=True)
    password = Column(String(30))


class Event(Base):
    __tablename__ = 'event'
    title = Column(String(200), primary_key=True)
    isFinished = Column(Integer)


class Detail(Base):
    __tablename__ = 'detail'
    title = Column(String(200), primary_key=True)
    decription = Column(String(300))
    deadline = Column(String(100))
    mask = Column(Integer)


class Events(Base):
    __tablename__ = 'events'
    username = Column(String(20), primary_key=True)
    title = Column(String(20), primary_key=True)
    description = Column(String(300))
    deadline = Column(String(20))
    mask = Column(Integer)
    flag = Column(Integer)


# 初始化数据库连接

# root 用户名  1-9 密码，  127.0.0.1
engine = create_engine('mysql+pymysql://root:123456''@127.0.0.1:3306/toDoList?charset=utf8')

# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)


# #插入数据
# # 创建session对象
# session = DBSession()
# new_admin = Admin(admin_id='admin2',password='123456')
# # 添加到session
# session.add(new_admin)
# #提交
# session.commit()
# # 关闭
# session.close()


# #查询数据
# # 创建session对象
# session = DBSession()
# admin = session.query(Admin).filter(Admin.admin_id=='admin2').one()
#
# print('type',type(admin))
# print('admin_id',admin.admin_id)
# print('password',admin.password)
# print('table_name',admin.__tablename__)

# results = engine.connect().execute('select m1.`id`,m1.`path`,m1.`component`,m1.`name`,m2.`component` as component2,m2.`name` as name2,m2.`path` as path2 from menu m1,menu m2 where m1.`id`=m2.`parentId` order by m1.`id`,m2.`id`')
# for result in results:
#     print(result)

def login(username, password):
    session = DBSession()
    try:
        account = session.query(Account).filter(Account.username == username, Account.password == password).one()
    except BaseException:
        account = None
    print(account)
    if account != None:
        session.close()
        return True
    else:
        session.close()
        return False


def adminLogin(username, password):
    session = DBSession()
    try:
        admin = session.query(Admin).filter(Admin.username == username, Admin.password == password).one()
    except BaseException:
        admin = None
    if admin != None:
        session.close()
        return True
    else:
        session.close()
        return False


def register(usern, passw):
    session = DBSession()
    account = session.query(Account).filter(Account.username == usern).all()
    print('10080' + usern)
    if len(account):
        message = {'status': 1, 'message': '该账号已注册'}
    else:
        new_account = Account(username=usern, password=passw)
        session.add(new_account)
        session.commit()
        message = {'status': 0}
        session.close()
        # message = {'status': 1, 'message': '注册失败'}
    return message


def findEvent(usern, flag):
    session = DBSession()
    affairList = session.query(Events).filter(Events.username == usern, Events.flag == flag).all()
    returnResult = {'code': 0, 'msg': '', 'count': 10}
    eventList = []
    for item in affairList:
        event = {'username': item.username, 'title': item.title, 'description': item.description,
                 'deadline': item.deadline, 'mask': item.mask, 'flag': item.flag}
        eventList.append(event)
    returnResult['data'] = eventList
    return json.dumps(returnResult, ensure_ascii=False)


# 管理员查找所有事务
def findAllEvents():
    session = DBSession()
    affairList = session.query(Events).all()
    returnResult = {'code': 0, 'msg': '', 'count': 10}
    eventList = []
    for item in affairList:
        event = {'username': item.username, 'title': item.title, 'description': item.description,
                 'deadline': item.deadline, 'mask': item.mask, 'flag': item.flag}
        eventList.append(event)
    returnResult['data'] = eventList
    return json.dumps(returnResult, ensure_ascii=False)


# 删除事务
def delAffair(username, title):
    session = DBSession()
    session.query(Events).filter(Events.username == username, Events.title == title).delete()
    session.commit()
    session.close()


# 更改事务
def editAffair(username, title, field, value):
    session = DBSession()
    affair = session.query(Events).filter(Events.username == username, Events.title == title).first()
    if field == 'description':
        affair.description = value
    elif field == 'deadline':
        affair.deadline = value
    elif field == 'mask':
        affair.mask = value
    elif field == 'flag':
        affair.flag = value
    session.commit()
    session.close()


# 增加事务
def addAffair(username, title, description, deadline, mask, flag):
    session = DBSession()
    events = Events(username=username, title=title, description=description, deadline=deadline, mask=mask, flag=flag)
    session.add(events)
    session.commit()
    session.close()


# def stucdent_login(student_id,password):
#     session=DBSession()
#     student=session.query(Student).filter(Student.student_id==student_id,Student.password==password).all()
#     length =len(student)
#     if length==0:
#         session.close()
#         return False
#     else:
#         session.close()
#         return True
#
#
# def getStudentProfileByStudent_id(student_id):
#     session=DBSession()
#     studentProfile=session.query(StudentProfile).filter(StudentProfile.student_id==student_id).first()
#     session.close()
#     return studentProfile
#
# def getAllMembers(username):
#     session=DBSession()
#     allMembers=session.query(StudentProfile).filter(StudentProfile.username!=username).all()
#     if len(allMembers)==0:
#         return False
#     return allMembers
#
#
# def formatMembers(allMembers):
#     membersList=[]
#     for member in allMembers:
#         memberDict={'username':member.username,'userface':member.userface}
#         membersList.append(memberDict)
#     result=json.dumps(membersList,ensure_ascii=False)
#     return result
#
#
# def getAllRoomMatesInf(student_id,building_name,room_name):
#     session=DBSession()
#     allRomatesInf=session.query(StudentProfile).filter(StudentProfile.student_id != student_id , StudentProfile.building_name==building_name , StudentProfile.room_name==room_name).all()
#     session.close()
#     if(len(allRomatesInf)==0):
#         return False
#     else:
#         allRomatesInf=formatRMMembers(allRomatesInf)
#         return allRomatesInf
#
#
# def formatRMMembers(allMembers):
#     membersList=[]
#     for member in allMembers:
#         memberDict={'username':member.username,'userface':member.userface,'student_id':member.student_id}
#         membersList.append(memberDict)
#     result=json.dumps(membersList,ensure_ascii=False)
#     return result

