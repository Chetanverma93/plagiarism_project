
from plag import *
from flask import *
import sys
import difflib


app=Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        refFile=request.form['file1']
        sourceFile=request.form['file2']
        returnedMsg = check(refFile,sourceFile)

        return render_template('success.html',msg=returnedMsg)

if __name__=="__main__":
    app.run(debug=True)