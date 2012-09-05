from xml.sax import handler

class Get_Watts_Handler(handler.ContentHandler):
    """
    Returns a list of watt readings from a given XML file
    """


    def __init__(self,outfile):
        self.outfile = outfile
        self.inWatt = False
        self.count = 0
        self.total = 0
        self.list_watt_readings = []


    def startDocument(self):
        """ 
        ContentHandler mthd - 
        called when parse starsts immediately before first element
        """
        print "--------  Document Start --------"
    def endDocument(self):                                      
        """called after all elmnts have been processed"""
        print "--------  Document End --------"


    def startElement(self, name, attrs): 
        """
        called at each opening tag of elmnt
        passd elmnt nme(str) & obj containing attibs (inst xml.sax.saxlib.Attibutes)
        """
        if name == 'watts':
            self.count = self.count + 1
            self.inWatt = True
    def endElement(self, name): 
        """called at each end of tag"""
        if name == 'watts':
            self.inWatt = False


    def characters(self,chrs):
        print "this reading: "
        print chrs
#        if self.inWatt:
#            print "This is a reading: "
#            print chrs
#            self.list_watt_readings.append(chrs)
