from flask import Flask, render_template, request, redirect, url_for
# Pour l'instant, on utilise une liste pour stocker les articles (pas une vraie base de données)
articles = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/create', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        articles.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
