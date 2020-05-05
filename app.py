from flask import Flask,render_template,redirect,request
import joblib

app=Flask(__name__)

mod=joblib.load('model.pkl')

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def get_data():
	if request.method=='POST':
		hours=float(request.form['hours'])

		m=str(mod.predict([[hours]])[0][0])

	return render_template("index.html",answer=m)


if __name__ == '__main__':
	app.run(debug=True)