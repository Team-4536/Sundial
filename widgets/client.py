
import robotpy
import ntcore
from os.path import basename
import dearpygui.dearpygui as dpg

trackedDoubles = [
    "FL Pwr",
    "FR Pwr",
    "BL Pwr",
    "BR Pwr"
 ]


inst = ntcore.NetworkTableInstance.getDefault()
inst.startClient4(basename(__file__))
# inst.setServer("10.45.36.2")
inst.setServer("localhost")
robotInfo = inst.getTable("RobotInfo")






def create():

    with dpg.value_registry():
        for x in trackedDoubles:
            dpg.add_double_value(label=x, tag=x, default_value=0)


    with dpg.window(label="Client window", tag="Client window"):
        #dpg.add_button(label="Print pwr val", callback=getVal)
        dpg.add_drag_int(label="label is here")
        for x in trackedDoubles:
            dpg.add_slider_double(source=x, label=f"{x}: ", min_value=-1, max_value=1)



def tick():


    for x in trackedDoubles:

        v = robotInfo.getNumber(x, None)
        if v is not None:
            dpg.set_value(x, v)