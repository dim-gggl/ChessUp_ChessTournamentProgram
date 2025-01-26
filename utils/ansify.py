def ansify(text):
    """
    Replaces any occurrence of style(arg) in 'text'
    with the ANSI sequence defined in 'styles'.
    """

    styles = {
        "ttl_blu": "1;94",  # Title Blue
        "it_ttl": "3;94",  # Italic Title
        "disc_it": "2;3",  # Discreet Italic
        "ch_up": "1;38;5;202",  # "Chess-Up Orange"
        "rpt_gr": "1;38;5;118",  # Report green theme
        "b_blue": "1;96",  # Tournament Bright Blue
        "it_b_blue": "1;3;96",  # Tournament Bright Blue + italic
        "disc_b_blue": "2;3;96",  # Tournament Bright Blue Faded
        "red_err": "1;91",  # Red Error Message
        "bld": "1",  # Bold
        "bld_it": "1;3",  # Bold + Italic
        "blnk_": "5",  # Blinking
        "gld": "1;93",  # Gold
        "gldn": "1;38;5;226",  # Gold "Champion Style"
        "whte": "1;97",  # White
        "it_whte": "3;97", # Italic + White
        "fade_": "38;5;243",  # fading Grey
        "pnk": "1;95",  # Pink
        "disc_pnk": "2;95",  # Discreet Pink
        "it_pnk": "3;95",  # Italic Pink
        "disc_it_pnk": "2;3;95",  # Discreet italic pink
        "cppr": "1;38;5;208"  # Bright Copper Orange
    }

    i = 0
    result = ""
    length = len(text)

    while i < length:

        if text[i].isalpha() or text[i] == "_":
            start_style = i
            while i < length and (text[i].isalpha() or text[i] == "_"):
                i += 1
            style_name = text[start_style:i]

            if i < length and text[i] == "(":
                i += 1
                start_arg = i
                while i < length and text[i] != ")":
                    i += 1
                if i >= length:
                    result += style_name + "(" + text[start_arg:]
                    break

                argument = text[start_arg:i]
                i += 1
                if style_name in styles:
                    ansi_code = styles[style_name]
                    transformed = f"\033[{ansi_code}m{argument}\033[0m"
                    result += transformed
                else:
                    result += f"{style_name}({argument})"
            else:
                result += style_name
        else:
            result += text[i]
            i += 1

    return result
