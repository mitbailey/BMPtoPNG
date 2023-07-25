from PIL import Image
import os

indir = './input'
outdir = './output'

if not os.path.exists(indir):
    print('The input directory cannot be found. Please ensure all PNG files to be converted are placed in a folder named "input" at the same level as the executable.')
    exit(1)

if not os.path.exists(outdir):
    print('The output directory cannot be found. Please ensure there exists a folder named "output" at the same level as the executable.')
    exit(2)

print('Converting files:\n')

infilelist = os.listdir(indir)
infilelist = [name for name in infilelist if '.bmp' in name or '.BMP' in name]

for infile in infilelist:
    outfile = infile.rsplit('.', 1)[0]
    print('%s --> %s.png'%(infile, outfile))
    Image.open('%s/%s'%(indir, infile)).save(os.path.join(outdir, '%s.png'%(outfile)), format='png')

print('\nComplete.')