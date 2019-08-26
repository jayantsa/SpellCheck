# SpellCheck
A spell check Application using Flask
Steps to run:
Install Required dependencies : pip install -r requirements.txt
Run Flask Application : python spellCheck.py
Go to URL : http://127.0.0.1:5000/spellCorrect

structure:
spellCheck.py : Entry Point of application (Contains Routes)
spellCheckPN.py : Peter Norvig's Implementation of spell Check
spellCheckUsingGlove.py : Using Pretrained Glove vector for ranking.(Glove vector need to be downloaded.Link provided in wiki)
wordSegmentation.py : function for Word segmentation task
suggestedWords.py : words suggestion generation code.
wordSegmentationDP.py : Dynamic Programming approach for word segmentation task
