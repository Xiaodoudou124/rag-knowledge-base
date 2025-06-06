# 1.读取文件内容
with open("中医v1.txt", encoding='utf-8', mode='r') as fp:
    data = fp.read()

# 2.根据换行切割
chunk_list = data.split("\n\n")
chunk_list = [chunk for chunk in chunk_list if chunk]
print(chunk_list)
