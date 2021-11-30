import plotly.graph_objects as go
import pandas as pd
import plotly.figure_factory as ff
import statistics as s
import random

df = pd.read_csv('C:/Users/Krithi/Desktop/Python/Class111/School3.csv')
data = df["Math_score"].tolist()
#fig = ff.create_distplot([data], ["MathScore"], show_hist = False)
#fig.show()
mean = s.mean(data)
standardDeviation = s.stdev(data)
#print(standardDeviation)
print(mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = s.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    #show_fig(mean_list)
    
    mean = s.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

SD = s.stdev(mean_list)
print("Standard deviation of sampling distribution:- ", SD)

firstSt, firstEnd = mean - SD, mean + SD 
secondSt, secondEnd = mean - (2*SD), mean + (2*SD)
thirdSt, thirdEnd = mean - (3*SD), mean + (3*SD)

print(firstSt)
print(firstEnd)
print(secondSt)
print(secondEnd)
print(thirdSt)
print(thirdEnd)

#students who got the tab
df1 = pd.read_csv('C:/Users/Krithi/Desktop/Python/Class111/School_1_Sample.csv')
data1 = df1["Math_score"].tolist()
m1 = s.mean(data1)
print(m1)

#students who got extra classes
df2 = pd.read_csv('C:/Users/Krithi/Desktop/Python/Class111/School_2_Sample.csv')
data2 = df2["Math_score"].tolist()
m2 = s.mean(data2)
print(m2)

#students who got extra paper to slove
df3 = pd.read_csv('C:/Users/Krithi/Desktop/Python/Class111/School_3_Sample.csv')
data3 = df3["Math_score"].tolist()
m3 = s.mean(data3)
print(m3)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [m1, m1], y = [0, 0.17], mode = "lines", name = "mean1"))
fig.add_trace(go.Scatter(x = [m2, m2], y = [0, 0.17], mode = "lines", name = "mean2"))
fig.add_trace(go.Scatter(x = [m3, m3], y = [0, 0.17], mode = "lines", name = "mean3"))
fig.show()

#zed score
zed_score1 = (mean - m1)/SD
print(zed_score1)
zed_score2 = (mean - m2)/SD
print(zed_score2)
zed_score3 = (mean - m3)/SD
print(zed_score3)