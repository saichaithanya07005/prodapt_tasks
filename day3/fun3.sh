add_num()
{
	sum=$(( $1 + $2 ))
	echo "Sum is $sum"
}
echo "Enter first number: "
read a
echo
echo "Enter second number: "
read b
echo

add_num $a $b
