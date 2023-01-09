# Role-playing game using Artificial Intelligence
<b>Author: Almudena Ramírez</b>

This project consists of a role-playing game that can interact with a d20 die.
It was divided into two parts:
1. A neural network is trained to identify the number of a d20 die with a camera. 
2. The detected number would modify, depending on its value, a story presented through streamlit. 

## Workflow
1. Preparation of the dataset
2. Exploratory analysis of the data
3. Configuration of the model
4. Training of the data
5. Creation of the history and its different parts
6. Creation of the dashboard

## 1. Database
The database used for this project is https://www.kaggle.com/datasets/nellbyler/d6-dice. It contains one folder with the labels' annotations and another folder with 250 images. Each dice image has between 1 and 25 dice.
