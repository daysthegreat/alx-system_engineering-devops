0-alias: alias ls="rm *"        Script that creates an alias using Name: ls and value: rm *

1-hello_you: echo hello $USER      Script prints hello user, where user is the current Linux user.

2-path: export PATH=$PATH:/action        Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.

3-paths: echo $PATH | tr -s ":" "\n" | wc -l        Script that counts the number of directories in the PATH.

4-global_variables: printenv      Script lists environment variables.

5-local_variables: set   Script that lists all local variables and environment variables, and functions.

6-create_local_variable: BEST="School"     Script that creates a new local variable.

7-create_global_variable: export BEST="School"     Script that creates a new global variable.

8-true_knowledge: echo "$((TRUEKNOWLEDGE+=128))"    Script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.

9-divide_and_rule: echo $((POWER/DIVIDE))      A script that prints the result of POWER divided by DIVIDE, followed by a new line. POWER and DIVIDE are environment variables

10-love_exponent_breath: echo $((BREATH**LOVE))    A script that displays the result of BREATH to the power LOVE. BREATH and LOVE are environment variables

11-binary_to_decimal:  echo $((2#$BINARY))     A script that converts a number from base 2 to base 10.

12-combinations:    printf "%s\n" {a..z}{a..z} | grep -v "oo"       A script that prints all possible combinations of two letters, except oo.

13-print_float: printf "%.2f\n" $NUM     Script that prints a number with two decimal places, followed by a new line. The number will be stored in the environment variable NUM.

100-decimal_to_hexadecimal: printf "%x\n" $DECIMAL A script that converts a number from base 10 to base 16.

101-rot13: tr 'a-zA-Z' 'n-za-mN-ZA-M'     A script that encodes and decodes text using the rot13 encryption. Assume ASCII.

102-odd: perl -lne 'print if $. % 2 == 1'   Script that prints every other line from the input, starting with the first line.

103-water_and_stir: printf "%o\n" $((5#`echo $WATER | tr 'water' '01234'` + 5#`echo $STIR | tr 'stir.' '01234'`)) | tr '01234567' 'bestchol'    script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.

