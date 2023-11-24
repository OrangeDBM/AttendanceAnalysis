# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,redirect,session,Blueprint,make_response
from io import BytesIO
import xlwt
import pymysql
#导入数据库操作类
import os
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
#from werkzeug.wsgi import SharedDataMiddleware
from paste.translogger import TransLogger
from waitress import serve
import logging
import logging.handlers
LOG_FILE = "flask_hkcq_access.log"
log_format = "[%(levelname)s] %(asctime)s [%(filename)s:%(lineno)d, %(funcName)s] %(message)s"
logging.basicConfig(filename=LOG_FILE,
                    filemode="a",
                    format=log_format,
                    level=logging.INFO)
time_hdls = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=7)
logging.getLogger().addHandler(time_hdls)
logging.info("begin service")
import requests
DEPLOY_PORT = 5004

from sql_lianjie import Mysql
app = Flask(__name__)

app.secret_key='QWERTYUIOP' #对用户信息加密

@app.route('/login',methods=['GET',"POST"]) #路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。

def login():
    if request.method=='GET':
        return  render_template('login.html')
    user=request.form.get('user')
    pwd=request.form.get('pwd')
    if user=='admin' and pwd=='123':#这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        session['user_info']=user
        return redirect('/xzz')
    elif user=='lijuan' and pwd=='123':#这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        session['lijuan']=user
        return redirect('/lijuan')
    else:
        return  render_template('login.html',msg='用户名或密码输入错误')


@app.route("/xzz",methods=['GET','POST'])
def zongbu():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    #调用
    db = Mysql()
    results = db.getdata()
    return render_template("xzz_sql_select.html",results=results)

@app.route("/xzz/kaoqin",methods=['GET','POST'])  # type: ignore

def zongbu_xzz_kaoqin():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form
        #db = Mysql()
        #db.insertdata_lijuan(results)
        #return render_template("lijuan_result_insert.html",results=results)
        #调用
        db = Mysql()
        results = db.getdata_kaoqin(results)
        return render_template("xzz_sql_select_kaoqin.html",results=results)

@app.route("/xzz/kaoqin_daochu",methods=['GET','POST'])  # type: ignore

def zongbu_xzz_kaoqin_daochu():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form

        db = Mysql()
        results = db.getdata_kaoqin(results)
        #return render_template("lijuan_sql_select_kaoqin.html",results=results)
        
        fields = ['单位名称','部门','岗位名称','结果','姓名','考勤卡号','日期','超时外出次数','超时外出时间','刷卡时间']
        #fields = ['a11','a12','a13',"a14","a15","a16","a17","a18","a19","a20"]
        # 实例化，有encoding和style_compression参数
        #new = xlwt.Workbook(encoding='utf-8')
        new = xlwt.Workbook(encoding='utf-8')  #.encode('latin1').decode('gbk')
        # Workbook的方法，生成.xls文件
        sheet = new.add_sheet('考勤', cell_overwrite_ok=True)
        # 写上字段信息
        #for field in range(0, len(fields)):
        #    sheet.write(0, field, fields[field][0])
        for col, field in enumerate(fields):  # 写入excel表头
            sheet.write(0, col, field)

            # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row - 1][col])

        sio = BytesIO()
        new.save(sio)  # 将数据存储为bytes
        sio.seek(0)
        response = make_response(sio.getvalue())
        response.headers['Content-type'] = 'application/vnd.ms-excel'  # 响应头告诉浏览器发送的文件类型为excel
        response.headers['Content-Disposition'] = 'attachment; filename=kaoqin.xls'  # 浏览器打开/保存的对话框，data.xlsx-设定的文件名
        return response

@app.route("/xzz/kaoqin_daochu_gonghao",methods=['GET','POST'])  # type: ignore

def zongbu_xzz_kaoqin_gonghao_daochu():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form

        db = Mysql()
        results = db.getdata_kaoqin_gonghao(results)
        #return render_template("lijuan_sql_select_kaoqin.html",results=results)
        
        fields = ['单位名称','部门','岗位名称','结果','姓名','考勤卡号','日期','超时外出次数','超时外出时间','刷卡时间']
        #fields = ['a11','a12','a13',"a14","a15","a16","a17","a18","a19","a20"]
        # 实例化，有encoding和style_compression参数
        #new = xlwt.Workbook(encoding='utf-8')
        new = xlwt.Workbook(encoding='utf-8')  #.encode('latin1').decode('gbk')
        # Workbook的方法，生成.xls文件
        sheet = new.add_sheet('考勤', cell_overwrite_ok=True)
        # 写上字段信息
        #for field in range(0, len(fields)):
        #    sheet.write(0, field, fields[field][0])
        for col, field in enumerate(fields):  # 写入excel表头
            sheet.write(0, col, field)

            # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row - 1][col])

        sio = BytesIO()
        new.save(sio)  # 将数据存储为bytes
        sio.seek(0)
        response = make_response(sio.getvalue())
        response.headers['Content-type'] = 'application/vnd.ms-excel'  # 响应头告诉浏览器发送的文件类型为excel
        response.headers['Content-Disposition'] = 'attachment; filename=kaoqin.xls'  # 浏览器打开/保存的对话框，data.xlsx-设定的文件名
        return response

