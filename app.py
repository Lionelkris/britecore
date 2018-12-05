from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class Features(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(20), nullable=False)
	description=db.Column(db.String(1000), nullable=False)
	client=db.Column(db.String(20), nullable=False)
	priority=db.Column(db.Integer, nullable=False)
	target_date=db.Column(db.String(20), nullable=False)
	product_area=db.Column(db.String(20), nullable=False)
	created_on=db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/request_feature', methods=['POST'])
def request_feature():
	print(request.form['title'], request.form['message'], request.form['client'], request.form['priority'], request.form['tdate'], request.form['parea'])
	cl=str(request.form['client'])
	pr=int(request.form['priority'])
	res=Features.query.filter_by(client=cl).all()
	print res
	pri_list=[]
	for i in res:
		pri_list.append(i.priority)
	if pr in pri_list:
		return "The client " + cl + " already has a feature request with following priorities " + str(pri_list) + ". The priorities can not repeat for a given client. It has to be unique. Click the back button of your browser and choose the right priority / client."
			
	feature_req=Features(title=request.form['title'], description=request.form['message'], client=request.form['client'], priority=request.form['priority'], target_date=request.form['tdate'], product_area=request.form['parea'])
	db.session.add(feature_req)
	db.session.commit()
	return redirect(url_for("index"))

if __name__=="__main__":
	app.run(debug=True)
