import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):    #re.match looks to see if the pattern matches the supplied string
    print("match")
if re.match(pattern, "uhssjssusjausspamuudjunspam"):     #even if the pattern is in the string, unless the string follows the pattern exactly it isnt true
    print("not match")
if re.search(pattern, "ychsjsnsnsspamjdhshs"):    #this searches for the pattern in the supplied string
    print("found")
print(re.findall(pattern, "spamhcsdjsspamjdnshshspam")) #this finds all iterations of the pattern in the string
#re.finditer(pattern, "spamhcsdjsspamjdnshshspam")) ------ does basically the same thing as findall just returns an iterator not a list

print("=" * 20)

match = re.search(pattern, "ychsjsnsnsspamjdhshspamjdjddbspams")
if match:
    print(match.group())        #returns the pattern grouped into one
    print(match.span())         #returns the start and end of the first iteration of the pattern
    print(match.start())        #returns the start point of the first iteration of the pattern
    print(match.end())          ##returns the end point of the first iteration of the pattern

print("=" * 20)

str = "hi im david, david is my name, call me david"
pattern = r"david"
rep = "amy"
print(re.sub(pattern, rep, str,))             #replaces every iteration of "PATTERN" from "STR" with "REP"
print(re.sub(pattern, rep, str, count=1))     #does the same thing but only the first "1"
print(re.sub(pattern, rep, str, count=2))     #does the same thing but only the first "2"
print(re.sub(pattern, rep, str, count=3))     #does the same thing but only the first "3"

print("=" * 20)

pattern = r"^gr.y$"     #the ^ marks the beginning of the pattern, the . is like a blank scrabble tile, the $ mars the end of the pattern

if re.match(pattern, "grey"):     
    print("match")
if re.match(pattern, "gray"):     
    print("match1")
if re.match(pattern, "stingrays"):     
    print("match11")

print("=" * 20)

pattern = r"[A-Z]"          #the characters enclosed in the square braces represent a group of characters. it can be [aeiou], [1234567890] etc
                            #if there are two {[...][...]} it looks to see that at least one character from each is present in the order they appear
if re.match(pattern, "stingrays"):     
    print("match")
if re.match(pattern, "STingrays"):     
    print("match1")

print("=" * 20)

pattern = r"[^A-Z]"          #if there is a ^ sign{[^...]} it looks to match with characters not in the group

if re.match(pattern, "stingrays"):     
    print("match")
if re.match(pattern, "STingrays"):     
    print("match1")
    
print("=" * 20)

pattern = r"ice(-)?cream"      #the "?" sign looks for either "0" or "1" repititions of the object in parenthesis
                              #you could also put a "*" to look for "0" or more repetitions or a "+" to look for "1" or more
                              #if you want a fixed range use {int_1, int_2}. this matches with any number of repetitions btw int_1 and int_2
if re.match(pattern, "icecream"):     
    print("match")
if re.match(pattern, "ice--cream"):     
    print("match1")

print("=" * 20)

pattern = r"a(bc)d(ef(g))h(i)"           #these are groups. groups can have sub-groups

match = re.match(pattern, "abcdefghijklmnop")
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.groups())

print("=" * 20)

pattern = r"(?P<name>abc)(?:def)"    #2 types of groups as seen. the first can be accessed by name the second cant

match = re.match(pattern, "abcdefghijklmnop")
print(match.group())
print(match.group("name"))
print(match.groups())

print("=" * 20)

p = r"gr(a│e)y"     #the │ shows an either/or kind of situation

match = re.match(p, "grey")
if match:     
    print("match")
match = re.match(p, "gray")
if match:     
    print("match1")
match = re.match(p, "gruys")
if match:     
    print("match11")

print("=" * 20)

pattern = r"(.+) \1"        #i take is .+ means an infinite nmber of variables and \j (j is an integer) shows the number of repetitions
                            #you can also use: \d (for digits), \s (for whitespaces), or \w (for word characters). FYI if the etter is capitalized its like putting a ^ in the beginning of the square braces
                            #also there are: \A and \Z (for beginning and end of a string{much like ^ and $}), and \B (to show there are word characters surrounding it)
match = re.match(pattern, "word word")
if match:
    print("match")
match = re.match(pattern, "?! ?!")
if match:
    print("match1")
match = re.match(pattern, "abc def")
if match:
    print("match11")

print("=" * 20)

pattern = r"\b(gray)\b"        #\A and \Z (for beginning and end of a string{much like ^ and $}), and \b (to show there are word characters surrounding it)
                               #\B uses empty string where \b uses word characters
if re.search(pattern, "grey"):     
    print("match")
if re.search(pattern, "gray"):     
    print("match1")
if re.search(pattern, "stin>gray<s"):     #it is noticed if its enclosed in >...<
    print("match11")
if re.search(pattern, "stin gray s"):     
    print("match111")

print("=" * 20)

#this is to extract email addresses
text = "my email address is oolaitan13@gmail.com"
pattern = r"([\w\.-]+)@([\w\.]+)([\w]+)"        #look at the symbols and look up for any explanation

match = re.search(pattern, text)
if match:
    print(match.group())

print("=" * 20)