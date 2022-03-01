import plotly.figure_factory as ff
import plotly.graph_objects as go 
import pandas as pd
import statistics


df = pd.read_csv("StudentsPerformance.csv")
studentPer = df["reading score"].to_list()

mean = sum(studentPer) / len(studentPer)
median = statistics.median(studentPer)
mode = statistics.mode(studentPer)
std_deviation = statistics.stdev(studentPer)

print( f"Mean: {mean}")
print(f"Median: {median}")
print( f"Mode: {mode}")
print(f"Standard Deviation: {std_deviation}")

std_deviation = statistics.stdev(studentPer)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([studentPer], ["reading score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

thin_1_std_deviation = [result for result in studentPer if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in studentPer if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in studentPer if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(thin_1_std_deviation)*100.0/len(studentPer)))
print("{}% of data lies within 2 standard deviations".format(len(thin_2_std_deviation)*100.0/len(studentPer)))
print("{}% of data lies within 3 standard deviations".format(len(thin_3_std_deviation)*100.0/len(studentPer)))
