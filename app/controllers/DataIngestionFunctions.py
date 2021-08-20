# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:10:49 2021

@author: Hossein
"""
import lasio


def load_MSE(file):
    if file.lower().endswith('.las') or file.lower().endswith('.txt'):
        las = lasio.read(file)
        lasdf = las.df()

        lasdf['WELL'] = las.well.WELL.value
        lasdf['DEPTH'] = lasdf.index
        # METADATA

        # Version
        version = las.sections['Version']['VERS'].value
        createdOn = las.sections['Version']['CREA'].value
        # Well
        well = las.sections['Well']['Well'].value
        api = las.sections['Well']['API'].value
        uwi = las.sections['Well']['UWI'].value
        company = las.sections['Well']['SRVC'].value
        field = las.sections['Well']['FLD'].value

        state = las.sections['Well']['STAT'].value
        country = las.sections['Well']['CTRY'].value
        location = las.sections['Well']['LOC'].value
        location1 = las.sections['Well']['LOC1'].value

        start = las.sections['Well']['STRT'].value
        stop = las.sections['Well']['STOP'].value
        step = las.sections['Well']['STEP'].value

        elevation = las.sections['Well']['EPD'].value
        logMeasuredFrom = las.sections['Well']['LMF'].value
        drillMeasuredFrom = las.sections['Well']['DMF'].value
        abovePermDatum = las.sections['Well']['APD'].value

        elevKellyBushing = las.sections['Well']['EKB'].value
        elevDrillFloor = las.sections['Well']['EDF'].value
        elevDrillFloor = las.sections['Well']['EGL'].value
        date = las.sections['Well']['DATE'].value

        metadata = {
            'Version': version,
            'CreatedOn': createdOn,

            'Well': well,
            'API': api,
            'UWI': uwi,
            'Company': company,
            'Field': field,

            'State': state,
            'Country': country,
            'Location': location,
            'Location1': location1,

            'Start': start,
            'Stop': stop,
            'Step': step,

            'Elevation': elevation,
            'LogMeasuredFrom': logMeasuredFrom,
            'DrillMeasuredFrom': drillMeasuredFrom,
            'AbovePermDatum': abovePermDatum,

            'ElevKellyBushing': elevKellyBushing,
            'ElevDrillFloor': elevDrillFloor,
            'ElevDrillFloor': elevDrillFloor,
            'Date': date
        }

        return lasdf, metadata

    else:
        print('This module only supports LAS and TXT files.')
