import dearpygui.dearpygui as dpg



def float_callback(sender, app_data):
    print(app_data)



fVal = 0

def create():
    with dpg.window(label="Drive Info"):
        dpg.add_text(label="Text", default_value="Hello!")
        dpg.add_slider_float(label="Slider", default_value=0, min_value=0, max_value=1)
        dpg.add_text(label="Text", default_value="Hello!")
        fVal = dpg.add_plot(label="FL Pwr")

def tick():
    # dpg.set_value(fVal, 0.4)
    pass





