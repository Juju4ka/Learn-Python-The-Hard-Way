tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\n\n"
print "Escape Sequances"

print "\t1) Backslash: \\"
print "\t2) Single-quote: \'"
print "\t3) Double quote: \""
print "\t4) ASCII bell makes ringing the bell alert sounds ", "\a"
print "\t5) ASCII backspace ( BS ) removes previous character: "
print "cat" + "\b" + "r"
print "\t6) ASCII formfeed (FF): ", "\fhello\fworld"
print "\t7) ASCII linefeed (LF): ", "\npython\nis\nawesome\n"
print "\t8) Character named name in the Unicode database (Unicode only): ", u"\N{MICRO SIGN}"
print "\t9) ASCII carriage return (CR).",
print " Moves all characters after (CR) the the beginning ",
print "of the line while overriding same number of characters moved."
print "123456\rXX_XX"
print "\t10) ASCII horisontal tab (TAB) ", "\t*Apples"
print "\t11) Character with 16-bit hex value xxxx (Unicode only) ", u"\u0180"
print "\t12) Character with 32-bit hex value xxxxxxxx (Unicode only) ", u"\U00000180"
print "\t13) ASCII vertical tab (VT) ", "\v*Oranges"
print "\t14) \\ooo Prints character based on its octal value: \043"
print "\t15) \\xhh Prints character based on its hex value: \x23" 
