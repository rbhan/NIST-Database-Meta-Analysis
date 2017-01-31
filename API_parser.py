# NIST Database Meta-Analysis
# Rebecca Han
# all APIs from: http://adsorbents.nist.gov/api_list.php

import pandas as pd
import numpy as np
import json

###################################################################################################

# Read materials API
mater_file = 'materials.json'
mater_API = open(filename).read()
mater_parsed = json.loads(mater_API)

# Strip material Names, Synonyms
mater_Name = []
mater_Synonyms = []
for i in range(0, len(mater_parsed)-1):
    m = mater_parsed[i]
    mater_Name.append(m['Name'])
    mater_Synonyms.append(m['Synonyms'])

# Put into dataframe
mater_df = pd.DataFrame({'Name' : mater_Name,
                         'Synonyms' : mater_Synonyms})

###################################################################################################

# Read gases API
gas_file = 'gases.json'
gas_API = open(filename).read()
gas_parsed = json.loads(gas_API)

# Strip gas Names, Formulas, Synonyms
gas_Name = []
gas_Formula = []
gas_Synonyms = []
for i in range(0, len(gas_parsed)-1):
    g = mater_parsed[i]
    gas_Name.append(g['Name'])
    gas_Formula.append(g['Formula'])
    gas_Synonyms.append(g['Synonyms'])

# Put into dataframe
gas_df = pd.DataFrame({'Name' : gas_Name,
                       'Formula' : gas_Formula,
                       'Synonyms' : gas_Synonyms})

###################################################################################################

# Read bibliography API
bib_file = 'biblio.json'
bib_API = open(filename).read()
bib_parsed = json.loads(bib_API)

# Strip bibliography DOI, title, category, adsorbentMaterial, adsorbateGas, temperature, pressure, authors, journal, year
bib_DOI = []
bib_tit = []
bib_cat = []
bib_Mat = []
bib_Gas = []
bib_T = []
bib_P = []
bib_auth = []
bib_j = []
bib_year = []
for i in range(0, len(bib_parsed)-1):
    b = mater_parsed[i]
    bib_DOI.append(b['DOI'])
    bib_tit.append(b['title'])
    bib_cat.append(b['category'])
    bib_Mat.append(b['adsorbentMaterial'])
    bib_Gas.append(b['adsorbateGas'])
    bib_T.append(b['temperature'])
    bib_P.append(b['pressure'])
    bib_auth.append(b['authors'])
    bib_j.append(b['journal'])
    bib_year.append(b['year'])

# Put into dataframe
bib_df = pd.DataFrame({'DOI' : bib_DOI,
                       'title' : bib_tit,
                       'category' : bib_cat,
                       'adsorbentMaterial' : bib_Mat,
                       'adsorbateGas' : bib_Gas,
                       'temperature' : bib_T,
                       'pressure' : bib_P,
                       'authors' : bib_auth,
                       'journal' : bib_j,
                       'year' : bib_year})
