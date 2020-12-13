from flask import Flask, render_template, request
import sqlite3 as sql
from flask import render_template
from flask import Flask, request, jsonify

app = Flask(__name__)
#the first time ip+port:/
#the function go to the student.html
# in the end of the file "student.html" you can see redirct to the address"/addrec "
@app.route('/')
def new_student():
    return render_template('student.html')

#the function save data and the get data from database
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    s_name = ""
    ss_name = ""
    age = ""
    postcode = ""
    phone = ""
    email = ""
    print("request.form",request.form)
    print("requestlen",len(request.form))
    if len(request.form) < 5:
        return jsonify(code=65535, message="param are imcomplete")
    if request.method == 'POST':
       try:
          s_name = request.form['s_name']
          ss_name=s_name
          age = request.form['age']
          postcode = request.form['postcode']
          phone = request.form['phone']
          email = request.form['email']
          # if s_name=="" or age=="" or postcode=="" or phone=="" or email=="":
          #     print("erro")
          #     return jsonify(code=65535, message="参数不完整")
          print(s_name)
          print(age)
          print(postcode)
          print(email)
          with sql.connect("test1.db") as con:
             print("link")
             cur = con.cursor()
             print(cur)
             ##save to database
             yuju='''INSERT INTO students (s_name,age,postcode,phone,email) VALUES ("{}","{}","{}","{}","{}")'''.format(s_name,age,postcode,phone,email)
             print(yuju)
             cur.execute(yuju)
             print("???")
             con.commit()
             msg = "Record successfully added"
             con.close()
       except Exception as e:
           print("erro")
           return jsonify(code=65535, message="参数不完整")
           print(e)
           con.rollback()
       finally:
            con = sql.connect("test1.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            print("s_name", ss_name)
            yuju2 = '''select * from students where s_name="{}"'''.format(s_name)
            print(yuju2)
            cur.execute(yuju2)
            rows = cur.fetchall();
            return render_template("students2.html", data=rows)
            con.close()




if __name__ == '__main__':
    app.run(debug = True)