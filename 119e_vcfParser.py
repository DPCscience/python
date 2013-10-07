#-----------------------------------------------------------+
#                                                           |
# 119c_vcfParser.py - report callable loci                  |
#                                                           |
#-----------------------------------------------------------+
#                                                           |
# AUTHOR: Vikas Gupta                                       |
# CONTACT: vikas0633@gmail.com                              |
# STARTED: 09/06/2013                                       |
# UPDATED: 09/06/2013                                       |
#                                                           |
# DESCRIPTION:                                              | 
# Short script to convert and copy the wheat BACs           |
# Run this in the parent dir that the HEX* dirs exist       |
#                                                           |
# LICENSE:                                                  |
#  GNU General Public License, Version 3                    |
#  http://www.gnu.org/licenses/gpl.html                     |  
#                                                           |
#-----------------------------------------------------------+

# Example:
# python ~/Desktop/script/python/119_vcfParser.py -i snp.90.PhredQual_5000.vcf


### import modules
import os,sys,getopt, re, classVCF


### global variables
global ifile, HEADER

### make a logfile
import datetime
now = datetime.datetime.now()
o = open(str(now.strftime("%Y-%m-%d_%H%M."))+'logfile','w')



### write logfile

def logfile(infile):
    o.write("Program used: \t\t%s" % "100b_fasta2flat.py"+'\n')
    o.write("Program was run at: \t%s" % str(now.strftime("%Y-%m-%d_%H%M"))+'\n')
    o.write("Infile used: \t\t%s" % infile+'\n')
            
    
def help():
    print '''
            python 100b_fasta2flat.py -i <ifile>
            '''
    sys.exit(2)

### main argument to 

def options(argv):
    global ifile
    ifile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        help()
    for opt, arg in opts:
        if opt == '-h':
            help()
        elif opt in ("-i", "--ifile"):
            ifile = arg
            
    logfile(ifile)
            
### check if file empty
def empty_file(infile):
    if os.stat(infile).st_size==0:
        sys.exit('File is empty')
                                
        
def parseFile(ifile):
    o = open(ifile+'.NoBurttiiGifu','w')
    global HEADER
    count = 0
    for line in open(ifile,'r'):
        if len(line) > 1 and not line.startswith('#'):
            line = line.strip('\n')
            obj = classVCF.VCF(line)
            genotypes = obj.genotypes()
            write_flag = False
            ### check if the burttii is not 0/1 heterogyzous
            for i in range(3,len(genotypes)):
                if obj.genotype(i) == '0/1':
                    write_flag = True
            
            if write_flag == True:
                o.write(line+'\n')
                count += 1
    print 'Total positions printed:', count
    o.close()
 
if __name__ == "__main__":
    
    options(sys.argv[1:])
    empty_file(ifile)
    
    parseFile(ifile)
    
    
    ### close the logfile
    o.close()