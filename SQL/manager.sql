--//������ʱ��ռ�
create temporary tablespace TBS_JSNET_temp
tempfile 'D:/app/Administrator/oradata/orcl/TBS_JSNET_temp.dbf' --//Linux�µ��ļ�ϵͳ
size 64m
autoextend on
next 64m maxsize 2048m
extent management local;
--//�������ݱ�ռ�
create tablespace TBS_JSNET
logging
datafile 'D:/app/Administrator/oradata/orcl/TBS_JSNET.dbf' --//Linux�µ��ļ�ϵͳ
size 64m
autoextend on
next 65m maxsize 2048m
extent management local;

--//������ʱ��ռ�
create temporary tablespace IDX_JSNET_temp
tempfile 'D:/app/Administrator/oradata/orcl/IDX_JSNET_temp.dbf' --//Linux�µ��ļ�ϵͳ
size 64m
autoextend on
next 64m maxsize 2048m
extent management local;
--//�������ݱ�ռ�
create tablespace IDX_JSNET
logging
datafile 'D:/app/Administrator/oradata/orcl/IDX_JSNET.dbf' --//Linux�µ��ļ�ϵͳ
size 64m
autoextend on
next 65m maxsize 2048m
extent management local;

--//�����û���ָ����ռ� �û����������Ϊ"test"
create user manager identified by manager
default tablespace TBS_JSNET
temporary tablespace TBS_JSNET_temp;
--//���û�����Ȩ��
grant connect,resource to manager;
