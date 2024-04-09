from flask import Flask,render_template,request,session,redirect
import mysql.connector as mysql
#change below for MysqlConnection
mydb=mysql.connect(host="PrajwalProject.mysql.services.com",
               user="PrajwalProject" ,
               password="Admin@123" ,
               database="PrajwalProject$Mini_Project",
               autocommit=True)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM NoteUpdate")
myresult = mycursor. fetchall()

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'
@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        uname= request.form.get("username")
        psk=request.form.get("password")
        mycursor.execute(f"SELECT * FROM student  where uname='{uname}' and psk='{psk}' ")
        data =mycursor.fetchall()
        if len(data):
            session["name"]=data[0][1]
            session["id"]=data[0][0]
            return redirect("/NoteApp")
        return "Login Fail"
    return render_template("snippets.html")

@app.route('/register',methods=["GET","POST"])
def reg():
    if request.method == 'POST':
        reqester=request.form
        try:
            ds=mycursor.execute('INSERT INTO student values (default, "{}" , "{}", "{}" , "{}" , {} , {},"{}")'.format(
             reqester.get("name"),reqester.get("uname"),reqester.get("password"),reqester.get("branch"),reqester.get("year"),reqester.get("rolln"),reqester.get("email")))
            return redirect("/login")
        except:
            return "error occour"

    return render_template("reg.html")
@app.route('/NoteApp',methods=["GET","POST"])
def NoteApp():
    useris="guest"
    userid=None
    if "name" in session:
        useris=session["name"]
        userid=session["id"]
    if request.method == 'POST':
        f = request.files['files']
        f.save("/home/PrajwalProject/mysite/static/StudentNote/"+f.filename)
        NoteForm=request.form
        try:
            ds=mycursor.execute('INSERT INTO NoteUpdate values (default, "{}" , "{}", "{}" , "{}" , "{}" , "{}" , {} )'.format(
             NoteForm.get("program"),NoteForm.get("sem"),NoteForm.get("sub"),NoteForm.get("ref"),NoteForm.get("descN"),f"static/StudentNote/{f.filename}",userid))
            ds.commit()
        except:
            pass
        return 'INSERT INTO NoteUpdate values (default, "{}" , "{}", "{}" , "{}" , "{}" , "{}")'.format(NoteForm.get("sub"),NoteForm.get("sem"),NoteForm.get("program"),NoteForm.get("ref"),NoteForm.get("descN"),f"static/StudentNote/{f.filename}")
    mycursor.execute("SELECT * FROM NoteUpdate")
    myresult = mycursor.fetchall()
    return render_template("NoteApp.html",dataTable=myresult,name=useris)
