import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot( [data] ,["math"] ,show_hist = False)
#fig.show()

mean =st.mean(data)
std = st.stdev(data)
print(f"mean and standard deviation of data is : {mean,std}")

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = st.mean(data_set)
    return mean

mean_list = []
for i in range(0,1000):
    s = random_set_of_mean(100)
    mean_list.append(s)

mean =st.mean(mean_list)
std = st.stdev(mean_list)
print(f"mean and standard deviation of sample data is : {mean,std}")
fig = ff.create_distplot( [mean_list] ,["math"] ,show_hist = False)
#fig.show()


first_stdstart,first_stdend = mean-std, mean+std
second_stdstart,second_stdend = mean-(std*2), mean+(std*2)
third_stdstart,third_stdend = mean-(std*3), mean+(std*3)

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.

df= pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

mean_sample1 = st.mean(data)
fig = ff.create_distplot( [data] ,["math"] ,show_hist = False)
fig.add_trace(go.Scatter( x = [mean,mean] , y = [0,0.17] , mode = "lines", name = "mean"))

fig.add_trace(go.Scatter( x = [mean_sample1,mean_sample1] , y = [0,0.17] , mode = "lines", name = "mean for sample 1"))

fig.add_trace(go.Scatter( x = [first_stdend,first_stdend] , y = [0,0.17] , mode = "lines", name = "std start"))
#fig.show()

# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.

df= pd.read_csv("data2.csv")
data = df["Math_score"].tolist()

mean_sample2 = st.mean(data)
fig = ff.create_distplot( [data] ,["math"] ,show_hist = False)
fig.add_trace(go.Scatter( x = [mean,mean] , y = [0,0.17] , mode = "lines", name = "mean"))

fig.add_trace(go.Scatter( x = [mean_sample2,mean_sample2] , y = [0,0.17] , mode = "lines", name = "mean for sample 2"))

fig.add_trace(go.Scatter( x = [first_stdend,first_stdend] , y = [0,0.17] , mode = "lines", name = "first std end"))

fig.add_trace(go.Scatter( x = [second_stdend,second_stdend] , y = [0,0.17] , mode = "lines", name = "second std end"))
#fig.show()

# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.


df= pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean_sample3 = st.mean(data)
fig = ff.create_distplot( [data] ,["math"] ,show_hist = False)
fig.add_trace(go.Scatter( x = [mean,mean] , y = [0,0.17] , mode = "lines", name = "mean"))

fig.add_trace(go.Scatter( x = [mean_sample3,mean_sample3] , y = [0,0.17] , mode = "lines", name = "mean for sample 3"))

fig.add_trace(go.Scatter( x = [first_stdend,first_stdend] , y = [0,0.17] , mode = "lines", name = "first std end"))

fig.add_trace(go.Scatter( x = [second_stdend,second_stdend] , y = [0,0.17] , mode = "lines", name = "second std end"))

fig.add_trace(go.Scatter( x = [third_stdend,third_stdend] , y = [0,0.17] , mode = "lines", name = "third std end"))

# fig.show()

#finding the z score using the formula
#zScore = (New Sample Mean - Sampling Distribution Mean) / standard deviation

zscore1 = (mean_sample1-mean) / std
zscore2 = (mean_sample2-mean) / std
zscore3 = (mean_sample3-mean) / std
print(f"zscore of first intervention : {zscore1}")
print(f"zscore of second intervention : {zscore2}")
print(f"zscore of third intervention : {zscore3}")
# since the zscore for third intervention is greater than 2 than it is more impactful