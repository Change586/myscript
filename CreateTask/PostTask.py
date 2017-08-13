#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2

url = 'http://172.18.0.171:80/Task/GetTaskInfo?taskID=201708041949590001000000007'
data = {"dbName":"test",}
req = urllib2.Request(url)
resp = urllib2.urlopen(req)

html = type(resp.read())

print html

json1={
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
    "recogResult": {
        "faceAngle": {
            "pitch": 9.1073789596557617,
            "roll": -2.4049060344696045,
            "yaw": 5.8668875694274902
        },
        "faceRect": {
            "bottom": 100,
            "left": 1168,
            "right": 1236,
            "top": 34
        },
        "feature": "7qpXQpFlAACAAAAANJmRvCxUfj15kGi9W03JPWodyz3gLrw99blLvZcY0b1fZlI9PiwxvrhOfz3y+YS+8SuPO4F9w73YuSc9iPTDvIZxkDynAs49VloHPv8t/z3wx5W9MZXxPWK4p72ij349GftBvDiKyLxJnlO9Jeh3PVNfAb762us8AmjwvY5kQD4qBzW+mUWaPWuopjydVFs9JAtDPTJ4lLy4qhE8s1NKvV6bz71+YOI7HqIAvnNW5725ook9evtQvkc6Dj7p94U9sQpfvYaRQL0wSSY+/Y9PvdaTJD2lLZY8fLUzPRqDDj6pGbY9z8vCPQlcxjxi8Fu9NCZNPemU/j0fg3Y9T14sPcJ5gb2X1jK9em2ivIeTmbyilaE7cWT6PYp6DTxf+2g9/HQovtPDyDzDhBk9K/lVPaaZHb3K4cA9z2ZQPSMb6TzGF9g9L1PBPYSDj71vXp68KlqTPVv4BL481bM8PII1PUt0y725JCw+5TKQPVbcYb2ajSQ8OzcTvtjt+r2ZHAW8FNDXvN1XrT065GA9V8rPvYxzJr45Ogu9cXCQPaqFo71W/JM9skhKPdwnAb7D9gA9oWIAvvfzAL3DTpe8RbY2vkpGB74wj6887pTzvYHTUr2zaYm8tlICPVAJFj4uJP46e6WyvMg2er1Wpaw9OlcjPVMQvD1kiUi9OYbyPbBihL0=",
        "frameIdx": 0,
        "imgHeight": 1088,
        "imgMode": 1,
        "imgUrl": "http://172.18.0.210:18080/g1/M00/00/79/rBIA0lkmnf-AR7dXAAPfn6mdBlA857.jpg",
        "imgWidth": 1920,
        "qualityScore": 0.91852229833602905,
        "similars": [
            {
                "dbId": "123",
                "users": [
                    {
                        "score": 0.85619354248046875,
                        "user_idx": "2235b3794977448d8e931647a101beec"
                    },
                    {
                        "score": 0.59212017059326172,
                        "user_idx": "f1309eef90c04bd286412e41a6ad2641"
                    },
                    {
                        "score": 0.57564687728881836,
                        "user_idx": "149673cc8f5848c39b01a1c6cf1687f1"
                    },
                    {
                        "score": 0.5688931941986084,
                        "user_idx": "6d0ae58ca9ea4e11bc9f6ea8d945cb0b"
                    },
                    {
                        "score": 0.55960923433303833,
                        "user_idx": "840d7a1d92ed4997be656706d6ccf922"
                    }
                ]
            }
        ],
        "taskIdx": "201705251703320001000000007",
        "time": 1495703039,
        "trackIdx": "633"
    },
    "resultIdx": "7307",
    "type": 1
}
    json2 = {
    "frameHeader":{
        "data":0,
        "dataLen":0,
        "flag":0,
        "height":0,
        "index":605,
        "rebackInfo":0,
        "time":0,
        "width":0
    },
    "recogResult":{
        "faceAngle":{
            "pitch":10.563151359558105,
            "roll":8.689367294311523,
            "yaw":-1.7901479005813599
        },
        "faceRect":{
            "bottom":382,
            "left":560,
            "right":640,
            "top":302
        },
        "feature":"7qpXQiVeAAAAAQAAfKwUPQV9uzw/CN+9bpctvSbn0T32moY980VuvekodT0liiM8bQm5vTJnDj5i36S8UpMfvZ1yTLy+1ZG87SEju9lVG77wksS9Ao0cPqPhszw+PKm9WAi2uyqlrT0B3c29ErHsPJVuPb14Pgg+gVy2vLRB2bxMtb879PBPvPBoFL2hg4o9WfKjPQEpGT08+6S9/tCEPS/9ZjqqqFE9QOQoPUEeHL2WVYc9eAmNPa80Aj3sG+M71isDPYiTpr3R6o+9vwEWvb9kE7zo7tK8BuWnvB1Il717hdK8UXOuPflLcb1SsTs9BtFgPWB0k7yNtgK9YqxMPcD8x70Wk7Q9Un3CvCAror2Bk3E8cUSuvdshEr1K8I49u9hxvKsusLxxXYU8LxIrvT3rfr0hMe+8aPIXO+ukybzvRDM9a0qdvTj9VL3EHio9PUhavduMAr3RtEO8O6uiPcVLfbv5pDe9vb2JPPk7A74FNE+9GxOlPHPGrDsSj309AqapPet3Db2ltKY9RsYrPWwwOj3D9cA9bvb/vbNCBr1SV+u8dv5VvILWALxncAi8xvvEu7ZtI70gJhM9Iu8gvrueOT6K/CU754McPSkXBr5EZFg90JaGvUOxhT3iuRQ9ygPcPTWPCr5LXRA9f7g2vIu6AD0MV6a91rXxvDDPjzz6DtS76UyHu0eRHz6BwGC9qWhEPQs7zj1xBRg+5kwKvmQhY70vRnW9/tgwPIfhsr15Hde8zYIfvf1M1jx8uWi95jQYPBTz3rxZsA++AHnNO2XsHL19XKW9ZutLvBoFDD0254Q8j0WBPYIOXr0GA+o8j7X8vEpZsDoqbS+7aR7kvOFIwz0y3M66PvusPVvFiL1DB529ImbjPRlavT0k5Ae97B0PvUjSBTwzni46AxmSPGuWUD2i5Dc9U1vAPepkwjyWOK69Ch2tvOn1I7zqYwE9O15sPYD/x71apCq9ID0RPo5cR72nakm9baxcvT+Rcb0iYtY94bgWPeOV27yda8s8S8OOPWQo1byEQYC82HTwOyIQh73J3G886PGxvUqyHLzMXKC8fMg9vDLtwbqzuau9Rmk8vshlwTzlajK9U+XTvA3OBL4P5Mw8c2moPaKgEb0dbuK9zUsIPKkbjb0vQhk96uBUvUmfS73271e8aZ4dPUPeEbxfB0w94zgfPVdAPbzO7zO9e1waO9mQbj3y0AK8EOINvoE6z7yYOoM88UUUvSZvijvhI2m9nthjPXQfETwm1b894fnhPGNjF73Gv1w9+yr2O0ptCjzWLu87CX0IvTzRpTsniuY7AS4YPfSFBr3OBt873iM6PYhF3b0DOdY8mDqfvNSdlD2nm4Y98sGkvYZn5jxwM5Y9Dvp+PA==",
        "frameIdx":605,
        "imgHeight":1088,
        "imgMode":1,
        "imgUrl":"http://172.18.0.30:18080/g1/M01/CB/B0/rBIAHlmJiBmARTr6AAPEXTK58CI860.jpg",
        "imgWidth":1920,
        "qualityScore":0.4617648422718048,
        "similars":[
            {
                "dbId":"test2",
                "users":[
                    {
                        "score":0.8087414503097534,
                        "user_idx":"03cae68aed874e0385c6f87208ab3bc7"
                    },
                    {
                        "score":0.8087414503097534,
                        "user_idx":"f600c51f68ad44a2ad1cc8bd94c34e53"
                    },
                    {
                        "score":0.665553092956543,
                        "user_idx":"e1eb286f2afd4585b6100f7ad0ffc172"
                    },
                    {
                        "score":0.665553092956543,
                        "user_idx":"702bbbebe3f24d259f38e89c192ffe3c"
                    },
                    {
                        "score":0.6608696579933167,
                        "user_idx":"497732352cbc44b99416a18a945ff9cd"
                    }
                ]
            }
        ],
        "taskIdx":"201708072106540001000000002",
        "time":1502185497,
        "trackIdx":"43957"
    },
    "resultIdx":"453228",
    "type":1
}
    diffjs = diffJson(json1, json2)
    print (diffjs)