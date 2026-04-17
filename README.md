# Lab Experiment Journal: Real-World and Interactive Visualizations

---

## Experiment Details

| Field | Value |
|---|---|
| **Experiment Title** | Real-World and Interactive Visualizations |
| **Date** | 2026-04-10 |
| **Student Name** | Jayvee Shah |
| **PRN** | 25070123058 |
| **Batch** | EnTC A3 |
| **Experiment No.** | 18 |
| **Programming Language** | Python 3.x |
| **Libraries Used** | plotly, plotly.express, plotly.graph_objects, matplotlib, matplotlib_venn, scipy, networkx, pandas, numpy |

---

## 1. Objective

To understand and implement real-world and interactive data visualization techniques using Plotly and supporting libraries, including:

- Creating hierarchical charts (treemap, dendrogram, sunburst) to represent nested data
- Building set and flow diagrams (Venn, Sankey, funnel, waterfall) for relational and sequential data
- Using 3D visualizations (3D scatter, 3D surface) to explore multi-dimensional relationships
- Constructing radar and polar charts for directional and multi-attribute comparisons
- Building interactive dashboards with gauge, bullet, and Gantt charts for KPI monitoring
- Visualizing geographic data with choropleth maps
- Animating scatter plots to show temporal evolution
- Representing network relationships using graph theory with NetworkX
- Using density contour plots for 2D distribution estimation
- Applying parallel coordinates plots for high-dimensional multivariate analysis

---

## 2. Prerequisites

- Python 3.x installed
- Required libraries:


| Library | Install Command |
|---|---|
| plotly | `pip install plotly` |
| matplotlib | `pip install matplotlib` |
| matplotlib-venn | `pip install matplotlib-venn` |
| scipy | `pip install scipy` |
| networkx | `pip install networkx` |
| pandas | `pip install pandas` |
| numpy | `pip install numpy` |

---

## 3. Experiment Sections Overview

| No. | Chart | Library | Use Case |
|---|---|---|---|
| 4.1 | Treemap | `plotly.express` | Company department budget distribution |
| 4.2 | Dendrogram | `scipy` + `matplotlib` | Hierarchical clustering of 2D data points |
| 4.3 | Venn Diagram | `matplotlib_venn` | Set intersection between two groups |
| 4.4 | Sankey Diagram | `plotly.graph_objects` | Student flow across academic stages |
| 4.5 | 3D Scatter Plot | `plotly.express` | Student performance across 3 variables |
| 4.6 | Radar Chart | `plotly.graph_objects` | Student skill assessment |
| 4.7–4.20 | Self-Learning (14 charts) | `plotly` + `networkx` | Advanced interactive visualizations |

---

## 4. Core Experiment Sections (Detailed)

### 4.1 Treemap — Company Budget Distribution



**Observation:** A treemap represents hierarchical data as nested rectangles. The area of each rectangle is proportional to its value. IT has the largest budget (50,000) and HR the smallest (20,000). The `path` parameter defines hierarchy levels.

---

### 4.2 Dendrogram — Hierarchical Clustering



**Observation:** Ward's linkage minimises the total within-cluster variance at each merge step. The y-axis distance shows how dissimilar two clusters are at the point of merging — taller branches indicate more dissimilar clusters.

---

### 4.3 Venn Diagram — Set Relationships


**Set Breakdown:**

| Region | Elements | Count |
|---|---|---|
| A only | {1, 2} | 2 |
| A ∩ B (intersection) | {3, 4} | 2 |
| B only | {5, 6} | 2 |

**Observation:** `venn2` automatically computes and labels the three regions. The intersection region represents elements shared between both sets.

---

### 4.4 Sankey Diagram — Student Flow



**Flow Summary:**

| Stage | Students | Drop-off |
|---|---|---|
| Admission → First Year | 100 | — |
| First Year → Second Year | 80 | 20 |
| Second Year → Placed | 60 | 20 |

