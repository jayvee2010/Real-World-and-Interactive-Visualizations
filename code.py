

#1. Treemap (Company Department Budget)
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'Sales', 'Marketing'],
    'Budget': [20000, 50000, 40000, 30000]
})

fig = px.treemap(df, path=['Department'], values='Budget',
                 title="Company Budget Distribution")

fig.show()
     

#2.Dendrogram
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Sample data (can represent students, features, etc.)
data = np.array([
    [5, 3],
    [10, 15],
    [15, 12],
    [24, 10],
    [30, 30]
])

# Perform hierarchical clustering
linked = linkage(data, method='ward')

# Plot dendrogram
plt.figure(figsize=(6,4))
dendrogram(linked)

plt.title("Dendrogram Example")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.show()
     


# 3.Venn Diagram
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Create Venn Diagram
venn2([A, B], set_labels=('Set A', 'Set B'))

# Title
plt.title("Venn Diagram Example")

plt.show()
     


#4. Sankey Diagram (Student Flow)
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(label=["Admission", "First Year", "Second Year", "Placed"]),
    link=dict(
        source=[0, 1, 2],
        target=[1, 2, 3],
        value=[100, 80, 60])
)])

fig.show()
     

# 5. 3D Scatter Plot (Student Performance)
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'Study_Hours': [2,4,6,8,5],
    'Marks': [50,65,75,90,70],
    'Attendance': [60,75,80,90,70]
})

fig = px.scatter_3d(df,
                    x='Study_Hours',
                    y='Marks',
                    z='Attendance',
                    title="Student Performance Analysis")

fig.show()
     

# 6. Radar Chart (Skill Assessment)
import plotly.graph_objects as go

skills = ['Python','ML','DBMS','DSA','Communication']
values = [4,3,5,4,3]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=skills,
    fill='toself',
    name='Student Skills'
))

fig.show()
     
🚀 Extra / Self Learning (Advanced Interactive Visualizations)

This section demonstrates advanced interactive visualization techniques beyond the core experiment, showcasing independent learning in Plotly, network analysis, and specialized charts.

1. Sunburst Chart - Hierarchical Data Visualization

A Sunburst Chart is a hierarchical pie chart that shows how data is distributed across multiple levels of a hierarchy. It's ideal for visualizing nested categorical data.


# Sunburst Chart - Company Organization Structure
import plotly.express as px
import pandas as pd

# Hierarchical data: Company -> Department -> Team
data = {
    'Entity': ['Company', 'Company', 'Company', 'Company',
               'Engineering', 'Engineering', 'Marketing', 'Marketing',
               'Sales', 'Sales', 'HR', 'HR',
               'Frontend', 'Backend', 'Digital', 'Content',
               'North', 'South', 'Recruiting', 'Training'],
    'Parent': ['', '', '', '',
               'Company', 'Company', 'Company', 'Company',
               'Company', 'Company', 'Company', 'Company',
               'Engineering', 'Engineering', 'Marketing', 'Marketing',
               'Sales', 'Sales', 'HR', 'HR'],
    'Value': [0, 0, 0, 0,
              150, 80, 60, 40,
              50, 30, 20, 15,
              75, 75, 40, 20,
              30, 20, 10, 5],
    'Type': ['Root', 'Root', 'Root', 'Root',
             'Department', 'Department', 'Department', 'Department',
             'Department', 'Department', 'Department', 'Department',
             'Team', 'Team', 'Team', 'Team',
             'Team', 'Team', 'Team', 'Team']
}

df_sunburst = pd.DataFrame(data)

