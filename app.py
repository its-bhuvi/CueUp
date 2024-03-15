from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies/recommend')
def movie_recommend():
    return render_template('movie-recommend.html')

@app.route('/music/recommend')
def music_recommend():
    return render_template('music-recommend.html')

@app.route('/books/recommend')
def book_recommend():
    return render_template('book-recommend.html')

if __name__== '__main__':
    app.run(debug=True)
