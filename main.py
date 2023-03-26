
import dearpygui.dearpygui as dpg
import ui
import widgets.driveInfo
import widgets.drawTest
import widgets.client



if __name__ == "__main__":

    w = [
        widgets.driveInfo.create,
        widgets.drawTest.create,
        widgets.client.create,
        ]

    ui.createWindow(w)


    def loop():
        widgets.driveInfo.tick()
        widgets.drawTest.tick()
        widgets.client.tick()


    ui.startWindow(loop)