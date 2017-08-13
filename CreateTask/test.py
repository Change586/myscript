#import json

from urllib import request,parse
import json


# 封装HTTP POST请求方法
def get(host,port,url,params):
    params = parse.urlencode(params)
    url = 'http://' + host + ':' + str(port) + url + params
    print (url)
    try:
        response = request.urlopen(url)
        response = response.read().decode('utf-8')
        json_response = json.loads(response)
        # print (json_response)
        return json_response
    except Exception as e:
        print('%s' % e)
        return {}

# 封装HTTP GET请求方法
def post(host,port,url,datas):
    datas = parse.urlencode(datas).encode('utf-8')  # 将参数转为url编码字符串
    req = 'http://' + host + ':' + str(port) + url
    print (req)
    try:
        response = request.urlopen(req,datas)
        response = response.read().decode('utf-8')  ## decode函数对获取的字节数据进行解码
        json_response = json.loads(response)  # 将返回数据转为json格式的数据
        print (json_response)
        return json_response
    except Exception as e:
        print('%s' % e)
        return {}

def post2(host,port,url,datas):
    datas = parse.urlencode(datas).encode('utf-8')  # 将参数转为url编码字符串
    req = 'http://' + host + ':' + str(port) + url
    print (req)
    datas = json.dumps(datas)
    datas = bytes(datas,'utf8')
    try:
        response = request.urlopen(req,datas)
        response = response.read().decode('utf-8')
        json_response = json.loads(response)  # 将返回数据转为json格式的数据
        print (response)
        return response
    except Exception as e:
        print('%s' % e)
        return {}

if __name__ == '__main__':
    host = '172.18.0.30'
    port = '80'
    # url = '/verify/target/add'
    # datas = {'dbName':'autotest2'}
    # resp = post(host,port,url,datas)
    # print (resp)

    # get_task_url = '/verfy/Task/GetTaskInfo?'
    # params = {'taskID':'201708041736080001000000016'}
    # task_info = get(host,port,get_task_url,params)
    # print (task_info)

    get_taskinfo_url = "/Task/QueryResource?"
    params = {"ProjectID":1000}
    taskinfo = get(host,port,get_taskinfo_url,params)

    taskIds = taskinfo["taskIds"]
    print (taskIds)
    for task in taskIds:
        del_task_url = "/Task/DeleteTask"
        datas = {"taskID":task}
        # print (datas)
        post2(host,port,del_task_url,datas)
        break


    # url = '/verify/face/deletes'
    # datas = {'dbName':'test2','imageId':'2e82743f58e8478e9a6aa928f66c3ab4'}
    # resp = post(host,port,url,datas)
    # print (resp)