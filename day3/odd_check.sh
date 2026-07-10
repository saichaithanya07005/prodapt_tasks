check_odd_even()
{
	if [[ $(($1 %2)) -eq 0 ]];
	then
		echo "$1 is even"
	else
		echo "$1 is odd"
	fi
}
echo "Enter the number: "
read num

check_odd_even $num
