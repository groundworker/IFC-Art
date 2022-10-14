# -*- coding: utf-8 -*-
"""
@author:Andreas Sorgatz-Wenzel
"""

import random
import string
import math
import time
import pandas as pd


# randomString() by pynative.com: generate a random string of letters a. digits
def randomString(stringLength=22):
    rS = string.ascii_letters + string.digits
    return ''.join(random.choice(rS) for i in range(stringLength))


file_out = open("model_IFC-ART.ifc", "w")

n = 4  # Anzahl der Runden
radius = 100
step = 5
max_h = 300
list_ID = []
list_X = []
list_Y = []
list_Z = []
list_color = []

for counter, winkel in enumerate(range(0, n*360, step)):
    bogen = winkel * math.pi / 180
    list_ID.append(counter)
    list_X.append(radius * math.cos(bogen))
    list_Y.append(radius * math.sin(bogen))
    list_Z.append(max_h*counter/(n*360/step))
    list_color.append(counter/(n*360/step))

data = pd.DataFrame(list(zip(list_ID, list_X, list_Y, list_Z, list_color)),
                    columns=['ID', 'X', 'Y', 'Z','Color'])


file_out.write(
    "ISO-10303-21;\n HEADER;\nFILE_DESCRIPTION(( 'ViewDefinition [CoordinationView_V2.0]'),'2;1');\n")
file_out.write("FILE_NAME('Bohrungen','"+str(time.strftime("%Y-%m-%dT%H:%M:%S",
               time.localtime()))+"',('Andreas, Sorgatz-Wenzel'),(''),'','','');\n")
file_out.write("FILE_SCHEMA(('IFC2X3'));\nENDSEC;\n")

file_out.write("DATA;\n")
file_out.write("#100= IFCPROJECT('"+str(randomString(22)) +
               "',#110,'Projekt',$,$,$,$,(#201),#301);\n")
file_out.write("#110= IFCOWNERHISTORY(#111,#115,$,.NOCHANGE.,$,$,$,$);\n")

file_out.write("#111= IFCPERSONANDORGANIZATION(#112,#113,$);\n")
file_out.write("#112= IFCPERSON($,'BIM-Modellierer',$,$,$,$,$,$);\n")
file_out.write("#113= IFCORGANIZATION($,'ART@IFC',$,$,$);\n")
file_out.write("#115= IFCAPPLICATION(#113,'0.3','Skript',$);\n")
file_out.write("#116= IFCSITE('"+str(randomString(22)) +
               "',$,'IFC-ART',$,$,#118,$,$,.ELEMENT.,(0,0,0,0),(0,0,0,0),0.,$,$);\n")
file_out.write("#117= IFCRELAGGREGATES('" +
               str(randomString(22))+"',$,$,$,#100,(#116));\n")
file_out.write("#118= IFCLOCALPLACEMENT($,#120);\n")
file_out.write("#119= IFCCARTESIANPOINT((0.,0.,0.));\n")
file_out.write("#120= IFCAXIS2PLACEMENT3D(#119,$,$);\n")

file_out.write(
    "#201= IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.0E-5,#210,$);\n")
file_out.write(
    "#202= IFCGEOMETRICREPRESENTATIONSUBCONTEXT('Body','Model',*,*,*,*,#201,$,.MODEL_VIEW.,$);\n")
file_out.write("#210= IFCAXIS2PLACEMENT3D(#901,$,$);\n")

file_out.write("#301= IFCUNITASSIGNMENT((#311,#312));\n")
file_out.write("#311= IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);\n")
file_out.write(
    "#312= IFCCONVERSIONBASEDUNIT(#313,.PLANEANGLEUNIT.,'degree',#314);\n")
file_out.write("#313= IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);\n")
file_out.write(
    "#314= IFCMEASUREWITHUNIT(IFCPLANEANGLEMEASURE(0.017453293),#315);\n")
file_out.write("#315= IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);\n")

file_out.write("#500= IFCBUILDING('"+str(randomString(22)) +
               "',$,'Modell',$,$,#118,$,$,.ELEMENT.,$,$,$);\n")
file_out.write("#519= IFCRELAGGREGATES('" +
               str(randomString(22))+"',$,$,$,#116,(#500));\n")
file_out.write("#520= IFCBUILDINGSTOREY('"+str(randomString(22)) +
               "',#110,'Ebene 1',$,'Ebene:Ebene',#118,$,'Alpha',.ELEMENT.,.0);\n")
file_out.write("#521= IFCBUILDINGSTOREY('"+str(randomString(22)) +
               "',#110,'Ebene 2',$,'Ebene:Ebene',#118,$,'Betha',.ELEMENT.,.0);\n")
file_out.write("#530= IFCRELAGGREGATES('" +
               str(randomString(22))+"',#110,$,$,#500,(#520));\n")
file_out.write("#531= IFCRELAGGREGATES('" +
               str(randomString(22))+"',#110,$,$,#500,(#521));\n")

