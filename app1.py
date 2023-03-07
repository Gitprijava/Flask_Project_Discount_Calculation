from flask import Flask, request,render_template

app = Flask(__name__)
#route
@app.route("/")
def hello_world():
    return  render_template("index.html")

@app.route("/operation",methods = ['POST'])
def operation():
    if(request.method=='POST'):
        #total = int(request.form['total'])
        price1 = int(request.form['price1'])
        price2 = int(request.form['price2'])
        price3 = int(request.form['price3'])
        price4 = int(request.form['price4'])
        price5 = int(request.form['price5'])
        total = price1+price2+price3+price4+price5 
        if total  <= 1000:
          total = total - (total*10/100)
        elif total > 1000 and total <=2000:
            total = total - (total*20/100)
        elif total >2000:
            total = total - (total*30/100)
        return render_template("result.html",total = total)
        #return f'The operation is {operation} and result is {result}'


if __name__ == '__main__' :
    app.run(host = "0.0.0.0", port = 5000) 


