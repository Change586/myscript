create temporary tablespace jdmp_temp
tempfile '/opt/11g/oracle/oradata/js45ora/jdmp_temp.dbf' --//Linux�µ��ļ�ϵͳ
size 64m
autoextend on
next 64m maxsize 2048m
extent management local;
--//�������ݱ�ռ�
create tablespace jdmp_data
logging
datafile '/opt/11g/oracle/oradata/js45ora/jdmp_data.dbf' --//Linux�µ��ļ�ϵͳ
size 64m
autoextend on
next 65m maxsize 2048m
extent management local;
--//�����û���ָ����ռ� �û����������Ϊ"test"
create user jdmp identified by jdmp
default tablespace jdmp_data
temporary tablespace jdmp_temp;
--//���û�����Ȩ��
grant connect,resource to jdmp;
