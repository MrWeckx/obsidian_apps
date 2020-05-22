# Alias support
Using python and regex you can create aliases so every time you make a internal link such as [[star formation rate]] the program uses a predefined alias to rename to [[star formation rate|SFR]]

## Requirements.
- Python 3 with re, os and distutil libraries

### Implementation.
Clone the repository to a local file and add your Obsidian Valut path to the directories.py in the root folder. I **highly suggest to make a backup copy** before using anything. ***I'm not responsible for missing files or any trouble, use it with caution***

Execute python3 /path/to/root/aliases_ex.py

## Functioning

The way the programm works is it tries to find in all the vault pages a match for #alias='aliascomeshere' (with the quotation marks) and it assumes that is the current page alias.

---

For instance:

star formation rate.md
# Star formation rate
#alias='SFR'

The star formation rate is a key factor to study in ...

---

Second it finds all the internal links that match to that specific page and ads the alias [[star formation rate]] => [[star formation rate|SFR]].
It also asks if the user wants to correct internal links that don't match the alias. [[star formation rate|Stars]] => [[star formation rate|SFR]].

At last it shows the number of aliases, changes, the dictionary of the pages:aliases and corrections.

