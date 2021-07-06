import csv
import sys

inFile = sys.argv[1]

original_stdout = sys.stdout # Save a reference to the original standard output

class SongInfo:
  def __init__(self, shortname,name,artist,master,p2type,songTracks,guitarTracks,player2Tracks,songPan,guitarPan,player2Pan,songVolume,guitarVolume,player2Volume,songCores,guitarCores,player2Cores,hopoThresh,animTempo,prevStart,prevEnd,bandBass,bandCenter,tracksRhythmSong,tracksRhythmGuitar,tracksRhythmPlayer2,songRhythmPan,guitarRhythmPan,player2RhythmPan,songRhythmVolume,guitarRhythmVolume,player2RhythmVolume,songRhythmCores,guitarRhythmCores,player2RhythmCores):
    self.shortname = shortname
    self.name=name
    self.artist=artist
    if master == "TRUE":
        self.master = True
    else:
        self.master = False
    self.p2type=p2type
    try:
        self.songTracks=int(songTracks)
        self.guitarTracks=int(guitarTracks)
        self.player2Tracks=int(player2Tracks)
    except:
        self.songTracks=songTracks
        self.guitarTracks=guitarTracks
        self.player2Tracks=player2Tracks
    self.songPan=songPan
    self.guitarPan=guitarPan
    self.player2Pan=player2Pan
    self.songVolume=songVolume
    self.guitarVolume=guitarVolume
    self.player2Volume=player2Volume
    self.songCores=songCores
    self.guitarCores=guitarCores
    self.player2Cores=player2Cores
    try:
        self.hopoThresh=int(hopoThresh)
    except:
        self.hopoThresh=hopoThresh
    self.animTempo=animTempo
    self.prevStart=prevStart
    self.prevEnd=prevEnd
    if bandBass.lower() == "yes" or bandBass == "":
        self.bandBass="metal_bass"
    else:
        self.bandBass=False
    if bandCenter.lower() == "female":
        self.bandCenter = "female_singer"
    elif bandCenter.lower() == "keys":
        self.bandCenter = "metal_keyboard"
    else:
        self.bandCenter = "metal_singer"
    try:
        self.songRhythmTracks=int(tracksRhythmSong)
        self.guitarRhythmTracks=int(tracksRhythmGuitar)
        self.player2RhythmTracks=int(tracksRhythmPlayer2)
    except:
        self.songRhythmTracks=tracksRhythmSong
        self.guitarRhythmTracks=tracksRhythmGuitar
        self.player2RhythmTracks=tracksRhythmPlayer2
    self.songRhythmPan=songRhythmPan
    self.guitarRhythmPan=guitarRhythmPan
    self.player2RhythmPan=player2RhythmPan
    self.songRhythmVolume=songRhythmVolume
    self.guitarRhythmVolume=guitarRhythmVolume
    self.player2RhythmVolume=player2RhythmVolume
    self.songRhythmCores=songRhythmCores
    self.guitarRhythmCores=guitarRhythmCores
    self.player2RhythmCores=player2RhythmCores
    
def addQ(x): #Add quotations to strings
    x = "\""+x+"\")"
    return x

def closeSong():
    print(")")

def createBand(y):
    if y.bandBass == "metal_bass" and y.bandCenter == "metal_singer":
        return
    else:
        if y.bandBass == False:
            bandString = "metal_drummer "+y.bandCenter
        else:
            bandString = y.bandBass+" metal_drummer "+y.bandCenter
        print("   (band "+bandString.strip()+")")

def hopoCheck(y):
    if y.hopoThresh == 170:
        print("     (midi_file   songs/"+y.shortname+"/"+y.shortname+".mid))")
    else:
        print("     (midi_file   songs/"+y.shortname+"/"+y.shortname+".mid)")
        print("     (hopo_threshold "+str(y.hopoThresh)+"))")
    return

def isMaster(y): #check if a song is a master, and print the caption if true
    if y.master == True:
        print("   (caption performed_by)")
    return

