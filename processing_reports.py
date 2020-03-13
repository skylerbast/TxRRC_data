import codecs
import pandas as pd

from cobol_types import comp3, display
from mainframe import yield_blocks, parse_record
from r3_layouts import get_layout

block_len = 422

cobol_file = open('./data_files/R3_downloaded_20200312.ebc', 'rb')

root_dist = ''
root_serial = ''
cycle_key = ''

roots = []
cycles = []
intake_volumes = []
disposition_unprocessed = []
plant_liquid_production = []
drip_scrubber_recovery = []
plant_stock = []
gas_delivery_detail = []
remark_key = []
pressure = []
r3_remarks = []

def update_list(record_key, record):
  switcher = {
    '03' : intake_volumes.append,
    '04' : disposition_unprocessed.append,
    '05' : plant_liquid_production.append,
    '06' : drip_scrubber_recovery.append,
    '07' : plant_stock.append,
    '10' : gas_delivery_detail.append,
    '11' : remark_key.append,
    '12' : pressure.append,
    '13' : r3_remarks.append,
  }

  method = switcher.get(record_key, lambda: 'Invalid key')
  method(record)


for block in yield_blocks(cobol_file, block_len):
  rec_key = display(block[0:2])
  layout = get_layout(rec_key)['layout']
  record = parse_record(block, layout)

  if rec_key == '01':
    root_id = record['root_id']
    roots.append(record)
  elif rec_key == '02':
    cycle_key = record['GR_CYCLE_KEY']
    record['fk_root_id'] = root_id
    cycles.append(record)
  else:
    record['fk_root_id'] = root_id
    record['fk_cycle'] = cycle_key
    update_list(rec_key, record)

roots_df = pd.DataFrame(roots)
cycles_df = pd.DataFrame(cycles)
intake_volumes_df = pd.DataFrame(intake_volumes)
disposition_unprocessed_df = pd.DataFrame(disposition_unprocessed)
plant_liquid_production_df = pd.DataFrame(plant_liquid_production)
drip_scrubber_recovery_df = pd.DataFrame(drip_scrubber_recovery)
plant_stock_df = pd.DataFrame(plant_stock)
gas_delivery_detail_df = pd.DataFrame(gas_delivery_detail)
remark_key_df = pd.DataFrame(remark_key)
pressure_df = pd.DataFrame(pressure)
r3_remarks_df = pd.DataFrame(r3_remarks)


with pd.ExcelWriter('./output_files/processing_report_master.xlsx') as writer: # pylint: disable=abstract-class-instantiated
  roots_df.to_excel(writer, sheet_name='roots')
  cycles_df.to_excel(writer, sheet_name='cycles')
  intake_volumes_df.to_excel(writer, sheet_name='intake_volumes')
  disposition_unprocessed_df.to_excel(writer, sheet_name='disposition_unprocessed')
  plant_liquid_production_df.to_excel(writer, sheet_name='plant_liquid_production')
  drip_scrubber_recovery_df.to_excel(writer, sheet_name='drip_scrubber_recovery')
  plant_stock_df.to_excel(writer, sheet_name='plant_stock')
  gas_delivery_detail_df.to_excel(writer, sheet_name='gas_delivery_detail')
  remark_key_df.to_excel(writer, sheet_name='remark_key')
  pressure_df.to_excel(writer, sheet_name='pressure')
  r3_remarks_df.to_excel(writer, sheet_name='r3_remarks')