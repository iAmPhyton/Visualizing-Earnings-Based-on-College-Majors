import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
# controlling figure aesthetics: set font size, color, and style using seaborn
sns.set(font_scale=1.3)
sns.set_palette("husl")
sns.set_style("white")
recent_grads = pd.read_csv('recent-grads.csv')
'''recent_grads.iloc[:1] #return the first row formatted as a table
recent_grads.head() #getting familiar with the data structure
recent_grads.describe() #summary stats for all numeric columns
raw_data_count = len(recent_grads.index)
raw_data_count
#dropping rows containing missing values
recent_grads = recent_grads.dropna()
#checking number of rows of cleaned Dataframe
cleaned_data_count = len(recent_grads.index)
cleaned_data_count
#comparing 
'raw_data_count:'+str(raw_data_count)+'|'+'cleaned_data_count:'+str(cleaned_data_count)
#generating scatterplots in a go using a for loop
x_val = ['Sample_size','Sample_size','Full_time','ShareWomen','Men','Women']
y_val = ['Median','Unemployment_rate','Median','Unemployment_rate','Median','Median']
fig = plt.figure(figsize=(25,30))
for sp in range (len(x_val)):
    ax = fig.add_subplot(3,2,sp+1)
    ax = sns.scatterplot(data=recent_grads, x= x_val[sp], y= y_val[sp], hue= y_val[sp])
    plt.title(y_val[sp] + ' vs ' + x_val[sp], weight='bold').set_fontsize('13')
    sns.despine(left=True, bottom=True)
    plt.legend
plt.show()'''
#finding if students make more money in popular school majors - they don't.
'''fig, ax = plt.subplots(1,1, figsize =(10,5))
sns.scatterplot(data = recent_grads, x='Total', y='Median', hue ='Median')
sns.despine(left=True, bottom=True)
plt.title('Total vs. Median', weight='bold').set_fontsize('15')
plt.legend(bbox_to_anchor=(1.55, 0.5), title= 'Median')
plt.show()'''
#finding if students that majored in subjects that were majorly female make more money
#-ShareWomen = women as share of total
#-Median = median salary of full time , year-round workers.
'''fig, ax =plt.subplots(1,1, figsize =(10,5))
sns.scatterplot(data = recent_grads, x='ShareWomen', y='Median', hue ='Median')
sns.despine(left=True, bottom=True)
plt.title('Median vs. ShareWomen', weight='bold').set_fontsize('15')
plt.legend(bbox_to_anchor=(1.55,0.5), title= 'Median')
plt.show()'''
#deep dive intp median and sharewomen using groupby()
'''median_sharewomen = recent_grads.groupby(["ShareWomen"])["Median"].mean().sort_values(ascending=False)
print(median_sharewomen)'''
#splitting ShareWomen into 3 groups
'''sharewomen_grouped = recent_grads["ShareWomen"].value_counts(bins=3).sort_values(ascending=False)
print(sharewomen_grouped)'''
#using sns.barplot to create 3 bins
'''bins = [-0.0019690000000000003, 0.323, 0.646, 0.969] #using bins from previous results
median_sharewomen_grouped = recent_grads.groupby(pd.cut(recent_grads["ShareWomen"],
                                                 bins))["Median"].mean().sort_values(ascending= False)
print(median_sharewomen_grouped)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
plt.xlabel('ShareWomen')
plt.ylabel('Median')
sns.barplot(x=sorted(median_sharewomen_grouped.index), y=median_sharewomen_grouped, errorbar=None)
plt.title('Median vs ShareWomen (bins = 3)', weight='bold', fontsize=15)
sns.despine(left=True, bottom=True)
plt.show()'''

###generate histograms in a go using a for loop
#using 8 bins to simplify the visuals

'''cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]
colors = ['blue','green','red','purple','orange','pink','brown','gray']
# Iterate through the columns
for i, col in enumerate(cols):
    # Create a new figure for each histogram
    plt.figure(figsize=(8, 5))
    # Plot the histogram
    sns.histplot(data=recent_grads, x=col, bins=8, color=colors[i])
    sns.despine(left=True, bottom=True)
    plt.title(col, weight='bold', fontsize=16)
    plt.show()
    # Display statistics
    print('-------------------------------')
    print(recent_grads[col].describe())
    print('-------------------------------')'''

