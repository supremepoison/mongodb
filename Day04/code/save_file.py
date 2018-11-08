from mongo import MongoClient
import bson.binary



conn = MongoClient('localhost',27017)

db = conn.image

myset = db.tcp 

#存储图片
f = open('/home/tarena/AID1808/MongoDB/Day04/code/w.PNG','rb')

data = f.read()

#将data转换为mongodb存储格式

content = bson.binary.Binary(data)

#插入到文档
myset.insert({'filename':'tcp.jpg','data':content})

#文件提取
# img = myset.find_one({'filename':'tcp.jpg'})
# print(img)

# #将data写入到本地文件
# with open('/home/tarena/AID1808/MongoDB/Day04/code/ff.jpg','wb') as f:
#     f.write(img['data'])
conn.close()
