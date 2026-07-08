mkdir -p project/{src,docs,scripts,backup,archive}

touch project/src/app.py
touch project/src/config.txt
touch project/docs/readme.md
touch project/scripts/deploy.sh

# copying files
cp projects/src/config.txt project/backup

# moving files to archive
mv project/docs/readme.md project/archive

# renaming files
mv project/src/app.py project/src/main.py

# searching files
find project -name "main.py"
find project -name "*.txt"

chmod 755 project/scripts/deploy.sh

ls -l project/scripts/deploy.sh

# compressing the files
tar -cvzf project_backup.tar.gz project/

mkdir recovered_project
tar -xzvf project_backup.tar.gz -C recovered_project/

tree recovered_project

find recovered_project
