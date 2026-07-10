total=0

echo "Enter marks fro 5 subjects"

for ((i=1; i<=5; i++))
do
	read -p "Subject $iL " mark
	total=$((total + mark))
done

average=$((total/5))

echo
echo "Total Marks: $total"
echo "Average Marks: $average"

if [ $average -ge 90 ]; then
	grade="A"
elif [ $average -ge 75 ]; then
	grade="B"
elif [ $average -ge 60 ]; then
	grade="C"
elif [ $average -ge 50 ]; then
	grade="D"
else
	grade="Fail"

fi

echo "Grade: $grade"
