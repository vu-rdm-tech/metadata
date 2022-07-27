import getopt
import re
import sys, os

def main(argv):
    inputfile = ''
    outputfile = ''
    scriptname=os.path.basename(__file__)
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print(f'{scriptname} -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(f'{scriptname} -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    return inputfile, outputfile


def process(doc, root='./source'):
    matches = re.findall(r'{{([^{}]+)}}', doc)
    for filename in matches:
        file = f'{root}/{filename}'
        with open(file, encoding="utf8") as f:
            part = f.read().rstrip().replace('<br>\n','<br>')

        part = process(part)
        doc = doc.replace("{{%s}}" % filename, part)
    return doc


if __name__ == "__main__":
    inputfile, outputfile = main(sys.argv[1:])

print(f'process {inputfile}')

with open(inputfile, encoding="utf8") as f:
    doc = f.read()    

doc = process(doc)

with open(outputfile, 'w', encoding="utf8") as f:
    f.write(doc)

print(f'output written to {outputfile}')