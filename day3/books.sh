BOOKS="books.txt"
#Display All the avaiable books
display()
{
	echo "List of books in the inventory(including both availabel and non available)"
	cat "$BOOKS"
}

search()
{
	echo -n "Enter book name to search: "
	read book
	if grep -qi "$book" "$BOOKS"
	then
		echo "Book is present"
		grep -i "$book" "$BOOKS"
	else
		echo "Book not found"
	fi
}
# count out of stock books
count_outofstock()
{
	count=$(grep -ic "OutOfStock" "$BOOKS")
	echo "Out Of Stock Books: $count"
}

# book stock staus
update_stock_status()
{
	echo "Enter book id to update it's status: "
	read id
	echo -n "Enter New status (Avaliable/OutOfStock)"

	sed -i "/^$id,/ s/\(,[^,]*,\)\(Available\|OutOfStock\)/\1$status/" "$BOOKS"
	echo "Book status updated successfully."
}

# calculate book inventory
inventory_value()
{
	total=$(awk -F','$4==Available'{sum+=$5} END {print sum}'"$BOOKS")
	echo "Total Inventory Value = Rs. $total"
}

#displaying books by category
display_by_category()
{
	echo "Enter the category: "
	read category
	echo
	echo "Books in $category"
	awk -F',' -v cat=="$category" 'tolower($3)==tolower(cat)'"$BOOKS"
}

#costliest
costliest()
{
	echo "Costliest Book."
	awk -F','
	'BEGIN{max=0}
	{
		if($5>max)
		{
			max=$5
			line=$0
		}
	}
	END
	{
		print line
	}'"$BOOKS"
}

while true
do
	echo
	echo "==========BOOK STORE========="
	echo "1. View All books"
	echo "2. Search Book"
	echo "3. Count out of stock books"
	echo "4. Update stock status"
	echo "5. Total Inventory Value"
	echo "6. Display Books by Category"
	echo "7. Costliest Book"
	echo "8. Exit"

	echo -n "Enter choice: "
	read choice

	case $choice in
		1)display;;
		2)search;;
		3)count_outofstock;;
		4)update_stock_status;;
		5)Inventory_value;;
		6)display_by_category;;
		7)costliest;;
		8)echo "Thank you"; break;;
		*)echo "invalid Choice" ;;
	esac
done