**Observation:** Sankey diagrams show flow quantities between nodes. The width of each link is proportional to its value. Useful for tracking attrition across stages.

---

### 4.5 3D Scatter Plot — Student Performance



**Observation:** 3D scatter plots reveal relationships across three numeric variables simultaneously. Higher study hours correlate with higher marks and attendance. Plotly's interactive rotation allows exploring the cloud from any angle.

---

### 4.6 Radar Chart — Skill Assessment



**Skill Scores:**

| Skill | Score |
|---|---|
| Python | 4 |
| ML | 3 |
| DBMS | 5 |
| DSA | 4 |
| Communication | 3 |

**Observation:** `fill='toself'` shades the enclosed polygon. The area of the shape represents overall skill breadth. DBMS is the strongest skill; ML and Communication are weakest.

---

## 5. Self-Learning — Advanced Interactive Visualizations

### 1. Sunburst Chart — Hierarchical Organization


**Hierarchy:** Company → Department (Engineering, Marketing, Sales, HR) → Team (Frontend, Backend, Digital, Content, North, South, Recruiting, Training)

**Observation:** The inner ring shows top-level departments; outer rings show teams within each department. Slice size is proportional to headcount/value. Clicking a segment zooms into that branch.

---

### 2. Parallel Coordinates Plot — Multivariate Student Analysis

**Dataset:** 50 students with Math, Physics, Chemistry, English scores and Attendance Rate.

**Observation:** Each vertical axis represents a variable; each line is one student. Lines that follow similar paths across all axes indicate similar students. High-average students (yellow) tend to score consistently across all subjects. Axes can be dragged interactively to reorder and filter.

---

### 3. Animated Scatter Plot — GDP vs Life Expectancy (2010–2023)



**Dataset:** 8 countries × 14 years (2010–2023); GDP, Life Expectancy, and Population modelled with upward trends.

**Key Parameters:**

| Parameter | Effect |
|---|---|
| `animation_frame='Year'` | Creates one frame per year |
| `animation_group='Country'` | Tracks each country across frames |
| `log_x=True` | Logarithmic x-axis for compressed GDP range |
| `size='Population'` | Bubble area encodes population |

**Observation:** Press Play to animate. Each country follows an upward trajectory in both GDP and life expectancy. Larger bubbles indicate more populous countries.

---

### 4. Gauge Chart — System Performance Dashboard


**Dashboard Summary:**

| KPI | Value | Status |
|---|---|---|
| Server Uptime | 98.5% | Good (green zone) |
| CPU Usage | 65% | Warning (yellow zone) |
| Memory Usage | 78% | Warning (yellow zone) |
| Network Speed | 125 Mbps | Good (green zone) |

**Observation:** Colour zones (green/yellow/red) give immediate status feedback. A red threshold line on the Uptime gauge marks the 99% SLA target. `make_subplots` with `type='indicator'` is required for gauge layouts.

---

### 5. Funnel Chart — Sales Pipeline



**Conversion Rates:**

| Stage Transition | Conversion Rate |
|---|---|
| Website Visits → Sign Ups | 60.0% |
| Sign Ups → Product Views | 75.0% |
| Product Views → Add to Cart | 55.6% |
| Add to Cart → Checkout | 60.0% |
| Checkout → Purchase | 53.3% |

**Observation:** Only 8% of website visitors complete a purchase, a typical e-commerce pattern. The largest drop-off is between Product Views and Add to Cart. `textinfo='value+percent initial'` shows both raw count and percentage of the top-of-funnel.

---

### 6. Waterfall Chart — Monthly Budget Analysis



**Budget Summary:**

| Category | Amount | Type |
|---|---|---|
| Starting Balance | $50,000 | Absolute |
| Income | +$30,000 | Inflow |
| Marketing | -$8,000 | Outflow |
| Operations | -$12,000 | Outflow |
| R&D | -$15,000 | Outflow |
| Ending Balance | $45,000 | Absolute |

