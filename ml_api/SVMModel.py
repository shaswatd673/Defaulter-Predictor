import numpy as np
import pandas as pd
from sklearn import preprocessing,svm

df = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/loan_train.csv')

df['due_date'] = pd.to_datetime(df['due_date'])
df['effective_date'] = pd.to_datetime(df['effective_date'])
df['dayofweek'] = df['effective_date'].dt.dayofweek
df['weekend']= df['dayofweek'].apply(lambda x: 1 if (x>3)  else 0)
df['Gender'].replace(to_replace=['male','female'], value=[0,1],inplace=True)
Feature = df[['Principal','terms','age','Gender','weekend']]
Feature = pd.concat([Feature,pd.get_dummies(df['education'])], axis=1)
Feature.drop(['Master or Above'], axis = 1,inplace=True)
X = Feature
y = df['loan_status'].values
X = preprocessing.StandardScaler().fit(X).transform(X)
SVM_model = svm.SVC()
SVM_model.fit(X, y) 


class svm_predictor:
    def __init__(self,user):
        self.user=pd.DataFrame(user,index=[0])
        self.feature = self.user[['Principal','terms','age','Gender','weekend']]
        ad = {'Bechalor':[0],'High School or Below':[0],'college': [0]}
        add = pd.DataFrame(ad)
        self.feature = pd.concat([self.feature,add], axis=1)
        if self.user['education'][0]=='college':
            self.feature['college'][0]=1
        elif self.user['education'][0]=='High School or Below':
            self.feature['High School or Below'][0]=1
        elif self.user['education'][0]=='Bechalor':
            self.feature['Bechalor'][0]=1
        print(self.feature)

    def predict(self):
        X_test = preprocessing.StandardScaler().fit(self.feature).transform(self.feature)
        result = SVM_model.predict(X_test)
        return {'result':result[0]}


            
