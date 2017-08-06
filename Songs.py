import MusicNotes
import winsound


def cMajchord():
    MusicNotes.cnote()
    MusicNotes.enote()
    MusicNotes.gnote()


def eMinchord():
    MusicNotes.enote()
    MusicNotes.gnote()
    MusicNotes.bnote()


def Song1():
    cnt = 0
    while(cnt < 5):
        cnt += 1
        cMajchord()
        eMinchord()


def Song2():
    MusicNotes.enote()
    MusicNotes.dnote()
    MusicNotes.cnote()
    MusicNotes.dnote()
    MusicNotes.enote()
    MusicNotes.enote()
    Freq = 1318
    Dur = 800
    winsound.Beep(Freq, Dur)
    MusicNotes.dnote()
    MusicNotes.dnote()
    Freq = 1174
    Dur = 800
    winsound.Beep(Freq, Dur)
    MusicNotes.enote()
    MusicNotes.gnote()
    Freq = 1568
    Dur = 800
    winsound.Beep(Freq, Dur)


def Mario():
    # First section
    MusicNotes.hcnote()
    MusicNotes.gnote()
    MusicNotes.enote()
    MusicNotes.anote()
    MusicNotes.sbnote()
    MusicNotes.sbflatnote()
    MusicNotes.anote()
    MusicNotes.sgnote()
    MusicNotes.shenote()
    MusicNotes.shgnote()
    MusicNotes.hanote()
    MusicNotes.shfnote()
    MusicNotes.shgnote()
    MusicNotes.henote()
    MusicNotes.shcnote()
    MusicNotes.shdnote()
    MusicNotes.lbnote()

    # repeat of first section
    MusicNotes.hcnote()
    MusicNotes.gnote()
    MusicNotes.enote()
    MusicNotes.anote()
    MusicNotes.sbnote()
    MusicNotes.sbflatnote()
    MusicNotes.anote()
    MusicNotes.sgnote()
    MusicNotes.shenote()
    MusicNotes.shgnote()
    MusicNotes.hanote()
    MusicNotes.shfnote()
    MusicNotes.shgnote()
    MusicNotes.henote()
    MusicNotes.shcnote()
    MusicNotes.shdnote()
    MusicNotes.lbnote()

    # Next section

    MusicNotes.shgnote()
    MusicNotes.shfsharpnote()
    MusicNotes.shfnote()
    MusicNotes.shdsharpnote()
    MusicNotes.shenote()
    MusicNotes.sgsharpnote()
    MusicNotes.sanote()
    MusicNotes.shcnote()
    MusicNotes.sanote()
    MusicNotes.shcnote()
    MusicNotes.sdnote()

    MusicNotes.shgnote()
    MusicNotes.shfsharpnote()
    MusicNotes.shfnote()
    MusicNotes.shdsharpnote()
    MusicNotes.shenote()

    MusicNotes.hhcnote()
    MusicNotes.shhcnote()
    MusicNotes.shhcnote()
