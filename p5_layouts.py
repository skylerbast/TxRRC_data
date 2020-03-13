# These layouts are not complete yet.
#
# This mostly follows the layout described by the TxRRC in the
# manual available at: 
# https://rrc.texas.gov/media/24458/ora001_p5_manual_october-2014.pdf
#
# The main difference is that date fields described separately in the 
# layout provided are instead combined into one date field.

organization_information_layout = [
  ('OROR_ORGANIZATION_INFO_ID', 0, 2, 'pic_any'),
  ('OROR_ORG_OPERATOR_NUMBER', 2, 6, 'pic_numeric'),
  ('OROR_ORG_ORGANIZATION_NAME', 8, 32, 'pic_any'),
  ('OROR_REFILING_REQUIRED_FLAG', 40, 1, 'pic_any'),
  ('OROR_P_5_STATUS', 41, 1, 'pic_any'),
  ('OROR_HOLD_MAIL_CODE', 42, 1, 'pic_any'),
  ('OROR_RENEWAL_LETTER_CODE', 43, 1, 'pic_any'),
  ('OROR_ORGANIZATION_CODE', 44, 1, 'pic_any'),
  ('OROR_ORGAN_OTHER_COMMENT', 45, 20, 'pic_any'),
  ('OROR_GATHERER_CODE', 65, 5, 'pic_any'),
  ('OROR_ORG_ADDR_LINE1', 70, 31, 'pic_any'),
  ('OROR_ORG_ADDR_LINE2', 101, 31, 'pic_any'),
  ('OROR_ORG_ADDR_CITY', 132, 13, 'pic_any'),
  ('OROR_ORG_ADDR_STATE', 145, 2, 'pic_any'),
  ('OROR_ORG_ADDR_ZIP', 147, 5, 'pic_numeric'),
  ('OROR_ORG_ADDR_ZIP_SUFFIX', 152, 4, 'pic_numeric'),
  ('OROR_LOCATION_ADDR_LINE1', 156, 31, 'pic_any'),
  ('OROR_LOCATION_ADDR_LINE2', 187, 31, 'pic_any'),
  ('OROR_LOCATION_ADDR_CITY', 218, 13, 'pic_any'),
  ('OROR_LOCATION_ADDR_STATE', 231, 2, 'pic_any'),
  ('OROR_LOCATION_ADDR_ZIP', 233, 5, 'pic_numeric'),
  ('OROR_LOCATION_ADDR_ZIP_SUFFIX', 238, 4, 'pic_numeric'),
  ('OROR_DATE_BUILT', 242, 8, 'pic_numeric'),
  ('OROR_DATE_INACTIVE', 250, 8, 'pic_numeric'),
  ('OROR_PHONE_NUMBER', 258, 10, 'pic_numeric'),
  ('OROR_REFILE_NOTICE_MONTH', 268, 2, 'pic_numeric'),
  ('OROR_REFILE_LETTER_DATE', 270, 8, 'pic_numeric'),
  ('OROR_REFILE_NOTICE_DATE', 278, 8, 'pic_numeric'),
  ('OROR_REFILE_RECEIVED_DATE', 286, 8, 'pic_numeric'),
  ('OROR_LAST_P_5_RECEIVED_DATE', 294, 8, 'pic_numeric'),
  ('OROR_OTHER_ORGANIZATION_NO', 302, 6, 'pic_numeric'),
  ('OROR_FILING_PROBLEM_DATE', 308, 8, 'pic_any'),
  ('OROR_FILING_PROBLEM_LTR_CODE', 316, 3, 'pic_any'),
  ('OROR_TELEPHONE_VERIFY_FLAG', 319, 1, 'pic_any'),
  ('OROR_OP_NUM_MULTI_USED_FLAG', 320, 1, 'pic_any'),
  ('OROR_OIL_GATHERER_STATUS', 321, 1, 'pic_any'),
  ('OROR_GAS_GATHERER_STATUS', 322, 1, 'pic_any'),
  ('OROR_TAX_CERT', 323, 1, 'pic_any'),
  ('OROR_EMER_PHONE_NUMBER', 324, 10, 'pic_numeric'),
]

def get_layout(record_key):  
  layouts_map = {
    'A' : {'name': 'organization', 'layout': organization_information_layout},
  }
  
  return layouts_map[record_key]