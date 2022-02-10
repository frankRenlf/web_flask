# import redis   # 导入redis 模块
#
# r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
# #r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
#
# # r.set('xiesuper', 'xmh123')  # 设置 name 对应的值
# # print(r['xiesuper'])
# # # print(r.get('name'))  # 取出键 name 对应的值
# # # print(type(r.get('name')))  # 查看类型
# #
# # print(r.exists('flag'))
#
# # r.hset("xiesuper","username","value")
# # username=r.hget("xiesuper","username")
# # print(username)
# # print(r.exists("da"))
# def ifExistUsername(username):
#     return r.exists(username)
#
# def ifFindPasswordByUsername(username):
#     return r.get(username)
#
# def ifExistPerInf(student_id):
#      flag=r.exists(student_id)
#      if flag==0:
#          return False
#      else:
#          list=[]
#          list.append(r.hget(student_id,"student_id"))
#          list.append(r.hget(student_id,"username"))
#          list.append(r.hget(student_id,"building_name"))
#          list.append(r.hget(student_id,"phone"))
#          list.append(r.hget(student_id,"room_name"))
#          list.append(r.hget(student_id,"userface"))
#          list.append(r.hget(student_id,"sex"))
#          list.append(r.hget(student_id,"major"))
#          list.append(r.hget(student_id,"grade"))
#          list.append(r.hget(student_id,"class_"))
#
#
#          return list
#
# def storgeProfile(profile):
#     r.hmset(profile.get('student_id'),{'student_id':profile.get('student_id'),'username':profile.get('username'),'building_name':profile.get('building_name'),'phone':profile.get('phone'),'room_name':profile.get('room_name'),'userface':profile.get('userface'),'sex':profile.get('sex'),'major':profile.get('major'),'grade':profile.get('grade'),'class_':profile.get('class_')})
#
#
#
# # r.hdel('2507062649','student_id','username','building_name','phone','room_name','userface')
#
# if __name__=='__main__':
#     #r.set('xiesuper', 'xmh123')  # 设置 name 对应的值
#     print(r['xiesuper'])