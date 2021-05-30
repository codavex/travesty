macbeth = macbeth.1ch.txt
frankenstein = frankenstein.1ch.txt

all: $(macbeth) $(frankenstein)

$(macbeth): ../source_texts/macbeth.txt ../collate_character_statistics.py
	../collate_character_statistics.py 1 ../source_texts/macbeth.txt > macbeth.1ch.trv
	../collate_character_statistics.py 2 ../source_texts/macbeth.txt > macbeth.2ch.trv
	../collate_character_statistics.py 3 ../source_texts/macbeth.txt > macbeth.3ch.trv
	../collate_character_statistics.py 4 ../source_texts/macbeth.txt > macbeth.4ch.trv

$(frankenstein): ../source_texts/frankenstein.txt ../collate_character_statistics.py
	../collate_character_statistics.py 1 ../source_texts/frankenstein.txt > frankenstein.1ch.trv
	../collate_character_statistics.py 2 ../source_texts/frankenstein.txt > frankenstein.2ch.trv
	../collate_character_statistics.py 3 ../source_texts/frankenstein.txt > frankenstein.3ch.trv
	../collate_character_statistics.py 4 ../source_texts/frankenstein.txt > frankenstein.4ch.trv

clean:
	rm *.trv
