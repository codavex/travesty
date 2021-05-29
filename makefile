SUBDIRS := $(wildcard */.)

all: $(SUBDIRS)
$(SUBDIRS):
	cd $@ && $(MAKE)

.PHONY: all $(SUBDIRS)
