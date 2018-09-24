from bs4 import BeautifulSoup as Soup
import requests
import re


with open('naatp_final_information.txt', 'a') as w:
    with open('naatp_urlsfinal.txt', 'r', encoding='utf-8-sig') as r:

        for i in r.readlines():
            page = requests.get(i, headers={'User-Agent':'test'})
            soup = Soup(page.content)
            #print(soup)
            a = soup.find_all('div', {'class': ['views-field views-field-postal-code', 'views-field views-field-phone',
                                                'views - field views - field - email','views-field views-field-url',
                                                'views-field views-field-display-name-1','views-field views-field-ceo-77',
                                                'views-field views-field-ceo-email-80', 'views-field views-field-ceo-phone-78',
                                                'views-field views-field-admissions-contact-69', 'views-field views-field-admissions-email-72',
                                                'views-field views-field-admissions-phone-70', 'views-field views-field-marketing-contact-73',
                                                'views-field views-field-marketing-email-76', 'views-field views-field-marketing-phone-74',
                                                'views-field views-field-membership-type', 'views-field views-field-organization-description-11',
                                                'views-field views-field-mission-statement-21', 'views-field views-field-licensed-31',
                                                'views-field views-field-licensing-body-32', 'views-field views-field-accreditation-35',
                                                'views-field views-field-levels-of-treatment-care-25', 'views-field views-field-specialty-programs-30'
                                                'views-field views-field-length-of-stay-26', 'views-field views-field-number-of-beds-23',
                                                'views-field views-field-payments-accepted-27', 'views-field views-field-payment-assistance-available-28']})

            aux = {'Mailing Address': 0, 'Phone': 1, 'Website': 2, 'Facility Of': 3, 'CEO': 4, 'CEO Email': 5, 'CEO Phone': 6, 'Admissions': 7, 'Admissions Email': 8, 'Admissions Phone': 9, 'Marketing Contact': 10, 'Marketing Email': 11, 'Marketing Phone': 12, 'Membership Type': 13, 'About This Organization': 14, 'Mission Statement': 15, 'Licensed': 16, 'Licensing body': 17, 'Accreditation': 18, 'Levels of Treatment Care': 19, 'Number of Beds': 20, 'Payments Accepted': 21, 'Payment Assistance Available': 22}

            final = ['Cannot Find Data' for i in range(len(aux))]
            for j in a:
                final[aux[(j.get_text().strip().split(':')[0])]] = (''.join(j.get_text().strip().split(':')[1:]).strip()).replace('\n', ' ')

            #print(final)
            final = '~'.join(final)

            print(final)
            #w.write(final + '\n')



