# -*- coding: utf-8 -*-
# Signature Checker
# Developer. Nevaland
# Data. 19.03.17 - 19.03.18
# Version. 1
# Problem. Signature Overlap -> Color Problem
# Wav, Ani, doc, ppt, hwp, etc Signature needs to add
# SIGNATURE to External File

# COLOR SETTING --- {
from sys import platform
from random import randint
if platform.startswith('win'):
    from colorama import init
    init()
colorList = {
    'white': "\x1b[39m",
    'yellow': "\x1b[33m",
    'green': "\x1b[32m",
    'blue': "\x1b[34m",
    'cyan': "\x1b[36m",
    'red': "\x1b[31m",
    'magenta': "\x1b[35m",
    'black': "\x1b[2m",
    'darkwhite': "\x1b[37m",
    'darkyellow': "\x1b[33m",
    'darkgreen': "\x1b[32m",
    'darkblue': "\x1b[34m",
    'darkcyan': "\x1b[36m",
    'darkred': "\x1b[31m",
    'darkmagenta': "\x1b[35m",
    'darkblack': "\x1b[30m",
    'off': "\x1b[0m"
}
def cprint(data, color='white'):
    color = colorList.keys()[randint(0, len(colorList) - 1)] if color == 'rand' else color
    try:
        print '%s%s%s' % (colorList[color], data, colorList['off'])
    except KeyError:
        print '[-] Not exist color \'%s\'' % color
        print '===== sample ====='
        color_sample()
def cprint_comma(data, color='white'):
    color = colorList.keys()[randint(0, len(colorList) - 1)] if color == 'rand' else color
    try:
        print '%s%s%s' % (colorList[color], data, colorList['off']),
    except KeyError:
        print '[-] Not exist color \'%s\'' % color
        print '===== sample ====='
        color_sample()
def craw_input(data, color='white'):
    color = colorList.keys()[randint(0, len(colorList) - 1)] if color == 'rand' else color
    try:
        return raw_input('%s%s%s' % (colorList[color], data, colorList['off']))
    except KeyError:
        print '[-] Not exist color \'%s\'' % color
        print '===== sample ====='
        color_sample()
def color_sample():
    for color in colorList:
        cprint(color, color)
# COLOR SETTING END ---}

# MODULES
import sys, os

MORE = False
SIG_P = True
ROW_NUM = 65
SIGNATURE = [(['89','50','4E','47','0D','0A','1A','0A'],"PNG"),
             (['FF','D8','FF','E0'],"JPEG"),
             (['00','00','00','18','66','74','79','70'],"MP4"), # MPEG-4 Video File
             (['00','00','01','00'],"ICO"), # Graphics – Windows Icon Format
             (['00','6E','1E','F0'],"PPT"), # PowerPoint Presentation SubHeader
             (['0F','00','E8','03'],"PPT2"), # PowerPoint Presentation SubHeader (MS Office)
             (['0D','44','4F','43'],"DOC"), # DeskMate Document File
             (['31','BE','00','00','00','AB'],"DOC2"), # Word processor – MS Word 4
             (['21','42','44','4E'],"PST"), # Microsoft Outlook File
             (['25','50','44','46'],"PDF"), # Adobe Portable Document Format File
             (['37','7A','BC','AF','27','1C'],"7Z"), # Archive – 7-Zip Archive File
             (['38','42','50','53'],"PSD"), # Graphics – Adobe Photoshop File
             (['3C','3F','78','6D','6C','20','76','65'],"XUL"), # XML User Interface Language File
             (['47','49','46','38','37','61'],"GIF"), # Graphics – Graphics Interchange Format
             (['49','44','33'],"MP3"), # Sound – MPEG-1 Audio Layer 3 (MP3) Audio File
             (['50','4B','03','04'],"ZIP"), # Archive – Pkzip Archive File, DOCX, PPTX, XLSX
             (['50','4B','03','04','14','00','06','00'],"DOCX"), # Microsoft Office Open XML Format Document, PPTX, XLSX
             (['50','4B','03','04','14','00','08','00'],"JAR"), # Java Archive
             (['50','4B','4C','49','54','45'],"ZIP"), # Archive – PKLITE ZIP Archive (see also PKZIP)
             (['53','43','4D','49'],"IMG"), # Img Software Set Bitmap File
             (['D0','CF','11','E0','A1','B1','1A','E1'],"HWP") # HAANSOFT Compound Document File
             ]
