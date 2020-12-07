#!/usr/bin/env python3
# encoding: utf-8

from . import log as deployLog
import sys
import MySQLdb as mdb
from .utils import *

log = deployLog.getLocalLogger()

def addFrontToDb():
    # get properties
    mysql_ip = getCommProperties("mysql.ip")
    mysql_port = int(getCommProperties("mysql.port"))
    mysql_user = getCommProperties("mysql.user")
    mysql_password = getCommProperties("mysql.password")
    mysql_database = getCommProperties("mysql.database")
    front_org = getCommProperties("front.org")
    front_port = getCommProperties("front.port")
    fisco_version = getCommProperties("fisco.version")

    try:
        # connect
        conn = mdb.connect(host=mysql_ip, port=mysql_port, user=mysql_user, passwd=mysql_password, database=mysql_database, charset='utf8')
        conn.autocommit(1)
        cursor = conn.cursor()
        
        # add db
        add_db = "INSERT INTO tb_front (node_id,front_ip,front_port,agency,client_version, create_time, modify_time) \
                  VALUES ('init','127.0.0.1',%s,\'%s\',\'%s\', NOW(),NOW())" % \
                  (front_port, front_org, fisco_version)
        log.info(add_db)
        cursor.execute(add_db)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        import traceback
        log.info(" mysql except {}".format(traceback.format_exc()))
        traceback.print_exc()
        sys.exit(0)

def dbConnect():
    # get properties
    mysql_ip = getCommProperties("mysql.ip")
    mysql_port = int(getCommProperties("mysql.port"))
    mysql_user = getCommProperties("mysql.user")
    mysql_password = getCommProperties("mysql.password")
    mysql_database = getCommProperties("mysql.database")

    try:
        # connect
        conn = mdb.connect(host=mysql_ip, port=mysql_port, user=mysql_user, passwd=mysql_password, charset='utf8')
        conn.autocommit(1)
        cursor = conn.cursor()
        
        # check db
        result = cursor.execute('show databases like "%s"' %mysql_database)
        drop_db = 'DROP DATABASE IF EXISTS {}'.format(mysql_database)
        create_db = 'CREATE DATABASE IF NOT EXISTS {}'.format(mysql_database)
        if result == 1:
            info = "n"
            if sys.version_info.major == 2:
                info = raw_input("WeBASE-Node-Manager database {} already exists. Do you want drop and recreate it?[y/n]:".format(mysql_database))
            else:
                info = input("WeBASE-Node-Manager database {} already exists. Do you want drop and recreate it?[y/n]:".format(mysql_database))
            if info == "y" or info == "Y":
                log.info(drop_db)
                cursor.execute(drop_db)
                log.info(create_db)
                cursor.execute(create_db)
        else:
            log.info(create_db)
            cursor.execute(create_db)
        cursor.close()
        conn.close()
    except:
        import traceback
        log.info(" mysql except {}".format(traceback.format_exc()))
        traceback.print_exc()
        sys.exit(0)

def signDbConnect():
    # get properties
    mysql_ip = getCommProperties("sign.mysql.ip")
    mysql_port = int(getCommProperties("sign.mysql.port"))
    mysql_user = getCommProperties("sign.mysql.user")
    mysql_password = getCommProperties("sign.mysql.password")
    mysql_database = getCommProperties("sign.mysql.database")

    try:
        # connect
        conn = mdb.connect(host=mysql_ip, port=mysql_port, user=mysql_user, passwd=mysql_password, charset='utf8')
        conn.autocommit(1)
        cursor = conn.cursor()
        
        # check db
        result = cursor.execute('show databases like "%s"' %mysql_database)
        drop_db = 'DROP DATABASE IF EXISTS {}'.format(mysql_database)
        create_db = 'CREATE DATABASE IF NOT EXISTS {}'.format(mysql_database)
        if result == 1:
            info = "n"
            if sys.version_info.major == 2:
                info = raw_input("WeBASE-Sign database {} already exists. Do you want drop and recreate it?[y/n]:".format(mysql_database))
            else:
                info = input("WeBASE-Sign database {} already exists. Do you want drop and recreate it?[y/n]:".format(mysql_database))
            if info == "y" or info == "Y":
                log.info(drop_db)
                cursor.execute(drop_db)
                log.info(create_db)
                cursor.execute(create_db)
        else:
            log.info(create_db)
            cursor.execute(create_db)
        cursor.close()
        conn.close()
    except:
        import traceback
        log.info(" mysql except {}".format(traceback.format_exc()))
        traceback.print_exc()
        sys.exit(0)
    

def checkMgrDbAuthorized():
    print ("check mgr database user/password...")
    # get properties
    mysql_ip = getCommProperties("mysql.ip")
    mysql_port = int(getCommProperties("mysql.port"))
    mysql_user = getCommProperties("mysql.user")
    mysql_password = getCommProperties("mysql.password")

    try:
        # connect
        conn = mdb.connect(host=mysql_ip, port=mysql_port, user=mysql_user, passwd=mysql_password)
        # conn = mdb.connect(host=mysql_ip, port=mysql_port, user=mysql_user, passwd=mysql_password, database=mysql_database, charset='utf8')
        conn.close()
        print("check finished sucessfully.")        
        log.info("check mgr db user/password correct!")
    except:
        import traceback
        print("======mgr mysql user/password error!======")
        log.info("mgr mysql user/password error {}".format(traceback.format_exc()))
        traceback.print_exc()
        sys.exit(0)


def checkSignDbAuthorized():
    print ("check sign database user/password...")
    # get properties
    mysql_ip = getCommProperties("sign.mysql.ip")
    mysql_port = int(getCommProperties("sign.mysql.port"))
    mysql_user = getCommProperties("sign.mysql.user")
    mysql_password = getCommProperties("sign.mysql.password")

    try:
        # connect
        conn = mdb.connect(host=mysql_ip, port=mysql_port, user=mysql_user, passwd=mysql_password)
        conn.close()
        print("check finished sucessfully.")        
        log.info("check sign db user/password correct!")
    except:
        import traceback
        print("======sign mysql user/password error!======")
        log.info("sign mysql user/password error {}".format(traceback.format_exc()))
        traceback.print_exc()
        sys.exit(0)


if __name__ == '__main__':
    pass
