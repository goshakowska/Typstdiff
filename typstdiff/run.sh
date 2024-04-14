#!/bin/bash

if [ "$#" -lt 3 ]; then
    echo "Usage: $0 file_old.typ file_new.typ connected.typ [--pdf]"
    exit 1
fi

file_old="$1"
file_new="$2"
file_connected="$3"

file_old_json="${file_old%.typ}.json"
file_new_json="${file_new%.typ}.json"
connected_json="${file_connected%.typ}.json"

pandoc -t json -f typst "$file_old" -o "$file_old_json"
pandoc -t json -f typst "$file_new" -o "$file_new_json"

python main.py "$file_old_json" "$file_new_json" "$connected_json"

pandoc -f json -t typst "$connected_json" -o "$file_connected"

if [ "$3" == "--pdf" ]; then
    typst compile "$file_old" "${file_old%.typ}.pdf"
    typst compile "$file_new" "${file_new%.typ}.pdf"
    typst compile "$file_connected" "${file_connected%.typ}.pdf"
fi