**Observation:** `measure='relative'` makes bars float from the running total; `measure='absolute'` anchors them to zero. Green bars show inflows; red bars show outflows; blue bars show totals.

---

### 7. Network Graph — Social Network Analysis



**Network Stats:**

| Node | Connections (Degree) |
|---|---|
| Grace | 4 |
| Frank | 4 |
| Charlie | 4 |
| Alice | 3 |
| Bob | 3 |

**Observation:** Node size encodes degree centrality — larger nodes have more connections and greater influence. `nx.spring_layout()` positions nodes so highly connected ones appear closer together. Plotly renders the graph as interactive scatter traces.

---

### 8. Choropleth Map — World Population


**Sample Data:**

| Country | Population (M) | GDP (T USD) |
|---|---|---|
| China | 1,410 | 18.3 |
| India | 1,400 | 3.7 |
| USA | 330 | 25.5 |
| Indonesia | 274 | 1.3 |

**Observation:** `locationmode='country names'` maps country name strings to geographic boundaries. `projection='natural earth'` gives a familiar globe-like appearance. Hovering reveals GDP data alongside population.

---

### 9. Density Contour Plot — Height vs Weight Distribution



**Clusters generated (n=500):**

| Body Type | Height (mean) | Weight (mean) |
|---|---|---|
| Average | 170 cm | 65 kg |
| Athletic | 180 cm | 80 kg |
| Slim | 160 cm | 55 kg |

**Observation:** Contour rings show density — tighter rings indicate higher concentration of data points. `selector=dict(type='contour')` is required to apply `contours_coloring` only to contour traces and not the marginal histograms.

---

### 10. Polar Scatter Plot — Wind Speed and Direction



**Observation:** The radial axis encodes wind speed; the angular axis encodes compass direction. The dashed red circle at r=25 marks a warning threshold. `direction='clockwise'` matches compass convention (North at top, East at right).

---

### 11. Gantt Chart — Project Timeline


**Project Schedule:**

| Task | Start | Finish | Resource |
|---|---|---|---|
| Requirement Analysis | 2024-01-01 | 2024-01-15 | Planning |
| System Design | 2024-01-10 | 2024-01-31 | Design |
| Database Setup | 2024-01-25 | 2024-02-10 | Backend |
| Frontend Development | 2024-02-01 | 2024-02-28 | Frontend |
| Backend Development | 2024-02-05 | 2024-03-05 | Backend |
| Integration Testing | 2024-03-01 | 2024-03-15 | Testing |
| Deployment | 2024-03-18 | 2024-03-25 | DevOps |

**Observation:** A Gantt chart is implemented as a horizontal bar chart with date x-axis. Overlapping bars reveal parallel tasks (e.g., Frontend and Backend development run concurrently). Colour differentiates team/resource assignments.

---

### 12. 3D Surface Plot — Mathematical Function

**Function:** z = sin(√(x² + y²)) — a ripple/wave pattern radiating from the origin.

**Observation:** `np.meshgrid()` creates a 2D coordinate grid from 1D arrays. `contours=dict(z=dict(project=dict(z=True)))` projects contour lines onto the base plane, creating a shadow-like topographic map below the surface.

---

### 13. Multiple Radar Charts — Employee Skills Comparison



**Average Scores:**

| Employee | Average Score |
|---|---|
| Employee A | 3.92 / 5.0 |
| Employee B | 4.08 / 5.0 |
| Employee C | 3.92 / 5.0 |

**Observation:** Closing the polygon by appending the first element (`scores + [scores[0]]`) is required to draw a complete shape. Areas where one polygon extends beyond others indicate that employee's competitive advantage. Employee C leads in Python and Leadership; Employee B leads in SQL, Communication, and Teamwork.

---

### 14. Bullet Chart — KPI Performance vs Target


**KPI Results:**

