from flask import Flask,render_template,request
import requests,json,urllib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    features=[x for x in request.form.values()]
    age = request.form['age']
    job= request.form['job']
    mar = request.form['mar']
    edu = request.form['edu']
    deff = request.form['deff']
    house=request.form['house']
    loan=request.form['loan']
    contact = request.form['contact']
    month = request.form['month']
    duration = request.form['duration']
    camp=request.form['camp']
    pdays=request.form['pdays']
    prev = request.form['prev']
    post = request.form['post']
    empp=request.form['empp']
    index = request.form['index']
    consu = request.form['consu']
    eu = request.form['eu']
    num = request.form['num']
    data = {
        "data":
            [
                {
                    'age': age,
                    'job': job,
                    'marital': mar,
                    'education': edu,
                    'default': deff,
                    'housing': house,
                    'loan': loan,
                    'contact': contact,
                    'month': month,
                    'duration': duration,
                    'campaign': camp,
                    'pdays': pdays,
                    'previous': prev,
                    'poutcome': post,
                    'emp.var.rate': empp,
                    'cons.price.idx': index,
                    'cons.conf.idx': consu,
                    'euribor3m': eu,
                    'nr.employed': num,
                },
            ],
    }
    #print(data)
    #list1=[age,job,mar,edu,deff,house,loan,contact,month,duration,camp,pdays,prev,post,empp,index,consu,eu,num]
    #print(list)
    #input_data = "{\"data\": [" + str(list(list1)) + "]}"
    #print(input_data)
    body = str.encode(json.dumps(data))
    key = 'e214pM0NaGP1Y9TZv02gEoP62OoqUuET'
    headers = {'Content-Type': 'application/json'}
    headers['Authorization'] = f'Bearer {key}'
    service = 'http://464c378e-089b-4db7-9bc1-4fa1d8035d39.centralus.azurecontainer.io/score'
    #resp = requests.post(service, body, headers=headers)
    req = urllib.request.Request(service, body, headers)

    response = urllib.request.urlopen(req)

    result = response.read()
        #print(result)
    data=json.loads(result)
        #print(data)


    #m = resp.text

    return render_template('index.html',prediction_text=' {}'.format(data[13:]))