# Create sunburst chart
fig = px.sunburst(
    df_sunburst,
    names='Entity',
    parents='Parent',
    values='Value',
    title='🏢 Company Organization Structure - Sunburst Chart',
    color='Type',
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig.update_layout(
    width=700,
    height=700,
    title_font_size=16
)

fig.show()

print("📊 Sunburst Chart shows hierarchical data in a circular layout.")
print("   - Inner ring: Top-level categories")
print("   - Outer rings: Sub-categories")
print("   - Size: Proportional to values")
     
📊 Sunburst Chart shows hierarchical data in a circular layout.
   - Inner ring: Top-level categories
   - Outer rings: Sub-categories
   - Size: Proportional to values
Insight: Sunburst charts are excellent for showing how categories break down into sub-categories, making it easy to see both the hierarchy and relative proportions.

2. Parallel Coordinates Plot - Multivariate Analysis

A Parallel Coordinates Plot is used for visualizing high-dimensional data. Each vertical axis represents a variable, and each line represents an observation.


# Parallel Coordinates Plot - Student Performance Analysis
import plotly.express as px
import pandas as pd
import numpy as np

# Generate sample student data
np.random.seed(42)
n_students = 50

df_parallel = pd.DataFrame({
    'Student_ID': range(1, n_students + 1),
    'Math_Score': np.random.randint(40, 100, n_students),
    'Physics_Score': np.random.randint(35, 95, n_students),
    'Chemistry_Score': np.random.randint(45, 98, n_students),
    'English_Score': np.random.randint(50, 100, n_students),
    'Attendance_Rate': np.random.randint(60, 100, n_students),
    'Study_Hours': np.random.randint(2, 10, n_students)
})

# Calculate average and assign grade
df_parallel['Average'] = df_parallel[['Math_Score', 'Physics_Score', 'Chemistry_Score', 'English_Score']].mean(axis=1)
df_parallel['Grade'] = pd.cut(df_parallel['Average'],
                               bins=[0, 50, 60, 70, 80, 100],
                               labels=['Fail', 'Pass', 'Second Class', 'First Class', 'Distinction'])

# Create parallel coordinates plot
fig = px.parallel_coordinates(
    df_parallel,
    dimensions=['Math_Score', 'Physics_Score', 'Chemistry_Score', 'English_Score', 'Attendance_Rate'],
    color='Average',
    color_continuous_scale=px.colors.sequential.Viridis,
    title='📚 Student Performance - Parallel Coordinates Plot'
)

fig.update_layout(
    width=900,
    height=500,
    title_font_size=16
)

fig.show()

print("📊 Parallel Coordinates Plot shows multivariate data.")
print("   - Each vertical line represents a variable")
print("   - Each horizontal line represents a student")
print("   - Color indicates overall average score")
     
📊 Parallel Coordinates Plot shows multivariate data.
   - Each vertical line represents a variable
   - Each horizontal line represents a student
   - Color indicates overall average score
Insight: Parallel coordinates plots help identify patterns, clusters, and outliers in high-dimensional data. Lines that follow similar paths indicate similar observations.

3. Animated Scatter Plot - Time Series Animation

An Animated Scatter Plot shows how data changes over time by animating the transition between different time points. This is powerful for showing trends and evolution.


# Animated Scatter Plot - GDP vs Life Expectancy Over Time
import plotly.express as px
import pandas as pd
import numpy as np

# Create sample country development data over years
np.random.seed(42)
countries = ['USA', 'China', 'India', 'Germany', 'Japan', 'Brazil', 'UK', 'France']
years = list(range(2010, 2024))

data_animated = []
for country in countries:
    base_gdp = np.random.randint(1000, 50000)
    base_life = np.random.randint(60, 75)
    for year in years:
        data_animated.append({
            'Country': country,
            'Year': year,
            'GDP_per_Capita': base_gdp + (year - 2010) * np.random.randint(200, 800),
            'Life_Expectancy': base_life + (year - 2010) * np.random.uniform(0.1, 0.3),
            'Population': np.random.randint(10, 300) * 1000000
        })

df_animated = pd.DataFrame(data_animated)

# Create animated scatter plot
fig = px.scatter(
    df_animated,
    x='GDP_per_Capita',
    y='Life_Expectancy',
    animation_frame='Year',
    animation_group='Country',
    size='Population',
    color='Country',
    hover_name='Country',
    log_x=True,
    size_max=60,
    range_x=[1000, 60000],
    range_y=[55, 90],
    title='🌍 GDP vs Life Expectancy (2010-2023)'
)

fig.update_layout(
    width=900,
    height=600,
    title_font_size=16,
    xaxis_title='GDP per Capita (USD, log scale)',
    yaxis_title='Life Expectancy (years)'
)

fig.show()

print("🎬 Animated plots show temporal evolution of data.")
print("   - Press Play to start animation")
print("   - Use slider to navigate through years")
print("   - Each dot represents a country")
     
🎬 Animated plots show temporal evolution of data.
   - Press Play to start animation
   - Use slider to navigate through years
   - Each dot represents a country
Insight: Animated visualizations are powerful for storytelling and showing how metrics evolve. The bubble size represents population, color represents country.

4. Gauge Chart (Speedometer) - KPI Dashboard

A Gauge Chart displays a single metric within a range, commonly used for KPIs and performance indicators.


# Gauge Chart - Performance Metrics Dashboard
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create subplots for multiple gauges
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'type': 'indicator'}, {'type': 'indicator'}],
           [{'type': 'indicator'}, {'type': 'indicator'}]],
    subplot_titles=['Server Uptime', 'CPU Usage', 'Memory Usage', 'Network Speed']
)

# Server Uptime Gauge
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=98.5,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': 'Uptime %'},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "darkgreen"},
        'steps': [
            {'range': [0, 50], 'color': "lightgray"},
            {'range': [50, 80], 'color': "yellow"},
            {'range': [80, 100], 'color': "lightgreen"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 99
        }
    }
), row=1, col=1)

