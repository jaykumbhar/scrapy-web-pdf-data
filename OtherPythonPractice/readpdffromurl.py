# from urllib2 import urlopen
from urllib.request import urlopen,Request
from PyPDF2 import PdfFileWriter, PdfFileReader
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

url = "https://ir.antheminc.com/static-files/42a5e02c-6196-4246-8f50-cf466940800c"
writer = PdfFileWriter()

remoteFile = urlopen(Request(url)).read().decode("ISO-8859-1")
# print(type(remoteFile.decode("ISO-8859-1")))
memoryFile = StringIO(remoteFile)
pdfFile = PdfFileReader(memoryFile)

for pageNum in xrange(pdfFile.getNumPages()):
        currentPage = pdfFile.getPage(pageNum)
        #currentPage.mergePage(watermark.getPage(0))
        writer.addPage(currentPage)


outputStream = open("output.pdf","wb")
writer.write(outputStream)
outputStream.close()