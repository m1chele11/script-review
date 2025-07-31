

#!/bib/bash


LOG_FILE="server.log"
OUT_FILE="error_logs2.txt"

grep "ERROR" $LOG_FILE > $OUT_FILE
ERROR_COUNT=$(cat $OUT_FILE | wc -l)

if [ "$ERROR_COUNT" -gt 5 ]; then
    echo "🚨 Alert: High number of errors detected!"
else
    echo "✅ Error count normal."
fi