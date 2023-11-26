def extract_states(productions): #ini cuma buat mastiin apakah states yang ditulis di txt udah semua
    states = set()
    for state, transitions in productions.items():
        realstate = state[0]
        if realstate not in states:
            states.add(realstate)

    html_tags = [
    "INIT","HTML", "XHTML", "CHTML",
    "HEAD", "XHEAD", "CHEAD",
    "TITLE", "XTITLE",
    "SCRIPT", "XSCRIPT", "CSCRIPT",
    "LINK", "CLINK", "REL",
    "BODY", "XBODY", "CBODY",
    "H1", "XH1", "CH1",
    "H2", "XH2", "CH2",
    "H3", "XH3", "CH3",
    "H4", "XH4", "CH4",
    "H5", "XH5", "CH5",
    "H6", "XH6", "CH6",
    "P", "XP", "CP",
    "BR", "CBR",
    "EM", "XEM", "CEM",
    "B", "XB", "CB",
    "ABBR", "XABBR", "CABBR",
    "STRONG", "XSTRONG", "CSTRONG",
    "SMALL", "XSMALL", "CSMALL",
    "HR", "CHR",
    "DIV", "XDIV", "CDIV",
    "A", "XA", "CA",
    "IMG", "CIMG", "SRC",
    "BUTTON", "XBUTTON", "CBUTTON", "TYPE",
    "FORM", "XFORM", "CFORM", "METHOD",
    "INPUT", "CINPUT",
    "TABLE", "XTABLE", "CTABLE",
    "TR", "XTR", "CTR",
    "TH", "XTH", "CTH",
    "TD", "XTD", "CTD"]

    print (len(html_tags))
    count = 0
    for state in states:
        if state not in html_tags:
            print (state)
        else:
            count += 1
    for html_tag in html_tags:
        if html_tag not in states:
            print (html_tag)
    print (count)
    return states