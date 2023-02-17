Parse mqpar.xml file and extract useful information

## R

```
source("parse_mqpar.R")
f = "./example_mqpar.xml"
v = parse_mqpar(f)

# fasta file
v$fasta

# experimental design
v$experimental_design


```

## Python

```
import parse_mqpar
f = "./example_mqpar.xml"
v = parse_mqpar.parse(f)

# fasta file
v["fasta"]

# experimental design
v["experimental_design"]

```
