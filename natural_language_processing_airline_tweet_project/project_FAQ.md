# FAQ - Twitter US Airline Sentiment
#### 1. How should one approach the Twitter US Airline Sentiment project?

- Before starting the project, please read the problem statement carefully and go through the criteria and descriptions mentioned in the rubric.
- Once you understand the task, download and import the dataset into a Jupyter/Colab notebook to get started with the project.
- Start by adding your view and opinion along with the problem statement, the shape of the data, and the data description.
- Keep the structure and flow of the notebook as mentioned in the rubric.
- It is important to finish the notebook with a summary from the understanding of the application of various pre-processing, vectorization, and performance of the model on the dataset.

#### 2. What does that mean by "Note: Each text pre-processing step should be mentioned in the notebook separately" of step 3 in the problem statement?

You are expected to apply each pre-processing function on the required column
one at a time & print the first few rows after applying each time.

#### 3. I keep getting the following error while installing spacy:
```
ModuleNotFoundError: No module named 'spacy'
```

How to fix this issue?
Please try using the following code to install spacy:
```
conda install -c conda-forge spacy
```

It is not mandatory to use spacy for performing the text pre-processing step of
this project.


#### 4. I am trying to Install the contractions package but getting the error each time.

Try the below code in the anaconda prompt:
```
conda config --add channels conda-forge
```
```
conda install pyahocorasick
```
```
pip install contractions
```
If the above installation doesn't work, you can apply the below function on the required column for de-contraction.
```
import re
```
```
def decontracted(phrase):
# specific & general contracted words
phrase = re.sub(r"won\'t", "will not", phrase)
phrase = re.sub(r"can\'t", "can not", phrase)
phrase = re.sub(r"n\'t", " not", phrase)
phrase = re.sub(r"\'re", " are", phrase)
phrase = re.sub(r"\'s", " is", phrase)
phrase = re.sub(r"\'d", " would", phrase)
phrase = re.sub(r"\'ll", " will", phrase)
phrase = re.sub(r"\'t", " not", phrase)
phrase = re.sub(r"\'ve", " have", phrase)
phrase = re.sub(r"\'m", " am", phrase)
return phrase
```

#### 5. Do we need to follow the exact sequence in pre-processing?
You can follow any order for pre-processing, as long as you are able to perform
the further steps of the project after pre-processing.

#### 6. Do I have to convert the sentiment column values to integers before training the model?

It is not mandatory to encode the target column before training the model.
You can proceed with modeling without encoding too.

#### 7. Which classification algorithm should I use to fit the model for this project?

You can apply any classification algorithm which has been covered in the course so far.

#### 8. Can I perform any additional pre-processing steps apart from the ones that are mentioned in the list?

You are expected to include all text pre-processing step that is asked in the
project problem statement. Yes, you can also include additional pre-processing
steps apart from the ones that are mentioned in the problem statement.
