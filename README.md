# Predykcja satysfakcji klientów lini lotniczych za pomcą uczenia maszynowego
Projekt ma na celu najepszej klasyfikacji zadowolenia klientow lini lotniczych, database składa się z 22 kolumn, w którym są zaprezentowane czynniki które mają wpływ na zadowolenie pasażerów. 
Używam zbioru danych z [Kaggle](https://www.kaggle.com/datasets/yakhyojon/customer-satisfaction-in-airline) 
i będę to robił za pomocą biblioteki Scikit-learn do nauczenia maszynowego tego modelu
# Wyniki poszczególnych modeli
## K Nearest Neighbors
![alt table](https://github.com/ELJarzynski/UM-Customer-Airline-Satisfaction-Prediction-RandomForestClassifier/blob/main/images/errorKNN.png)
## Logistic Regression
![alt table](https://github.com/ELJarzynski/UM-Customer-Airline-Satisfaction-Prediction-RandomForestClassifier/blob/main/images/errorLR.png)
## Decision Tree Classifier
![alt table](https://github.com/ELJarzynski/UM-Customer-Airline-Satisfaction-Prediction-RandomForestClassifier/blob/main/images/errorTree.png)
## Random Forest Classifier
![alt table](https://github.com/ELJarzynski/UM-Customer-Airline-Satisfaction-Prediction-RandomForestClassifier/blob/main/images/errorForest.png)

# Jak widać najlepiej zpredyktował model Random Forest Classifier z wynikami 
### Accuracy 0.952
### Precision 0.969
### Recall 0.943
# A tak się prezentuje macierz pomyłek
![alt table](https://github.com/ELJarzynski/UM-Customer-Airline-Satisfaction-Prediction-RandomForestClassifier/blob/main/images/CMDRF.png)
