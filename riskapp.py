from flask import Flask , render_template , request
app = Flask(__name__) # interfacee between by server and my application wsgi
import pickle
from sklearn.preprocessing import StandardScaler
model=pickle.load(open('frisk.pkl','rb'))
scaler=pickle.load(open("scalar.pkl","rb"))
@app.route('/') # bind to an url 
def helloworld():
    return render_template("index.html")
@app.route('/login',methods = ['POST']) # bind to an url 
def admin():
    a = request.form["js"]
    b = request.form["hs"]
    #b = request.form["s"]
    #if (s=='Free'):
    #    s1,s2,s3=1,0,0
    #if (s=='Own'):
    #   s1,s2,s3=0,1,0
    #if (s=='Rent'):
    #    s1,s2,s3=0,0,1
    c = request.form["sa"]
    d = request.form["ca"]
    e = request.form["cra"]
    f = request.form["dh"]
        #Note while passing t see the order of dataset
    t = [[int(f),int(e),int(d),int(c),int(b),int(a)]]
    y=model.predict(scaler.transform(t))
    if(y==0):
        return render_template("index.html", y ="The risk would be "+str(y)+", which is bad.")
    if(y==1):
        return render_template("index.html", y ="The risk would be "+str(y)+", which is good.")
    
@app.route('/user')#url
def user():
    return "hie user"

if __name__ == '__main__' :
    app.run(debug = True)


#<select name = "s">
#<option value = "Free"> Free </option>
#<option value = "Own"> Own </option>
#<option value = "Rent"> Rent </option>
#</select>
#background-image:url('/static/risk.jpg');background-color:Ivory:background-size: cover;height: 100%;