# CPU Usage Gauge
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=65,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': 'CPU %'},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "blue"},
        'steps': [
            {'range': [0, 40], 'color': "lightgreen"},
            {'range': [40, 70], 'color': "yellow"},
            {'range': [70, 100], 'color': "lightcoral"}
        ]
    }
), row=1, col=2)

# Memory Usage Gauge
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=78,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': 'Memory %'},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "purple"},
        'steps': [
            {'range': [0, 50], 'color': "lightgreen"},
            {'range': [50, 80], 'color': "yellow"},
            {'range': [80, 100], 'color': "red"}
        ]
    }
), row=2, col=1)

# Network Speed Gauge
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=125,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': 'Speed (Mbps)'},
    gauge={
        'axis': {'range': [0, 200]},
        'bar': {'color': "orange"},
        'steps': [
            {'range': [0, 50], 'color': "lightcoral"},
            {'range': [50, 100], 'color': "yellow"},
            {'range': [100, 200], 'color': "lightgreen"}
        ]
    }
), row=2, col=2)

fig.update_layout(
    height=600,
    width=800,
    title_text="🖥️ System Performance Dashboard",
    title_font_size=18
)

fig.show()

print("📊 Gauge charts are perfect for KPI dashboards.")
print("   - Color zones indicate status (good/warning/critical)")
print("   - Threshold line shows target value")
print("   - Number display shows exact value")
     
📊 Gauge charts are perfect for KPI dashboards.
   - Color zones indicate status (good/warning/critical)
   - Threshold line shows target value
   - Number display shows exact value
Insight: Gauge charts are widely used in dashboards and reports to show performance against targets. The color zones make it easy to identify status at a glance.

5. Funnel Chart - Process Flow Analysis

A Funnel Chart visualizes stages in a process, showing how values decrease through successive stages. Ideal for sales pipelines, conversion funnels, and process analysis.


# Funnel Chart - Sales Pipeline Analysis
import plotly.graph_objects as go

# Sales pipeline stages
stages = ['Website Visits', 'Sign Ups', 'Product Views', 'Add to Cart', 'Checkout', 'Purchase']
values = [10000, 6000, 4500, 2500, 1500, 800]

# Calculate conversion rates
conversion_rates = [f"{round((values[i+1]/values[i])*100, 1)}%" for i in range(len(values)-1)]

fig = go.Figure(go.Funnel(
    y=stages,
    x=values,
    textposition='inside',
    textinfo='value+percent initial',
    marker={
        'color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
        'line': {'width': 2, 'color': 'white'}
    }
))

fig.update_layout(
    title='📈 Sales Funnel - Customer Journey Analysis',
    width=800,
    height=500,
    title_font_size=18
)

fig.show()

print("📊 Funnel Chart Analysis:")
print("   - Shows progression through stages")
print("   - Width represents quantity at each stage")
print("   - Ideal for conversion analysis")
print(f"\n📊 Conversion Rates:")
for i, stage in enumerate(stages[:-1]):
    print(f"   {stage} → {stages[i+1]}: {conversion_rates[i]}")
     
📊 Funnel Chart Analysis:
   - Shows progression through stages
   - Width represents quantity at each stage
   - Ideal for conversion analysis

📊 Conversion Rates:
   Website Visits → Sign Ups: 60.0%
   Sign Ups → Product Views: 75.0%
   Product Views → Add to Cart: 55.6%
   Add to Cart → Checkout: 60.0%
   Checkout → Purchase: 53.3%
Insight: Funnel charts help identify drop-off points in processes. This example shows a typical e-commerce conversion funnel where 92% of visitors are lost before purchase.

6. Waterfall Chart - Cumulative Changes

A Waterfall Chart shows how positive and negative values contribute to a running total. Perfect for financial analysis, budget changes, and understanding cumulative effects.


# Waterfall Chart - Monthly Budget Analysis
import plotly.graph_objects as go

# Budget categories
categories = ['Starting Balance', 'Income', 'Marketing', 'Operations', 'R&D', 'Ending Balance']
values = [50000, 30000, -8000, -12000, -15000, 45000]

# Define which are relative and totals
measure = ['absolute', 'relative', 'relative', 'relative', 'relative', 'absolute']

fig = go.Figure(go.Waterfall(
    name='Budget',
    orientation='v',
    measure=measure,
    x=categories,
    y=values,
    connector={'line': {'color': 'rgb(63, 63, 63)', 'width': 2}},
    increasing={'marker': {'color': 'green'}},
    decreasing={'marker': {'color': 'red'}},
    totals={'marker': {'color': 'blue'}}
))

