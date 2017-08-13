#!/usr/bin/python
# -*- coding: utf-8 -*-

imageDatas=[]

for i in xrange(3564,3583):
    imageData='-F imageDatas=@'+str(i)+'.jpg'
    imageDatas.append(imageData)

print ' '.join(imageDatas)

