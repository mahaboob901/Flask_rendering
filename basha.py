from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'hi how are you'
@FAI.route('/first')
def first():
    return render_template('first.html',name='Mehaboob',age=24)

if __name__=='__main__':
    FAI.run(debug=True)