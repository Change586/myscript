--//创建临时表空间
create temporary tablespace TBS_JSNET_temp
tempfile 'D:/app/Administrator/oradata/orcl/TBS_JSNET_temp.dbf' --//Linux下的文件系统
size 64m
autoextend on
next 64m maxsize 2048m
extent management local;
--//创建数据表空间
create tablespace TBS_JSNET
logging
datafile 'D:/app/Administrator/oradata/orcl/TBS_JSNET.dbf' --//Linux下的文件系统
size 64m
autoextend on
next 65m maxsize 2048m
extent management local;

--//创建临时表空间
create temporary tablespace IDX_JSNET_temp
tempfile 'D:/app/Administrator/oradata/orcl/IDX_JSNET_temp.dbf' --//Linux下的文件系统
size 64m
autoextend on
next 64m maxsize 2048m
extent management local;
--//创建数据表空间
create tablespace IDX_JSNET
logging
datafile 'D:/app/Administrator/oradata/orcl/IDX_JSNET.dbf' --//Linux下的文件系统
size 64m
autoextend on
next 65m maxsize 2048m
extent management local;

--//创建用户并指定表空间 用户名和密码均为"test"
create user manager identified by manager
default tablespace TBS_JSNET
temporary tablespace TBS_JSNET_temp;
--//给用户授予权限
grant connect,resource to manager;
