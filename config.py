# config.py

APP_CONFIG = {
    'home' : '',
}

DATABASE_CONFIG = {
    'host': 'postgres://127.0.0.1/',
    'dbname': 'tkrapi',
    'user': 'tkrapi',
    'password': 'tkrapi',
    'port': 3306
}

CRAWL_CONFIG = {
    'ticker_list_file' : '\\data\\input\\tkrlist_small.txt',
    'ticker_output_csv_path'  : '\\data\\raw\\tkrcsv',
    'ticker_output_html_path'  : '\\data\\raw\\tkrhtml',
    'start_date' : '20100101',
    'end_date' : '20171028',
    'ticker' : ''
}
