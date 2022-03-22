from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('map.html')
@app.route('/velo')
def index2():
	return render_template('velo.html')

if __name__ == "__main__":
    app.run(port=5002, debug=True, threaded=True)
