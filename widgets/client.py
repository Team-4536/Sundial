
import robotpy
import ntcore
from os.path import basename
import dearpygui.dearpygui as dpg



valDict = { }


inst = ntcore.NetworkTableInstance.getDefault()
inst.startClient4(basename(__file__))
# inst.setServer("10.45.36.2")
inst.setServer("localhost")
robotInfo = inst.getTable("RobotInfo")






def create():

    with dpg.value_registry():
        dpg.add_double_value(label="fl_pwr", tag="fl_pwr", default_value=0)


    with dpg.window(label="Client window"):
        #dpg.add_button(label="Print pwr val", callback=getVal)
        dpg.add_drag_double(source="fl_pwr", label="FL Power: ")




def tick():
    x = robotInfo.getNumber("FL Pwr", None)
    if x is not None:
        dpg.set_value("fl_pwr", x)