from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.metrics import roc_auc_score, recall_score, f1_score, accuracy_score, log_loss
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import json
from plot_learning_curve import plot_learning_curve
from sklearn.externals import joblib

with open('data.json', 'r') as json_data:
    data = json.load(json_data)
    json_data.close()

samples = []
image = []

c = 0

for x, y in data['stats']:
    if y == 1 or c <= 804:
        samples.append(x)
        image.append(y)

        if y == 0:
            c += 1

print(len(samples))

lr = LogisticRegression()
score_func = accuracy_score

x_train, x_test, y_train, y_test = train_test_split(samples, image, test_size=0.2)


print('fitting ...')
lr.fit(x_train, y_train)

print('predicting ...')
y_pred = lr.predict(x_test)
loss = log_loss(y_test, y_pred)
print('log_loss ... {}'.format(loss))
accuracy = accuracy_score(y_test, y_pred)
print('accuracy is ... {}'.format(accuracy))
auc = roc_auc_score(y_test, y_pred)
print('auc is  ... {}'.format(auc))
recall_1 = recall_score(y_test, y_pred)
print('recall for 1 is  ... {}'.format(recall_1))
recall_0 = recall_score(y_test, y_pred, pos_label=0)
print('recall for 0 is ... {}'.format(recall_0))

f1 = f1_score(y_test, y_pred)
print('f1 is  ... {}'.format(f1))


joblib.dump(lr, 'classifier.sav')

plot_learning_curve(lr, "Curva de aprendizaje", x_train, y_train)

# AB C H RBI BB K