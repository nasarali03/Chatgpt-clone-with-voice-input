from flask import Flask, render_template, request, jsonify,session,redirect, url_for,abort
from authlib.integrations.flask_client import OAuth
from flask_pymongo  import PyMongo
from datetime import datetime
from python import googleAuth

import openai
import bcrypt



app=Flask(__name__)
openai.api_key="OpenAi API key"
app.config["SECRET_KEY"]="mysecretkey"
app.config["MONGO_URI"] = "Mongo_URI"
app.config["SERVER_NAME"] = "localhost:5000"
mongo=PyMongo(app)
oauth = OAuth(app)



@app.route("/")
def home():
    session["url"]="/"
    return render_template("home.html")

@app.route("/developers")
def developer():
    session["url"]="/developers"
    return render_template("developers.html")

@app.route("/chatbot",methods=["GET","POST"])
def chatbot():
    if "user" not in session:
        session['url']=""
        session["url"]="/chatbot"
        return redirect(url_for("signin"))
    else:
        if request.method=="POST":
            try:
                question=request.json.get("question")
                email=session['user']
                
                chat=mongo.db.chats.find_one({"question":question})
                if chat:
                    data={"answer":f"{chat['answer']}"}
                else:
                    print(question)
                    response=openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role":"user","content":question}],
                    temperature=0.2,
                    max_tokens=1000,
                )
                    
                    answer = response["choices"][0]["message"]["content"]
                    print(answer)
                    data={"answer":answer}
                    mongo.db.chats.insert_one({"email":email,"question":question,"answer":answer})
                return jsonify(data)
            except Exception as e:
                return jsonify({"error": str(e)})
        return render_template("chatbot.html")

@app.route("/image",methods=["GET","POST"])
def getImage():
    email=session['user']
    user=mongo.db.Users.find_one({"email":email})
    image=user.get("image")
    return jsonify({"image":image})

@app.route("/signup", methods=["GET","POST"])
def signup():
    if "user" in session:
        url=session['url']
        
        return redirect(url)
    else:
        if request.method=="POST":
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
        
            if len(password)<8:
                return jsonify({"error":"Your password must be at least 8 characters long","type":"passowrd"})
            
            has_upper=any(char.isupper() for char in password)
            has_digit=any(char.isdigit() for char in password)

            if not has_upper:
                return jsonify({"error":"Your password must contain at least one uppercase letter","type":"password"})
            if not has_digit:
                return jsonify({"error":"Please add at least one digit to your password","type":"password"})
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            hashed_password=hashed_password.decode('utf-8')
            profile_img = googleAuth.get_gravatar_url(email)
            user=mongo.db.Users.find_one({"email":email})

            if googleAuth.is_valid_email(email):
                if user is None:
                    data={
                        "name":name,
                        "email":email,
                        "password":hashed_password,
                        "date":datetime.now(),
                        "image":profile_img
                    }
                    session['user']=email
                    mongo.db.Users.insert_one(data)
                    url=session['url']
                    session.pop('url',None)
                    return redirect(url)
                else:
                    message = "The user with this email is already exist"
                    print(message)
                    return jsonify({"error": message, "type": "email"})
            else:
                message = "Please enter a valid email address"
                print(message)
                return jsonify({"error": message, "type": "email"})

        return render_template("register.html")




@app.route("/signin",methods=["GET","POST"])
def signin():

    if request.method=="POST":
        email = request.form['emails']
        password = request.form['passwords']
        print(email,password)
        if len(password)<8:
            return jsonify({"error":"Your password must be at least 8 characters long","type":"passowrd"})
            
        
        hash_password=password.encode('utf-8')
        user=mongo.db.Users.find_one({"email":email})
        if user and bcrypt.checkpw(hash_password,user["password"].encode('utf-8')):
            session['user']=email
            url=session['url']
            session.pop('url',None)
            return redirect(url)
        else:
            return jsonify({"error":"Invalid Credentials","type":"password"})
    return render_template("register.html")



@app.route("/google/")
def google_login():
    
    GOOGLE_CLIENT_ID = (
            "Google_client_id"
        )
    GOOGLE_secrete_ID = "google_secrete_id"
    CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"

    oauth.register(
            name="google",
            client_id=GOOGLE_CLIENT_ID,
            client_secret=GOOGLE_secrete_ID,
            client_kwargs={
                "scope": "profile email" 
            },
            server_metadata_url=CONF_URL,
            base_url="https://www.googleapis.com/oauth2/v1/certs",
            # access_token_method="POST",
        )
    if "user" in session:
        abort(404)
    redirect_uri = url_for("google_auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route("/google/auth/")
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, None)
    
    email=user['email']
    name=user['name']
    password=googleAuth.generate_password(10)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_password=hashed_password.decode('utf-8')
    profile_img = user['picture']
    print(profile_img)
    User=mongo.db.Users.find_one({"email":email})
    if User is None:
        data={
            "name":name,
            "email":email,
            "password":hashed_password,
            "date":datetime.now(),
            "image":profile_img
        }
        mongo.db.Users.insert_one(data)
        url=session['url']
        session.pop('url',None)
        return redirect(url)
    else:
        session['user']=email
        url=session['url']
        session.pop('url',None)
        return redirect(url)
    


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/logout")
def logout():
    session.pop('user',None)
    url=session['url']
    session.pop('url',None)
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)