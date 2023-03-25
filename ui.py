import dearpygui.dearpygui as dpg



def createWindow(widgetInits):

    dpg.create_context()
    dpg.create_viewport(title='Sundial', width=600, height=300)

    for x in widgetInits:
        x()

    dpg.setup_dearpygui()





def startWindow(loopFunc):

    dpg.show_viewport()

    while dpg.is_dearpygui_running():

        loopFunc()
        dpg.render_dearpygui_frame()

    dpg.destroy_context()