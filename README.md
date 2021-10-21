# Project Title : STORE SALES PREDICTION
# Technologies : Machine Learning Technology
# Domain : Sales And Marketing

## Problem Statement:
### -> Nowadays, shopping malls and Big Marts keep track of individual items sales data in order to forecast future client demand and adjust inventory management. In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. By mining the data store from the data warehouse, more anomalies and patterns can be discovered.

## Approach
### -> The classical machine learning tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and Model Testing. Try out different machine learning algorithms that's best fit for the above case.

## Dataset
### -> We have train(8523) and test(5681) data set, train data set has both input and output variables.
### The dataset is taken from kaggle.
### Link :- Click [Here](https://bit.ly/2V1oRKl)
### We need to predict the sales for test data set on data as follow.

### Features:
### Item_weight : Weight of product
### Item_Fat_Content : Whether the product is low fat or not
### Item_Visibility : The % of total display area of all products in a store allocated to a particular product.
### Item_Type : The category to which the product belongs
### Item_MRP : Maximum Retail Price (list price) of the product
### Outlet_Identifier : Unique Store ID
### Outlet_Establishment_Year : The year in which store was established
### Outlet_Size : The size of the store in terms of ground area covered
### Outlet_Location_Type : The type of city in which the store is located
### Outlet_Type : Whether the outlet is just a grocery store or some sort of supermarket

### Target:
### Item_Outlet_Sales : Sales of the product in the particular store. This is the outcome variable to be predicted.




## Tools Used:
### 1. Python 
### 2. Numpy, Pandas
### 3. Matplotlib, Seaborn, Plotly
### 4. Sklearn
### 5. Logging
### 7. Html, CSS
### 8. Flask
### 9. Cassandra Database
### 10. Heroku




## Platforms Used:
### Jupyter Notebook, Spyder, Github, Heroku 




## Operations Performes:
### 1. Data Collection: 
#### -> Data is taken from kaggle which is a Store Sales Dataset.
### 2. Data Cleaning:
#### -> Every dataset consists of some missing values and outliers. The categorical missing values are filled with most frequent value i.e. mode while the numeric values are filled with mean. Also the outliers are treated with the mean value correspoiding to their item type.
### 3. Data Visualization: 
#### -> Visualizations are performed using libraries like matplotlib, seaborn and plotly by plotting histogram, countplots, scatter plot, etc. Also simple visualizations are performed on Power Bi Dashboard.
#### Link :- Click [Here](https://app.powerbi.com/links/Is9Uzs3CJH?ctid=6ea1ed1a-46b4-4653-83cf-7ecec89a3b1a&pbi_source=linkShare)
### 4. Feature Engineering: 
#### -> We use one-hot encoding to convert categorical features to numeric data.
### 5. Model Training: 
#### -> Comparing various regression models by training them on the modified dataset.
### 6. Hyperparameter Tuning:
#### -> To gain more accuracy on the data we perform hyperparameter tuning. This process take much time but can give us better results.
### 7. Model Evaluation and Selection: 
#### -> We choose our model based on their time taken and R2 value.
### 8. Model Deployment:
#### -> Using flask library the model is deployed on heroku.


## Database:
### -> The data is stored in the cassandra database which is connected with our program using cassandra drive of python.


## Logging:
### -> Using python's logging library we are tracking our logs which are obtained during program execution. This helps to understand our code in more efficient way and resolve any error or bug.


## Model Deployment Link:
#### -> Heroku Link: Click [Here](https://store-sales-predictor.herokuapp.com/)
##### Have a patience it will take a little bit to load.



## User Interface:
![](https://github.com/adityanaranje/Store_Sales_Prediction/blob/main/static/image/sales_interface.jpg)

## Data In Database:
![](https://github.com/adityanaranje/Store_Sales_Prediction/blob/main/static/image/Database_data.jpg)


## High Level Design (HLD)
Click [Here](https://drive.google.com/file/d/1gD1E-nLN9FZIsrCl4pT73ASjN2a2Ecsv/view?usp=sharing)


## Low Level Design (LLD)
Click [Here](https://drive.google.com/file/d/1jCoclqPnYnkD71jeSHkNXXO9LF4Idn3e/view?usp=sharing)


## Archirecture
Click [Here](https://drive.google.com/file/d/1-Hjh6kW1j8MW75hXg88hK2GcWyBJg3Kl/view?usp=sharing)


## Wireframe Document
Click [Here](https://drive.google.com/file/d/1rkoovjreKGkd6lL4NpKym1cDCHTM8AOm/view?usp=sharing)


## Project Report
Click [Here](https://docs.google.com/presentation/d/1T9OjrWsSReIsp9xt9diQFmdzePlOzCHT/edit?usp=sharing&ouid=107047844624939518429&rtpof=true&sd=true)

### Please feel free to inform me about any error or difficulty in my repository.
# Thank You
