import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np
import matplotlib.pyplot as plt
from NuistRadar.draw.SingleRadarPlot import RadarGraph
from NuistRadar.io.auto_io import radar_io

file_cc = r"E:\RadarBaseData\CINRAD-CC\2016070818.00V"
file_sc = r"E:\RadarBaseData\CINRAD_SC_old\Z_RADR_I_Z9280_20180209132700_O_DOR_SC_CAP.bin"
file_98d = r"E:\RadarBaseData\郑玉\利奇马\LQM_Z9250_NJ\Z_RADR_I_Z9250_20190809232559_O_DOR_SAD_CAP_FMT.bin.bz2"

radar_obj = radar_io(file_98d)
NRadar = radar_obj.ToNuistRadar()
PyartRadar = radar_obj.ToPyartRadar()

graph = RadarGraph(NRadar)
graph.plot(3, "ZDR")
plt.show()