# Read from the file file.txt and output the tenth line to stdout.

count=0
while read -r line; do
    count=$((count + 1))
    if [ "$count" -eq 10 ]; then
        echo "$line"
        exit 0
    fi
done < file.txt