fig.update_layout(
    title='💰 Monthly Budget Waterfall Analysis',
    width=800,
    height=500,
    title_font_size=18,
    yaxis_title='Amount ($)',
    showlegend=True
)

fig.show()

print("📊 Waterfall Chart Analysis:")
print("   - Green bars: Positive contributions (income)")
print("   - Red bars: Negative contributions (expenses)")
print("   - Blue bars: Total values (starting/ending)")
print("   - Shows cumulative effect of changes")
     
📊 Waterfall Chart Analysis:
   - Green bars: Positive contributions (income)
   - Red bars: Negative contributions (expenses)
   - Blue bars: Total values (starting/ending)
   - Shows cumulative effect of changes
Insight: Waterfall charts clearly show how individual contributions affect the bottom line. Essential for financial reporting and understanding variance analysis.

7. Network Graph - Relationship Visualization

A Network Graph visualizes relationships between entities using nodes and edges. Useful for social networks, dependency analysis, and organizational structures.


# Network Graph - Social Network Analysis
import plotly.graph_objects as go
import networkx as nx
import numpy as np

# Create a sample social network
G = nx.Graph()

# Add nodes (people)
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry']
G.add_nodes_from(people)

# Add edges (connections)
connections = [
    ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'David'),
    ('Bob', 'Charlie'), ('Bob', 'Eve'),
    ('Charlie', 'David'), ('Charlie', 'Frank'),
    ('David', 'Grace'),
    ('Eve', 'Frank'), ('Eve', 'Grace'),
    ('Frank', 'Grace'), ('Frank', 'Henry'),
    ('Grace', 'Henry')
]
G.add_edges_from(connections)

# Calculate positions using spring layout
pos = nx.spring_layout(G, k=1.5, iterations=50)

# Create edges trace
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.5, color='#888'),
    hoverinfo='none',
    mode='lines'
)

# Create nodes trace
node_x = [pos[node][0] for node in G.nodes()]
node_y = [pos[node][1] for node in G.nodes()]

# Calculate degree for node size
node_degree = [G.degree(node) * 5 + 10 for node in G.nodes()]

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=list(G.nodes()),
    textposition='top center',
    hoverinfo='text',
    marker=dict(
        size=node_degree,
        color=node_degree,
        colorscale='Viridis',
        line=dict(width=2, color='white'),
        showscale=True,
        colorbar=dict(title='Connections')
    )
)

