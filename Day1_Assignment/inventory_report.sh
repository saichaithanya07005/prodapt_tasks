create_folder()
{
    mkdir -p reports
}
 
display_inventory()
{
    echo "------ Inventory Details ------"
    cat inventory.txt
}
 
low_stock()
{
    echo
    echo "------ Low Stock Products ------"
 
    awk -F',' '$3<10 {print $0}' inventory.txt > reports/low_stock.txt
 
    cat reports/low_stock.txt
}
 
total_products()
{
    echo
    echo "Total Products:"
    wc -l inventory.txt
}
 
replace_name()
{
    sed 's/USB/Pen Drive/' inventory.txt > reports/updated_inventory.txt
}
 
compress_reports()
{
    tar -czf reports/inventory_backup.tar.gz reports
    echo
    echo "Reports Archived Successfully."
}
 
display_reports()
{
    echo
    echo "Files in reports folder:"
    ls reports
}
 
# Main Program
create_folder
display_inventory
low_stock
total_products
replace_name
compress_reports
display_reports
