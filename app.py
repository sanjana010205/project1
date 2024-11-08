from flask import Flask,request,render_template

app = Flask(_name_)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        return render_template('registration.html',name=name)
    return render_template('registration.html')
if _name_=='_main_':
    app.run(host='0.0.0.0',port=5000)