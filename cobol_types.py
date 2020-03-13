STRIP_PIC_X = True # Set this to False if trimming PIC X causes problems.

import codecs
from array import array

# This contains functions to deal with COBOL COMP-3 compressed numbers and elementary
# items, such as PIC A, PIC 9, and PIC X.
#
# COMP-3 Binary Coded Decimals store values in binary form; each digit is one nibble
# and the last nibble indicates the sign. They are stored high-order to low-order.
#   For example, +12345 would be stored as:
#     0x12 0x34 0x5c 
# 
# Therefore, an n-digit number can be stored in ceil(n/2) bytes
#
# In order to convert an n-nibble (n/2 - byte) COMP-3 packed field to an integer:
#   1)  For each nibble from 1 to n-1:
#     a)  Perform bitwise and with 0xf0 (binary 11110000)
#           --> this clears the last four bits
#     b)  Shift right (arithmetic) by 4 bits
#           --> This is the most significant digit in this nibble
#     c)  Perform bitwise and with 0xf (binary 1111)
#           --> This clears the first four bits
#           --> The result is the least significant digit in this nibble
#   2) For nibble n:
#     a)  Perform bitwise and with 0xf0 (binary 11110000)
#     b)  Shift right (arithmetic) by 4 bits
#           --> This is the last digit in the number
#     c)  Perform bitwise and with 0xf (binary 1111)
#           --> If the result is 0xc, the number is positive
#           --> If the result is 0xd, the number is negative
#           --> If the result is 0xf, the number is unsigned
# 
# For more see: http://3480-3590-data-conversion.com/article-packed-fields.html
# Some code snippits taken from zorchenhimer: https://github.com/zorchenhimer/


def comp3(packed, decimal_location=0):
  # Function unpacks a COMP-3 number with number of digits n
  # Also optionally allows for conversion to float, which is specificed by PICture,
  # rather than in the data itself
  bin_arr = array('B', packed)
  val = float(0)

  # For nibbles 1 to n - 1
  # First digit in nibble is found by performing bitwise and with 0xf0, shifting 
  # right by 4 bits, and then multiplying the integer result by 10. The second 
  # digit in the nibble is found by performing a bitwise and with 0xf. These are
  # added together, and added to the existing (more significant) digits
  for i in bin_arr[:-1]:
    val = (val * 100) + (((i & 0xf0) >> 4) * 10) + (i & 0xf) 

  # For nibble n, only the first four bits represent a digit; the last 4 bits of 
  # nibble n represent the sign of the number
  i = bin_arr[-1]
  val = (val * 10) + ((i & 0xf0) >> 4)
  if (i & 0xf) == 0xd:
    val = -val

  # If we've been told how many decimals there are, leave the result float and 
  # put the decimal in the proper place; otherwise make it an integer 
  val = val / (10 ** decimal_location)
  if decimal_location == 0:
    val = int(val)

  return val


# For non-packed data, we can simply decode the EBCDIC characters and convert
# to integers if necessary
def display(data):
  ebcdic_decoder = codecs.getdecoder('cp500')
  decoded = ebcdic_decoder(data)
  val = decoded[0]

  return val


def pic_numeric(data):
  # PIC 9 will contain only numbers 0-9. We return it as an integer.
  ebcdic_decoder = codecs.getdecoder('cp500')
  decoded = ebcdic_decoder(data)
  decoded = str(decoded[0]).strip()
  val = int(decoded)

  return val


def pic_any(data):
  # PIC X can contain any information, including binary. We return it as 
  # a string after decoding it. For convenience, we strip any blank characters.
  ebcdic_decoder = codecs.getdecoder('cp500')
  decoded = ebcdic_decoder(data)
  val = decoded[0]

  if STRIP_PIC_X == True:
    val = val.strip()

  return val


def pic_alpha(data):
  # PIC Alpha will only contain A-Z, a-z, and spaces. We return it as
  # a string. Since we don't care about the restrictions on the content,
  # we just call the same function we use on PIC X here.
  val = pic_any(data)

  return val