| KPI | Actual | Target | Status |
|---|---|---|---|
| Revenue | 85 | 100 | ⚠️ Below Target |
| Customer Satisfaction | 92 | 95 | ⚠️ Below Target |
| New Users | 1,250 | 1,000 | ✅ Above Target |
| Task Completion | 78 | 90 | ⚠️ Below Target |

**Observation:** Bullet charts layer three elements: a background range bar for context, a narrow actual-value bar, and a target marker (rendered as a line-shaped scatter point). New Users is the only KPI exceeding its target.

---

## 6. Key Learnings

### 6.1 Chart Type Selection Guide

| Chart Type | Function | Best For |
|---|---|---|
| Treemap | `px.treemap()` | Hierarchical part-to-whole with nested rectangles |
| Dendrogram | `scipy.dendrogram()` | Visualising hierarchical clustering merge steps |
| Venn Diagram | `venn2()` | Set intersections between 2–3 groups |
| Sankey Diagram | `go.Sankey()` | Flow quantities between sequential stages |
| 3D Scatter | `px.scatter_3d()` | Relationships across three continuous variables |
| Radar / Spider | `go.Scatterpolar(fill='toself')` | Multi-attribute comparison for one or more entities |
| Sunburst | `px.sunburst()` | Circular hierarchical breakdown with drill-down |
| Parallel Coordinates | `px.parallel_coordinates()` | High-dimensional multivariate pattern detection |
| Animated Scatter | `px.scatter(animation_frame=)` | Temporal evolution of scatter relationships |
| Gauge | `go.Indicator(mode='gauge+number')` | Single KPI against a target range |
| Funnel | `go.Funnel()` | Stage-by-stage conversion / attrition |
| Waterfall | `go.Waterfall()` | Cumulative effect of positive and negative changes |
| Network Graph | `nx` + `go.Scatter` | Node-edge relationships and centrality |
| Choropleth Map | `px.choropleth()` | Geographic data comparison across regions |
| Density Contour | `px.density_contour()` | 2D concentration and cluster identification |
| Polar Scatter | `go.Scatterpolar(mode='markers')` | Directional / circular magnitude data |
| Gantt Chart | `px.bar(orientation='h')` | Project schedule and task dependencies |
| 3D Surface | `go.Surface()` | Mathematical function z = f(x, y) |
| Bullet Chart | `go.Bar` + `go.Scatter` (target marker) | Actual vs target with qualitative ranges |

---

### 6.2 Plotly API — Express vs Graph Objects

| Aspect | `plotly.express` (`px`) | `plotly.graph_objects` (`go`) |
|---|---|---|
| API Level | High-level, one-liner | Low-level, full control |
| Best For | Quick standard charts | Custom layouts, subplots, mixed chart types |
| Subplots | Limited | Full support via `make_subplots()` |
| Examples in Exp. 18 | Treemap, 3D Scatter, Choropleth, Sunburst, Animated Scatter, Parallel Coordinates, Gantt, Density Contour | Sankey, Radar, Gauge, Funnel, Waterfall, Network Graph, Polar, 3D Surface, Bullet |

---

### 6.3 Key Parameters Reference

| Parameter | Used In | Effect |
|---|---|---|
| `path=` | `px.treemap()` | Defines hierarchy levels as a list |
| `method='ward'` | `linkage()` | Minimises within-cluster variance at each merge |
| `textinfo='value+percent initial'` | `go.Funnel()` | Shows raw value and % of first stage |
| `measure='relative'/'absolute'` | `go.Waterfall()` | Float bar from running total vs anchor to zero |
| `animation_frame=` | `px.scatter()` | Column to use as animation time dimension |
| `log_x=True` | `px.scatter()` | Logarithmic x-axis scale |
| `mode='gauge+number'` | `go.Indicator()` | Render both gauge arc and numeric display |
| `locationmode='country names'` | `px.choropleth()` | Map string names to geographic boundaries |
| `projection='natural earth'` | `px.choropleth()` | Map projection style |
| `marginal_x='histogram'` | `px.density_contour()` | Add marginal histogram on x-axis |
| `selector=dict(type='contour')` | `fig.update_traces()` | Target only contour traces, not marginals |
| `direction='clockwise'` | `polar.angularaxis` | Match compass direction convention |
| `contours_coloring='fill'` | `fig.update_traces()` | Fill contour regions with colour |
| `corner=True` | `sns.pairplot()` | Show only lower triangle of pair grid |
| `k=` in `spring_layout` | `nx.spring_layout()` | Optimal node spacing in force-directed layout |

