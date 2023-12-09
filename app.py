# from flask import Flask, render_template, request, redirect, url_for

# import random

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/', methods=['post'])
# def index_post():
#     word = request.form.get('form1')
#     print(word)
#     return redirect(url_for('erase', msg=word))

# @app.route('/erase/<string:msg>')
# def erase(msg):
#     return render_template('word.html', html_word=msg)



# @app.route('/img', methods=['GET', 'POST'])
# def img():
#     html_img = "your_image_filename.png"
#     return render_template('img.html',html_img=html_img)

# @app.route('/flower', methods=['GET', 'POST'])
# def flower():
#     return render_template('flower.html')

# @app.route('/img', methods=['GET', 'POST'])
# def phrase_img():
#     if request.method == 'GET':
#         # インデントを追加
#         phrases = ['今日はいっぱい食べよう', 'そんな日もあるよね', 'こんな日は早く寝よう']
#         images = ['static/img/bear.png', 'static/img/cat.png', 'static/img/dog.png']

#         chosen_phrase = phrases[random.randint(0, 2)]
#         chosen_img = images[random.randint(0, 2)]

#         print(chosen_phrase, chosen_img)

#         return render_template('phrase_img.html', html_phrase=chosen_phrase, html_img=chosen_img)

#     # インデントを追加
#     return render_template('img.html', html_phrase="", html_img="")
# if __name__ == '__main__' :
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['post'])
def index_post():
    word = request.form.get('form1')
    print(word)
    return redirect(url_for('erase', msg=word))

@app.route('/erase/<string:msg>')
def erase(msg):
    return render_template('word.html', html_word=msg)

# @app.route('/img', methods=['GET', 'POST'])
# def img():
#     html_img = "your_image_filename.png"
#     return render_template('img.html', html_img=html_img)

@app.route("/img")
def img():
    count = random.randint(0,2)
    if count == 0:
        return render_template("img.html")
    elif count == 1:
        return render_template("img2.html")
    else:
        return render_template("img3.html")
    # elif count == 3:
    #     return render_template("img4")
    

@app.route('/flower', methods=['GET', 'POST'])
def flower():
    return render_template('flower.html')

@app.route('/phrase_img', )
def phrase_img():
    if request.method == 'POST':
        phrases = ['今日はいっぱい食べよう', 'そんな日もあるよね', 'こんな日は早く寝よう']
        images = ['static/img/bear.png', 'static/img/cat.png', 'static/img/dog.png']

        chosen_phrase = phrases[random.randint(0, 2)]
        chosen_img = images[random.randint(0, 2)]

    #     print(chosen_phrase, chosen_img)

    #     return render_template('phrase_img.html', html_phrase=chosen_phrase, html_img=chosen_img)

    # # GET メソッドが実行された場合は空の情報を返す
    # return render_template('img.html', html_phrase="", html_img="")

if __name__ == '__main__':
    app.run(debug=True)