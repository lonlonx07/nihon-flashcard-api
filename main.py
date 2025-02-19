from flask import Flask 
import socket

app = Flask(__name__) 
 
@app.route('/GET/<cnd>', methods = ['GET']) 
def disp(cnd): 
    try:
        with open(f"{cnd}.json", "r") as f:
            data = f.read()

        res = data
    except:
        res = "none"

    return res
  
if __name__ == '__main__': 
    
    host = socket.gethostbyname(socket.gethostname())
    port = 10000
    app.run(host=host, port=port, debug = True)