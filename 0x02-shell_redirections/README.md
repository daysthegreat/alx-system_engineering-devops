0-hello_world: echo Hello, World Script prints hello, world

1-confused_smiley: echo "\"(Ôo)'" Script prints a confused smiley

2-hellofile: cat /etc/passwd Script displays the content of /etc/passwd file

3-twofiles: cat /etc/passwd /etc/hosts Script displays the contents of /etc/passwd file and /etc/hosts files

4-lastlines: tail /etc/passwd Script displays the last 10 lines of /etc/passwd

5-firstlines: head /etc/passwd Script displays the first 10 lines of /etc/passwd

6-third_line: head --lines=3 iacta | tail --lines=1 Script displays third line of file iacta

7-file: echo "Best School" > "\*\\\'\"Best School\"\'\\\*$\?\*\*\*\*\*:)" Script creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

8-cwd_state: ls -la > ls_cwd_content Script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it would be overwritten. If the file ls_cwd_content does not exist, create it.

9-duplicate_last_line: echo -en "" | tail --lines=1 iacta >> iacta Script that duplicates the last line of the file iacta

10-no_more_js: find . -name '*.js' -type f -delete Script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

11-directories: find -mindepth 1 -type d | wc -l Script that counts the number of directories and sub-directories in the current directory (including hidden directories. Excluding current and parent directories).

12-newest_files: ls -t | head Script that displays (newest to oldest) the 10 newest files in the current directory (one file per line).

13-unique: sort | uniq -u Script that takes a list of words (words are sorted) as input and prints only words that appear exactly once. Input format: one line, one word. Output format: one line, one word

14-findthatword: grep -i root /etc/passwd Script that displays lines containing the pattern “root” from the file /etc/passwd

15-countthatword: grep -i bin /etc/passwd | wc -l Display the number of lines that contain the pattern “bin” in the file /etc/passwd

16-whatsnext: grep -iA 3 root /etc/passwd Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

17-hidethisword: grep -iv bin /etc/passwd Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

18-letteronly: grep -i "^[a-z]" /etc/ssh/sshd_config Display all lines of the file /etc/ssh/sshd_config starting with a letter (include capital letters as well).

19-AZ: tr Ac Ze Replace all characters A and c from input to Z and e respectively.

20-hiago: tr -d cC Script that removes all letters c and C from input

21-reverse: rev Script that reverse its input.

22-users_and_homes: cut -d':' -f1,6 /etc/passwd | sort Displays all users and their home directories, sorted by users (based on the /etc/passwd file).

100-empty_casks: find . -empty -printf "%f\n" Finds all empty files and directories in the current directory and all sub-directories. *Only the names of the files and directories should be displayed (not the entire path) *Hidden files is listed.* *One file name per line.* *The listing ends with a new line.*

101-gifs: find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f Lists all the files with a .gif extension in the current directory and all its sub-directories.

102-acrostic: cut -c 1 | tr -d '\n' | sort Script that decodes acrostics that use the first letter of each line.

103-the_biggest_fan: tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev Script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

