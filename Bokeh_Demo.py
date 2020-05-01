from bokeh.models import Div
from bokeh.layouts import *
from bokeh.models import Select, CustomJS
from bokeh.plotting import *
from bokeh.io import *
from bokeh.models.tools import *
from bokeh.palettes import *
from bokeh.transform import *
from bokeh import colors
import numpy as np
import pandas as pd


df = pd.read_csv(r'http://bit.ly/2cLzoxH', header=0)

dfPivot =df.pivot_table(index='continent', values='lifeExp', aggfunc=np.mean)
dfPivot = pd.DataFrame(dfPivot.to_records())

y = dfPivot['continent']
x = dfPivot['lifeExp']

output_file(r'C:\Users\xxxx\Desktop\Bokeh_Demo.html')

p1 = figure(
    y_range=y,
    title="Mean Life Exp Over Time",
    x_axis_label="Life Exp",
    y_axis_label="Continent",
    plot_width=400,
    plot_height=400,
    tools="pan,box_select,zoom_in,zoom_out",   #lasso_select,click,poly_select,xwheel_pan,ywheel_pan,undo,reset,crosshair,hover
    toolbar_location="above"                        #"above" "below" "left" "right"
)
p1.toolbar.logo = None


p1.hbar(
    y=y,
    right=x,
    left=0,
    height=0.4,
    color="orange",
    fill_alpha=0.5,
)








dfPivot =df.pivot_table(index='continent', values='lifeExp', aggfunc=np.mean)
dfPivot = pd.DataFrame(dfPivot.to_records())

source = ColumnDataSource(dfPivot)
continent_list = source.data['continent'].tolist()


p2 = figure(
    y_range=continent_list,
    title="Mean Life Exp Over Time",
    x_axis_label="Life Exp",
    y_axis_label="Continent",
    plot_width=400,
    plot_height=400,
    tools="pan,box_select,zoom_in,zoom_out",   #lasso_select,click,poly_select,xwheel_pan,ywheel_pan,undo,reset,crosshair,hover
    toolbar_location="above",                       #"above" "below" "left" "right"
)
p2.toolbar.logo = None


p2.hbar(
    y='continent',
    right='lifeExp',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'continent',
        palette=Accent6, #Blues8
        factors=continent_list
    ),
    fill_alpha=0.9,
    source=source,
    legend='continent'
)


p2.legend.orientation = 'horizontal' # vertical
p2.legend.location = 'top_center'
p2.legend.label_text_font_size = '10px'
p2.legend.click_policy = "mute"
p2.y_range.range_padding = 0.30

hover = HoverTool()

hover.tooltips = """
<div>
<h3>@continent</h3>
<div><strong>lifeExp:</strong>@lifeExp</div>
</div>
"""
p2.add_tools(hover)



#Stacked Bar
dfPivot = df.pivot_table(index="continent", values="lifeExp", columns='year', aggfunc=np.mean)
dfPivot = pd.DataFrame(dfPivot.to_records())
dfPivot = pd.melt(dfPivot, id_vars=["continent"])
df1 = pd.melt(dfPivot, id_vars=["continent"])

Asia = df1[df1["continent"] == "Africa"]
Asia = Asia[Asia["variable"] == "value"]
Asia = Asia['value'].tolist()


Europe = df1[df1["continent"] == "Africa"]
Europe = Europe[Europe["variable"] == "value"]
Europe = Europe['value'].tolist()


Africa = df1[df1["continent"] == "Africa"]
Africa = Africa[Africa["variable"] == "value"]
Africa = Africa['value'].tolist()


Americas = df1[df1["continent"] == "Africa"]
Americas = Americas[Americas["variable"] == "value"]
Americas = Americas['value'].tolist()

Oceania = df1[df1["continent"] == "Africa"]
Oceania = Oceania[Oceania["variable"] == "value"]
Oceania = Oceania['value'].tolist()



continent = list(dfPivot['continent'].unique())
years = list(dfPivot['variable'].unique())

colors = [
    "#c9d9d3",
    "#718dbf",
    "#e84d60",
    "#f56f42",
    "#cd4fd6"
]

data = {
    'years': years,
    'Asia': Asia,
    'Europe': Europe,
    'Africa': Africa,
    'Americas': Americas,
    'Oceania': Oceania,
}

p3 = figure(
    x_range=years,
    plot_height=800,
    plot_width=800,
    title="Life Exp Mean"
)

p3.vbar_stack(
    continent,
    x='years',
    width=0.9,
    color=colors,
    source=data,
    legend_label=continent
)

p3.y_range.start = 0
p3.x_range.range_padding = 0.00
p3.xgrid.grid_line_color = None
p3.axis.minor_tick_line_color = None
p3.outline_line_color = None
p3.legend.location = "top_left"
p3.legend.orientation = "vertical"
p3.toolbar.logo = None







df = pd.read_csv(r'https://www.quandl.com/api/v3/datasets/EOD/MSFT.csv?api_key=HLPpJK9ng5A8MKxjawf1', header=0)
df = df.iloc[::-1]

# print(df.columns)
# 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividend', 'Split', 'Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close', 'Adj_Volume'


sDate = df['Date'].min()
eDate = df['Date'].max()
xLab = "Days " + str(sDate) + " - ", str(eDate)
x = list(range(np.count_nonzero(df['Open'])))
y = list(df['Open'])




p4 = figure(
    title="Stock Prices Over Time",
    x_axis_label=str(xLab),
    y_axis_label="Price",
    plot_width=800,
    plot_height=400
)
#   legend_label="test"
p4.line(x, y, line_width=2)


p1.toolbar.logo = None
p2.toolbar.logo = None
p3.toolbar.logo = None
p4.toolbar.logo = None


div = Div(text="""

<style>
.btn {
  border: none;
  background-color: inherit;
  padding: 5px 15px;
  font-size: 16px;
  cursor: pointer;
  display: inline-block;
}

.btn:hover {background: #eee;}

.success {color: green;}
.info {color: dodgerblue;}
.warning {color: orange;}
.danger {color: red;}
.default {color: black;}
a { text-decoration: none; }
</style>




<button class="btn success" ><a class="btn success" href="Bokeh_Demo.html">Bokeh Demo</a></button>
<button class="btn info"><a class="btn info" href="range_slider.html">Slider</a></button>
<button class="btn danger" ><a class="btn danger" href="tabbed_content.html">Tabbed Content</a></button>
<button class="btn default" ><a class="btn default" href="data_table.html">Data Table</a></button>
""",
          width=1200, height=30)



grid = layout(
    [div,
        [[p4,[p1, p2]],[p3]]
    ]
)

show(grid)
save(grid)


