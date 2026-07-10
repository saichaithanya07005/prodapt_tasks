info_count=0
error_count=0
warn_count=0

analyze_log()
{
	file=$1
	
	if echo "$line" | grep -q "WARNING"
	then
		((info_count++))
	elif echo "$line" | grep -q "WARNING"
	then
		((warn_count++))
	else
		((error_count++))
	fi
OA}

check_status()
{
	if [[ $error_count -gt 10 ]]
	then
		status="Critical"
	elif [[ $error_count -gt 0 ]]
	then
		status="warning"
	else
		status="healthy"
	fi
}

#read imput file

echo "enter log file:"
read logfile
if [[ ! -f $logfile ]]
then
	echo "file doesn't exist"
	exit
fi

#loop through file
while read line
do
	analyze_log "$line"
done < $logfile

#Determine status
check_status
#Generate report
{
	echo "System Log Analyzer Report"
	echo "=========================="
	echo "INFO count: $info_count"
	echo "WARNING count: $warn_count"
	echo "ERROR count: $error_count"
	echo
	echo "System status: $status"
} > report.txt

echo "Report generated in file report.txt"
