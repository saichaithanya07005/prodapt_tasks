count_word()
{
	file=$1
	word=$2

	count=$(grep -o "$word" "$file" | wc -l)

	echo "Occurence of $word is $count"
}

count_word file1.txt Linux
