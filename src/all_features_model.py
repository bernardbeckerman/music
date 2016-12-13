from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
import pandas as pd
import dill

#import data
with open('df_train_anon.csv') as f:
    df = pd.read_csv(f,header=None)
X = df.drop(549, 1).as_matrix()
y = df[549].as_matrix()
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0
#fit model
param_grid = {"max_depth": [3, None],
              "max_features": [1, 3, 10],
              "min_samples_split": [1, 3, 10],
              "min_samples_leaf": [1, 3, 10],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}
rfc = GridSearchCV(RandomForestClassifier(n_estimators=100), param_grid=param_grid)
print 'starting fit'
rfc.fit(X,y)
print 'fit complete'
with open('q1.d', 'w') as f:
    dill.dump(rfc,f)
