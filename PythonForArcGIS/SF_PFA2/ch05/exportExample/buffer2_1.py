# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# buffer2_1.py
# Created on: 2016-04-18 15:30:25.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Distance__value_or_field_ = "100 Feet"
Input_Features = "..\\data\\park.shp"
Output_Feature_Class = "..\\scratch\\parkbuffer.shp"

# Process: Buffer
arcpy.Buffer_analysis(Input_Features, Output_Feature_Class, Distance__value_or_field_, "FULL", "ROUND", "NONE", "")

