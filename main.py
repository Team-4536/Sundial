
import dearpygui.dearpygui as dpg
import ui
import widgets.driveWidget
import widgets.client



if __name__ == "__main__":

    w = [
        widgets.driveWidget.create,
        widgets.client.create,
        ]

    ui.createWindow(w)





    with dpg.font_registry():
        default_font = dpg.add_font("consolab.ttf", 13)
    dpg.bind_font(default_font)




    def loop():
        widgets.driveWidget.tick()
        widgets.client.tick()


    dpg.show_style_editor()
    ui.startWindow(loop)