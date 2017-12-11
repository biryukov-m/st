def title_case(title, minor_words=''):
    if len(title) < 1:
        return ''
    out = []
    mw = minor_words
    for word in title.split():
        if word.lower() in mw:
            out.append(word)
            continue
        out.append(word.capitalize())
    out[0] = out[0].capitalize()
    return ' '.join(out)

title_case('a clash of KINGS', 'a an the of')
title_case('a clash of KINGS')
