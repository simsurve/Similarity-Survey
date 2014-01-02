
from reader.readXLSX import readXLSX


from similarityCalculator.SimilarityOperations import *

read = readXLSX()

allUserProp = read.start_reading()
print allUserProp

simop = SimilarityOperations(allUserProp)
simop.apply()


