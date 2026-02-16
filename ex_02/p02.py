#i
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv("C:/Users/Mohamed/Sowlution_Test/ex_02/prediction.csv")

X = df[["Card Suit", "Animal Name", "Fruit"]]
y = df["Result"]

encoder = ColumnTransformer(transformers=[("", OneHotEncoder(),
             ["Card Suit", "Animal Name", "Fruit"])])
X_encoded = encoder.fit_transform(X)
model = LogisticRegression()
model.fit(X_encoded, y)

def probabilityToBeatBoss(suit, animal, fruit):
    player = pd.DataFrame([[suit, animal, fruit]],
                              columns=["Card Suit", "Animal Name", "Fruit"])
    new_encoded = encoder.transform(player)
    probability = model.predict_proba(new_encoded)[0][1]
    return round(probability * 100, 2)


print(probabilityToBeatBoss("Hearts", "Lion", "Mango"), "%")