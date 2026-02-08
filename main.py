import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

#Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
df = df.drop_duplicates()
print(df.columns)

#Numerical Columns Cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float).astype(int)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

#Categorical Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approve by rera': True, 'not approve by rera': False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()


# print(df)
print(df.info())

#Question 1:Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000} crores in {costliest_flat['socity']} society.")

#Question 2:Which locality has the highest average price?
avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {avg_price_locality}.") 

#Question 3: Which loacality has highest rate per sqft?
avg_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest average rate per sqft is {avg_rate_locality}.")

#Question 4: Do ready to move property cost more than under construction property?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].median()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].median()
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready to move properties cost more than under construction properties.")
else:    
    print("Under construction properties cost more than ready to move properties.")    

# Question 5: Do rera approve properties command the price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].median()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].median()
if rera_approved_avg_price > not_rera_approved_avg_price:
    print("RERA approved properties command a price premium.")
else:
    print("RERA approved properties do not command a price premium.")   

#Question 6: How does area impact the price?
# sns.scatterplot(x='area', y='price', data=df)
# plt.title('Area vs Price')
# plt.show() 

#Question 7: Which BHK Configuration is most expensive on per sqft basis?
avg_rate_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The BHK configuration with the highest average rate per sqft is {avg_rate_bhk} BHK.")

#Question 8: Which property type is costliest?
avg_price_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The costliest property type is {avg_price_property_type}.")

#Question 9: Do certain builders price higher?
top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
print("The top 5 builders that price higher are:", ", ".join(top_5_builders.index))

#Question 10: Are larger homes more expensive on a per sqft basis?
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area vs Rate per Sqft') 
plt.show()
    
    