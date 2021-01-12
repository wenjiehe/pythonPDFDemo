import json
import requests

def main():
    filePath = '/Users/hewenjie/Desktop/江南.txt'
    #一次性读取整个文件内容
    # f = None
    # try:
    #     f = open('/Users/hewenjie/Desktop/江南.txt', 'r', encoding='utf-8')
    #     print(f.read())
    # except FileNotFoundError:
    #     print('无法打开指定的文件')
    # except LookupError:
    #     print('指定了未知的编码')
    # except UnicodeDecodeError:
    #     print('读取文件时解码错误!')
    # finally:
    #     if f:
    #         f.close()
    # with open(filePath, 'r', encoding='utf-8') as f:
    #     print(f.read())
    #通过for-in循环逐行读取
    # with open(filePath, mode='r') as f:
    #     for line in f:
    #         print(line, end='')
    #         # time.sleep(0.5)
    # print()
    #读取文件按行读取到列表中
    # with open(filePath) as f:
    #     lines = f.readlines()
    # print(lines)

    #把数字写入到文件中，如果文件不存在，那么自动创建文件
    # filenames = ('/Users/hewenjie/Desktop/a.txt', '/Users/hewenjie/Desktop/b.txt', '/Users/hewenjie/Desktop/c.txt')
    # fs_list = []
    # try:
    #     for filename in filenames:
    #         fs_list.append(open(filename, 'w', encoding='utf-8'))
    #     for number in range(1, 10000):
    #         if number % 2 == 0:
    #             fs_list[0].write(str(number) + '\n')
    #         elif number % 3 == 0:
    #             fs_list[1].write(str(number) + '\n')
    #         else:
    #             fs_list[2].write(str(number) + '\n')
    # except IOError as ex:
    #     print(ex)
    #     print('写文件时发生出错误!')
    # finally:
    #     for fs in fs_list:
    #         fs.close()
    # print('操作完成')

    #读写二进制文件,复制图片文件
    # try:
    #     with open('/Users/hewenjie/Desktop/120x120.png', 'rb') as fs1:
    #         data = fs1.read()
    #         print(type(data))
    #     with open('/Users/hewenjie/Desktop/suji.png', 'wb') as fs2:
    #         fs2.write(data)
    # except FileNotFoundError as e:
    #     print('指定的文件无法打开')
    # except IOError as e:
    #     print('读写文件时出现错误')
    # print('程序执行结束')

    #把字典或列表以JSON格式保存到文件中
    # dump - 将Python对象按照JSON格式序列化到文件中
    # dumps - 将Python对象处理成JSON格式的字符串
    # load - 将文件中的JSON数据反序列化成对象
    # loads - 将字符串的内容反序列化成Python对象
    # dic = {
    #     "name" : "凌峰",
    #     "age" : 38,
    #     "qq" : 543968493,
    #     "friends" : ["白起", "后羿"],
    #     "cars" : [{"brand" : "BYD", "max_speed" : 180}, {"brand" : "Audi", "max_speed" : 280}, {"brand" : "BWM", "max_speed" : 320}]
    # }
    # try:
    #     with open('/Users/hewenjie/Desktop/data.json', 'w', encoding='utf-8') as fs:
    #         json.dump(dic, fs)
    # except IOError as e:
    #     print(e)
    # print('保存数据完成')

    #get和post请求
    # resp = requests.get('http://api.tianapi.com/txapi/hsjz/index?key=314e9134dcf011febc2b511d1709ef12')
    resp = requests.post('http://api.tianapi.com/txapi/hsjz/index?key=314e9134dcf011febc2b511d1709ef12')
    if resp.text:
        data_model = json.loads(resp.text)
        code = data_model['code']
        print(code)
        if int(code) == 200:
            for news in data_model['newslist']:
                print(news['content'])


if __name__ == '__main__':
    main()