# Create figure
fig = go.Figure(data=[edge_trace, node_trace],
    layout=go.Layout(
        title='🔗 Social Network Graph - Node Size = Connections',
        title_font_size=18,
        showlegend=False,
        width=800,
        height=600,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
)

fig.show()

print("📊 Network Graph Analysis:")
print("   - Nodes represent individuals")
print("   - Edges represent connections")
print("   - Node size indicates number of connections")
print("   - Color intensity shows centrality")
     
📊 Network Graph Analysis:
   - Nodes represent individuals
   - Edges represent connections
   - Node size indicates number of connections
   - Color intensity shows centrality
Insight: Network graphs reveal community structure, important connectors, and relationship patterns. The size of each node indicates its influence (degree centrality).

8. Choropleth Map - Geographic Data Visualization

A Choropleth Map displays data on a geographic map using color intensity to represent values. Essential for regional analysis and geographic comparisons.


# Choropleth Map - Population by Country
import plotly.express as px
import pandas as pd

# Sample population data for countries
data_map = {
    'Country': ['India', 'United States', 'China', 'Brazil', 'Russia',
                'Japan', 'Germany', 'United Kingdom', 'France', 'Canada',
                'Australia', 'Mexico', 'Indonesia', 'South Korea', 'Italy'],
    'Population_Millions': [1400, 330, 1410, 213, 144,
                           126, 83, 68, 67, 38,
                           26, 128, 274, 52, 60],
    'GDP_Trillions': [3.7, 25.5, 18.3, 1.9, 1.8,
                      4.2, 4.1, 3.1, 2.9, 2.0,
                      1.7, 1.3, 1.3, 1.8, 2.1]
}

df_map = pd.DataFrame(data_map)

# Create choropleth map
fig = px.choropleth(
    df_map,
    locations='Country',
    locationmode='country names',
    color='Population_Millions',
    hover_name='Country',
    hover_data=['GDP_Trillions'],
    color_continuous_scale=px.colors.sequential.Plasma,
    title='🗺️ World Population by Country (Millions)',
    projection='natural earth'
)

fig.update_layout(
    width=1000,
    height=600,
    title_font_size=18,
    coloraxis_colorbar=dict(title='Population (M)')
)

fig.show()

print("📊 Choropleth Map Features:")
print("   - Color intensity represents data values")
print("   - Hover shows detailed information")
print("   - Interactive zoom and pan")
print("   - Multiple projection options available")
     
📊 Choropleth Map Features:
   - Color intensity represents data values
   - Hover shows detailed information
   - Interactive zoom and pan
   - Multiple projection options available
Insight: Choropleth maps provide immediate visual comparison across geographic regions. Hover to see additional data like GDP for each country.

9. Density Contour Plot - 2D Density Estimation

A Density Contour Plot shows the density of data points in 2D space, similar to a topographical map. Useful for identifying clusters and distributions.


import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go # Import go for trace type selection

# Generate sample height-weight data
np.random.seed(42)
n = 500

# Create clustered data (different body types)
height_cluster1 = np.random.normal(170, 8, n//3)
weight_cluster1 = np.random.normal(65, 10, n//3)

height_cluster2 = np.random.normal(180, 7, n//3)
weight_cluster2 = np.random.normal(80, 12, n//3)

height_cluster3 = np.random.normal(160, 6, n//3)
weight_cluster3 = np.random.normal(55, 8, n//3)

df_density = pd.DataFrame({
    'Height_cm': np.concatenate([height_cluster1, height_cluster2, height_cluster3]),
    'Weight_kg': np.concatenate([weight_cluster1, weight_cluster2, weight_cluster3]),
    'Body_Type': ['Average']* (n//3) + ['Athletic']* (n//3) + ['Slim']* (n//3)
})

# Create density contour plot
fig = px.density_contour(
    df_density,
    x='Height_cm',
    y='Weight_kg',
    color='Body_Type',
    title='📊 Height vs Weight Density Distribution',
    marginal_x='histogram',
    marginal_y='histogram'
)

# Update traces, specifying 'go.Contour' to only apply to contour traces
fig.update_traces(selector=dict(type='contour'), contours_coloring='fill', contours_showlabels=True)

fig.update_layout(
    width=900,
    height=600,
    title_font_size=18,
    xaxis_title='Height (cm)',
    yaxis_title='Weight (kg)'
)

fig.show()

print("📊 Density Contour Features:")
print("   - Contours show data concentration")
print("   - Higher density = more data points")
print("   - Marginal histograms show distributions")
print("   - Color distinguishes different groups")
     
📊 Density Contour Features:
   - Contours show data concentration
   - Higher density = more data points
   - Marginal histograms show distributions
   - Color distinguishes different groups
Insight: Density contour plots reveal the concentration of data points and help identify clusters. Marginal histograms show individual distributions.

10. Polar Scatter Plot - Circular Data Distribution

A Polar Scatter Plot displays data points on a circular coordinate system using radius and angle. Useful for directional data, radar comparisons, and circular patterns.


# Polar Scatter Plot - Wind Direction and Speed
import plotly.graph_objects as go
import numpy as np

# Generate wind data
np.random.seed(42)
n_points = 100

# Wind directions (angles in degrees)
angles = np.random.uniform(0, 360, n_points)
# Wind speeds (radius)
speeds = np.random.uniform(0, 50, n_points)

# Create polar scatter plot
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=speeds,
    theta=angles,
    mode='markers',
    marker=dict(
        size=8,
        color=speeds,
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title='Speed (km/h)')
    ),
    name='Wind Measurements'
))

# Add reference circles
fig.add_trace(go.Scatterpolar(
    r=[25, 25],
    theta=[0, 360],
    mode='lines',
    line=dict(color='red', width=2, dash='dash'),
    name='Warning Level'
))

fig.update_layout(
    title='🌪️ Wind Speed Distribution by Direction',
    title_font_size=18,
    width=700,
    height=600,
    polar=dict(
        radialaxis=dict(range=[0, 60]),
        angularaxis=dict(direction='clockwise')
    ),
    showlegend=True
)

fig.show()

print("📊 Polar Plot Applications:")
print("   - Wind direction and speed analysis")
print("   - Antenna radiation patterns")
print("   - Circular periodic data")
print("   - Compass and navigation data")
     
📊 Polar Plot Applications:
   - Wind direction and speed analysis
   - Antenna radiation patterns
   - Circular periodic data
   - Compass and navigation data
Insight: Polar plots are essential for directional data analysis. The radial axis represents magnitude (wind speed) and the angular axis represents direction.

11. Timeline / Gantt Chart - Project Schedule

A Gantt Chart displays project schedules showing start and end times for tasks. Essential for project management and timeline visualization.


# Gantt Chart - Project Timeline
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Define project tasks
tasks = [
    dict(Task='Requirement Analysis', Start='2024-01-01', Finish='2024-01-15', Resource='Planning'),
    dict(Task='System Design', Start='2024-01-10', Finish='2024-01-31', Resource='Design'),
    dict(Task='Database Setup', Start='2024-01-25', Finish='2024-02-10', Resource='Backend'),
    dict(Task='Frontend Development', Start='2024-02-01', Finish='2024-02-28', Resource='Frontend'),
    dict(Task='Backend Development', Start='2024-02-05', Finish='2024-03-05', Resource='Backend'),
    dict(Task='Integration Testing', Start='2024-03-01', Finish='2024-03-15', Resource='Testing'),
    dict(Task='User Acceptance Testing', Start='2024-03-10', Finish='2024-03-20', Resource='Testing'),
    dict(Task='Deployment', Start='2024-03-18', Finish='2024-03-25', Resource='DevOps'),
    dict(Task='Documentation', Start='2024-03-20', Finish='2024-03-31', Resource='Documentation')
]

df_gantt = pd.DataFrame(tasks)

# Create Gantt chart
fig = px.bar(
    df_gantt,
    x='Start',
    y='Task',
    color='Resource',
    orientation='h',
    hover_data=['Finish'],
    title='📅 Project Timeline - Gantt Chart',
    color_discrete_sequence=px.colors.qualitative.Set2
)

# Calculate task durations and update
fig.update_layout(
    width=1000,
    height=500,
    title_font_size=18,
    xaxis_title='Timeline',
    yaxis_title='Tasks',
    bargap=0.3,
    showlegend=True
)

fig.show()

print("📊 Gantt Chart Features:")
print("   - Shows task durations on timeline")
print("   - Color-coded by resource/team")
print("   - Identifies parallel tasks")
print("   - Shows project dependencies")
     
📊 Gantt Chart Features:
   - Shows task durations on timeline
   - Color-coded by resource/team
   - Identifies parallel tasks
   - Shows project dependencies
Insight: Gantt charts are essential for project management, helping teams visualize task dependencies, parallel activities, and overall project timeline.

12. 3D Surface Plot - Mathematical Surface Visualization

A 3D Surface Plot visualizes a mathematical function z = f(x, y) as a 3D surface. Useful for understanding relationships between three continuous variables.


# 3D Surface Plot - Mathematical Function
import plotly.graph_objects as go
import numpy as np

# Create mesh grid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Mathematical function: z = sin(sqrt(x² + y²))
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(
    z=Z, x=X, y=Y,
    colorscale='Viridis',
    colorbar=dict(title='Z Value'),
    contours=dict(
        z=dict(show=True, usecolormap=True, highlightcolor='lime', project=dict(z=True))
    )
)])

fig.update_layout(
    title='📐 3D Surface: z = sin(√(x² + y²))',
    title_font_size=18,
    width=800,
    height=700,
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        camera=dict(eye=dict(x=1.5, y=1.5, z=0.8))
    )
)

fig.show()

print("📊 3D Surface Plot Features:")
print("   - Visualizes mathematical functions")
print("   - Interactive rotation and zoom")
print("   - Color indicates Z value")
print("   - Contours show elevation levels")
     
📊 3D Surface Plot Features:
   - Visualizes mathematical functions
   - Interactive rotation and zoom
   - Color indicates Z value
   - Contours show elevation levels
Insight: 3D surface plots are powerful for visualizing mathematical functions and understanding relationships between three continuous variables. The interactive rotation helps explore the surface from different angles.

13. Multiple Radar Charts Comparison

Comparing multiple entities on radar charts helps identify strengths and weaknesses across different dimensions.


# Multiple Radar Charts - Employee Skills Comparison
import plotly.graph_objects as go
import numpy as np

# Define skill categories
skills = ['Python', 'SQL', 'Communication', 'Leadership', 'Problem Solving', 'Teamwork']

# Skills data for multiple employees
employees = {
    'Employee A': [4.5, 4.0, 3.5, 3.0, 4.5, 4.0],
    'Employee B': [3.5, 4.5, 4.5, 4.0, 3.5, 4.5],
    'Employee C': [5.0, 3.5, 3.0, 4.5, 4.0, 3.5]
}

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

fig = go.Figure()

for i, (name, scores) in enumerate(employees.items()):
    fig.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],  # Close the polygon
        theta=skills + [skills[0]],  # Close the polygon
        fill='toself',
        name=name,
        line=dict(color=colors[i], width=2),
        opacity=0.6
    ))

