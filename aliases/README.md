# Alias support

Using python and regex you can create aliases so every time you make a internal link such as [[star formation rate]] the program uses a predefined alias to rename to [[star formation rate|SFR]]

## Requirements.

- Python 3 with `re`, `os`, `distutil` and `shutil` libraries

### Implementation.

Clone the repository to a local file and *add your Obsidian Valut path to the `directories.py` obsidan_base_path variable in the root folder*. I **highly suggest to make a backup copy** before using anything. ***I'm not responsible for missing files or any trouble, use it with caution.*** Also in order to help the programme make more backup copies *add an example folder to the safe_obsidian variable in `directories.py`*. 

*Execute python3 /path/to/root/aliases_ex.py*.

I have this command linked to an alias on Linux so it's easy like a internal Obsidian button to update all my aliases.

## Functioning

The way the programm works is it tries to find in all the vault pages a match for `#alias='aliascomeshere'` (with the quotation marks) and it assumes that is the current page alias. It searches for all the internal links to that page and adds |alias]] to the internal features. It does simply that.

For instance:

---

Let this be `star formation rate.md`

# Star formation rate

#alias='SFR'

The star formation rate is a key factor to study in ...



Let this be `other page.md`

## Other page

Hello [[Star formation rate]]! => Hello [[Star formation rate|SFR]]!

---

---

It also asks if the user wants to correct internal links that don't match the alias. [[star formation rate|Stars]] => [[star formation rate|SFR]].

At last it shows the number of aliases, changes, the dictionary of the pages:aliases and corrections.

Yo can try it using:

python3 /path/to/root/aliases_ex.py.

`aliases_ex.py` is composed of 3 functions contained in `obsidian_classes.py` "aliases_finder", "aliases_applier", "aliases_corrector". There's also another internal functions in this script for listing pages and another special function `obsidian_bak`. 

### Obsidian_bak()

This function saves the current state of your obsidian folder set in `directories.py` >`obsidian_base_path` variable and saves the content to another folder path set in `safe_obsidian` variable as "Obsidian_copy_0".

If you apply obsidian_bak() function several times it does copies of the current state of the Obsidian folder and sorts the result so the Obsidian_copy _0 is the most recent copy. It also clears copies if the directories exceed the max number of copies set in the `total_num_copies` variable in the obsidian_bak() definition.

### Contact info

First of all sorry for the roughness of the program, I'm not a fully fledge programmer but a physics undergraduate so forgive the messy stuff or english misspelling.

Feel free to colaborate, ask or update anything so we start developing our own plugins untill Obsidian v1 lauches (aw yea) :clap: :dancer:
