def journal_article_form(request):
    print('JOURNAL ARTICLE - ' + str(request))

    r = request

    reference_string = r['author_surname'] + ', ' + r['author_initial1'] + '.' + r['author_initial2'] + '. '
    reference_string += r['article_name'] + ' / '
    reference_string += r['author_initial1'] + '.' + r['author_initial2'] + '. ' + r['author_surname']
    reference_string += '. // ' + r['journal_name'] + '. – ' + r['publishing_year'] + '. – № ' + r['journal_number'] + '.'

    return(reference_string)
