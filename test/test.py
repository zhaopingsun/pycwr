# -*- coding: utf-8 -*-
from pycwr.io.auto_io import radar_io
from pycwr.draw.SingleRadarPlotMap import RadarGraphMap
from pycwr.draw.SingleRadarPlot import RadarGraph
from pycwr.qc.attenuation import correct_attenuation_HB, correct_attenuation
import matplotlib.pyplot as plt

file = r"E:\RadarBaseData\CINRAD-SA\温州\2015080816.59A"
#file = r"E:\RadarBaseData\CINRAD-CC\2016070817.03V"
#radar = SCBaseData(file)
Radar = radar_io(file)
NRadar = Radar.ToPRD()
PyartRadar = Radar.ToPyartRadar()

dbz = NRadar.fields[0]["dBZ"]
y = correct_attenuation_HB(dbz)
graph = RadarGraph(NRadar)
z = correct_attenuation(dbz, "X")
#graph.plot(0, "dBZ", continuously=False)
graph.simple_plot_ppi(dbz.range, dbz.azimuth, dbz.elevation, dbz, cmap="CN_ref")
plt.show()