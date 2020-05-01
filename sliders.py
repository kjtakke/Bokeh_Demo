import numpy as np
from bokeh.io import save

from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import Div
x = np.linspace(0, 10, 500)
y = np.sin(x)

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(y_range=(-10, 10), plot_width=800, plot_height=800)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

amp_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
freq_slider = Slider(start=0.1, end=10, value=1, step=.1, title="Frequency")
phase_slider = Slider(start=0, end=6.4, value=0, step=.1, title="Phase")
offset_slider = Slider(start=-5, end=5, value=0, step=.1, title="Offset")

callback = CustomJS(args=dict(source=source, amp=amp_slider, freq=freq_slider, phase=phase_slider, offset=offset_slider),
                    code="""
    const data = source.data;
    const A = amp.value;
    const k = freq.value;
    const phi = phase.value;
    const B = offset.value;
    const x = data['x']
    const y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = B + A*Math.sin(k*x[i]+phi);
    }
    source.change.emit();
""")

amp_slider.js_on_change('value', callback)
freq_slider.js_on_change('value', callback)
phase_slider.js_on_change('value', callback)
offset_slider.js_on_change('value', callback)




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

layout = row(
     column(div,plot),
    column(amp_slider, freq_slider, phase_slider, offset_slider),
)

output_file(r'C:\Users\krist\Desktop\range_slider.html', title="slider.py example")




show(layout)
save(layout)