@app.route("/xzz/submit_insert")
def submit_insert():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template("xzz_sql_insert.html")
    
@app.route("/xzz/insert",methods=['GET','POST'])  # type: ignore
def insert():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form
        db = Mysql()
        db.insertdata(results)
        return render_template("xzz_result_insert.html",results=results)

@app.route("/xzz/submit_update")
def submit_update():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template("xzz_sql_update.html")
    
@app.route("/xzz/update",methods=['GET','POST'])  # type: ignore
def update():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form
        db = Mysql()
        db.updatedata(results)
        return render_template("xzz_result_update.html",results=results)

@app.route("/xzz/delete")
def delete():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    id = request.args.get("id")
    db = Mysql()
    db.deletedata(id)
    return render_template("xzz_result_delete.html",id=id)

@app.route("/lijuan",methods=['GET','POST'])

def zongbu_lijuan():
    user_info=session.get('lijuan')
    if not user_info:
        return redirect('/login')
    #调用
    db = Mysql()
    results = db.getdata_lijuan()
    return render_template("lijuan_sql_select.html",results=results)

@app.route("/lijuan/kaoqin",methods=['GET','POST'])  # type: ignore

def zongbu_lijuan_kaoqin():
    user_info=session.get('lijuan')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form
        #db = Mysql()
        #db.insertdata_lijuan(results)
        #return render_template("lijuan_result_insert.html",results=results)
        #调用
        db = Mysql()
        results = db.getdata_kaoqin_lijuan(results)
        return render_template("lijuan_sql_select_kaoqin.html",results=results)

@app.route("/lijuan/kaoqin_daochu",methods=['GET','POST'])  # type: ignore

def zongbu_lijuan_kaoqin_daochu():
    user_info=session.get('lijuan')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form

        db = Mysql()
        results = db.getdata_kaoqin_lijuan(results)
        #return render_template("lijuan_sql_select_kaoqin.html",results=results)
        
        fields = ['单位名称','部门','岗位名称','结果','姓名','考勤卡号','日期','超时外出次数','超时外出时间','刷卡时间']
        #fields = ['a11','a12','a13',"a14","a15","a16","a17","a18","a19","a20"]
        # 实例化，有encoding和style_compression参数
        #new = xlwt.Workbook(encoding='utf-8')
        new = xlwt.Workbook(encoding='utf-8')  #.encode('latin1').decode('gbk')
        # Workbook的方法，生成.xls文件
        sheet = new.add_sheet('考勤', cell_overwrite_ok=True)
        # 写上字段信息
        #for field in range(0, len(fields)):
        #    sheet.write(0, field, fields[field][0])
        for col, field in enumerate(fields):  # 写入excel表头
            sheet.write(0, col, field)

            # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row - 1][col])

        sio = BytesIO()
        new.save(sio)  # 将数据存储为bytes
        sio.seek(0)
        response = make_response(sio.getvalue())
        response.headers['Content-type'] = 'application/vnd.ms-excel'  # 响应头告诉浏览器发送的文件类型为excel
        response.headers['Content-Disposition'] = 'attachment; filename=newlist.xls'  # 浏览器打开/保存的对话框，data.xlsx-设定的文件名
        return response

@app.route("/lijuan/submit_insert")
def submit_insert_lijuan():
    user_info=session.get('lijuan')
    if not user_info:
        return redirect('/login')
    return render_template("lijuan_sql_insert.html")
    
@app.route("/lijuan/insert",methods=['GET','POST'])  # type: ignore
def insert_lijuan():
    user_info=session.get('lijuan')
    if not user_info:
        return redirect('/login')
    if request.method == "POST":
        results = request.form
        db = Mysql()
        db.insertdata_lijuan(results)
        return render_template("lijuan_result_insert.html",results=results)

@app.route("/lijuan/delete")
def delete_lijuan():
    user_info=session.get('lijuan')
    if not user_info:
        return redirect('/login')
    id = request.args.get("id")
    db = Mysql()
    db.deletedata_lijuan(id)
    return render_template("lijuan_result_delete.html",id=id)

#if __name__ == "__main__":
#    app.run(app.run(debug=True,port=5002,host='0.0.0.0'))

@app.route('/')
def index():
  # 这样写日志
  logging.info("myendpoint We are computering now")
  return 'We are computering now'

@app.route('/server_status_code')
def server_status_code():
  """用于探活"""
  return "ok"


def process_is_alive():
  """检测本地进程是否存在"""
  try:
    r = requests.get(f"http://127.0.0.1:{DEPLOY_PORT}/server_status_code")
    if r.status_code == 200 and r.text == "ok":
      return True
    return False
  except Exception as e:
    return False

if __name__ == "__main__":
    logging.info("try check and start app, begin")
    if process_is_alive():
        logging.info("process_is_alive_noneed_begin")
    else:
        logging.info("process_is_not_alive_begin_new")
        serve(TransLogger(app, setup_console_handler=False), host='0.0.0.0', port=DEPLOY_PORT, threads=30)  # WAITRESS!
        #serve(app, host='0.0.0.0', port=DEPLOY_PORT, threads=30)  # WAITRESS!
    logging.info("try check and start app, end")