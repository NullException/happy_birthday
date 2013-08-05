#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
__author__ = 'nullexception'
import sys
import time

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses

        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False


has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
    if has_colours:
        seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
        sys.stdout.write(seq)
    else:
        sys.stdout.write(text)

lett_hb = """
                         _     _  _
                        | |__ | || |  _ __  _ __  _   _
                        | '_ \| || |_| '_ \| '_ \| | | |
                        | | | |__   _| |_) | |_) | |_| |
                        |_| |_|  |_| | .__/| .__/ \__, |
                                     |_|   |_|    |___/
                  ___ ___ ____  _____ _     ____  _  ___   ___
                 ( _ )_ _|  _ \|___  | |__ |  _ \| || \ \ / / |
                 / _ \| || |_) |  / /| '_ \| | | | || |\ V /| |
                | (_) | ||  _ <  / / | | | | |_| |__   _| | |_|
                 \___/___|_| \_\/_/  |_| |_|____/   |_| |_| (_)


"""
rus_text = """
Уверенно иди по жизни!
Снеси любую стену, вставшую на пути! Если нет пути — проложи его!
И пусть всегда магма раскаляет твое сердце!
Живи, раздавая пинки здравому смыслу!
И тогда ты пронзишь небеса!
Удачи!
С днем рождения!
"""

