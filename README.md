# PredictFinancialMarketsByAnalyzingSpeechByCentralBanks

## Project Repository for Data Science for Text Analytics 

Project Name: Predict Financial Markets By Analyzing Speech By Central Banks

# Group Members:

Anusha Chattopadhyay - anusha.chattopadhyay@stud.uni-heidelberg.de

Keerthan Ugrani - ugranikeerthan6@gmail.com

Renuka Jawaharlal Sahani - renukasahani16@gmail.com

Shruti Ghargi - shruti.ghargi@gmail.com

# Resources
project training data from the challenge https://challengedata.ens.fr/challenges/70

initial test data also from the same challenge

creating fresh final test data after bert transformation - aritcles from https://www.kaggle.com/datasets/magnushansson/central-bank-speeches?resource=download 

First set of financial market data from https://www.cboe.com/tradable_products/vix/vix_historical_data/

-------------------------------------------------------------------------------------------------------------------------------------------------
requiremnts.txt contains the actively being used libraries:(updated by team whenever new libraries are required)

--------------------------------------------------------------------------------------------------------------------------------------------------
![project architecture](project_arch.PNG)
Project Proposed Architecture
![project flow chart](flow_chrt.PNG)
Project Flow Chart
-------------------------------------------------------------------------------------------------------------------------------------------------
# Status of project as of 18/01/2023 - the main.py file doesn't have any imports as of now and mainly serves as a placeholder, most progress is in the .ipynb files in the src/snippets folder. the main.py folder is mainly kept empty as we have till this stage worked independently. However the process of compilation is being tested in another branch. An inital Approach to the model has been attempted. New test data to be compiled
# tasks completed - update

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
11. Model A created for training initial Data, test with Model A remaining
12. Raw data to be stored in financial_data_articles_raw
# tasks pending -
1. 1st iteration Prediction model with train and test data- Model A created, Model B and C pending
2. creating a bert transformed test set to test the model after the inital training
3. Begin converting snippets into py files to be directly run in main, as of now main.py is empty - process begun as test in branch Anusha
4. Clean up script to compile articles remaining
5. Create Frontend
--------------------------------------------------------------------------------------------------------------------------------------------------

# Notes for Repo contributers

# repository overview - as of december 12/12/2022
1. Training and test data are in the data folder
2. Models folder is for storing trained models
3. The plots folder is for any plots you may want to save as .png or any other format
4. src/snippets is for independent code files: or files that can run on their own or were created as external .pynb files and then added into the repo
    this code is meant to be eventually integrated into the main.py file
5. The main.py file is for compilation of the snippets and other external file. ideally this should have minimal algorims in it and mostly imports.
# guidelines
1. Please PULL before you push before every editing session, to avoid merge conflits while pushing.
2. Please avoid non specific commits such as  "small changes" , "bug fix (with no description of which bug)".
3. Please create a pull request or contact the members before making a large change on a file you aren't solely working on (non snippet file) or is a dependency for a file someone else is working on
4. For Vscode users, git lens is recommended
5. Refering to point 2, try to not keep the same commit for a large commit, ideally commits should be in small batches so the other contributers can read them easily.
6. After a push, please also update the logs in the README file as frequently as possible.

# git commands cheat sheet - please don't directly push to main, create a PR and request review or directly contact another member to review before you push. if unsure please just create a PR and wait after requesting review, (patience is a virtue ;-) ) .
1. git pull origin - update your local with your active branch
2. git pull origin main - update your local branch with the latest updates from main
3. git merge --abort - to cancel your merge incase conflicts occur


---------------------------------------------------------------------------------------------------------------------------------------------------

# log contributer - for detailed logs, with timings, please refer to the commits page, but we are trying to keep this readme as updated as possible as well
-----------------------------------------------------------
Readme, Logs and repo maintenance main - Anusha Chattopadhyay
-------------------------------------------------------------

Data Files Aquired- Keerthan Ugrani

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
