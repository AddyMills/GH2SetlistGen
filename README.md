# GH2SetlistGen
A script to read a specialized tsv/txt file to generate the songs.dta necessary for Guitar Hero 2

Please use the spreadsheet found here: https://docs.google.com/spreadsheets/d/1ZJYcCRtjQQCHWxvZhQ2f0bRaN2VeWK7IJ4Dnb_H9EuY/edit?usp=sharing

##Song Tier List

Here you start filling out your song data.

Orange cells are required, blue cells change the game logic (eg number of songs in a setlist or the ho/po threshold for a song). All relevant cells have "notes" in the spreadsheet you can hover over to see (denoted with a black triangle in the corner of the cell)

Yellow cells are for Rhythm tracks. They are not needed to make a proper song definition if only using bass. You can define the number of tracks separate for single player/co-op for these cells

Grey cells are formulas and should not be touched, this counts for all tabs

After finishing, view the summary tab to make sure your tiers are equal

The "Song Order" column determines tier placements for the campaign

Your final encore name must have "freebird" as the shortname or your game will crash upon career completion (quickplay is fine with a changed final encore)

If using Google Sheets and you get an error after exporting, you may need to fill in all cells before export (even the yellow optional ones, you can fill them in with 0) as Sheets does not fill in zeroes if INDEX finds nothing. Exporting as an .xlsx file will circumvent the necessity to fill in all cells.

##Songs.dta tab

Copy all shortnames in "Song Tier List" to column A of the Songs.dta tab, drag down the formulas in column B onward, if needed

Export this workbook as a tab-delimited file (tsv or txt) and feed into the songsGen Python script

The Python script will generate a songs.dta ready for use in-game, you can use it by calling the script and having the tsv/txt file as the only argument eg. "GH2SetlistGen.py songlist.tsv"
If the opening and closing brackets are not equal in the dta, please make sure you filled in something for the "number of tracks" for each part

##Campaign.dta tab

Go to Campaign.dta and extend/retract the formulas to the amount of songs per tier (if you added three to each tier, totalling 6, you would extend the formulas to column H. Copy and paste this directly into your campaign.dta file (make sure to include the closing parentheses on each row!)

##Store.dta tab

Copy/paste your bonus short names into column A of the Store.dta tab and drag down the formula in Column C if needed.

The default price is 550 in-game, but feel free to change the default, or use column B to set your own price for particular songs. There are examples in the tab currently

Column C can be copy/pasted into store.dta right away under the songs section.
