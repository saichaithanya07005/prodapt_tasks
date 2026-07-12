create_folder()
{
    mkdir -p processed_logs
}
 
find_errors()
{
    echo "Extracting ERROR logs..."
    grep "ERROR" system.log > processed_logs/error_logs.txt
}
 
analyze_logs()
{
    echo "Number of ERROR entries:"
    grep -c "ERROR" system.log
 
    echo
    echo "Log Summary:"
    awk -F':' '{print $1}' system.log
}
 
compress_logs()
{
    tar -czf processed_logs/log_backup.tar.gz processed_logs
    echo "Logs compressed successfully."
}
 
display_files()
{
    echo
    echo "Files in processed_logs:"
    ls processed_logs
}
 
# Main Program
create_folder
find_errors
analyze_logs
compress_logs
display_files
