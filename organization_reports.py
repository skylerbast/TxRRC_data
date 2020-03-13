import pandas as pd

from sqlalchemy import create_engine

from cobol_types import comp3, display
from mainframe import yield_blocks, parse_record
from p5_layouts import get_layout

block_len = 350

cobol_file = open('./data_files/P5_downloaded_20200313.ebc', 'rb')

org_list = []

for block in yield_blocks(cobol_file, block_len):
  rec_key = display(block[0:1])
  if rec_key == 'A':
    layout = get_layout(rec_key)['layout']
    record = parse_record(block, layout)
    org_list.append(record)

df = pd.DataFrame(org_list)
engine = create_engine('sqlite:///output_files/p5_master.sqlite3')
df.to_sql('organization', con=engine)