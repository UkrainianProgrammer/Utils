# Word (for now) to PDF converter
import sys
import os
from docx2pdf import convert

# Note: if the output path simply ends with a dir name
# the new pdf file will use the same name as the docx one
inFile = os.path.abspath(sys.argv[1])
outFile = os.path.abspath(sys.argv[2])

convert(inFile, outFile)