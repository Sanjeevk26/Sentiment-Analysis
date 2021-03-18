import os, webbrowser
#app.py

from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

query = ''

@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    global query
    if request.method == 'POST': #this block is only entered when the form is submitted
        query = request.form.get('query')
        x = ''
        x = x.join(query.split()) #Will convert input with spaces to input without spaces
                          # Eg. SRH vs RCB will become SRHvsRCB
        os.system('python Youtube_DataAnalysis.py --q ' + x)
    return '''<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Youtube Analysis</title>
        <style>
              body{
    background-color: #92a8d1;
    background-size: cover;
    background-position: center;
    height: 100vh;
    background-attachment: fixed;
  }
    .btn:link,
    .btn:visited,
    input[type=submit]{
      display: inline-block;
      padding: 10px 30px 10px 30px;
      font-weight: 300;
      text-decoration: none;
      border-radius: 200px;
      transition: background-color 0.2s,border 0.2s,color 0.2s;
    }

    .btn:hover,
    .btn:active,
    input[type=submit]:hover,
    input[type=submit]:active{
      background-color: #cf6d17;
    }

    .btn-full:hover,
    .btn-full:active{
      border: 1px solid #cf6d17;    
    }

    .btn-ghost:hover,
    .btn-ghost:active{
      border: 1px solid #cf6d17;    
      color : #fff;
    }

    label{
      color: white;
      font-size: 25px;
      margin-left: 10px;
    }
    h1{
      text-align: center;
    }

    input[type=text],
    input[type=email],
    input[type=password],
    input[type=number],
      select{
      width: 60%;
      padding: 5px;
      border-radius: 3px;
      margin-left: 40px;
      margin-top: 20px;
      padding: 10px;
    }

    input[type=submit]{
      font-size: 120%;
      border-radius: 200px;
      background-color: crimson;
    }
        </style>
    </head>
    <body>
        <h1>Youtube Analysis</h1>
        <form method="post">
            <label>Query</label>
                <input type="text" placeholder="Please enter your query" name="query" required >
                <br>
                <br>
                <a class="btn btn-ghost js--scroll-to-start"><input type="submit" value="Submit"></a><br>
        </form>
    </body>
</html> '''

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
