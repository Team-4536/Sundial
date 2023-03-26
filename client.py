import robotpy
import ntcore
from os.path import basename



if __name__ == "__main__":

    inst = ntcore.NetworkTableInstance.getDefault()

    inst.startClient4(basename(__file__))
    inst.setServer("10.45.36.2")


    robotInfo = inst.getTable("RobotInfo")

    while True:
        print("FLPwr:", robotInfo.getNumber("FL Pwr", -1))