def songBlock(y): #Create the "song" portion of the package. Also adds rhythm data if present.
    print("   (song ")
    print("     (name        songs/"+y.shortname+"/"+y.shortname+")")
    trackCount = y.songTracks - 1
    if y.p2type.lower() == "bass":
        gtrString = trackString(y.guitarTracks)
        bassString = trackString(y.player2Tracks)
        for x in range(0,y.guitarTracks):
            trackCount += 1
            gtrString = gtrString + str(trackCount)
            if x != y.guitarTracks - 1:
                gtrString = gtrString + " "
        for x in range(0,y.player2Tracks):
            trackCount += 1
            bassString = bassString + str(trackCount)
            if x != y.player2Tracks - 1:
                bassString = bassString + " "
        if y.player2Tracks > 1:
            bassString = bassString + ")"
        print("     (tracks      ((guitar "+gtrString+")) ("+y.p2type.lower()+" "+bassString+")))")
        print("     (pans        ("+y.songPan+y.guitarPan+y.player2Pan.strip()+"))")
        print("     (vols        ("+y.songVolume+y.guitarVolume+y.player2Volume.strip()+"))")
        print("     (cores       ("+y.songCores+y.guitarCores+y.player2Cores.strip()+"))")
        hopoCheck(y)
    else:
        gtrString = trackString(y.guitarTracks)
        rhythmString = trackString(y.player2Tracks)
        for x in range(0,y.guitarTracks):
            trackCount += 1
            gtrString = gtrString + str(trackCount)
            if x != y.guitarTracks - 1:
                gtrString = gtrString + " "
        for x in range(0,y.player2Tracks):
            trackCount += 1
            rhythmString = rhythmString + str(trackCount)
            if x != y.player2Tracks - 1:
                rhythmString = rhythmString + " "
        if y.player2Tracks > 1:
            rhythmString = rhythmString + ")"
        if y.player2Tracks > 0:
            print("     (tracks      ((guitar "+gtrString+")) ("+y.p2type.lower()+" "+rhythmString+")))")
            print("     (pans        ("+y.songPan+y.guitarPan+y.player2Pan.strip()+"))")
            print("     (vols        ("+y.songVolume+y.guitarVolume+y.player2Volume.strip()+"))")
            print("     (cores       ("+y.songCores+y.guitarCores+y.player2Cores.strip()+"))")
        else:
            print("     (tracks      ((guitar "+gtrString+"))))")
            print("     (pans        ("+y.songPan+y.guitarPan.strip()+"))")
            print("     (vols        ("+y.songVolume+y.guitarVolume.strip()+"))")
            print("     (cores       ("+y.songCores+y.guitarCores.strip()+"))")
        hopoCheck(y)
        print("   (song_coop ")
        print("     (name        songs/"+y.shortname+"/"+y.shortname+"_coop)")
        trackCount = y.songRhythmTracks - 1
        gtrString = trackString(y.guitarRhythmTracks)
        rhythmString = trackString(y.player2RhythmTracks)
        for x in range(0,y.guitarRhythmTracks):
            trackCount += 1
            gtrString = gtrString + str(trackCount)
            if x != y.guitarRhythmTracks - 1:
                gtrString = gtrString + " "
        for x in range(0,y.player2RhythmTracks):
            trackCount += 1
            rhythmString = rhythmString + str(trackCount)
            if x != y.player2RhythmTracks - 1:
                rhythmString = rhythmString + " "
        if y.player2RhythmTracks > 1:
            rhythmString = rhythmString + ")"
        print("     (tracks      ((guitar "+gtrString+")) ("+y.p2type.lower()+" "+rhythmString+")))")
        print("     (pans        ("+y.songRhythmPan+y.guitarRhythmPan+y.player2RhythmPan.strip()+"))")
        print("     (vols        ("+y.songRhythmVolume+y.guitarRhythmVolume+y.player2RhythmVolume.strip()+"))")
        print("     (cores       ("+y.songRhythmCores+y.guitarRhythmCores+y.player2RhythmCores.strip()+"))")
        hopoCheck(y)
    return

def trackString(songTracks):
    if songTracks > 1:
        songString = "("
    else:
        songString = ""
    return songString

def createDTA(y): #Function to create nice looking .dta Files. y is the song class.
    print("("+y.shortname)
    print("   (name "+addQ(y.name))
    print("   (artist "+addQ(y.artist))
    isMaster(y)
    songBlock(y)
    print("   (anim_tempo "+y.animTempo+")")
    print("   (preview "+y.prevStart+" "+y.prevEnd+")")
    createBand(y)
    closeSong()
    return

with open ("songs.dta","w") as f:
    sys.stdout = f
    with open(inFile,"r") as songs:
        songs_reader = csv.reader(songs, delimiter='\t')
        next(songs_reader)
        next(songs_reader)
        for song in songs_reader:
            s = SongInfo(*song) #s is short for song
            if not str(s.songTracks).isnumeric():
                continue
            else:
                createDTA(s)
    songs.close()
    sys.stdout = original_stdout # Reset the standard output to its original value
    
f.close()