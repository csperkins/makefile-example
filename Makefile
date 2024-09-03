
DATA = data/pg11.txt \
       data/pg76.txt \
       data/pg84.txt \
       data/pg145.txt \
       data/pg345.txt \
       data/pg1342.txt \
       data/pg2600.txt \
       data/pg2701.txt \
       data/pg5200.txt \
       data/pg6130.txt

NORMALISED = $(DATA:data/%.txt=results/%.normalised.txt)
WORDS      = $(DATA:data/%.txt=results/%.json)

RESULTS    = results/most-common-word.dat

all: $(RESULTS)

results/most-common-word.dat: scripts/most-common-word.py $(WORDS) | results
	python3 $^ $@

results/%.json: scripts/count-words.py results/%.normalised.txt | results
	python3 $^ $@

results/%.normalised.txt: scripts/normalise.py data/%.txt | results
	python3 $^ $@

results:
	mkdir $@

clean:
	rm -f $(NORMALISED)
	rm -f $(WORDS)
	rm -f $(RESULTS)

# List of targets that don't represent files or directories:
.PHONY: all clean

# The presence of the .DELETE_ON_ERROR target with no dependencies causes
# make to remove a target if the command used to create it fails. It is
# common for a command that crashes to leave behind a partially written
# output file. With this target specified, such files are automatically
# cleaned-up by make.
.DELETE_ON_ERROR:

# The presence of the .NOTINTERMEDIATE target with no dependencies tells
# make not to delete intermediate files.  An intermediate file is a file
# that's created by applying a chain of pattern rules but that isn't
# explicitly mentioned as a dependency of any rule. 
#
# In this Makefile, files matching the pattern results/%.normalised.txt
# are intermediate files. They're built as part of a chain of pattern rules
# (results/%.json <- results/%.normalised.txt <- data/%.txt), but there is
# no rule that explicitly depends on the list of files with names matching
# the intermediate step (the depenency of results/most-common-words.dat on
# $(WORDS) gives an explicit dependency on files matching results/%.json,
# but there is no such explicit dependency on the files matching
# results/%.normalised.txt)
#
# The use of .NOTINTERMEDIATE equires GNU make v4.4.1 or later.
.NOTINTERMEDIATE:

# Configuration for make:
#   --output-sync
#       When using -j to run in commands in parallel, buffer the output
#       to avoid interspersing the results of multiple commands
#   --warn-undefined-variables
#       Warn if a rule refers to an undefined variable
#   --no-builtin-rules
#   --no-builtin-variables
#       Remove the built-in rules and variables used to compile programs,
#       build archives, etc., leaving behind only the rules and variables
#       that are explicitly defined in the makefile.
# Adding options to MAKEFLAGS in this way is equivalent to specifying the
# options on the command line when running make.
MAKEFLAGS += --output-sync --warn-undefined-variables --no-builtin-rules --no-builtin-variables

