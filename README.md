# PredictFinancialMarketsByAnalyzingSpeechByCentralBanks

## Project Repository for Data Science for Text Analytics 

Project Name: Predict Financial Markets By Analyzing Speech By Central Banks

## Group Members:

Anusha Chattopadhyay - anusha.chattopadhyay@stud.uni-heidelberg.de

Keerthan Ugrani - ugranikeerthan6@gmail.com

Renuka Jawaharlal Sahani - renukasahani16@gmail.com

Shruti Ghargi - shruti.ghargi@gmail.com

#scroll to the last section for logs

## Table of Contents
- [1. Project Description](#1-project-description)
- [2. Installation](#2-installation)
- [3. Data Understanding](#3-data-understanding)
- [4. Code Description](#4-code-description)
- [5. Conclusion](#5-conclusion)
- [6. Resources and References](#6-resources-and-references)
- [7. Different tasks taken up while doing the project](#7-different-tasks-taken-up-while-doing-the-project)
- [8. Git commands cheat sheet for project ](#8-git-commands-cheat-sheet)
- [9. Log of contributors to the Project](#notes-for-repo-contributers)

## 1. Project Description
 
The project's problem statement is taken from Natixis' ongoing ["Bankers and Markets"](https://challengedata.ens.fr/challenges/70) data science challenge. On occasion, central bankers will deliver speeches in which they will analyze the state of the world economy. These comments are widely watched by all financial actors globally, and as a result, they have a big impact on how the financial markets grow and, to a greater extent, how the economy is doing. In actuality, communications from central banks may have an effect on a number of crucial economic factors, such as interest rates, monetary policy, inflation expectations, lending, debt, and overall financial leverage for both the public and private sectors.

Due to the potential impact these speeches may have on vital macro-economic variables and move financial markets, the ability to effectively understand and comprehend "central bank language" has become a crucial topic of study for all sorts of financial analysts and economic actors. 

The goal of this project is to train and evaluate the data provided by the competition as well as to assess the effectiveness of our model by mining the raw data of central bank speeches and market closing data of that day. First, the numerical data were subjected to data preprocessing procedures. Later, to examine if latent features might be used to more accurately predict the market movement at each of the central bank statements, text pre-processing technology was applied to the text data.

![project architecture](project_arch.PNG)
Project Proposed Architecture
![project flow chart](flow_chrt.PNG)
Project Flow Chart

## 2. Installation

Required libraries are described in requirements.txt. The code should run with no issues using Python versions 3.6+. Create a virtual environment of your choice. Here uses Anaconda:

conda create -n movemarket python=3.6 jupyter
conda activate movemarket
pip install -r requirements.txt

1. clone the repo
2. Download the raw data and competition data from [this link](https://www.kaggle.com/datasets/keerthan27/data-for-predicting-financial-markets?select=merged_finance_1w_2w) in folder "data"
3. Create a folder Embeddings and download the embeddings from  
[this link](https://www.kaggle.com/datasets/leadbest/googlenewsvectorsnegative300)
4. For running each model please refer to [Code Description](#4-code-description)


## 3. Data Understanding

Competition Data:
The data provided in the competition contains the word embeddings The application of this technique transforms a speech into a vector of 768 real numbers that should represent all key information conveyed in the speech. which was embedded using the powerful BERT-Style transformer. They have not provided the speeches themselves as the participants could quickly find out the date and the market moves and this gives the input of the problem. The output is the mean price evolution of a collection of 39 different time series; these time series correspond to 13 different markets mesured at 3 different time scales.

They have computed the difference between closing prices of these 13 markets at 3 different maturities and the price of these markets at the closing time of the date of the speech. They are not interessed in very short time effects (between the beginning of the speech and the closing of the same day) and leaking effects (trading occuring because of information leakage before the beginning of the speech). A few tests have given us an indication that if a speech has an effect on the markets, it seems to intervene before the end of 2 weeks following the date of the speech: we have chosen 1 day lag, 1 week lag and 2 week lag to measure the possible effects on the markets.

The 13 markets are the following :

VIX: Index for the volatility of US stocks.
V2X: Index for the volatility of european stocks.
EURUSD: Change Rate EURO - US Dollars.
EUROUSDV1M: Volatility of at the money 1 month options on the EURUSD.
SPX: Index of the US Stocks.
SX5E: Index of Euro Stocks.
SRVIX: Swap Rate Volatility Index , it is an interest rate volatility index.
CVIX: Crypto Volatility Index, it is a crypto-currency volatility index.
MOVE: developed by Merrill Lynch, measures fear within the bond market.
USGG2YR: US Bonds 2 years.
USGG10YR: US Bonds 10 years.
GDBR2YR: German Bonds 2 years.
GDBR10YR: German Bonds 2 years.

The training data consists in 2000 transformed speeches and their subsequent market moves. More precisely:

x_train.csv is a (2024, 768) array. Each line represents one speech issued at some date by some central banker (FED or ECB); for obvious reasons, they are anonymous. They were transformed into a feature vector of dimension 768 using a Bert-style transformer. These transformer are known to be extremely successfull for conveying the semantics of a natural language text.
y_train.csv is a (2024, 39) array. Line i represents the market variations consecutive to the i-th speech whose transformed version is in the i-th line of the x_train file. These variations are relative.

The test data is as follows: 

x_test.csv is a (415, 768) array. Each line represents one speech, at dates that are different than for the x_train.

The participant must submit a (415, 39) csv file for the predicted values of the market moves. The metric is simply the L2 metric between the predicted market moves and the real market moves.

Raw Data:
Acquired central bank speeches dataset from: https://www.kaggle.com/datasets/magnushansson/central-bank-speeches?resource=download The dataset contains speeches (in English) held by central bank boards affiliated with the Bank for International Settlements over the period 1997-01-07 to 2020-01-10. This can be our raw articles dataset and the corresponding market data is also extracted of 1day difference, 1 week difference and and 2 week difference.

There are some cases in the data where the data for the 1day is available and 1 week and 2 week data is NaN. Hence we decided to check the efficiency of the model to only 1 day market data.

## 4. Code Description
1. cd src/XGBOOST CODE and submission file/exercise-xgboost (1)-Copy1.ipynb
This is the first method we tried with the data1 (data given in the competition). We did not pass the benchmark with this particular method
Input:
X_train data given in the competition
Y_train data given in the competition
X_test data given in the competition
Sample submission file given in the competition

Output:
submission file for the competition

Process:
- using the XGBoost Regressor model to train the word embeddings with the market data
- using the tsne model to check for the change in the RMSE value
- using the PCA along with XGBoost Regressor for training and testing
- comparing the results between scaled word embeddings and non-scaled word embeddings
- conclusion: training and testing the scaled word embeddings is better than non-scaled

2. cd src/XGBOOST Which crossed benchmark/exercise-xgboost (1)-Copy1.ipynb
This is the second method we tried with data1 (data given in the competition). We did crosss the benchmark with this particular method.
Input:
X_train data given in the competition
Y_train data given in the competition
X_test data given in the competition
Sample submission file given in the competition

Output:
submission file for the competition

Process:
- using the modified XGBoost Regressor model to train the word embeddings with the market data
- using the tsne model to check for the change in the RMSE value
- using the PCA along with fine tuned XGBoost Regressor for training and testing
- comparing the results between scaled word embeddings and non-scaled word embeddings
- conclusion: training and testing the scaled word embeddings is better than non-scaled

3. cd src/Generating_Prediction.ipynb
Here we take our raw dataset (data2) to check whether our methodology really works when we pre-process the raw data and use the same word embedding methods as used in converting the text data to word embeddings in the competition(data1) and also to check if our fine tuned XGBoost regressor along with PCA works exactly as it worked with data1.
Input:
raw data of speech and market values

Output:
RMSE value and the predicted market value file for the test data

Process:
- Loading the data
- Preprocessing of the data
- building the vocabulary and checking the coverage with existing embeddings
- loading the BERT model for converting the text data into 768 word embeddings
- spliting the data for training and testing
- using the modified XGBoost Regressor model to train the word embeddings with the market data
- using the tsne model to check for the change in the RMSE value
- using the PCA along with fine tuned XGBoost Regressor for training and testing
- comparing the results between scaled word embeddings and non-scaled word embeddings
- conclusion: training and testing the scaled word embeddings is better than non-scaled and the same trained model holds good for both the data hence checking whether our methodology works in real time raw data too is also completed.

## 5. Conclusion
There has been a significant effect of the speeches given by the Central Banks on the market movements on that particular day, after the week and also after 2 weeks which has been objectively presented in the project. The methodology used is fine tuned XGBoost regressor with PCA analysis gave us the smallest possible RMSE value and also crossed the bench mark of the competition of 18.3909 where as our result was 18.3670. We also checked for the efficiency of our methodology with raw data by pre-processing, converting it to word embeddings and then training and testing with the same methodolgy as used for the competition data and the MSE value for the raw data came up to be 7.97 which is better than other models and methodology.

Future Scope and Betterments:

There were many objectives and other different approach we can take in the future improvement in solving the problem, those are to apply the machine learning tools to the market time series data and to use those metrics along with the text article and see the correlation between them as to see how much percentage it can effect in moving the market up and down and also to study the impact of other factors. We can also make the dynamic full-stack web application which can automatically analyse both market data and the central bank speeches to predict the market indicators. Due to time constraint and many other academic factors we were not able to fully implement all these extra objectives.
# 6. Resources and References
project training data from the challenge https://challengedata.ens.fr/challenges/70

initial test data also from the same challenge

creating fresh final test data after bert transformation - aritcles from https://www.kaggle.com/datasets/magnushansson/central-bank-speeches?resource=download 

First set of financial market data from https://www.cboe.com/tradable_products/vix/vix_historical_data/

Compiled Dataset: https://www.kaggle.com/datasets/keerthan27/data-for-predicting-financial-markets?select=merged_finance_1w_2w

Understanding BERT:
https://www.kaggle.com/code/tanulsingh077/deep-learning-for-nlp-zero-to-transformers-bert#Contents
http://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/
https://www.analyticsvidhya.com/blog/2021/09/an-explanatory-guide-to-bert-tokenizer/

NLP similarity Analogy: http://www.d2l.ai/chapter_natural-language-processing-pretraining/similarity-analogy.html#applying-pretrained-word-vectors
# 7. Different tasks taken up while doing the project
1. initial data acquired
2. Folder structure and repo initalization done (subject to change as main model gets built)
3. Initial Project Architecture plotted
4. Static loading of files completed
5. Max and Min plotted for each market and it's corresponding article plotted - plotted in ipynb file
6. Simple Moving average for all markets at 2weeks plotted - plots stored in separate plots/simple_moving folder
7. Corelation Matrix From 1st day to 1st week and 2nd week after the speech is delivered plotted - plotted in ipynb file
8. files all carried in snippets and put in snippets folder
9. Market articles aquired from https://www.kaggle.com/datasets/magnushansson/central-bank-speeches?resource=download 
10. VIX market data aquired from from 2009 to 2003 aquired, along with updating data from 2004 to present from https://www.cboe.com/tradable_products/vix/vix_historical_data/
11. Model A created for training initial Data, test with Model A 
12. Raw data to be stored in financial_data_articles_raw
13. Processable Data created and set up, zip stored in Data/ folder
14. Market data and articles formatted ready for bert transformation, excluding combination
15. 1w and 2w compilation done and files uploaded to data folder under merged_finance_1w_2w parts 1,2,3,4
16. Article data and market data formatted separately and added. Combination along with 1w and 2w dates remaining - DONE
17.	Text analytics:
i.	Building the vocabulary of the text data.
ii.	First 5 to 10 elements and their counts.
iii.	Import the embeddings that we want to use in our model and for that, we need to check the intersection of our vocabulary data/ text data with the provided embeddings.
iv.	This intersection will output a list of vocabulary (OOV) words that we can use to improve our pre-processing.
v.	Then check the coverage.
vi.	Check for the top OOV and also the punctuation, while removing or deleting the punctuation marks we need to check whether the punctuation needs to be deleted or considered as a token.
vii.	Then split off the punctuation which is considered as a token and remove other punctuation from the data.
viii.	Then check for the embedding and our data coverage.
ix.	Check for the numbers in the dataset as the bank statements can contain many numerical data as well, and check how the numbers are represented in the embeddings.
x.	Again, check for the OOV and remove the words since those have obviously been down-sampled when training the embeddings.
xi.	If there is an increase in the vocab coverage and data coverage is more than 80% and 90% respectively, then we can go ahead with BERT transform.
18.	visual representation
19.	Model training + getting the result: Model Training: 
i.	Split entire test data into 80-20 test-train sets
ii.	Training with XG BOOST and LSTM machine learning algorithms
iii.	Comparison of ML algo accuracies
iv.	Representation of the results
20.	Fine-tune the model that has got a better accuracy and check the results

--------------------------------------------------------------------------------------------------------------------------------------------------

# Notes for Repo contributers
# guidelines
1. Please PULL before you push before every editing session, to avoid merge conflits while pushing.
2. Please avoid non specific commits such as  "small changes" , "bug fix (with no description of which bug)".
3. Please create a pull request or contact the members before making a large change on a file you aren't solely working on (non snippet file) or is a dependency for a file someone else is working on
4. For Vscode users, git lens is recommended
5. Refering to point 2, try to not keep the same commit for a large commit, ideally commits should be in small batches so the other contributers can read them easily.
6. After a push, please also update the logs in the README file as frequently as possible.
7. upzip.py file created for quick multi unzips, however please ensure to keep gitignore updated

# 8. git commands cheat sheet
 - please don't directly push to main, create a PR and request review or directly contact another member to review before you push. if unsure please just create a PR and wait after requesting review, (patience is a virtue ;-) ) .
1. git pull origin - update your local with your active branch
2. git pull origin main - update your local branch with the latest updates from main
3. git merge --abort - to cancel your merge incase conflicts occur


---------------------------------------------------------------------------------------------------------------------------------------------------

# 9. log contributer - for detailed logs, with timings, please refer to the commits page, but we are trying to keep this readme as updated as possible as well
-------------------------------------------------------------

Data Files Acquired- Keerthan Ugrani

Git Repo Creation - Anusha Chattopadhyay

Folder Creation data,src and models - Renuka Jawaharlal Sahani

Uploaded datasets in data folder - Renuka Jawaharlal Sahani

Project Architecture Diagram - Keerthan Ugrani

Wrote static pynb file in src snippets for load the market data size of the column mean median sd for combined as well as one day one week or two week.- Renuka Jawaharlal Sahani

Computed the highs and lows for each stock market company for 1st day, 1st week and 2nd week- Shruti Ghargi

Plotted High and Low graph for visualization (in ipynb file, not stored separately for now) - Shruti Ghargi

Added the pynb script for High and Low values of the stock market - Shruti Ghargi

Plotted the Moving average for the market results data in y_train file - Anusha Chattopadhyay

Added pynb script for moving average plots - Anusha Chattopadhyay

pynb files added to snippets folder - Anusha Chattopadhyay

Plots extracted and saved in plots/data(will tie everything with the main.py file at a later date) - Anusha Chattopadhyay

Analysis of the correlation of 13 markets on 1st day, 1st week and 2nd week after the speech was delivered. - Keerthan Ugrani

Choosing the perfectly correlated data and assigning it to the variable - Keerthan Ugrani

data paths updated for the pynb files so as to match the new data folder path - Anusha Chattopadhyay

Researched on getting the alternate dataset which is in text format. Acquired central bank speeches dataset from: https://www.kaggle.com/datasets/magnushansson/central-bank-speeches?resource=download The dataset contains speeches (in English) held by central bank boards affiliated with the Bank for International Settlements over the period 1997-01-07 to 2020-01-10. This can be our raw articles dataset and we are yet to get respective market values for it- Shruti Ghargi

Raw articles for financial market added , market data for available dates pending - Anusha Chattopadhyay

VIX-Market data uploaded - Anusha Chattopadhyay

Implemented XG Boost with the Bert Data and Trained the model   - Renuka Jawaharlal Sahani

Did cleaning with PCA Analysis method to reduce the dimensionality of a dataset - Renuka Jawaharlal Sahani

Trained the Model via Principal Components - Renuka Jawaharlal Sahani

Implemente the T-SNE Implementatione - Renuka Jawaharlal Sahani

Implemeted the code to convert final data to final_normal_submission.csv file which will be output result - Renuka Jawaharlal Sahani

VIX market data from 2009 to 2003 aquired, along with updating data from 2004 to present from https://www.cboe.com/tradable_products/vix/vix_historical_data/ - Anusha Chattopadhyay

Raw data stored in financial_data_articles_raw - Anusha Chattopadhyay

Uploaded First implemented code test reult file on challenge data webiste on 25th dec 2022- Renuka Jawaharlal Sahani

Uploaded Second implemented code test reult file on challenge data webiste on 25th Jan 2023 - Renuka Jawaharlal Sahani

Caputred the screenshot and uploaded on github(benchmark results which we achieved) - Renuka Jawaharlal Sahani

Did changes to the old xgboost code implemeted by me.Which is now without randomization.This code crossed the bench mark - Renuka Jawaharlal Sahani

Wrote steps how to execute the model - Renuka Jawaharlal Sahani

Updated requirement.txt - Renuka Jawaharlal Sahani

Added processed csv into data into .zip - Anusha Chattopadhyay

Driver code added to snippets - Anusha Chattopadhyay

Project progress and checklists updated - Keerthan Ugrani, Shruti Ghargi

Article data and market data formatted separately and added. Combination along with 1w and 2w dates remaining - Anusha Chattopadhyay

1w-2w dates combined code uploaded - Anusha Chattopadhyay

upzip.py file created for users to add any zip files they are uploading and do not wish to upzip them manually later - Anusha Chattopadhyay

Pre-processing of the data - Keerthan Ugrani, Shruti Ghargi

BERT word embeddings - Keerthan Ugrani

Training and Testing the model with XGBoost - Shruti Ghargi

Training and Testing the model with XGBoost along with PCA feature extraction - Keerthan Ugrani

Training and Testing the model with fine tuned XGBoost - Keerthan Ugrani, Shruti Ghargi

Training and Testing the model with fine tuned XGBoost along with PCA feature extraction - Keerthan Ugrani, Shruti Ghargi