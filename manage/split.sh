#!/bin/bash

# Split a PDF into 12 parts, each containing 100 pages

INPUT="The_PDF.pdf"
mkdir -p part
cd part

for i in {0..11}; do
    start=$((i*100+1))
    end=$(((i+1)*100))
    pdftk "../$INPUT" cat "$start-$end" output "part$((i+1)).pdf"
    echo "Created part$((i+1)).pdf with pages $start to $end"
done
