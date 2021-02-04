from fastapi import APIRouter
from datetime import date
import pandas as pd
import numpy as np

router = APIRouter()


def finyear(date: date):
    findate = pd.to_datetime(date)
    if findate.month > 3 and findate.month < 13:
        finyr = str(findate.year)+'-'+str(findate.year + 1)
    else:
        finyr = str(findate.year - 1) + '-' + str(findate.year)
    return finyr


def revdata(startdate, enddate, freqtype):

    dates = pd.date_range(start=startdate, end=enddate, freq=freqtype)

    acc_code = ['Bulk Water Charges', 'Profession Tax', 'Property Tax', 'Semi Bulk Charges',
                'Semi Bulk Charges', 'Others', 'Shop Room Rents', 'Tap Connection', 'Trade License Fee', 'Water Charges']
    finaldata = []
    for code in acc_code:
        for d in dates:
            data = {}
            data['date'] = d.strftime("%Y-%m-%d")
            data['amount'] = round(np.random.uniform(low=0, high=1000), 2)
            data['arrear'] = round(np.random.uniform(low=0, high=100), 2)
            data['acc_code'] = code
            data['fin_year'] = finyear(d)
            data['year'] = d.year
            data['month'] = d.month
            # print(data)
            finaldata.append(data)
    return finaldata


@router.get("/collection")
async def collection(startdate: date, enddate: date):
    return revdata(startdate, enddate, 'D')


@router.get("/demand")
async def collection(startdate: date, enddate: date):
    return revdata(startdate, enddate, 'm')
