1. To find the whale, use the `grep` command. The command itself is a
shortening of the commands "**G**lobally search a **Re**gular expression and
**P**rint"---a regular expression is a way of searching for patterns in a
text.  The basic syntax of grep is: `grep [search string] [file to search]`.
By default it outputs any lines on which the search string appears. For more
detail and options, type `man grep` into the terminal.

Note that everything that follows the pound sign (#) is only a comment. You
don't have to type that part out.

```
# Find the Whale
grep "whale" moby.txt
```

2. Let's substitute all of our "whales" with "chickens" using `cat`, `sed`,
pipes, and redirections. The `cat` command con**cat**enates the text data from
`moby.txt`, turning it into a stream of data we can manipulate.

Next, we pass the stream to `sed` using a pipe (`|`). `sed`, the **s**erial
**ed**itor, replaces the search string with something else. The syntax is as
follows: `s` tells sed to **s**ubstitute something; next comes the search
string; after that, the replacement string; and after that, the scope, which
is `g` for **g**lobal.

The final redirection `>` points to a file where our output will be
stored---here, `chicken.txt`. Without the redirection, many commands default to
displaying the results on the screen.

```
# substitute whale for chicken globally
cat moby.txt | sed 's/whale/chicken/g' > chicken.txt
```

3. You are already familiar with `grep`. Take a look at the output to see what
*Moby Chicken* looks like.

```
# see what happened to the whales
grep "chicken" chicken.txt
```

4. Eventually, we'll want to create a frequency list for the words in *Moby
Dick*. First, we have to throw out punctuation so that 'whale' is not counted
differently from 'whale!'

You know `cat`, piping, and redirection, but have not seen `tr` yet, or
**tr**anslate. Type `man tr` to see the full range of what `tr` can do. With
the `-d` option specified it will **d**elete every occurrence of a search
string from a text. In this case, instead of a specific search string, we will
search for a whole class of characters. We specify the punctuation character
class with `[:punct:]`. (Note: if this doesn't work on your machine, try
`[[:punct:]]`.)

```
# remove punctuation.
cat moby.txt | tr -d "[:punct:]" > moby-nopunct.txt
```

Note that we are saving each transformation in its own, descriptively named
file. It is a good practice not to overwrite your original file to avoid losing
data.

5. Confirm that it had the desired result by returning the `tail` of the new
file.

```
# check if it worked
tail moby-nopunct.txt
```

6. We don't want any upper-case characters, but we don't want to delete them
either. We'll use `tr` and character classes again to replace every upper-case
character with its lower-case equivalent. This time, we won't use the `-d`
flag.

```
# translate all upper case into lower
cat moby-nopunct.txt | tr '[:upper:]' '[:lower:]' > moby-clean.txt
tail moby-clean.txt
```

7. This might look complex, but it is made up of many steps you already know.
The `sed` command in this case will replace spaces with line breaks, placing
every word onto its own line. The syntax here is a little messy, but `\'$'\n`
uses the newline character as a replacement string.

```
# sort by word frequency
cat moby-clean.txt | sed 's/[[:space:]]/\'$'\n/g' | sort | uniq -c | sort -gr -k1 > word-count.txt head word-count.txt
```

The `sort` and `uniq -c` commands go together. The second, `uniq`, eliminates
duplicate lines, but only *contiguous* duplicate lines. In other words, if
these letters were lines, it would reduce `abbbaab` to `abab`, when what we
want is just `ab`. We have to put all the duplicates in a row so they are all
eliminated, and therefore we use `sort` before using `uniq`. The `-c` option on
`uniq` includes a count of the duplicate string after removing the extras. If
this is getting too complex, output to a file after each step to inspect the
results visually.

After we have a count for each word, we want to sort again, but now based on
the numeric order of the count rather than the alphabetical order of the word.
We also want to have the most frequent words float to the top. The first two
options, `-g` and `-r` (combined as `-gr`), tell the computer to do a
**g**eneral numeric sort in **r**everse order. The next option, `-k1`,
specifies the column of the data to base the sort on. If a sample line of
`moby-clean.txt`, where we stored our counts, might be "whale 987", it is
composed of two elements: the word and the number. The shell language uses
index notation, meaning the word is indexed as the 0th element and the number
as the 1st. Therefore, we use `-k` to tell it what to use as a **k**ey, and `1`
to specify the second column, which contains the numbers. If we wanted to
operate on the first column containing the words we would use `-k0`.

When you've stored the output, use the `head` command to take a look at the
most common words. Do you notice anything interesting about this list?  How
far down do you have to go until you find something that surprises you? What
does it show us about *Moby Dick* that we didn't know already?
