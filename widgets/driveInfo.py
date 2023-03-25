import dearpygui.dearpygui as dpg



def float_callback(sender, app_data):
    print(app_data)




def create():
    dpg.enable_docking(dock_space=True)
    with dpg.window(label="Drive Info"):
        dpg.add_text(label="Text", default_value="Hello!")






