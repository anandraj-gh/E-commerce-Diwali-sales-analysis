import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##======= CONCLUSION AT THE BOTTOM =======##

df = pd.read_csv('Diwali Sales Data.csv', encoding='latin1')


print(df.head())

df.drop(["Status","unnamed1"], axis=1, inplace=True)
print(df.shape)
print(df.head())

print(df.isnull().sum())

df.dropna(inplace = True)
print(df)

df['Amount'] = (df['Amount'].astype(int))
print(df['Amount'])
print(df[['Age', 'Orders', 'Amount']].describe())

##-----------------------------------------------------------

## TOTAL COUNT OF MALE AND FEMALE
ax= sns.countplot(data = df, x='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

##-----------------------------------------------------------

sales_gender = df.groupby('Gender')['Amount'].sum().reset_index().sort_values(by='Amount',ascending=True)
sns.barplot(x='Gender', y='Amount', data = sales_gender)
plt.show()

##-----------------------------------------------------------

## AGE
sales_age = df.groupby('Age Group')['Amount'].sum().reset_index().sort_values(by='Amount', ascending=True)
sns.barplot(x = 'Age Group', y ='Amount', data=sales_age)
plt.show()

ax = sns.countplot(x = 'Age Group', data=df, hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

##-----------------------------------------------------------

## Orders BY STATE TOP 10
sales_state = df.groupby('State')['Orders'].sum().reset_index().sort_values(by='Orders', ascending=False).head(10)
sns.set_theme(rc={'figure.figsize': (17,5)})
sns.barplot(x = 'State', y = 'Orders', data = sales_state, palette='pastel')
plt.show()

##-----------------------------------------------------------

## Sales BY STATE TOP 10
sales_state = df.groupby('State')['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False).head(10)
sns.set_theme(rc={'figure.figsize': (17,5)})
sns.barplot(x = 'State', y = 'Amount', data = sales_state, palette='pastel')
plt.show()

##-----------------------------------------------------------

## Martial status 
ax = sns.countplot(x = 'Marital_Status', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_marital = df.groupby(['Marital_Status', 'Gender'])['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False)
sns.set_theme(rc={'figure.figsize': (6,5)})
sns.barplot(x = 'Marital_Status', y = 'Amount', data = sales_marital, hue = 'Gender')
plt.show()

##-----------------------------------------------------------

## OCCUPATION 
ax = sns.countplot(x = 'Occupation', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_occupation = df.groupby(['Occupation'])['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False).head(10)
sns.set_theme(rc={'figure.figsize': (15,5)})
sns.barplot(x = 'Occupation', y = 'Amount', data = sales_occupation)
plt.show()

##-----------------------------------------------------------

## PRODUCT CATEGORY
ax = sns.countplot(x = 'Product_Category', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_product_c = df.groupby(['Product_Category'])['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False).head(10)
sns.set_theme(rc={'figure.figsize': (15,5)})
sns.barplot(x = 'Product_Category', y = 'Amount', data = sales_product_c)
plt.show()

##-----------------------------------------------------------

## PRODUCT CATEGORY
sales_product_c = df.groupby(['Product_ID'])['Orders'].sum().reset_index().sort_values(by='Orders', ascending=False).head(10)
sns.set_theme(rc={'figure.figsize': (15,5)})
sns.barplot(x = 'Product_ID', y = 'Orders', data = sales_product_c)
plt.show()

# print(df.columns)

##==== CONCLUSION ====##

# Married women between the age group of "26-35"yrs from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviation are 
# more likely to buy products from food, clothing and electronic category.