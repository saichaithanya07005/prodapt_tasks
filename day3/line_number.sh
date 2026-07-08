show_line()
{
	file=$1
	word=$2

	grep -n "$word" "$file"
}

show_line file1.txt Mac
