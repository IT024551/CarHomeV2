LDFLAGS=-lmosquitto -liw -lbluetooth
CFLAGS=-g -O0

.PHONY: all install uninstall clean

all : btclient

btclient: btclient.o config.o blue.o tprintf.o

clean : 
	-rm -f *.o btclient
##
btclient.o: btclient.c config.h btclient.h blue.h
config.o: config.c btclient.h config.h
blue.o: blue.c blue.h
tprintf.o: tprintf.c
