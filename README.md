# PalmerPenguinsPrediction
# [Check it out Live](https://palmerpenguinspredictionwebapp.herokuapp.com/ "Penguins WebApp in Heroku") {:target="_blank"}
A web app that predicts the species of a Palmer penguin based on its features using Machine Learning
(Random Forest Classifier)

![alt text][image]

[image]: https://images.unsplash.com/photo-1462888210965-cdf193fb74de?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=967&q=80 "Photo by Jay Ruzesky on Unsplash"

The purpose of this ML Web App is to make a dynamic prediction of the species of a penguin based on its characteristics:

* Island
* Bill length
* Bill depth
* Flipper length
* Body mass
* Sex

In order to improve its performance, this project has two python files: one to create the model that will make the prediction of the species and another to execute the web app and get the user’s input to make the prediction with a call to the model.

The model can be updated to predict the species, sex or island of the penguin, just requiring to change the values of the corresponding column in the dataset that has the info to be predicted and its target information within the code.

In order to execute this project, it is necessary to have `pandas`, `sklearn`, `streamlit`, `pickle` and `numpy` installed with **python**, all of these to be run into an **Anaconda** environment.

**Procedure:**

1. Write the code for the classification model in Atom and save it as a .py file (`model_building_penguins.py`)
2. Launch Anaconda prompt to have python execute the .py file and return a pickle file with the ready-to-use model in the same folder (`penguins_clf.pkl`)
3. Write the code for the web app in Atom and save it as a .py file (`model_building_penguins.py`)
4. Execute the web app with Streamlit using Anaconda
5. Upload a .csv file with the the characteristics of a penguin, or change the values of its characteristics in the left panel to predict in real time its species

![alt text][image1]

[image1]: https://github.com/jzambrano-xyz/PalmerPenguinsPrediction/blob/master/PenguinsModelBuilding.jpg "Code for the model"

![alt text][image2]

[image2]: https://github.com/jzambrano-xyz/PalmerPenguinsPrediction/blob/master/PenguinsPickle.jpg "Creation of the pickle (model)"

![alt text][image3]

[image3]: https://github.com/jzambrano-xyz/PalmerPenguinsPrediction/blob/master/WebAppPenguins.jpg "Code for the Web app"

![alt text][image4]

[image4]: https://github.com/jzambrano-xyz/PalmerPenguinsPrediction/blob/master/StreamlitPenguins.jpg "Execution of the Web app using Streamlit"

![alt text][image5]

[image5]: https://github.com/jzambrano-xyz/PalmerPenguinsPrediction/blob/master/PalmerPenguins.gif "Web app running on Streamlit"


