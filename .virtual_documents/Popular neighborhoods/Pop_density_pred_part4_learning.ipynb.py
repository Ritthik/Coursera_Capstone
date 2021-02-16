import pandas as pd
df=pd.read_pickle("./df_analysis_part1")
import warnings; warnings.simplefilter('ignore')


df.shape


from sklearn.linear_model import LinearRegression


from statsmodels.regression.linear_model import OLS


from sklearn.model_selection import train_test_split


X=df[['Travel', 'Outdoors', 'Food', 'Arts',
       'Shops', 'Residence', 'Professional', 'Distance_to_Downtown [Km]',
       'Ratio_commuting', 'Ratio_renting', 'Average_income',
       'Population_change_ratio']]
y=df.Population_density


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.2)


result=OLS(y_train,X_train).fit()


result.summary()


from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test=train_test_split(X.values,y.values,random_state=0,test_size=0.3)


from sklearn.linear_model import LinearRegression


l=LinearRegression().fit(X_train,y_train)


l.coef_


l.intercept_


y_pred=l.predict(X_test)


from sklearn.metrics import explained_variance_score,r2_score


import matplotlib.pyplot as plt


plt.scatter(y_test,y_pred)


y_pred.shape


explained_variance_score(y_test,y_pred)


r2_score(y_test,y_pred)


df=pd.read_pickle("./df_analysis_scaled")


x=df["Population_change_ratio"]>0


df["Pop_change_direction"]=x.astype(int)


df


y=df["Pop_change_direction"].values


X=df[['Travel', 'Outdoors', 'Food', 'Arts',
       'Shops', 'Residence', 'Professional', 'Distance_to_Downtown [Km]',
       'Ratio_commuting', 'Ratio_renting', 'Average_income',
       'Population_density']].values


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.3)


import numpy as np
Ks = 20
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))
ConfustionMx = [];
for n in range(1,Ks):  
    neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
    yhat=neigh.predict(X_test)
    mean_acc[n-1] = accuracy_score(y_test, yhat)

    
    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])


plt.figure(figsize=(8,4))
plt.plot(range(1,Ks),mean_acc,'co-', linewidth=2, markersize=8)
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc, mean_acc + 1 * std_acc, alpha=0.10)
plt.legend(('Accuracy ', '+/- std X 3'))
plt.xlim(0.5,20.5)
plt.xticks(range(1,20))
plt.title('Finding the optimal $k$ with the elbow method', size=14)
plt.ylabel('Accuracy ')
plt.xlabel('Num of neighbors (K)')
plt.tight_layout()
plt.show()


df=pd.read_pickle("./df_analysis_scaled")


x=df["Population_change_ratio"]>0


df["Pop_change_direction"]=x.astype(int)


sum(x)


y=df["Pop_change_direction"].values
X=df[['Travel', 'Outdoors', 'Food', 'Arts',
       'Shops', 'Residence', 'Professional', 'Distance_to_Downtown [Km]',
       'Ratio_commuting', 'Ratio_renting', 'Average_income',
       'Population_density']].values

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.2)


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score

param_grid = {'max_depth': np.arange(3, 10), 'max_features':np.arange(2, 9), 'criterion':['gini','entropy']}

grid_DT = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=10, iid=False)
grid_DT.fit(X_train, y_train)
print(f'Best params: {grid_DT.best_params_}')
print(f'Best score: {grid_DT.best_score_}')
best_tree = grid_DT.best_estimator_


yhat=best_tree.predict(X_test)


from sklearn.metrics import f1_score, accuracy_score


print('F1 score: ', f1_score(y_test, yhat, average='weighted'))
print('accuracy_score: ', accuracy_score(y_test, yhat))


yhat


from sklearn.metrics import plot_confusion_matrix


plot_confusion_matrix(best_tree,X_test,y_test)


from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)


grid={"C":[0.001, 0.01, 0.1, 1, 10, 100, 1000], 
      "solver":["newton-cg", "lbfgs", "liblinear", "sag", "saga"]
     }
lr=LogisticRegression(max_iter=10000)
logreg=GridSearchCV(lr,grid,cv=10,iid=False)
logreg.fit(X_train,y_train)
best_lr = logreg.best_estimator_


yhat = best_lr.predict(X_test)
best_lr


print('F1 score: ', f1_score(y_test, yhat, average='weighted'))
print('Accuracy: ', accuracy_score(y_test, yhat))


from sklearn.metrics import classification_report

classification_report(y_test,yhat)


from sklearn.metrics import confusion_matrix


confusion_matrix(y_test,yhat)



