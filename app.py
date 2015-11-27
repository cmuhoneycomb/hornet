
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'ok!\n'

@app.route('/result/<value>')
def hornet(value):
    #db = get_db()
    #cur = db.execute('select * from entries order by id desc')
    #entries = cur.fetchall()
    return str(value) + '\n'

if __name__ == '__main__':
    app.run()
