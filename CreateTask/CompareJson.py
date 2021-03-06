#!/usr/bin/python
#_*_encoding:utf-8_*_

import argparse

import json
import sys
import imp

imp.reload(sys)

#sys.setdefaultencoding('utf-8')

def parseArgs():
    description = 'This program is used to output the differences of keys of two json data.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file', help='Given file containing two json data separated by a new line with three semicolons.')
    args = parser.parse_args()
    filename = args.file
    return filename


def readFile(filename):
    content = ''
    f = open(filename)
    for line in f:
        content += line.strip("\n")
    f.close()
    return content

def parseKeys(jsonobj):
    jsonkeys = list()
    addJsonKeys(jsonobj, jsonkeys, '')
    print (jsonkeys)
    return jsonkeys

def addJsonKeys(jsonobj, keys, prefix_key):
    if prefix_key != '':
        prefix_key = prefix_key+'.'
    if isinstance(jsonobj, list):
        addKeysIflist(jsonobj, keys, prefix_key)
    elif isinstance(jsonobj, dict):
        addKeysIfdict(jsonobj, keys, prefix_key)

def addKeysIflist(jsonlist, keys, prefix_key):
    if len(jsonlist) > 0:
        addJsonKeys(jsonlist[0], keys, prefix_key)

def addKeysIfdict(jsonobj, keys, prefix_key):
    for (key, value) in jsonobj.items():
        keys.append(prefix_key + key)
        addJsonKeys(value, keys, prefix_key+key)

def diffKeys(json1, json2):
    keys1 = parseKeys(json1)
    keys2 = parseKeys(json2)
    keyset1 = set(keys1)
    keyset2 = set(keys2)
    return keyset1.difference(keyset2)


def cmpArray(jsonArr1, jsonArr2, diff, prefix_key):
    '''
       need to be improved
    '''
    arrlen1 = len(jsonArr1)
    arrlen2 = len(jsonArr2)
    minlen = min(arrlen1, arrlen2)
    if arrlen1 != arrlen2:
        diff.append((prefix_key+'.length', arrlen1, arrlen2))
    for i in range(0, minlen):
        diffDict(jsonArr1[i], jsonArr2[i], diff, prefix_key)

def cmpPrimitive(key, value1, value2, diff, prefix_key):

    if isinstance(value1,list) or isinstance(value1, dict) \
       or isinstance(value2, list) or isinstance(value2, dict):
       return

    if value1 != value2:
       diff.append((prefix_key + key, str(value1), str(value2)))


def diffDict(json1, json2, diff, prefix_key):

    if prefix_key != '':
        prefix_key = prefix_key+'.'

    for (key, value) in json1.items():
        json2Value = json2.get(key)
        #print "key: ", key, ", value: ", value, " , value2: ", json2Value

        if json2Value == None:
            diff.append((prefix_key + key, value, None))

        if isinstance(value, dict) and isinstance(json2Value, dict):
            diffDict(value, json2Value, diff, prefix_key + key)

        if isinstance(value, list) and isinstance(json2Value, list):
            cmpArray(value, json2Value, diff, prefix_key + key)

        cmpPrimitive(key, value, json2Value, diff, prefix_key)


def diffJson(json1, json2):
    jsondiff = list()
    diffDict(json1, json2, jsondiff, '')
    return jsondiff


def diffJsonToFile(filename, json1, json2):
    f_res = open(filename, 'w')
    diff_res = diffJson(json1, json2)
    for diff in diff_res:
        (key,v1,v2) = diff
        if v2 is None:
            f_res.write('key %s in json1 not in json2. \n' % key)
        else:
            f_res.write('key %s in json1 = %s yet in json2 = %s. \n' %(key, v1, v2))

    f_res.close()


def tesParsetKeysSingle(jsonobj, expected):
    assert set(parseKeys(jsonobj)) == set(expected)

def testParseKeys():
    for v in ({}, [], "good", 1, 3.14, -2.71, -1, 0.1, 2.71E3, 2.71E+3, 2.71E-32, 2.71e3, 2.71e+3, 2.71e-32, True, False, None, "null\n\\\"\/\b\f\n\r\t\\u"):
        tesParsetKeysSingle(parseKeys(v), [])
    tesParsetKeysSingle({"code": 200}, ['code'])
    tesParsetKeysSingle({"code": 200, "msg": "ok", "list": [], "extra":{}}, ['code', 'msg', 'list', 'extra'])
    tesParsetKeysSingle({"code": 200, "msg": "ok", "list": [{"id": 20, "no":"115"}], "extra":{"size": 20, "info": {"owner": "qin"}}}, ['code', 'msg', 'list', 'list..id', 'list..no', 'extra', 'extra.size', 'extra.info', 'extra.info.owner'])
    tesParsetKeysSingle({'msg': 'ok', 'code': 200, 'list': [{'items': [{'price': 21, 'infos': {'feature': ''}, 'name': 'n1'}], 'id': 20, 'no': '1000020'}], 'metainfo': {'total': 20, 'info': {'owner': 'qinshu', 'parts': [{'count': 13, 'time': {'start': 1230002456, 'end': 234001234}}]}}}, ['msg', 'code', 'list', 'list..items', 'list..items..price', 'list..items..infos', 'list..items..infos.feature', 'list..items..name','list..id', 'list..no',  'metainfo', 'metainfo.total', 'metainfo.info', 'metainfo.info.owner', 'metainfo.info.parts', 'metainfo.info.parts..count', 'metainfo.info.parts..time' ,'metainfo.info.parts..time.start', 'metainfo.info.parts..time.end'])

    print('testPassed')


def test():
    testParseKeys()


if __name__ == "__main__":
    json1 = {
"endObjs": [
    {
        "frameIdx": 0,
        "time": 1495703039,
        "trackIdx": "630"
    }
],
"frameHeader": {
    "data": 0,
    "dataLen": 0,
    "flag": 0,
    "height": 0,
    "index": 0,
    "rebackInfo": 0,
    "time": 0,
    "width": 0
},
"resultIdx": "316",
"taskIdx": "201705251703320001000000007",
"type": 3
}
    json2 = {
    "endObjs":[
        {
            "frameIdx":1236,
            "time":1502188067,
            "trackIdx":"46098"
        }
    ],
    "frameHeader":{
        "data":0,
        "dataLen":0,
        "flag":0,
        "height":0,
        "index":1236,
        "rebackInfo":0,
        "time":0,
        "width":0
    },
    "resultIdx":"25319",
    "taskIdx":"201708072107300001000000013",
    "type":3
}



    print (diffKeys(json1,json2))