###analysis: going deep on Sample_size, Employed, SharedWomen, and Women
#exploring Sample_size: finding the percentage of sample size by dividing Sample_size by Full_time_year_round
'''common_samplesize = recent_grads[recent_grads["Sample_size"].between(0,500)]
common_samplesize.sort_values(by='Sample_size', ascending=False)
print(common_samplesize)'''
##calculating the sample size percentage of the dataset
'''sample_dataset = recent_grads["Sample_size"] / recent_grads["Full_time_year_round"]
sample_dataset.describe()
print(sample_dataset.describe())
#checking majors(0) with zero(0) people employed
print(recent_grads[recent_grads["Employed"] == 0])'''
###checking how many majors are predominantly male
#adding a new column
'''recent_grads["gender_majority"] = np.nan
#adding values to the new column
recent_grads.loc[recent_grads["ShareWomen"] > .5, "gender_majority"] = "Female"
recent_grads.loc[recent_grads["ShareWomen"] < .5, "gender_majority"] = "Male"
print(recent_grads)
# Create a figure with 1 row and 8 columns
fig = plt.subplots(1,2, figsize =(10,5))

#differentiate color b/w gender_majority using hue
sns.histplot(data = recent_grads, x= "gender_majority", hue = "gender_majority") 
sns.despine(left=True, bottom=True)
plt.title("gender_majority", weight='bold', fontsize=16)

#display #count on legend
plt.legend([str(count) for count in recent_grads["gender_majority"].value_counts()], bbox_to_anchor=(1, 1), title='Count')
plt.show() '''

#creating scatter plots to explore the relationship and distribution between Sample_size & median, Sample_size, median & Unemployment_rate
'''pairs = [['Sample_size','Median'], ['Sample_size','Median','Unemployment_rate']]
for pair in range(len(pairs)):
    pairplot = sns.pairplot(recent_grads[pairs[pair]])
    pairplot.fig.set_size_inches(10,10)
    for ax in pairplot.axes.flat: #rorating x-axis lables
        ax.tick_params("x",labelrotation=45)
plt.show()'''

#creating scatter matrix to explore the 3 questions
'''pairs = [['Total','Median'],['ShareWomen','Median'],['Full_time','Median']]
for pair in range(len(pairs)):
    pairplot = sns.pairplot(recent_grads[pairs[pair]])
    pairplot.fig.set_size_inches(10,10)
    for ax in pairplot.axes.flat: #rotating x-axis labels
        ax.tick_params("x", labelrotation=45)
plt.show()'''

#creating bar plots to compare columns
#first 10 rows
'''fig, ax = plt.subplots(1,1, figsize =(5,10))

plt.xlabel('Major')
plt.ylabel('ShareWomen')
sns.barplot(x=recent_grads[:10]['Major'], y=recent_grads[:10]['ShareWomen'], ci=None)
ax.set_xticklabels(recent_grads[:10]['Major'], rotation='vertical')
sns.despine(left=True, bottom=True)
plt.title("ShareWomen vs Major", weight='bold').set_fontsize('16')
plt.show() '''
#last 10 rows
'''fig, ax = plt.subplots(1,1, figsize =(0,5)) 

plt.xlabel('Major')
plt.ylabel('ShareWomen')
sns.barplot(x=recent_grads[-10:]['Major'], y=recent_grads[-10:]['ShareWomen'], ci=None)
ax.set_xticklabels(recent_grads[-10:]['Major'], rotation='vertical')
sns.despine(left=True, bottom=True)
plt.title("ShareWomen vs Major", weight='bold').set_fontsize('16')
plt.show()'''
#unemployment_rate vs major
#first 10 rows
'''fig, ax = plt.subplots(1,1, figsize=(10,5))

plt.xlabel('Major')
plt.ylabel('Unemployment_rate')
sns.barplot(x=recent_grads[:10]['Major'], y=recent_grads[:10]['Unemployment_rate'], ci=None)
ax.set_xticklabels(recent_grads[:10]['Major'], rotation='vertical')
sns.despine(left=True, bottom=True)
plt.title("Unemployment_rate vs Major", weight='bold').set_fontsize('16')
plt.show() '''
#last 10 rows
'''fig, ax = plt.subplots(1,1, figsize=(10,5))

plt.xlabel('Major')
plt.ylabel('Unemployment_rate')
sns.barplot(x=recent_grads[-10:]['Major'], y=recent_grads[-10:]['Unemployment_rate'], ci=None)
ax.set_xticklabels(recent_grads[-10:]['Major'], rotation='vertical')
sns.despine(left=True, bottom=True)
plt.title("Unemployment_rate vs Major", weight='bold').set_fontsize('16')
plt.show()'''

