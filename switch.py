
#!/usr/bin/env python

import sys
import serial

matrix_code = "QS\r"
print "Sending request", matrix_code, "to the matrix"

matrix = serial.Serial("/dev/ttyUSB0", 4800, timeout=1)
print "The serial port is open: ", matrix.isOpen()

matrix.write(matrix_code)

matrix_response = matrix.readlines()
print "Matrix response:"
for line in matrix_response:
  print ' '.join(line.split())

matrix.close()
print "The serial port is open: ", matrix.isOpen()

