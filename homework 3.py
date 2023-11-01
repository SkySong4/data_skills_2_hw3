import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas

#part2: old fips to new fips mapping
old_new = {19380:19660, #Dayton OH
           70750:12700, #Bangor, ME
           70900:12940, #Barnstable, MA
           71650:12700, #Boston, MA
           71950:14860, #Bridgeport, CT
           72400:15540, #Burlington, VT
           73450:25860, #Hartford, CT
           75700:35380, #New Haven, CT
           76450:35980, #Norwich, CT
           76750:38860, #Portland, ME
           77200:39300, #Providence, RI
           78100:44140} #Springfield, MA
