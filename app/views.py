from flask import render_template
from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
		return render_template('index.html')

		
# @app.route('/filtre', methods=['GET'])
# def filtre():
		# aprov = [49.9, 71.5, 6.4, 29.2, 44.0, 76.0, 35.6, 48.5, 16.4, 94.1]
		# percent = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3]
		# return render_template('index.html',
								# iframe = "{{ url_for('templates', filename='grafics2016.html') }}",
							    # aprov = aprov, 
								# percent = percent)	
								
@app.route('/filtre', methods=['POST'])
def filtre():
		aprov = [49.9, 71.5, 6.4, 29.2, 44.0, 76.0, 35.6, 48.5, 16.4, 94.1]
		percent = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3]
		return render_template('grafics2016.html',
								aprov = aprov, 
								percent = percent)
		# return render_template('index.html', iframe = "{{ url_for('templates', filename='grafics2016.html') }}")
								
# @app.route('/filtre', methods=['POST'])
# def filtre:
		# c = request.form['curs']
		# q = request.form['quad']
		# s = request.form['gender']
		# aprov=aprovats(c,q,s)
		# percent=percentatge(c,q,s)
		# return render_template('grafics2016.html', aprov = aprov, percent = percent)
	
if __name__ == '__main__':
	app.run()
