import codecs

from cobol_types import comp3, pic_alpha, pic_numeric, pic_any


def yield_blocks(in_file, block_size):
  block_bytes = in_file.read(block_size)
  while block_bytes:
    yield block_bytes
    block_bytes = in_file.read(block_size)


def parse_record(block, layout):
  record = dict()

  for name, start, size, convert in layout:
    if convert == 'comp':
      record[name] = comp3(block[start:start+size])
    elif convert == 'pic_alpha':
      record[name] = pic_alpha(block[start:start+size])
    elif convert == 'pic_numeric':
      record[name] = pic_numeric(block[start:start+size])
    else:
      record[name] = pic_any(block[start:start+size])
  
  return record