from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def today_date_check(file,today_date,cero_today_date):
    first_page = []

    for page_layout in extract_pages(file, page_numbers=0, maxpages=1):
        try:
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    first_page.append(element.get_text().rstrip())
        except:
            continue

    if cero_today_date in first_page or f"Buenos Aires, {today_date}" in first_page or today_date in first_page:
        return True
    else:
        return False