fig.update_layout(
    title='👥 Employee Skills Comparison',
    title_font_size=18,
    width=700,
    height=600,
    polar=dict(
        radialaxis=dict(range=[0, 5], visible=True),
        angularaxis=dict(rotation=30)
    ),
    showlegend=True,
    legend=dict(yanchor='top', y=0.99, xanchor='left', x=0.01)
)

fig.show()

# Calculate and display average scores
print("📊 Skills Analysis:")
for name, scores in employees.items():
    avg = np.mean(scores)
    print(f"   {name}: Average Score = {avg:.2f}/5.0")
print("\n   📈 Higher scores indicate stronger skills")
print("   📊 Overlapping areas show common strengths")
     
📊 Skills Analysis:
   Employee A: Average Score = 3.92/5.0
   Employee B: Average Score = 4.08/5.0
   Employee C: Average Score = 3.92/5.0

   📈 Higher scores indicate stronger skills
   📊 Overlapping areas show common strengths
Insight: Overlapping radar charts make it easy to compare multiple entities. Areas where one chart extends beyond others indicate competitive advantages.

14. Bullet Chart - Performance vs Target

A Bullet Chart is a variation of a bar chart developed for dashboard displays. It shows actual performance against target and qualitative ranges.


# Bullet Chart - KPI Performance Dashboard
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# KPI data: actual, target, and ranges
kpis = [
    {'title': 'Revenue', 'actual': 85, 'target': 100, 'ranges': [50, 75, 90, 100]},
    {'title': 'Customer Satisfaction', 'actual': 92, 'target': 95, 'ranges': [60, 80, 90, 100]},
    {'title': 'New Users', 'actual': 1250, 'target': 1000, 'ranges': [500, 800, 1000, 1500]},
    {'title': 'Task Completion', 'actual': 78, 'target': 90, 'ranges': [50, 70, 85, 100]}
]

