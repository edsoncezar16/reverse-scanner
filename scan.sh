#!/bin/bash

export INPUT_DIR="input_images"
export OUTPUT_DIR="output_files"
export OUTPUT_COLUMNS="'N2 ROMANEIO / NF' 'QTD. DE VOLUMES' 'DESTINO' 'CLIENTE' 'NECOLETA'"

python scripts/scanner.py
