# Named-Entity-Recognition
NER refers to extracting information and then locating and classifying named entities mentioned in unstructured text into predefined categories such as person names, organizations, locations, time expressions etc.
![WhatsApp Image 2021-04-12 at 11 06 07 AM](https://user-images.githubusercontent.com/57134054/114345368-2fcc4480-9b7f-11eb-8c28-905db34ec852.jpeg)

# Approach
This API has been designed using various python modules such as Streamlit, Spacy, BeautifulSoup, Wikipedia

Streamlit- It is an open source app framework for Machine Learning and Data Science projects. It can build and deploy attractive data apps within few minutes. It is a python library so make sure that you have Python 3.6-Python 3.8 installed.

Spacy-It is a free open source library for Natural Language Processing in Python. It is written in Cython and features NER, POS tagging, dependency parsing, word vectors and more. It is build for production use and provides user friendly API

BeautifulSoup- It is a python library for pulling data out of HTML, XML files and web pages. The content from wikipedia pages has been extracted using the same library.

Wikipedia- Wikipedia in python library is used to access and parse data from wikipedia. It is widely used to get summaries, extracting images, accessing full page content and much more. It has been used in task to extract summary out of lengthy wiki pages.

# Methodology
Below is the Flow chart for the methodology being used
![WhatsApp Image 2021-04-12 at 12 07 20 PM](https://user-images.githubusercontent.com/57134054/114351030-acfbb780-9b87-11eb-8be1-14c0bcff693f.jpeg)

Step 1- Extract summary for the wikipedia page using wikipedia.summary()

Step 2- Performing NER on the extracted summary using Spacy and basic HTML commands.

Step 3- Extract full page content from the wikipedia url using BeautifulSoup library.

Step 4- Performing NER on the extracted content using Space and basic HTML commands.

Step 5- Display Performed NER using Streamlit.

Step 6- Finally, Deploy the API using Heroku.

# How to run
To run ner.py

Type command in cmd: streamlit run ner.py
![WhatsApp Image 2021-04-12 at 12 18 13 PM](https://user-images.githubusercontent.com/57134054/114352179-2f38ab80-9b89-11eb-88bc-78a6311b07ad.jpeg)
Copy and Paste URL in the browser to access API.
# Screenshots of API
Click Name Entity Recognition:Summary from sidebar and Enter Page name to extract summary
![WhatsApp Image 2021-04-12 at 10 39 36 AM](https://user-images.githubusercontent.com/57134054/114352447-8179cc80-9b89-11eb-8051-272f9faa10df.jpeg)

Click check button to perform NER
![WhatsApp Image 2021-04-12 at 10 39 36 AM (1)](https://user-images.githubusercontent.com/57134054/114352820-eaf9db00-9b89-11eb-8d27-0b94b2ab1659.jpeg)

Click  Name Entity Recognition:URL from sidebar and Enter URL to extract content from web page.
![WhatsApp Image 2021-04-12 at 10 39 36 AM (2)](https://user-images.githubusercontent.com/57134054/114352937-18468900-9b8a-11eb-94aa-e6a04522c8c6.jpeg)

Click check button to perform NER
![WhatsApp Image 2021-04-12 at 10 39 36 AM (3)](https://user-images.githubusercontent.com/57134054/114353000-27c5d200-9b8a-11eb-9969-96b3b8455a68.jpeg)

That's How we will perform NER on Wikipedia API.

# Live URL for the task

https://name-entity-recognition.herokuapp.com/


