import plotly
from plotly import graph_objs as go

def render(fig, title, width=500, height=500, x_axis_title=None, y_axis_title=None):
    
    fig["layout"]["title"] = title
    fig["layout"]["xaxis_title"] = x_axis_title
    fig["layout"]["yaxis_title"] = y_axis_title
    fig["layout"]["xaxis_title_font_color"] = '#ffffff'
    fig["layout"]["yaxis_title_font_color"] = '#ffffff'
    fig["layout"]["width"] = width
    fig["layout"]["height"] = height
    
    fig["layout"]["title"]["font"]["color"] = "#9398A4"
    fig["layout"]["xaxis"]["gridcolor"] = "#3F434F"
    fig["layout"]["yaxis"]["gridcolor"] = "#3F434F"
    fig["layout"]["xaxis"]["tickfont"]["color"] = "#ffffff"
    fig["layout"]["yaxis"]["tickfont"]["color"] = "#ffffff"

    fig["layout"]["legend"]["font"]["color"] = "#ffffff"
    fig["layout"]["plot_bgcolor"] = "#292C34"
    fig["layout"]["paper_bgcolor"] = "#22252B"  
    
    fig.show()

def scatter( x, y, name, mode='lines', opacity=0.5, color=None, size=3):
    return go.Scatter(x=x, y=y, mode =mode, opacity = opacity, name = name, marker=dict( size=size, color=color ))
