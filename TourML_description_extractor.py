import xml.etree.ElementTree as ET
from FREDDialer import FREDDialer
import logging as log
log.basicConfig(level=log.INFO)
from pathlib import Path
import sys


def extractGraphFromStops(xml_file, outfolder, fred_endpoint, mime, prefix):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    fredDialer = FREDDialer(fred_endpoint, mime)
    
    namespaces = {'tourml': 'http://tapintomuseums.org/TourML'} 

    for stop in root.findall('.//tourml:Stop', namespaces):
        identifier = stop.attrib.get("{http://tapintomuseums.org/TourML}id")
        print("processing " + identifier)
        for description in stop.findall('tourml:Description', namespaces):
            if description.text is not None:
                outfile = outfolder + identifier + '.ttl'
                my_file = Path(outfile)
                if not my_file.is_file():
                    g = fredDialer.dial(description.text, prefix + identifier + "/")
                    g.serialize(destination=outfile, format='turtle')
                else:
                    log.debug("discarding " + identifier + " since it is already processed!")
            else:
                log.debug("discarding " + identifier + " since the description is empty")


if __name__ == '__main__':
    extractGraphFromStops(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]))
