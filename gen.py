import time
from random import randrange
import plotly.plotly as pyOn
import plotly.offline as py
py.init_notebook_mode()
from plotly.tools import FigureFactory as FF
from datetime import datetime,timedelta

from pandas_datareader import data

pyOn.sign_in('param.rajpura', 'UlMLjIL2ATHoQDKV9MWX')


dateform = '%Y-%m-%d'
start_date = '2016-01-01'
end_date = '2017-01-01'
dest_img_folder = '/home/param/ml_project/images/'
dest_txt_folder = '/home/param/ml_project/txt/'
def random_date(start, end,dateformat):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    day1 = start + timedelta(seconds=random_second)
    day15 = day1 + timedelta(days=16)
    return day1.strftime(dateformat),day15.strftime(dateformat)

d1 = datetime.strptime(start_date, dateform)
d2 = datetime.strptime(end_date, dateform)
#print(random_date(d1, d2,dateform))
for i in range(500):
    plot_start,plot_end = random_date(d1, d2,dateform)
    #print(plot_start,plot_end)
    dest_img_filename = dest_img_folder + str(i).zfill(3)+'.png'
    dest_txt_filename = dest_txt_folder + str(i).zfill(3)+'.txt'
    aapl = data.DataReader('AAPL', 'yahoo', plot_start, plot_end)
    #print(aapl)
    #print(aapl.Open[-1])
    #print(aapl.Open[last_index])
    fig = FF.create_candlestick(aapl.Open[:-1], aapl.High[:-1], aapl.Low[:-1], aapl.Close[:-1], dates=aapl.index[:-1])
    #py.iplot(fig, filename='aapl-candlestick', validate=False)
    pyOn.image.save_as(fig, filename=dest_img_filename)
    with open(dest_txt_filename, "a") as file:
        file.write( "%f %f %f %f" % (aapl.Open[-1],aapl.High[-1],aapl.Low[-1],aapl.Close[-1]) )
