def journal_article_form(request):
    print('JOURNAL ARTICLE - ' + str(request))

    r = request

    reference_string = r['author_surname'] + ', ' + r['author_initial1'] + '.' + r['author_initial2'] + '. '
    reference_string += r['article_name'] + ' / '
    reference_string += r['author_initial1'] + '.' + r['author_initial2'] + '. ' + r['author_surname']
    reference_string += '. // ' + r['journal_name'] + '. – ' + r['publishing_year'] + '. – № ' + r['journal_number'] + '.'

    try:
        first_page = r['first_page']
    except Exception:
        first_page = None
        print("fp var doesn't exist")

    try:
        last_page = r['last_page']
    except Exception:
        last_page = None
        print("lp var doesn't exist")

    if (first_page != None and last_page == None):
        reference_string += ' – C. ' + first_page + '.'
    if (first_page == None and last_page != None):
        reference_string += ' – C. ' + last_page + '.'
    if (first_page != None and last_page != None):
        reference_string += ' – C. ' + first_page + '–' + last_page + '.'

    return(reference_string)

def book_1_author_form(request):
    print('BOOK_1_AUTHOR - ' + str(request))

    r = request

    reference_string = r['author_surname'] + ', ' + r['author_initial1'] + '.' + r['author_initial2'] + '. '
    reference_string += r['book_name'] + ' / '
    reference_string += r['author_initial1'] + '.' + r['author_initial2'] + '. ' + r['author_surname'] + '.'
    reference_string += ' – ' + r['edition_number'] + '-е изд. – ' + r['publishing_locality'] + ': '
    reference_string += r['publishing_house'] + ', ' + r['publishing_year'] + '. – ' + r['pages_count'] + ' с.'

    return(reference_string)