file_out.write("#801= IFCPRESENTATIONSTYLEASSIGNMENT((#802));\n")
file_out.write("#802= IFCSURFACESTYLE($,.POSITIVE.,(#804));\n")
file_out.write("#803= IFCCOLOURRGB($,0.,0.,0.);\n")
file_out.write("#804= IFCSURFACESTYLESHADING(#803);\n")

file_out.write("#901= IFCCARTESIANPOINT((0.,0.,0.));\n")
file_out.write("#902= IFCDIRECTION((1.,0.,0.));\n")
file_out.write("#903= IFCDIRECTION((0.,1.,0.));\n")
file_out.write("#904= IFCDIRECTION((0.,0.,1.));\n")
file_out.write("#905= IFCDIRECTION((-1.,0.,0.));\n")
file_out.write("#906= IFCDIRECTION((0.,-1.,0.));\n")
file_out.write("#907= IFCDIRECTION((0.,0.,-1.));\n")
file_out.write("#908= IFCCIRCLEPROFILEDEF(.AREA.,$,$,"+str(5)+");\n")

i = 10  # Counter für Zähler ab 10XX
for j, row in enumerate(data['ID']):
    Z = data['Z'][j]
    RW = data['X'][j]
    HW = data['Y'][j]

    file_out.write("#"+str(i)+"00= IFCBUILDINGELEMENTPROXY('"+str(randomString(22))+"',4,'" +
                   str(data['ID'][j])+"','Cylinder Extrusion',$,#"+str(i)+"01,#"+str(i)+"10,$,$);\n")
    file_out.write("#"+str(i)+"01= IFCLOCALPLACEMENT($,#"+str(i)+"02);\n")
    file_out.write("#"+str(i)+"02= IFCAXIS2PLACEMENT3D(#"+str(i)+"03,$,$);\n")
    file_out.write("#"+str(i)+"03= IFCCARTESIANPOINT((0.0,0.0,0.0));\n")
    file_out.write("#"+str(i)+"10= IFCPRODUCTDEFINITIONSHAPE($,$,(#"+str(i)+"20));\n")
    file_out.write("#"+str(i)+"11= IFCRELCONTAINEDINSPATIALSTRUCTURE('" +
                   str(randomString(22))+"',$,'Physical model',$,(#"+str(i)+"00),#520);\n")

    # CSG-Primitive
    file_out.write("#"+str(i)+"20= IFCSHAPEREPRESENTATION(#202,'Body','CSG',(#"+str(i)+"21));\n")
    file_out.write("#"+str(i)+"21= IFCCSGSOLID(#"+str(i)+"22);\n")
    file_out.write("#"+str(i)+"22= IFCBLOCK(#"+str(i)+"35,5.,5.,5.);\n")

    # ExtrudedAreaSolid
    file_out.write("#"+str(i)+"30= IFCSHAPEREPRESENTATION(#202,'Body','SweptSolid',(#"+str(i)+"31));\n")
    file_out.write("#"+str(i)+"31= IFCEXTRUDEDAREASOLID(#908,#" +
                   str(i)+"35,#907,"+str(5)+");\n")
    file_out.write("#"+str(i)+"34= IFCRELCONTAINEDINSPATIALSTRUCTURE('" +
                   str(randomString(22))+"',$,'Physical model',$,(#"+str(i)+"00),#520);\n")
    file_out.write("#"+str(i)+"35= IFCAXIS2PLACEMENT3D(#"+str(i)+"36,$,$);\n")
    file_out.write("#"+str(i)+"36= IFCCARTESIANPOINT((" +
                   str(RW)+","+str(HW)+","+str(Z)+"));\n")

    file_out.write("#"+str(i)+"40= IFCPROPERTYSET('" +
                   str(randomString(22))+"',$,'Merkmale',$,(#"+str(i)+"41));\n")
    file_out.write("#"+str(i)+"41= IFCPROPERTYSINGLEVALUE('_Nummer',$,IFCLABEL('"+str(data['ID'][j])+"'),$);\n")
    file_out.write("#"+str(i)+"50= IFCRELDEFINESBYPROPERTIES('" +
                   str(randomString(22))+"',$,$,$,(#"+str(i)+"00),#"+str(i)+"40);\n")

    file_out.write("#"+str(i)+"55= IFCCOLOURRGB($,"+str(data['Color'][j])+","+str(1-data['Color'][j])+",0.0);\n") 
    file_out.write("#"+str(i)+"56= IFCSURFACESTYLERENDERING(#"+str(i)+"55,$,$,$,$,$,$,$,.FLAT.);\n") 
    file_out.write("#"+str(i)+"57= IFCSURFACESTYLE($,.BOTH.,(#"+str(i)+"56));\n") 
    file_out.write("#"+str(i)+"58= IFCPRESENTATIONSTYLEASSIGNMENT((#"+str(i)+"57));\n") 
    file_out.write("#"+str(i)+"59= IFCSTYLEDITEM(#"+str(i)+"21,(#"+str(i)+"58),$);\n")
    
    i = i+1

file_out.write("ENDSEC;\n")
file_out.write("END-ISO-10303-21;")

file_out.close()
