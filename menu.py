from flask import Flask, render_template, request
import json

app = Flask(__name__)

age=0
gender=""
family=0

@app.route('/', methods=['GET', 'POST'])
def index():
    age=request.form.get("age", False)
    gender=request.form.get("gender", False)
    family=request.form.get("family", False)
    data = {
        'age': age,
        'gender': gender,
        'family': family
    }
    my_json = json.dumps(data)
    
    return render_template('index.html', age=age, gender=gender, family=family)