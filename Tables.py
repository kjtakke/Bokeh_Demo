import pandas as pd
import numpy as np
from bokeh.models import Div
from datetime import date
from random import randint
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
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn




df = pd.read_csv(r'https://www.quandl.com/api/v3/datasets/EOD/MSFT.csv?api_key=HLPpJK9ng5A8MKxjawf1', header=0)
df = df.iloc[::-1]

# print(df.columns)


print(df.head())
# 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividend', 'Split', 'Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close', 'Adj_Volume'
#df['Date']
#df['Open']
#df['High']
#df['Low']
#df['Close']
#df['Volume']
#df['Dividend']
#df['Split']
#df['Adj_Open']
#df['Adj_High']
#df['Adj_Low']
#df['Adj_Close']
#df['Adj_Volume']

output_file(r"C:\Users\xxxx\Desktop\data_table.html")


sDate = df['Date'].min()
eDate = df['Date'].max()
xLab = "Days " + str(sDate) + " - ", str(eDate)
x = list(range(np.count_nonzero(df['Open'])))
y = list(df['Open'])




p4 = figure(
    title="Stock Prices Over Time",
    x_axis_label=str(xLab),
    y_axis_label="Price",
    plot_width=1600,
    plot_height=400
)
#   legend_label="test"
p4.line(x, y, line_width=2)



p4.toolbar.logo = None









data = df
source = ColumnDataSource(data)

columns = [
    TableColumn(field="Date", title="Date", formatter=DateFormatter()),
    TableColumn(field="Open", title="Open"),
    TableColumn(field="High", title="High"),
    TableColumn(field="Low", title="Low"),
    TableColumn(field="Close", title="Close"),
    TableColumn(field="Volume", title="Volume"),
    TableColumn(field="Dividend", title="Dividend"),
    TableColumn(field="Split", title="Split"),
    TableColumn(field="Adj_Open", title="Adj_Open"),
    TableColumn(field="Adj_High", title="Adj_High"),
    TableColumn(field="Adj_Low", title="Adj_Low"),
    TableColumn(field="Adj_Close", title="Adj_Close"),
    TableColumn(field="Adj_Volume", title="Adj_Volume"),
]
data_table = DataTable(source=source, columns=columns, width=1600, height=400)


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
    [
        div, p4, data_table
    ]
)

show(grid)
save(grid)


