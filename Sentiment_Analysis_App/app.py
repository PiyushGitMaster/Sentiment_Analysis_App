from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_text = request.form['text']
        if user_text.strip():
            blob = TextBlob(user_text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Classify sentiment
            if polarity > 0:
                sentiment = "Positive 😊"
            elif polarity < 0:
                sentiment = "Negative 😞"
            else:
                sentiment = "Neutral 😐"
            
            result = {
                'text': user_text,
                'sentiment': sentiment,
                'polarity': round(polarity, 4),
                'subjectivity': round(subjectivity, 4)
            }
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)