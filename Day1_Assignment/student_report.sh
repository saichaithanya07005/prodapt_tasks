create_folder()
{
    mkdir -p reports
}
 
display_students()
{
    echo "------ Student Marks ------"
    cat students.txt
}
 
pass_students()
{
    echo
    echo "------ Pass Students ------"
    awk -F',' '$3>=35 {print $0}' students.txt > reports/pass_students.txt
    cat reports/pass_students.txt
}
 
top_students()
{
    echo
    echo "------ Students Scoring Above 80 ------"
    grep -E '8[0-9]|9[0-9]|100' students.txt > reports/top_students.txt
    cat reports/top_students.txt
}
 
update_marks()
{
    sed 's/30/35/' students.txt > reports/updated_marks.txt
}
 
count_students()
{
    echo
    echo "Total Students:"
    wc -l students.txt
}
 
compress_reports()
{
    tar -czf reports/student_reports.tar.gz reports
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
display_students
pass_students
top_students
update_marks
count_students
compress_reports
display_reports
