# Data-Modeling-ETL-Postgres
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# Introduction

In this project, I conducetd data modeling with Postgres and build an ETL pipeline using Python for extract the data from csv files into postgre database.
For e-commerce industry, the good data modeling and a robust etl pipeline is vital for data storage and following analytical works.

# Dataset
The e-commerce dataset is [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce)
The data Schema is showing like this:
![data schema](https://i.imgur.com/HRhd2Y0.png)

# Project Files
`data` folder:  where the data file located in
`script` folder: where the script file located in

`data_modeling.py` It contains the code for setting up the database. By running this script, **ecommerce** database will be created, as well as  **customer**, **geolocation**, **order_item**, **order_payments**, **order_reviews**, **orders**, **products**, **sellers**, **pcnt** tables.

`etl.py` It contains a process of reading datasets in `.csv` file, extracting the fields we need and transforming data into postgres database.

`data_set_preprocessing.py` preprocessing of the dataset.

`queries.py` which contains the `SQL` scripts for table inserting, table dropping, data inserting.