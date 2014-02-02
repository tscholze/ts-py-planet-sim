# -*- coding: utf-8 -*-
"""
    Wrapper class to compensate for vtk5.4 / designer incompability
"""
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class QVTKWidget(QVTKRenderWindowInteractor):
    """
        Simple Wrapper without own functionality.
    """
    pass
