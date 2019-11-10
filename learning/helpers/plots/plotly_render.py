

def render(fig, width=500, height=500):
    
    
    fig["layout"]["width"] = width
    fig["layout"]["height"] = height
    
    fig["layout"]["title"]["font"]["color"] = "#9398A4"
    fig["layout"]["xaxis"]["gridcolor"] = "#3F434F"
    fig["layout"]["yaxis"]["gridcolor"] = "#3F434F"
    fig["layout"]["xaxis"]["tickfont"]["color"] = "#ffffff"
    fig["layout"]["yaxis"]["tickfont"]["color"] = "#ffffff"
    fig["layout"]["plot_bgcolor"] = "#292C34"
    fig["layout"]["paper_bgcolor"] = "#22252B"  
    
    return fig