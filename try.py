import plotly.graph_objs as go
import plotly.offline as pyo

trace = go.Bar(x=['Team A', 'Team B', 'Team C'], y=[20, 14, 23])
data = [trace]

layout = go.Layout(title='Sample Bar Chart')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bar_chart.html')
