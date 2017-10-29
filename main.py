import os
from gevent import monkey
import gevent
import shutil
import sys
import config
import logging
import config

def crawl(tkr='') :

    '''
    Crawling function using yahoo finance api
    https://finance.yahoo.com/quote/IBM/
    It runs parallely to maximize usage of every cpu core
    '''

    import core.crawl.yahoo as cralwer
    yahoo = cralwer.CrawlYahooTkr()

    if tkr == '' :
        rootdir = os.path.dirname(os.path.abspath(__file__))
        fname = rootdir + '\\data\\input\\tkrlist_small.txt'
        content = []
        with open(fname) as f :
            content = [x.strip() for x in f.readlines()]
        monkey.patch_all()
        threads = [gevent.spawn(yahoo.download_csv, tkr) for tkr in content]
        gevent.joinall(threads)

    else :
        yahoo.download_csv(tkr)

def csv_to_db(tkrhdir) :
    import core.transport.csv2db as csv2db
    csv2db.copy2db(tkrhdir,'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi')

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Started..')

    home = os.environ.get('home', None);

    if(home is None) :
        config.APP_CONFIG['HOME'] = os.path.dirname(sys.modules['__main__'].__file__)
    else :
        config.APP_CONFIG['HOME'] = os.environ['HOME']

    logging.debug('root project path : %s', config.APP_CONFIG['HOME'])

    mode = os.environ.get('mode', None)

    if not mode:
       raise ValueError('You must have "mode" variable')

    logging.debug('mode : %s', mode)

    if mode == 'crawl' :
        print('crawl')
        ticker = os.environ.get('ticker', None)
        if ticker is None :
            crawl()
        else:
            #crawl('BAC')
            #crawl('DIA')
            crawl(ticker)
    elif mode is 'import-to-db' :
        # csv to database
        # 위에서 수집한 csv 파일을 postgre database로 옮기는 함수
        #csv_to_db('D:\\dev\\workspace\\stock-analysis\\data\\tkrcsv')
        csv_to_db(config.CRAWL_CONFIG['ticker_output_csv_path'])

# generate features
#import core.genf as genf
#genf.genf('postgres://tkrapi:tkrapi@127.0.0.1/tkrapi')

# learn, predict
#import core.kerastkr as kerastkr
# out_df = kerastkr.learn_predict_kerasnn('^GSPC', 6, '2017-08')
# print(out_df)

# out_df = kerastkr.load_predict_keraslinear()
# print(out_df)

