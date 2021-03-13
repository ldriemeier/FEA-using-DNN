# -*- coding: utf-8 -*-
import connectorBehavior
import displayGroupOdbToolset as dgo
import xyPlot
import visualization
import sketch
import job
import optimization
import mesh
import load
import interaction
import step
import assembly
import material
import part
import displayGroupMdbToolset as dgm
import regionToolset
import section
from abaqus import *
from abaqusConstants import *
import __main__

import csv
# CHANGE IT BEFORE RUN THE SCRIPT!
basedir = 'C:/AbaqusTemp'

# Para gravar em um csv único
from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d_%H-%M")
result_csv = '{0}/extracted_data_{1}.csv'.format(basedir, now)

# Grava os cabeçalhos da saída
# Áreas em mm^2; u3 em mm; F em N
with open(result_csv, 'w') as f:
#    f.write('iteration,area_id,')
    f.write('area_id,')
    f.write('time,u3,force\n')

with open('{0}/areas24.csv'.format(basedir), 'r') as f:
    reader = csv.reader(f)
    todas_as_areas = []
    next(reader)  # Pula a primeira linha com o cabeçalho
    for row in reader:
        if row[0][0] != '#':  # Pula as linhas comentadas
            todas_as_areas.append([float(x) for x in row])


mdb.ModelFromInputFile(name='model-x',
                       inputFileName='{0}/Job-24bar.inp'.format(basedir))
del mdb.models['Model-1']
mdb.models.changeKey(fromName='model-x', toName='Model-1')

m = mdb.models['Model-1']

def muda_areas(areas):
    for j, area in enumerate(areas):
        m.sections['Section-{0}-NEW-SET-{0}'.format(j+1)].setValues(area=area, material='STEEL')


mdb.Job(name='Job-24bar', model='Model-1',
        description='A job for the analysis of a 24 bar truss system', type=ANALYSIS, atTime=None,
        waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB)

len_areas = len(todas_as_areas)
deslocamentos = []

for i, areas in enumerate(todas_as_areas):
    muda_areas(areas[1:])

    mdb.jobs['Job-24bar'].submit(consistencyChecking=OFF)
    mdb.jobs['Job-24bar'].waitForCompletion()

    o3 = session.openOdb(name='{0}/Job-24bar.odb'.format(basedir))
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))

    odb = session.odbs['{0}/Job-24bar.odb'.format(basedir)]
    print('{0} de {1}'.format(areas[0], len_areas))

    # linha que extrai o deslocamento
    session.xyDataListFromField(odb=odb,
                                outputPosition=NODAL,
                                variable=(('U', NODAL, ((COMPONENT, 'U3'), )), ),
                                nodeLabels=(('PART-1-1', ('3', )), ))
    # linha que extrai a resultante em z
    session.xyDataListFromField(odb=odb,
                                outputPosition=NODAL,
                                variable=(('RF', NODAL, ((COMPONENT, 'RF3'), )), ),
                                nodeLabels=(('PART-1-1', (3)), ))

    us = session.xyDataObjects['U:U3 PI: PART-1-1 N: 3']
    fs = session.xyDataObjects['RF:RF3 PI: PART-1-1 N: 3']

    print('final force: {0}'.format(fs[-1][1]))
    # Adiciona ao csv a iteração, as áreas, o tempo, o deslocamento e a força
    with open(result_csv, 'a') as arq:
        for time, u, f in ((ux[0], ux[1], fx[1]) for ux, fx in zip(us, fs)):
            arq.write('{0},{1},{2},{3}\n'.format(int(areas[0]), time, u, f))

    xyKeys = session.xyDataObjects.keys()
    for key in xyKeys:
        del session.xyDataObjects[key]

print("THE END! THAT'S ALL, FOLKS!!! ;)")
