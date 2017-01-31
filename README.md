# NIST Database Meta-Analysis

Database: http://adsorbents.nist.gov/

APIs: http://adsorbents.nist.gov/api_list.php

Goal: score each material based on how "knowledge" exists for it in the database

In this repository:
* three (3) .json files containing metadata for all adsorbent materials, adsorbate gases, and bibliography references
* API_parser.py reads in the .json files, strips the relevant categorical data and stores it in dataframes
