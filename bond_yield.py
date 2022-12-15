import pandas as pd
import requests
import datetime
import numpy as np
from scipy.interpolate import CubicSpline
import os
data_path = os.path.dirname(__file__) + "/yield_data/"
def china_rf(current_date):
    """
    Commonly previous trading day as risk free rate dataframe
    :param date: datetime.date
    """

    date_str = current_date.strftime('%Y%m%d')
    df = bond_china_yield(date_str, date_str)
    df.to_csv(data_path+ "yield_curve_" + date_str + ".csv")


def bond_china_yield(
        start_date: str = "20200204", end_date: str = "20210124"
) -> pd.DataFrame:
    """
    source website:
    https://www.chinabond.com.cn/
    http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2019-02-07&endDate=2020-02-04&gjqx=0&qxId=ycqx&locale=cn_ZH
    noting: end_date - start_date should be less than one year
    :param start_date: required start date, return data for a year after that date
    :type start_date: str
    :param end_date: required end date, return data for a year after that date
    :type end_date: str
    :return: returns data for the last year between specified dates
    :rtype: pandas.DataFrame
    """
    url = "http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery"
    params = {
        "startDate": '-'.join([start_date[:4], start_date[4:6], start_date[6:]]),
        "endDate": '-'.join([end_date[:4], end_date[4:6], end_date[6:]]),
        "gjqx": "0",
        "qxId": "ycqx",
        "locale": "cn_ZH",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    }
    res = requests.get(url, params=params, headers=headers)
    data_text = res.text.replace("&nbsp", "")
    data_df = pd.read_html(data_text, header=0)[1]

    data_df['日期'] = pd.to_datetime(data_df['日期']).dt.date
    data_df['3月'] = pd.to_numeric(data_df['3月'])
    data_df['6月'] = pd.to_numeric(data_df['6月'])
    data_df['1年'] = pd.to_numeric(data_df['1年'])
    data_df['3年'] = pd.to_numeric(data_df['3年'])
    data_df['5年'] = pd.to_numeric(data_df['5年'])
    data_df['7年'] = pd.to_numeric(data_df['7年'])
    data_df['10年'] = pd.to_numeric(data_df['10年'])
    data_df['30年'] = pd.to_numeric(data_df['30年'])
    data_df.sort_values('日期', inplace=True)
    data_df.reset_index(inplace=True, drop=True)
    data_df.rename(columns={'日期': 'current_date',
                            '3月': '0.25',
                            '6月': '0.50',
                            '1年': '1.0',
                            '3年': '3.0',
                            '5年': '5.0',
                            '7年': '7.0',
                            '10年': '10.0',
                            '30年': '30.0'}, inplace=True)

    data_df = data_df
    return data_df


def bond_yield(date, yield_name):
    """
    :param date: datetime.date, normally previous trading day
    :param yield_name: string, supported three types: 'Treasury_bond'. 'Interbank', 'Short-term'
    """
    china_rf(date)
    rf_date_string = date.strftime('%Y%m%d')
    rf_df = pd.read_csv(data_path+ "yield_curve_" + rf_date_string + ".csv").T
    rf_df = rf_df.drop(rf_df.index[0:3], axis=0)
    bond_ttm = rf_df.index.to_numpy(dtype="float")
    if yield_name == 'Treasury_bond':
        risk_free_rate = rf_df.iloc[:, 0].to_numpy(dtype="float") / 100.0
    elif yield_name == 'Interbank':
        risk_free_rate = rf_df.iloc[:, 1].to_numpy(dtype="float") / 100.0
    elif yield_name == 'Short-term':
        risk_free_rate = rf_df.iloc[:, 2].to_numpy(dtype="float") / 100.0
        risk_free_rate = risk_free_rate[~np.isnan(risk_free_rate)]
        bond_ttm = bond_ttm[:-1]
    else:
        raise Exception("Unsupported yield name!")

    df = pd.DataFrame({'bond_ttm': bond_ttm, 'risk_free_rate': risk_free_rate})
    df.to_csv(data_path + yield_name + "_" + rf_date_string + ".csv")


def cubic_spline_bond(yield_name, date, ttm):
    rf_date_string = date.strftime('%Y%m%d')
    df = pd.read_csv(yield_name + "_" + rf_date_string + ".csv")
    cubic_spline_result = CubicSpline(df.bond_ttm, df.risk_free_rate)
    return cubic_spline_result(ttm)


if __name__ == "__main__":
    bond_yield(datetime.date(2022, 12, 14), 'Short-term')
    # create bond yield csv file: bond_yield(rf_day, 'Treasury_bond')
    # rf = cubic_spline_bond('Treasury_bond', rf_day, ttm)
