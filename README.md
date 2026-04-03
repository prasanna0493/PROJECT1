# AI Resume Screener

## Overview

AI Resume Screener is a simple machine learning project that automatically ranks resumes based on their relevance to a given job description. It uses Natural Language Processing (NLP) techniques to compare text similarity and help shortlist candidates efficiently.


##  Features

* Compares multiple resumes with a job description
* Ranks resumes based on relevance score
* Uses TF-IDF vectorization
* Calculates similarity using cosine similarity
* Easy to modify and extend



##  Technologies Used

* Python
* Scikit-learn
* NumPy



##  Project Structure


AI-Resume-Screener/
 23KE1A093.py 
 README.md

##  Usage

Run the script:

python 23KE1A0493.py


## Example Output

Resume 1 Score: 0.78
Experienced Python developer with strong background in machine learning and TensorFlow.

Resume 3 Score: 0.65
Data analyst with Python experience and knowledge of machine learning.

Resume 4 Score: 0.20
Software engineer with Java and system design experience.

Resume 2 Score: 0.05
Frontend developer skilled in HTML CSS JavaScript.


##  How It Works

* Converts job description and resumes into numerical vectors using TF-IDF
* Measures similarity using cosine similarity
* Ranks resumes based on similarity score


## Future Improvements

* Add PDF resume parsing
* Build a web interface using Flask or Stream lit
* Improve accuracy with advanced NLP libraries
* Add keyword extraction and weighting
