from flask import render_template
from kimgija import app

@app.route('/')
def main():
	return render_template("main.html")