fig = make_subplots(
    rows=4, cols=1,
    subplot_titles=[kpi['title'] for kpi in kpis],
    vertical_spacing=0.1
)

for i, kpi in enumerate(kpis, 1):
    # Normalize values
    max_val = kpi['ranges'][-1]
    actual_norm = (kpi['actual'] / max_val) * 100
    target_norm = (kpi['target'] / max_val) * 100
    ranges_norm = [(r / max_val) * 100 for r in kpi['ranges']]

    # Background ranges
    fig.add_trace(go.Bar(
        x=[ranges_norm[3]], y=[f"KPI {i}"],
        orientation='h', marker_color='lightgray', name='',
        showlegend=False, width=0.5
    ), row=i, col=1)

    # Actual performance bar
    fig.add_trace(go.Bar(
        x=[actual_norm], y=[f"KPI {i}"],
        orientation='h', marker_color='darkblue', name='Actual',
        showlegend=(i==1), width=0.3
    ), row=i, col=1)

    # Target marker
    fig.add_trace(go.Scatter(
        x=[target_norm], y=[f"KPI {i}"],
        mode='markers', marker_symbol='line-ns', marker_size=15,
        marker_color='red', name='Target', showlegend=(i==1)
    ), row=i, col=1)

fig.update_layout(
    height=600,
    width=800,
    title='📊 KPI Performance Dashboard - Bullet Charts',
    title_font_size=18,
    showlegend=True
)

fig.show()

print("📊 Bullet Chart Analysis:")
for kpi in kpis:
    status = '✅ Above Target' if kpi['actual'] >= kpi['target'] else '⚠️ Below Target'
    print(f"   {kpi['title']}: {kpi['actual']} / {kpi['target']} {status}")
     
📊 Bullet Chart Analysis:
   Revenue: 85 / 100 ⚠️ Below Target
   Customer Satisfaction: 92 / 95 ⚠️ Below Target
   New Users: 1250 / 1000 ✅ Above Target
   Task Completion: 78 / 90 ⚠️ Below Target
Insight: Bullet charts efficiently compare actual performance against targets. The target marker clearly shows goals, while background ranges provide context for performance levels.

15. Summary Statistics Dashboard

A comprehensive dashboard combining multiple visualization types for complete data analysis.


# Comprehensive Summary Dashboard
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

print("=" * 70)
print("📊 COMPREHENSIVE VISUALIZATION SUMMARY")
print("=" * 70)
print()

# Summary of all visualization types covered
visualizations = {
    'Core Experiment': {
        'Treemap': 'Hierarchical part-to-whole relationships',
        'Dendrogram': 'Hierarchical clustering visualization',
        'Venn Diagram': 'Set relationships and intersections',
        'Sankey Diagram': 'Flow between stages/nodes',
        '3D Scatter Plot': 'Three-dimensional data relationships',
        'Radar Chart': 'Multi-dimensional comparison'
    },
    'Self-Learning': {
        'Sunburst Chart': 'Circular hierarchical visualization',
        'Parallel Coordinates': 'High-dimensional data analysis',
        'Animated Scatter': 'Time-series evolution',
        'Gauge Chart': 'KPI performance indicators',
        'Funnel Chart': 'Process conversion analysis',
        'Waterfall Chart': 'Cumulative changes analysis',
        'Network Graph': 'Relationship/dependency visualization',
        'Choropleth Map': 'Geographic data representation',
        'Density Contour': '2D density estimation',
        'Polar Scatter': 'Directional/circular data',
        'Gantt Chart': 'Project timeline management',
        '3D Surface Plot': 'Mathematical function visualization',
        'Multiple Radar': 'Multi-entity comparison',
        'Bullet Chart': 'Performance vs target'
    }
}