---

### 6.4 Best Practices

1. Use `px` (Plotly Express) for standard charts and `go` (Graph Objects) when you need custom layouts, subplots, or chart types not in Express.
2. Always use `make_subplots(specs=[{'type': 'indicator'}])` when combining gauge or indicator charts in a grid.
3. Close radar / polar polygons by appending the first element: `r + [r[0]]` and `theta + [theta[0]]`.
4. Use `np.meshgrid()` to generate coordinate grids for 3D surface plots from 1D linspace arrays.
5. For animated plots, set fixed `range_x` and `range_y` so axes do not rescale between frames, which would make the animation misleading.
6. In density contour plots, use `selector=dict(type='contour')` in `update_traces()` to avoid accidentally styling marginal histogram traces.
7. Use `nx.spring_layout(k=, iterations=)` to control node spacing in network graphs — higher `k` spreads nodes further apart.
8. Export important figures with `fig.write_html('file.html')` to share interactive Plotly charts without a Python environment.

---

## 7. Observations

- The Sankey diagram shows a 40% attrition from admission to placement — 100 admitted, 80 complete first year, only 60 are placed.
- The funnel chart reveals that only 8% of website visitors complete a purchase, with the largest drop-off between Product Views and Add to Cart (55.6% conversion).
- The waterfall chart shows a net loss of $5,000 despite $30,000 income, as combined expenses total $35,000.
- The network graph shows Grace, Frank, and Charlie as the most connected nodes (4 edges each), making them key connectors in the social network.
- In the bullet chart dashboard, only New Users (1,250 vs target 1,000) exceeds its target; all other KPIs are below.
- The density contour plot clearly separates three body-type clusters (Average, Athletic, Slim) with minimal overlap, confirming well-separated synthetic distributions.
- The 3D surface plot of z = sin(√(x² + y²)) produces a circular ripple pattern, demonstrating how mathematical functions can be explored interactively in 3D.
- Employee B has the highest average skill score (4.08/5.0) and leads in SQL, Communication, and Teamwork, while Employee C leads in Python and Leadership.

---

## 8. Conclusion

This experiment successfully demonstrated a broad range of real-world and interactive visualization techniques using Plotly and supporting libraries. The core experiment covered six foundational chart types — treemap, dendrogram, Venn diagram, Sankey diagram, 3D scatter, and radar chart — applicable to hierarchical, relational, flow, and multi-dimensional data.

The self-learning section extended this with 14 additional advanced visualizations, covering geographic analysis (choropleth), time-series animation, KPI dashboards (gauge, bullet), process analysis (funnel, waterfall), network theory (NetworkX), mathematical visualization (3D surface), and multivariate analysis (parallel coordinates, density contour).

The overarching principle is that interactive visualizations, unlike static plots, allow the audience to explore data themselves — filtering, rotating, hovering, and animating — which makes them far more effective for dashboards, business intelligence, and data storytelling.

---

## 9. References

- Plotly Python Documentation: https://plotly.com/python/
- Plotly Express Reference: https://plotly.com/python-api-reference/plotly.express.html
- Plotly Graph Objects Reference: https://plotly.com/python/graph-objects/
- NetworkX Documentation: https://networkx.org/documentation/stable/
- SciPy Hierarchical Clustering: https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
- Matplotlib-Venn: https://pypi.org/project/matplotlib-venn/
- Pandas Documentation: https://pandas.pydata.org/docs/
- NumPy Documentation: https://numpy.org/doc/
