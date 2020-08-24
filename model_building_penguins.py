#Model used to create a pickle file that will be used to create a Model
#Import the necessary library to build the model
import pandas as pd

#Define the dataset that will be used to create the Model
penguins = pd.read_csv('penguins_cleaned.csv')

#Specify the feature to be predicted and its comparison features
#The target parameter can be switched between species, sex and island
df = penguins.copy()
target = 'species'
encode = ['sex', 'island']

#Define the alternatives for the prediction
#Since we are predicting the species,
#and it is set in column 1 in the csv file,
#we remove it from the model
for col in encode:
    dummy = pd.get_dummies(df[col], prefix = col)
    df = pd.concat([df, dummy], axis = 1)
    del df[col]

#We define the possible alternatives set as an array
target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

#Create a table fot the output
X = df.drop('species', axis=1)
Y = df['species']

#Build a random forest model to make the prediction
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, Y)

#Save the model as a picke file
import pickle
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))
