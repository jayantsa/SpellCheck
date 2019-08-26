# SpellCheck
A spell check Application using Flask<br />
Steps to run:<br />
Install Required dependencies : pip install -r requirements.txt<br />
Run Flask Application : python spellCheck.py<br />
Go to URL : http://127.0.0.1:5000/spellCorrect<br />

structure:<br />
spellCheck.py : Entry Point of application (Contains Routes)<br />
spellCheckPN.py : Peter Norvig's Implementation of spell Check<br />
spellCheckUsingGlove.py : Using Pretrained Glove vector for ranking.(Glove vector need to be downloaded.Link provided in wiki)<br />
wordSegmentation.py : function for Word segmentation task<br />
suggestedWords.py : words suggestion generation code.<br /><br />
wordSegmentationDP.py : Dynamic Programming approach for word segmentation task<br />
