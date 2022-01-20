# travesty /ˈtravɪsti/ (noun) - a false, absurd, or distorted representation of something.

This project collects statistics based on source texts.

These statistics can then be used to generate text that should have the same statistcal properties as the original text, 

Currently these statistics are character based, but I aim to add word based statistics also.

See also [travesty](https://en.wikipedia.org/wiki/Travesty) and [parody generator](https://en.wikipedia.org/wiki/Parody_generator)

## Use of scripts

To get the statistics from a source text:

  ./collate_character_statistics.py N ./source_texts/input.txt > ./statistics/output.trv

where N is the size of N-Gram used, i.e. the higher the number the more realistic the generated text.

To generate a travesty:

  ./generate_character_travesty.py 500 statistics/macbeth.5gram.trv