sig_on_cnt = 0

def usage(program):
    print "Usage: " + program + " file_name"
def setting(op_file_name):
    # Options : "more", "sig_p"
    global MORE
    global SIG_P
    global ROW_NUM

    f = file_open(op_file_name)
    data_lst = f.read().split('\n')
    f.close()

    # MORE SET
    i = -1
    for e in data_lst:
        if "more" in e : i = data_lst.index(e)
    if i == -1:
        print "[ERROR] Doesn't Exist more in options"
        exit()
    data = data_lst[i]
    MORE = bool(int(data[data.find('-')+1:]))

    # MORE SET
    i = -1
    for e in data_lst:
        if "sig_p" in e : i = data_lst.index(e)
    if i == -1:
        print "[ERROR] Doesn't Exist more in options"
        exit()
    data = data_lst[i]
    SIG_P = bool(int(data[data.find('-')+1:]))

    # ROW_NUM SET
    i = -1
    for e in data_lst:
        if "row_num" in e : i = data_lst.index(e)
    if i == -1:
        print "[ERROR] Doesn't Exist row_num in options"
        exit()
    data = data_lst[i]
    ROW_NUM = int(data[data.find('-')+1:])
def banner():
    banner = u"""
  *--------------------*
  * Sig_Checker (ver.1)
  *-* Nevaland
  *--------------------*
  """
    cprint(banner,"yellow")

def file_open(file_name):
    if not os.path.isfile(file_name):
        print "[ERROR] Doesn't Exist " + file_name
        exit()
    f = open(file_name, 'rb')
    return f

def sig_check(data_lst, i, sig):
    for j in range(len(sig[0])):
        if sig[0][j] != data_lst[i]: return ""
        i += 1
        j += 1
    global sig_on_cnt
    sig_on_cnt = len(sig[0])
    return sig[1]

# MAIN
if __name__ == "__main__":
    # Banner Printing
    banner()

    # Usage
    if len(sys.argv) !=2:
        usage(sys.argv[0])
        exit()

    # External Options Set
    setting("options")

    # Set Target
    file_name = sys.argv[1]
    cprint("TARGET: " + file_name,"green")
    cprint("-"*ROW_NUM, "green")

    # Get Hex Value
    f = file_open(file_name)
    data_lst = list()
    i = 0
    while True:
        i += 1
        data = f.read(1)
        if data != "":
            value = str(hex(ord(data)))[2:].upper().zfill(2)
            data_lst.append(value)
        else: break
    f.close()

    # Hex View
    offset = 0
    sig_content = ""
    i = 0
    cprint_comma("[ Hex View ]\n"+str(hex(offset))[2:].upper().zfill(5), "cyan")
    for value in data_lst:
        i += 1
        # Check Signature front value
        for sig in SIGNATURE:
            if value == sig[0][0]:
                content = sig_check(data_lst, i-1, sig)
                if sig_content == "": sig_content += content
                elif content != "": sig_content += "," + content

        # Hex Data Printing
        if sig_on_cnt != 0:
            cprint_comma(value, "cyan")
            sig_on_cnt -= 1
        else: cprint_comma(value)
        # Signature Content Printing
        if i % 16 == 0:
            if sig_content != "" :
                # Sinature Pause
                cprint_comma(sig_content, "cyan")
                if SIG_P: raw_input(" (Pause)")
            else: cprint(sig_content, "cyan")
            sig_content = ""

            # More
            if i % 480 == 0 and MORE:
                if raw_input("("+str(i/480)+")") == 'q' : MORE = False

            # Offset
            offset += 16
            cprint_comma(str(hex(offset))[2:].upper().zfill(5), "cyan")
    print ""
    # End Line Printing
    cprint("-" * ROW_NUM, "cyan")
