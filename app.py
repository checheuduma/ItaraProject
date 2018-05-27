from flask import Flask, render_template, redirect, request, Session, flash,session
from werkzeug.utils import secure_filename
from utils import common_words, classify__, allowed_file, Track, caTe, viewMore,span
from compareData import class_dataA, class_dataB
import os

# setup flask
app = Flask(__name__)
app.config.from_object(__name__)
SECRET_KEY = os.urandom(20)
app.secret_key = SECRET_KEY

Upload_Folder = "C:/Users/zncuduma/PycharmProjects/Itara Project/uploads"

app.config['UPLOAD_FOLDER'] = Upload_Folder

sess = Session()

@app.route('/')
def index():
    return render_template('html/home.html')

@app.route('/showupload')
def showupload():
    return render_template('html/upload.html')

@app.route('/home')
def home():
    session.pop('screen_name', None)
    classifier = request.values.get('classifier') or "Support Vector Machine"
    pe, nee, neu, positives, negatives, neutrals, avPos, avNeg, getIt = classify__(classifier)
    call, call2, call3, call4, call5, cutt1, cutt2, cutt3, cutt4, cutt5, top_tweets = common_words()
    holdOn = caTe()
    categories = request.values.get('categories')
    categorizeTwwts = []
    if(categories != None):
        categorizeTwwts = caTe(categories)

    span1 = span(cutt1)
    span2 = span(cutt2)
    span3 = span(cutt3)
    span4 = span(cutt4)
    span5 = span(cutt5)

    front, back = Track()
    return render_template('html/index.html', pgtitle='Home', postive = pe , negative = nee, neutral = neu,
                           positives=positives,holdOn=categorizeTwwts,negatives=negatives,
                           getIt=getIt, neutrals=neutrals, call=call, call2=call2, call3=call3, call4=call4, call5=call5,
                           cutt1=cutt1,cutt2=cutt2, cutt3=cutt3, cutt4=cutt4, cutt5=cutt5, avPos=avPos, avNeg=avNeg,
                           most_tweets=top_tweets, front=front,back=back, span1=span1, span2=span2, span3=span3, span4=span4, span5=span5 )

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        fow = print('file')
        print(fow)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "TWEETS.csv"))
            return "Upload successful"

    return "Upload not successful method" + request.method

@app.route('/viewMore')
def view():
    monthData =  request.values.get('monthData')
    if(monthData == None):
        return render_template("html/blank.html")
    else:
        sentData =  request.values.get('sentData')
        result = viewMore(monthData, sentData)
        return render_template("html/blank.html", result=result)

@app.route('/compare')
def compare():
    classifier = request.values.get('classifier') or "Support Vector Machine"
    posData, negData, pA, nA = class_dataA(classifier)
    positives, negatives, pB, nB = class_dataB(classifier)
    return render_template("html/compare.html", posData=posData, negData=negData, positives=positives,
                           negatives=negatives, pa=pA, na=nA, pb=pB, nb=nB)

@app.route('/upload2', methods=['GET', 'POST'])
def uLoad():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "dataA.csv"))
            return "Upload successful"
    return "Upload not successful method" + request.method

@app.route('/upload3', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "dataB.csv"))
            return "Upload successful"
    return "Upload not successful method" + request.method


if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run()

