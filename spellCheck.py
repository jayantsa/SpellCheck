from flask import Flask, request, render_template
import re
from flask import jsonify
from suggestedWords import *
from wordSegmentation import *
app = Flask(__name__)


# Route for Home Page
@app.route('/')
def appHomePage():
   return "Welcome To Spell Check. Please use /spellCorrect route to access the main tool"

# Route for spell Correction. Will return a form
@app.route('/spellCorrect')
def spellCheckForm():
   return render_template('wordForm.html')

@app.route('/spellCorrect', methods=['POST'])
def spellCheckCore():
    text = request.form['text']
    # removing Specaial Characters and spaces from the input and keeping only Alphabets
    text = re.sub('[^A-Za-z]+', '', text)
    # Converting the string to Lower Case 
    preprocessed_text = text.lower()
    # This function return a string of words after segmenting the input string. Used to handle cases when there are joined words
    wordsList=wordSegmentation(preprocessed_text)
    verbosity_type=0
    if(len(wordsList)!=1):
        verbosity_type = 1
        wordsList.append(preprocessed_text)

    wordSuggestions = []
    for word in wordsList:
    	wordSuggestions.extend(correctedWords(word,verbosity_type))

    return jsonify(suggesttions=wordSuggestions)

if __name__ == '__main__':
   app.run()