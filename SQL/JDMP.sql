create temporary tablespace jdmp_temp
tempfile '/opt/11g/oracle/oradata/js45ora/jdmp_temp.dbf' --//Linux下的文件系统
size 64m
autoextend on
next 64m maxsize 2048m
extent management local;
--//创建数据表空间
create tablespace jdmp_data
logging
datafile '/opt/11g/oracle/oradata/js45ora/jdmp_data.dbf' --//Linux下的文件系统
size 64m
autoextend on
next 65m maxsize 2048m
extent management local;
--//创建用户并指定表空间 用户名和密码均为"test"
create user jdmp identified by jdmp
default tablespace jdmp_data
temporary tablespace jdmp_temp;
--//给用户授予权限
grant connect,resource to jdmp;
