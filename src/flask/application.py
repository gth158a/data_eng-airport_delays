'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request
from application import db
from application.models import Data, DailyTemp, WeatherDelay
from application.forms import EnterDBInfo, RetrieveDBInfo

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form1 = EnterDBInfo(request.form)
    form2 = RetrieveDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        data_entered = Data(notes=form1.dbNotes.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=form1.dbNotes.data)

    if request.method == 'POST' and form2.validate():
        try:
            num_return = int(form2.numRetrieve.data)
            query_db = Data.query.order_by(Data.id.desc()).limit(num_return)
            for q in query_db:
                print(q.notes)
            db.session.close()
        except:
            db.session.rollback()
        return render_template('results.html', results=query_db, num_return=num_return)

    return render_template('index.html', form1=form1, form2=form2)

@application.route('/temps') #methods=['POST'])
def temps_all():

    query_db = DailyTemp.query.order_by(DailyTemp.id.asc())
    for q in query_db:
        print(q.date)
    db.session.close()

    return render_template('temps.html', results=query_db) #, num_return=num_return)


@application.route('/temps/<iata>') #methods=['POST'])
def temps_by_iata(iata):
    query_db = DailyTemp.query.filter_by(iata=iata).order_by(DailyTemp.id.asc())
    for q in query_db:
        print(q.date)
    db.session.close()

    return render_template('temps.html', results=query_db)

    # return render_template('temps.html', results=query_db)#, form1=form1, form2=form2)

@application.route('/delays') #methods=['POST'])
def delays_all():

    query_db = DailyDelays.query.order_by(DailyDelays.id.asc())
    for q in query_db:
        print(q.date)
    db.session.close()

    return render_template('delays.html', results=query_db) #, num_return=num_return)


@application.route('/delays/<iata>') #methods=['POST'])
def delays_by_iata(iata):
    query_db = DailyDelays.query.filter_by(iata=iata).order_by(DailyDelays.id.asc())

    for q in query_db:
        print(q.date)
    db.session.close()

    return render_template('delays.html', results=query_db) #, num_return=num_return)


@application.route('/weather_and_delays') #methods=['POST'])
def weather_delays_all():

    query_db = WeatherDelay.query.order_by(WeatherDelay.id.asc())
    # for q in query_db:
    #     print(q.date)
    db.session.close()

    return render_template('weather_delays.html', results=query_db) #, num_return=num_return)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
