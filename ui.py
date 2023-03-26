import dearpygui.dearpygui as dpg



def createWindow(widgetInits):

    dpg.create_context()
    dpg.create_viewport(title='Sundial', width=600, height=300)
    dpg.enable_docking(dock_space=True)
    # dpg.configure_app(docking=True, docking_space=dock_space) 
    for x in widgetInits:
        x()

    dpg.setup_dearpygui()





def startWindow(loopFunc):

    dpg.show_viewport()

    while dpg.is_dearpygui_running():

        loopFunc()
        dpg.render_dearpygui_frame()

    dpg.destroy_context()