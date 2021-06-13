macbeth = macbeth.1ch.txt
frankenstein = frankenstein.1ch.txt

all: $(macbeth) $(frankenstein)

$(macbeth): ../source_texts/macbeth.txt ../collate_character_statistics.py
	../collate_character_statistics.py 1 ../source_texts/macbeth.txt > macbeth.1gram.trv
	../collate_character_statistics.py 2 ../source_texts/macbeth.txt > macbeth.2gram.trv
	../collate_character_statistics.py 3 ../source_texts/macbeth.txt > macbeth.3gram.trv
	../collate_character_statistics.py 4 ../source_texts/macbeth.txt > macbeth.4gram.trv
	../collate_character_statistics.py 5 ../source_texts/macbeth.txt > macbeth.5gram.trv

$(frankenstein): ../source_texts/frankenstein.txt ../collate_character_statistics.py
	../collate_character_statistics.py 1 ../source_texts/frankenstein.txt > frankenstein.1gram.trv
	../collate_character_statistics.py 2 ../source_texts/frankenstein.txt > frankenstein.2gram.trv
	../collate_character_statistics.py 3 ../source_texts/frankenstein.txt > frankenstein.3gram.trv
	../collate_character_statistics.py 4 ../source_texts/frankenstein.txt > frankenstein.4gram.trv
	../collate_character_statistics.py 5 ../source_texts/frankenstein.txt > frankenstein.5gram.trv

clean:
	rm *.trv
