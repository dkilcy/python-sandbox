
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def generate_csv():
    def generate():
        return "A,B,C\n100,200,300\n"
     
    return Response(generate(), mimetype='text/csv')

if __name__=='__main__':
    app.run(host="0.0.0.0",port=int("30080"))
    
    