gurren_symbol = """

                                                                  N
                                                                  M ..
                                                                .7$M.
                                                                 M$M=.
                                                                .MZ$MM
                                                               . MM$$ZM..
                                                             .M...MM$$$MM..
                                                      + .     .M..7MM$$ZNM+,.     ..
                                                      ,M      ZM.. ,MM$7$$MM.     .M
                                                      ZM     .M$....,MM$$$$MM.    .M
                                                    . MM   ..M$O..  ..MM$$$$MM....MM~ .
                                                    .Z$M.  DM$$M..   .$MN$$$$MM...MZM..
                            ...                  ...M$$M  7M$$$M..    .MM$$$$8M~..M$M..                       . .
                             M.                 ..7M$$DM. M8$$$M..     MM$$$$7MM..M$OM.                       ,M.
                            .MM              ....MM$$$M   MO$$$M..    .MM7$$$$MM. $O$M.                     ..MM.
                           ..MM              ..MMZ$$$MN.  MM$$$MMO ...ZMM$$$$ZM,...M$8M .                   .DMM.
                            .NN$           ..MMMZ$$$MM..  IMN$$$NMMMMMMM$$$$$MM. ..M8$MM...                 .M$M..
                            M$$M           ,MM8$$$$ZM... . MNN$$$$$$Z$$Z$$$$$M..  . M$ZMM..                 .M$M...
                           .M$$M          $MM$$$$$$MM...   ..MM$$$$$$$$$$$$OM?..   .MM$$MM.                 .M$7M.
                           M$$$M         NMM$$$$$$MM         .NMO$$$$$$$$$OMM.     .MM$$$DMM..              .M$$M..
                          =M$$O?        OMM$$$$$$$MM          .MNM$$$$$$$$MM~      .$MN$$$7MM.              .M$$$M.
                        ..M$$$M.        MM7$$$$$$$MM.           MMD$$$$$$$MM.      .8MN$$$$$MM..            .M$$$NM
                        .M$$$$M .      7MM$$$$$$$$MM           .MMM$$$$$$$MMM      .MM$$$$$$NMM             ..M$$$MN
                        MM$$$8M        MMM$$$$$$$$MMM. .       .MMM$$$$$$$$MMM8...+MMN$$$$$$$MMN.           ..M$$$$M$..
                       +M$$$$M.        MMM$$$$$$$$OMMM  .    . MMMM$$$$$$$$7MNMMMMMMN$$$$$$$$NMM .          ..MN$$$DM..
                     .,M$$$$$M.        OMM$$$$$$$$$$MMMMZ....MMMMMN$$$$$$$$$$$$ODO$$$$$$$$$$$ZMM .   ..       .M$$$$NM.
                    ..MM$$$$M..        .MM$$$$$$$$$$$MMMMMMMMMMMNM$$$$$$$$$$$$$$$$$$$$$$$$$$$$MM  . .D.       .MN$$$$MM.
                    .7M$$$$$M..         MMD$$$$$$$$$$$7MMMMMMMMMN$$$$$$$$$$$$$$$$$$$$$$$$$$$$ZMM  M?M .        ,M$$$$8M..
                     MO$$$$DM..    M+.  .MM$$$$$$$$$$$$$$$ZNNO$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$MMM=.,,           .M$$$$$MM..
                    ~M$$$$$M+..    ..MMMZ.MM7$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$M~...M             .MM$$$$$M..
                    MN$$$$$M.       .  M.,MMMO$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ZN=.. .::.             .DM$$$$$M+.
                   .M$$$$$NM             M....MMM$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NM.. . ..M                .,M$$$$$NM.
                 ..MM$$$$$MM              .M.    .:MMM$$$$$$$$$$$$$$$$$$$$$$$$$$$8MM.      .M                   .M$$$$$$M.
                 . MM$$$$$MM                .M.     ...MMM8$$$$$$$$$$$$$$$$$77MMO...     . M                   ..M$$$$$$MM
                 ..M8$$$$$MM.                .MM....     . MMMM$$$$$$$$$$$ZMM8         ..MMM           ..       .M$$$$$$MM
                 ..M$$$$$$MM.               ..7MMD..       ....NMMMZ$$$8MMM..        . $M7MM           .I      ..M$$$$$$MM..
                 .=M$$$$$$MM       M.      . MMZ$$MZ ...    .......MMMMM?....       ..MZ$$$MM.          N.     .~M7$$$$$NM.
                 .IM$$$$$$8M       M.     .MMN$$$$$$M=..          .  ...           .8M$$$$$$MMM.       .MM .    NM$$$$$$NM .
                 .IM$$$$$$$M:      M$.    .MM$$$$$$$$ZM.                          .NN$$$$$$$$MM.       .MM .    MM$$$$$$NM
                 .:MO$$$$$$MM..  .~ZM.    .:MM$$$$$$$$7DM..       .DMZOMM....   .MM$$$$$$$$$NMI      ...MM..   .M7$$$$$$MM .
                 ..MM$$$$$$$M..  .?ZM.    . :MM$$$$$$$$$$MM .   .MM$$$Z$$MM.. .=MD$$$$$$$$$$MM..     ..MZM.   .ZM$$$$$$$MM
                   MM$$$$$$$MM.   =O$M .     +MM$$$$$$$$$$7MM..MM$$$MMMN$$$NMMMM$$$$$$$$$$$MM.    ,  ..M$M...  MZ$$$$$$$MM
                   MM$$$$$$$7M.   .M$M,   ?  ..MM$$$$$$$$$$$OMM7$$ZN....M$$$$O$$$$$$$$$$$$MM..    M  .MZ$M....MM$$$$$$$8M.
                   .MN$$$$$$$NM....M$$M8..M..   MM7$8MMMMD$$$$$$$$M..Z...M$$$$$$MMMMMM$8MNM   ...7M..MM$$M...:M$$$$$$$$MM.
                    MM$$$$$$$$NM...M7$OMMMMM?.  .NMMMO..NMM$$$$$$$MMN$$MMM$$$$$$MM....MM7..   ..MMMMMM$$NN..~M$$$$$$$$ZM..
                     MM$$$$$$$$NM..MM$$$$$$$$M........ . MM7$$$$$$$$$$$$$$$$$$$$MM..  ..... . MM$$$$$$$$M..OM7$$$$$$$$M7.
                    ..MM$$$$$$$$$M8.MN$$$$$$$MM.       .=MM$$$$$$$$$$$$$$$$$$$$$MM..        .DMM$$$$$$$MM.MM$$$$$$$$$MM.
                    ...MNZ$$$$$$$$MMMM$$$$$MMD...     .MN$$$$$$8M8$$$$$$$MMO$$$$$8MO.        ,7MMM$$$$DM=MD$$$$$$$$$MN..
                        MN$$$$$$$$$ZMMM$$$$MM           M$$$$MMMMMN$$$$$NMMMMO$$$$ZM.         ..MM$$$8MMM7$$$$$$$$$MO..
                        .$M7$$$$$$$$78MM$$$DM..        ..MMMNMM..M7$$$$$$M..+M$$$MM.          .+M$$$$MM$$$$$$$$$$MM...
                           MM$$$$$$$$$$$N$$$DM...  M .   .  :$Z OMM7$$$7NMD .MMM7...   ..=. ..$N$$$ZM$$$$$$$$$$$M:.
                           ..MM$$$$$$$$$$$$$$$MO...NMM..        . ,MMMMM,.           ..MM....MM$$$$$$$$$$$$Z$OMN...
                             ..:NMZ$$$$$$$$$$$$OMMMMMZMM...                        ..MNMMM,MM$$$$$$$$$$$$$NMM.
                               ...,MMN$$$$$$$$$$$ZMMM$$$M..                       .NM$$NMMM$$$$$$$$$$ZZMMM..
                               .  ....NMMM8$$$$$$$$$$$$$ZMM....                 ..MN$$$$$$$$$$$$$$NMMMO . .
                                      .  .,MMMMO7$$$$$$$$ZNM..                  .M$$$$$$$$$$$NMMMM...
                                         .......ZMMM$$$$$$$MM..               . M$$$$$$$8MMM$........
                                                   .:MMN$$$$NN.             ...M$$$$$MMN...
                                                    .. .MM$$$M+.             .M$$$MM:.. .
                                                           MM$M...          .OO$M?..
                                                           ..M$D..          .MM8....
                                                              ZM .         . M .
                                                               =            M.
"""

printout(lett_hb, WHITE)
time.sleep(1)
printout(rus_text, GREEN)
time.sleep(10)
printout(gurren_symbol, RED)