print("\n📚 VISUALIZATION TECHNIQUES COVERED:")
print("-" * 50)

for category, plots in visualizations.items():
    print(f"\n{category}:")
    for plot, description in plots.items():
        print(f"  • {plot}: {description}")

print("\n" + "=" * 70)
print("✅ Key Takeaways:")
print("=" * 70)
print("""
1. 🎯 Choose the right visualization for your data type
2. 📊 Interactive plots enable deeper exploration
3. 🌍 Geographic data needs specialized plots (Choropleth)
4. 🔄 Hierarchical data works well with Treemap/Sunburst
5. 📈 Time-series data benefits from animation
6. 🔗 Networks require graph visualizations
7. 📏 Multi-dimensional data needs parallel coordinates
8. 🎨 Color and interactivity enhance understanding
""")

print("\n🔧 Libraries Used:")
print("   • Plotly Express - High-level interactive plots")
print("   • Plotly Graph Objects - Low-level customization")
print("   • NetworkX - Network graph creation")
print("   • Matplotlib - Static visualizations")
print("   • SciPy - Scientific computing (dendrogram)")
print("   • Matplotlib-Venn - Venn diagrams")
     
======================================================================
📊 COMPREHENSIVE VISUALIZATION SUMMARY
======================================================================


📚 VISUALIZATION TECHNIQUES COVERED:
--------------------------------------------------

Core Experiment:
  • Treemap: Hierarchical part-to-whole relationships
  • Dendrogram: Hierarchical clustering visualization
  • Venn Diagram: Set relationships and intersections
  • Sankey Diagram: Flow between stages/nodes
  • 3D Scatter Plot: Three-dimensional data relationships
  • Radar Chart: Multi-dimensional comparison

Self-Learning:
  • Sunburst Chart: Circular hierarchical visualization
  • Parallel Coordinates: High-dimensional data analysis
  • Animated Scatter: Time-series evolution
  • Gauge Chart: KPI performance indicators
  • Funnel Chart: Process conversion analysis
  • Waterfall Chart: Cumulative changes analysis
  • Network Graph: Relationship/dependency visualization
  • Choropleth Map: Geographic data representation
  • Density Contour: 2D density estimation
  • Polar Scatter: Directional/circular data
  • Gantt Chart: Project timeline management
  • 3D Surface Plot: Mathematical function visualization
  • Multiple Radar: Multi-entity comparison
  • Bullet Chart: Performance vs target

======================================================================
✅ Key Takeaways:
======================================================================

1. 🎯 Choose the right visualization for your data type
2. 📊 Interactive plots enable deeper exploration
3. 🌍 Geographic data needs specialized plots (Choropleth)
4. 🔄 Hierarchical data works well with Treemap/Sunburst
5. 📈 Time-series data benefits from animation
6. 🔗 Networks require graph visualizations
7. 📏 Multi-dimensional data needs parallel coordinates
8. 🎨 Color and interactivity enhance understanding


🔧 Libraries Used:
   • Plotly Express - High-level interactive plots
   • Plotly Graph Objects - Low-level customization
   • NetworkX - Network graph creation
   • Matplotlib - Static visualizations
   • SciPy - Scientific computing (dendrogram)
   • Matplotlib-Venn - Venn diagrams
Conclusion

This self-learning section demonstrated advanced interactive visualization techniques beyond the core experiment, including:

Core Techniques Covered:

Sunburst Chart - Hierarchical data in circular format
Parallel Coordinates - High-dimensional data analysis
Animated Scatter - Temporal data evolution
Gauge Chart - KPI dashboards
Funnel Chart - Process conversion analysis
Waterfall Chart - Cumulative changes
Network Graph - Relationship visualization
Choropleth Map - Geographic data
Density Contour - 2D density estimation
Polar Scatter - Directional data
Gantt Chart - Project timelines
3D Surface Plot - Mathematical surfaces
Multiple Radar Charts - Multi-entity comparison
Bullet Chart - Performance vs targets
Key Learning Points:

Interactive visualizations enable data exploration
Different data types require specific visualization techniques
Plotly provides both high-level (express) and low-level (graph_objects) APIs
Dashboards combine multiple visualization types
Animation enhances temporal data understanding
These techniques are essential for modern data storytelling, dashboards, and business intelligence applications.
