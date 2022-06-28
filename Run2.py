from xml.dom.minidom import Element
from GetData import GetData
# from GetUrls import GetUrls
from bs4 import BeautifulSoup as BS
from Config import *
from write import Write


class Scrap(GetData, Write):
    def __init__(self, firstPageUrl=None):
        self.firstPageUrl = firstPageUrl
        super().__init__(None)

    """
    Here we will write a specific script for each website using the methods we wrote in other classes
    """

    def Geoc_jp(self):

        self.GetPagsUrlsByIncrement(
            69, 20, 'http://www.geoc.jp/rashinban/dantai.php?from=', 0)
        self.GetSubPagesUrlsRGXList(
            self.pagesUrls, 'dantai_detail', 'http://www.geoc.jp/rashinban/', 'tbody')

        # The Source code for scrapping that specific website
        row = int(1)
        for subpage in self.subpages:
            print(f'Org Number {row} is in process')
            self.DirectHtmlParser(subpage, 'html.parser')
            tbodyCounter = int()
            for tbody in self.parsedHtml.find_all('tbody'):
                tbodyCounter += 1
                if tbodyCounter == 2:
                    for Name in tbody.find_all('td')[1]:
                        self.row_list.append(
                            str(Name).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 1:
                        self.row_list.append('Not Found')

                    for type in tbody.find_all('td')[2]:
                        self.row_list.append(
                            str(type).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 2:
                        self.row_list.append('Not Found')

                    for phone in tbody.find_all('td')[4]:
                        self.row_list.append(
                            str(phone).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 3:
                        self.row_list.append('Not Found')

                    for a in tbody.find_all('td')[6]:
                        for mail in BS(str(a), 'html.parser'):
                            self.row_list.append(
                                str(mail.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 4:
                        self.row_list.append('Not Found')

                    for a2 in tbody.find_all('td')[7]:
                        for web1 in BS(str(a2), 'html.parser'):
                            self.row_list.append(
                                str(web1.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 5:
                        self.row_list.append('Not Found')

                    for a3 in tbody.find_all('td')[8]:
                        for web2 in BS(str(a3), 'html.parser'):
                            self.row_list.append(
                                str(web2.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 6:
                        self.row_list.append('Not Found')

                    for a4 in tbody.find_all('td')[9]:
                        for web3 in BS(str(a4), 'html.parser'):
                            self.row_list.append(
                                str(web3.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 7:
                        self.row_list.append('Not Found')

                    for a5 in tbody.find_all('td')[10]:
                        for web4 in BS(str(a5), 'html.parser'):
                            self.row_list.append(
                                str(web4.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list) < 8:
                        self.row_list.append('Not Found')

            print(f'Org Number {row} has been added')
            row += 1

            for c in range(len(self.row_list)):
                if self.row_list[c] == '' or self.row_list[c] == ' ':
                    self.row_list[c] = 'Not Found'
                print(self.row_list[c])
            print()

            self.collective_list.append(self.row_list)
            self.row_list = list()
            Name, type, phone, mail, a, a2, a3, a4, a5, web1, web2, web3, web4 = '', '', '', '', '', '', '', '', '', '', '', '', ''

        return self.collective_list

    ####################New Website here############################

    def Arab(self):

        catgLinks = dict({
            'advocacy': {
                'civil-rights': 'https://arab.org/directory/activity/civil-rights/',
                'human-rights': 'https://arab.org/directory/activity/human-rights/',
                'labor-rights': 'https://arab.org/directory/activity/labor-rights/',
                'legal-affairs': 'https://arab.org/directory/activity/legal-affairs/',
                'media': 'https://arab.org/directory/activity/media/',
                'peace': 'https://arab.org/directory/activity/peace/',
                'security': 'https://arab.org/directory/activity/security/'
            },

            'animals': {
                'animal-welfare': 'https://arab.org/directory/activity/animal-welfare/',
                'hunting': 'https://arab.org/directory/activity/hunting/',
                'wildlife-conservation': 'https://arab.org/directory/activity/wildlife-conservation/'
            },

            'development': {
                'cultural': 'https://arab.org/directory/activity/cultural/',
                'research': 'https://arab.org/directory/activity/research/',
                'social': 'https://arab.org/directory/activity/social/',
                'sports': 'https://arab.org/directory/activity/sports/',
                'sustainability': 'https://arab.org/directory/activity/sustainability/'
            },

            'education': {
                'education': 'https://arab.org/directory/activity/education/',
                'skills-development': 'https://arab.org/directory/activity/skills-development/'
            },

            'environment': {
                'bio-diversity': 'https://arab.org/directory/activity/bio-diversity/',
                'conservation-protection': 'https://arab.org/directory/activity/conservation-protection/'
            },

            'faith-Based': {
                'beliefs': 'https://arab.org/directory/activity/beliefs/',
                'ethics': 'https://arab.org/directory/activity/ethics/',
                'religious': 'https://arab.org/directory/activity/religious/'
            },

            'finance': {
                'funding': 'https://arab.org/directory/activity/funding/',
                'micro-financing': 'https://arab.org/directory/activity/micro-financing/',
                'trade': 'https://arab.org/directory/activity/trade/'
            },

            'food': {
                'agriculture': 'https://arab.org/directory/activity/agriculture/',
                'food-security': 'https://arab.org/directory/activity/food-security/',
                'hunger': 'https://arab.org/directory/activity/hunger/',
                'nutrition': 'https://arab.org/directory/activity/nutrition/'
            },

            'health': {
                'ageing': 'https://arab.org/directory/activity/ageing/',
                'disabilities': 'https://arab.org/directory/activity/disabilities/',
                'diseases-disorders': 'https://arab.org/directory/activity/diseases-disorders/',
                'medical': 'https://arab.org/directory/activity/medical/',
                'patient-support': 'https://arab.org/directory/activity/patient-support/'
            },

            'people': {
                'children': 'https://arab.org/directory/activity/children/',
                'elderly': 'https://arab.org/directory/activity/elderly/',
                'family': 'https://arab.org/directory/activity/family/',
                'human-settlements': 'https://arab.org/directory/activity/human-settlements/',
                'indigenous-people': 'https://arab.org/directory/activity/indigenous-people/',
                'population': 'https://arab.org/directory/activity/population/',
                'women': 'https://arab.org/directory/activity/women/',
                'youth': 'https://arab.org/directory/activity/youth/'
            },

            'relief': {
                'disaster': 'https://arab.org/directory/activity/disaster/',
                'humanitarian': 'https://arab.org/directory/activity/humanitarian/',
                'refugees': 'https://arab.org/directory/activity/refugees/'
            }


        })

        subCatgNums = [363, 505, 76, 191, 147, 150, 96, 42, 14, 78, 648, 445, 927, 39, 433, 860, 739, 79, 181, 21, 30,
                       103, 105, 105, 139, 90, 54, 28, 39, 16, 157, 116, 222, 241, 560, 34, 192, 60, 89, 236, 414, 683, 51, 169, 132]

        mainCatg = ['advocacy', 'animals', 'development', 'education', 'environment',
                    'faith-Based', 'finance', 'food', 'health', 'people', 'relief']

        subCatg = [['civil-rights', 'human-rights', 'labor-rights', 'legal-affairs', 'media', 'peace', 'security'],
                   ['animal-welfare', 'hunting', 'wildlife-conservation'],
                   ['cultural', 'research', 'social', 'sports', 'sustainability'],
                   ['education', 'skills-development'],
                   ['bio-diversity', 'conservation-protection'],
                   ['beliefs', 'ethics', 'religious'],
                   ['funding', 'micro-financing', 'trade'],
                   ['agriculture', 'food-security', 'hunger', 'nutrition'],
                   ['ageing', 'disabilities', 'diseases-disorders',
                    'medical', 'patient-support'],
                   ['children', 'elderly', 'family', 'human-settlements',
                    'indigenous-people', 'population', 'women', 'youth'],
                   ['disaster', 'humanitarian', 'refugees']
                   ]

        ###########################################
        # Writing the Subpages on a list
        NofPagesIndex = int()
        catgIndex = int()
        for main in mainCatg:

            # The sub Category is list of lists
            if catgIndex == len(mainCatg):
                pass
            elif catgIndex < len(mainCatg):
                catgIndex += 1

            for sub in subCatg[catgIndex-1]:
                url = str()

                # Get the first page url
                try:
                    url = catgLinks[main][sub]
                except BaseException as error:
                    print(error)
                    pass

                # Add the first url that has no number
                self.subpages.append(url)
                print(f'subpage added | {len(self.subpages)}')

                # Generating the pages number or amount
                if NofPagesIndex == 44:
                    print(catgLinks[main][sub])

                while True:
                    try:
                        num = int((subCatgNums[NofPagesIndex] / 5) + 1)
                        break
                    except IndexError as error:
                        print(error)
                        # num -= 1

                # Adding the subpages with increment numbers
                self.GetSubPagsUrlsByIncrement(
                    num, 1, f'{self.subpages[-1]}/page', 2)

                # adding the categories to the lists
                for add in range(num):
                    self.Categories.append(main)
                    self.subCategories.append(sub)

                # To follow up with the pages numbers
                NofPagesIndex += 1

        ####################################################################
        # Getting the data

        listingNumList = list()
        print(f'{len(self.subpages)} page has been added')
        for i in range(len(self.subpages)):
            if 'ageing' in self.subpages[i]:
                print(i)

            if 'children' in self.subpages[i]:
                print(i)
                break

        w = open('W:\ExtraC\Internships\Goodera\Contacts\Arab.org\Record02.txt', 'a')
        for subpage in self.subpages:

            print('############################')
            print(f"Page {self.subpages.index(subpage)} is being scrapped")
            w.write(
                f"\n\nPage {self.subpages.index(subpage)} is being scrapped\n")
            w.write(f"{str(subpage)}\n")

            print(subpage)
            print('############################')
            print()

            self.DirectHtmlParseBlocked(subpage, 'html.parser')
            PageParsedHtml = self.parsedHtml

            for org in RGX.findall('wpbdp\-listing\-\d{3,6}', self.textHtml):

                if org not in listingNumList:
                    listingNumList.append(org)
                    for div1 in PageParsedHtml.find_all('div', class_=org):

                        print(
                            f'Org ||{len(self.collective_list)}|| is being scrapped')
                        w.write(
                            f'Org ||{len(self.collective_list)}|| is being scrapped\n')
                        print()
                        # Name storing
                        for div2 in div1.find_all('div', class_='listing-title'):
                            Name = ''
                            for a in div2.find_all('a'):
                                Name = str(a.text)
                                if len(Name) > 1:
                                    self.row_list.append(Name)
                                else:
                                    self.row_list.append('Not Found')

                        # The rest of the data:
                        for dataContainer in div1.find_all('div', class_='listing-details'):
                            # Here we can loop in the title and the data itself one by one

                            phone, acronym, offName, type, website, sMedia, activity = '', '', '', '', '', '', ''

                            for data in dataContainer.find_all('div', class_='wpbdp-field-display'):

                                # Title of the data is here
                                for span in data.find_all('span', class_='field-label'):
                                    title = str(span.text).strip()

                                # if condition to catch each type of data
                                if title.startswith("Organization's Official Na"):
                                    for value in data.find_all('div', class_="value"):
                                        for a1 in value.find_all('a'):
                                            offName = str(a1.text).strip()
                                            if len(offName) > 1:
                                                self.row_list.append(offName)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                                elif title.startswith("Acrony"):
                                    for value in data.find_all('div', class_="value"):
                                        acronym = str(value.text).strip()
                                        if len(acronym) > 1:
                                            self.row_list.append(acronym)
                                        else:
                                            self.row_list.append('Not Found')

                                elif title.startswith("Typ"):
                                    for value in data.find_all('div', class_="value"):
                                        type = str(value.text).strip()
                                        if len(type) > 1:
                                            self.row_list.append(type)
                                        else:
                                            self.row_list.append('Not Found')

                                elif title.startswith("Activit"):
                                    for value in data.find_all('div', class_="value"):
                                        temp = list()
                                        for a2 in value.find_all('a'):
                                            temp.append(a2.text)
                                        for act in temp:
                                            activity = activity + \
                                                f', {act}'.strip()
                                        activity = activity[2:]
                                        temp = list()
                                        if len(activity) > 1:
                                            self.row_list.append(activity)
                                        else:
                                            self.row_list.append('Not Found')

                                elif title.startswith("Phone"):
                                    for value in data.find_all('div', class_="value"):
                                        for a3 in value.find_all('a'):
                                            phone = str(a3.text).strip()
                                            if len(phone) > 1:
                                                self.row_list.append(phone)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                                elif title.startswith("Website"):
                                    for value in data.find_all('div', class_="value"):
                                        for a4 in value.find_all('a'):
                                            website = str(
                                                a4.get('href')).strip()
                                            if len(website) > 1:
                                                self.row_list.append(website)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                                # Getting the email
                                    if len(website) > 8:
                                        try:
                                            emailList = self.GetEmailByRGXMethod(
                                                website)
                                            if len(emailList) == 0:
                                                emailList = ['Not Found']
                                                self.emailsListofLists.append(
                                                    emailList)
                                            elif emailList == self.emailsListofLists[-1]:
                                                emailList = ['Not Found']
                                                self.emailsListofLists.append(
                                                    emailList)
                                            else:
                                                self.emailsListofLists.append(
                                                    emailList)
                                                emailList = ['Not Found']

                                        except BaseException as error:
                                            print(error)
                                            self.emailsListofLists.append(
                                                ['Error'])
                                            emailList = ['Not Found']
                                    else:
                                        emailList = ['Not Found']
                                        self.emailsListofLists.append(
                                            emailList)

                                    for em in self.emailsListofLists[-1]:
                                        if str(em).startswith('fancybox') or str(em).startswith('wght') or str(em).endswith('png') or str(em).endswith('localhost') or str(em).endswith('jpj') or len(em) < 5:

                                            indx = list(
                                                self.emailsListofLists[-1]).index(em)
                                            self.emailsListofLists[-1][indx] = "Not Found"

                                elif title.startswith("Social"):
                                    for value in data.find_all('div', class_="value"):
                                        for a5 in value.find_all('a'):
                                            sMedia = str(
                                                a5.get('href')).strip()
                                            if len(sMedia) > 1:
                                                self.row_list.append(sMedia)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                            # print(Name)
                            # print(type)
                            # print(website)
                            # print(sMedia)
                            # print()

                            for c in range(len(self.row_list)):
                                if self.row_list[c] == '' or self.row_list[c] == ' ':
                                    self.row_list[c] = 'Not Found'
                                print(self.row_list[c])
                            print()

                            self.collective_list.append(self.row_list)
                            while len(self.emailsListofLists) < len(self.collective_list):
                                self.emailsListofLists.append(['Not Found'])
                            phone, acronym, offName, type, website, sMedia, activity = '', '', '', '', '', '', ''
                            div1, div2, dataContainer, data, span, a, a1, a2, a3, a4, a5, span, title = '', '', '', '', '', '', '', '', '', '', '', '', ''
                            self.row_list = list()

        # The writing part: ############

        self.writeFromListofStrings(
            self.Categories, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'Categories', "catgsData")
        self.writeFromListofStrings(
            self.subCategories, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'SubCategories', "subcatgsData")
        self.writeFromListofLists(
            self.collective_list, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'ArabOrgh', 'Data')
        self.writeFromListofLists(
            self.emailsListofLists, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'Emailsh', 'mails Lists')

    #################################################

    def npo_search(self):

        def email(string):
            r = int(string[:2], 16)
            email = ''.join([chr(int(string[i:i+2], 16) ^ r)
                             for i in range(2, len(string), 2)])
            return email

        """
        It has 104 mainpages

        """
        self.firstPageUrl = 'https://npo-search.com/k-%E7%92%B0%E5%A2%83%E3%81%AE%E4%BF%9D%E5%85%A8/%E6%9D%B1%E4%BA%AC%E9%83%BD/'
        self.pagesUrls.append(self.firstPageUrl)
        self.GetPagsUrlsByIncrement(
            105, 1, 'https://npo-search.com/k-%E7%92%B0%E5%A2%83%E3%81%AE%E4%BF%9D%E5%85%A8/%E6%9D%B1%E4%BA%AC%E9%83%BD/page', 2, '.html')

        # Getting the subpages manually
        row = int(1)
        for page in self.pagesUrls:

            print('Getting Pages html --> subpages')
            print()
            self.DirectHtmlParser(page, 'html.parser')
            # Writing thr subpages of each mainpage
            for div in self.parsedHtml.find_all('div', class_="panel-heading"):
                for a in div.find_all('a'):
                    link = a.get('href')
                    self.subpages.append(f'https://npo-search.com/{link}')

        # Getting the data
        for subpage in self.subpages:
            print(f'Org Number {row} is in process')
            self.DirectHtmlParser(subpage, 'html.parser')

            for table in self.parsedHtml.find_all('table', class_='table table-striped'):

                for Name in table.find_all('td')[0]:
                    self.row_list.append(Name[9:])
                if len(self.row_list) < 1:
                    self.row_list.append('Not Found')

                for phone in table.find_all('td')[4]:
                    self.row_list.append(phone)
                if len(self.row_list) < 2:
                    self.row_list.append('Not Found')

                for a in table.find_all('td')[6]:
                    if str(a).startswith('<a'):
                        # temp_a = self.HtmlParser(a, 'html.parser')
                        web = a.text
                        self.row_list.append(web)
                if len(self.row_list) < 3:
                    self.row_list.append('Not Found')

                for a2 in table.find_all('td')[7]:
                    # temp_a2 = self.HtmlParser(a2, 'html.parser')
                    if str(a2).startswith('<a'):
                        temp_m = email(a2.get('data-cfemail'))
                        self.row_list.append(temp_m)
                if len(self.row_list) < 4:
                    self.row_list.append('Not Found')

            print(f'Org Number {row} has been added')
            print()
            print()
            row += 1

            for c in range(len(self.row_list)):
                if self.row_list[c] == '' or self.row_list[c] == ' ':
                    self.row_list[c] = 'Not Found'
                print(self.row_list[c])
            print()

            try:
                if (self.row_list[-1] == 'Not Found' or self.row_list[-1] == '') and (self.row_list[2] != 'Not Found' or self.row_list[1] != ''):
                    self.DirectHtmlToTextOnline(self.row_list[2])
                    m = self.GetEmailByRGXMethod()
                    if len(m) > 0:
                        self.row_list.append(m[0])
                    if len(m) > 1:
                        self.row_list.append(m[1])
                    if len(m) > 2:
                        self.row_list.append(m[2])
            except BaseException as error:
                print(error)
                pass

            # zeros
            self.collective_list.append(self.row_list)
            self.row_list = list()

            Name, phone, a, temp_a, temp_m, web, a2, temp_a2, mail = '', '', '', '', '', '', '', '', ''

        return self.collective_list

    ####################New Website here############################

    def hkngo(self):
        listOfCatgs = [
            "https://www.hkngo.hk/hk/category_list/financial_aid",
            "https://www.hkngo.hk/hk/category_list/health",
            "https://www.hkngo.hk/hk/category_list/counselling",
            "https://www.hkngo.hk/hk/category_list/leisure_and_cultural",
            "https://www.hkngo.hk/hk/category_list/legal_aid",
            "https://www.hkngo.hk/hk/category_list/education",
            "https://www.hkngo.hk/hk/category_list/other_type"]

        listOfPagesNums = [3, 14, 12, 10, 1, 21, 21]

        CatgCounter = int()
        for catg in listOfCatgs:

            print(f"Category N.0{CatgCounter+1}")
            print()

            self.GetPagsUrlsByIncrementV02(
                listOfPagesNums[CatgCounter], 1, catg, 1, '?page=')
            CatgCounter += 1
        for page in self.pagesUrls:

            self.DirectHtmlParser(page)
            # for div in self.parsedHtml.find_all('div', class_="ngo_list_wrapper"):
            #     for ul in div.find_all('ul', class_="ngo_list"):
            #         for li in ul.find_all('li', class_="ngo"):
            repeated = []
            for a in self.parsedHtml.find_all('a'):
                temp_url = str(a.get('href'))
                if temp_url.startswith('https://www.hkngo.hk/hk/org'):
                    if temp_url not in self.subpages:
                        self.subpages.append(temp_url)
                        print(f"Subpage added |N.0{len(self.subpages)}")
                    else:
                        repeated.append(temp_url)
        # by finishing this last three smain loops, we would have the organizations urls in the
        # self.subpages list so we can re loop on it, and that's for all the categories

        #########################
        #########################
        NamesList = []
        TelList = []
        FaxList = []
        AddList = []
        WebList = []
        EmailList = []
        TypeList = []
        for subpage in self.subpages:
            print(f'Subpage N.0{self.subpages.index(subpage)+1} is adding')
            self.DirectHtmlParser(subpage)
            for div in self.parsedHtml.find_all('div', class_='ngo_h1_wrapper'):
                for h1 in div.find_all('h1', class_='ngo_h1'):
                    Name = h1.text
                    NamesList.append(Name)
            for ul in self.parsedHtml.find_all('ul', class_="basic_info"):
                for li in ul.find_all('li'):
                    x = li.get('class')[0]
                    if str(x).startswith('tel'):
                        if str(li.text)[5:] not in TelList:
                            TelList.append(str(li.text)[5:])
                        else:
                            TelList.append("Not Found")

                    elif str(x).startswith('fax'):
                        # x = li.get('class')[0]
                        if str(li.text)[5:] not in FaxList:
                            FaxList.append(str(li.text)[5:])
                        else:
                            FaxList.append("Not Found")
                    elif str(x).startswith('address'):
                        pass
                    elif str(x).startswith('web'):
                        for web in li.find_all("a"):
                            # x = a.get('href')[0]
                            Website = web.get('href')
                        if Website not in WebList:
                            WebList.append(Website)
                        else:
                            WebList.append("Not Found")
                    elif x.startswith('email'):
                        for mail in li.find_all("a"):
                            x = mail.get('href')[0]
                            Email = x
                        try:
                            if Email not in EmailList:
                                EmailList.append([Email])
                        except BaseException as error:
                            EmailList.append(self.GetEmailByRGXMethod(Website))
                            print(EmailList[-1])
                        else:
                            EmailList.append("Not Found")
                    elif str(x).startswith('npo'):
                        pass
            print(
                f'Subpage N.0{self.subpages.index(subpage)+1} has been added')
            print()

        print("Creating the list to write......")
        print()
        for N, T, W in zip(NamesList, TelList, WebList):
            self.row_list.append(N)
            self.row_list.append(W)
            self.row_list.append(T)
            self.collective_list.append(self.row_list)
            self.row_list = []

        self.writeFromListofLists(
            self.collective_list, "W:\ExtraC\Internships\Goodera\Contacts\Hkngo", "HkngoData", "Data")
        self.writeFromListofLists(
            EmailList, "W:\ExtraC\Internships\Goodera\Contacts\Hkngo", "HkngoEmails", "Emails")

    ####################New Website here############################

    def ngo20map(self):

        self.GetPagsUrlsByIncrementV02(
            1352, 1, 'http://www.ngo20map.com/Index/list_index?type=ngo&', 1, 'p=')

        for page in self.pagesUrls:
            print(
                f'A page is being scrapped now | N.0{self.pagesUrls.index(page)}')
            self.DirectHtmlParser(page)
            for tbody in self.parsedHtml.find_all('tbody'):
                for a in tbody.find_all('a'):
                    org = a.get('href')
                    if str(org).startswith("["):
                        org = org[0]
                    url = str(f'http://www.ngo20map.com{org}')
                    if url not in self.subpages:
                        self.subpages.append(url)
                        print(f"Url Appended | N.0{len(self.subpages)}")
                        print(url)
                        print()
            print(
                f'A page has been scrapped now | N.0{self.pagesUrls.index(page)}')
            print()

        for subpage in self.subpages:
            print(
                f'A SubPage is being scrapped now | N.0{self.subpages.index(subpage)}')
            html = self.parsedHtml
            self.DirectHtmlParser(subpage)

            if self.parsedHtml == html:
                for n in range(34):
                    self.row_list.append("Error")
            else:
                for div in self.parsedHtml.find_all('div', id="ngo-basic-info"):
                    temp = []
                    for td in div.find_all('td'):
                        x = str(td.text)

                        while x.startswith("\n") or x.endswith("\n"):
                            if x.startswith("\n"):
                                x = x[1:]
                            if x.endswith("\n"):
                                x = x[:-1]

                        if len(x) > 0:
                            self.row_list.append(x)
                        else:
                            self.row_list.append("Not Found")

            self.collective_list.append(self.row_list)
            print(self.row_list[1])
            self.row_list = []
            print(
                f'A SubPage has been scrapped now | N.0{self.subpages.index(subpage)}')
            print()

        self.writeFromListofLists(
            self.collective_list, r'W:\ExtraC\Internships\Goodera\Contacts\ngo20map',  "DataFull", "DataPure")

    ####################New Website here############################
    def minatolibra(self):

        self.DirectHtmlParser("https://www.minatolibra.jp/dantai/")

        for div in self.parsedHtml.find_all('div', class_="arconix-toggle-content"):
            Email, Name, Url, Manager = "", "", "", ""
            for tbody in div.find_all('tbody'):
                for strong in tbody.find_all('strong'):
                    Name = strong.text

                get = False
                for td in tbody.find_all('td'):
                    temp = str(td.text)
                    if get == False and temp.startswith('メール'):
                        get = True
                        continue
                    if get == True:
                        Email = str(td.text)
                        get == False
                        break

                get = False
                for td in tbody.find_all('td'):
                    temp = str(td.text)
                    if get == False and temp.startswith('サイト'):
                        get = True
                        continue
                    if get == True:
                        Url = str(td.text)
                        get == False
                        break

                get = False
                for td in tbody.find_all('td'):
                    temp = str(td.text)
                    if get == False and temp.startswith('担当'):
                        get = True
                        continue
                    if get == True:
                        Manager = str(td.text)
                        get == False
                        break
            print(Email, Name, Url, Manager)
            self.collective_list.append([Name, Email, Url, Manager])
            Email, Name, Url, Manager = "", "", "", ""
            print("################")
            print()
        self.writeFromListofLists(
            self.collective_list, 'W:\ExtraC\Internships\Goodera\Contacts\minatolibra', 'PageData', 'Data')
    ##############################

    def yamagata(self):

        with open("test.html", "r", encoding='utf-8') as f:
            self.HtmlParser(f, 'html.parser')
            # print(self.textHtml)

        x = 0
        for table in self.parsedHtml.find_all('table', class_='mdb_metadata_table'):
            for tbody in table.find_all('tbody'):
                for tr in tbody.find_all('tr'):
                    for td in tr.find_all('td'):
                        try:
                            self.row_list.append(td.text)
                            print(f"done : {x+1}")
                            x += 1
                        except:
                            self.row_list.append('error/notfound')
                            print(f"error : {x+1}")
                            x += 1
            self.collective_list.append(self.row_list)
            self.row_list = []

        self.writeFromListofLists(
            self.collective_list, 'S:\Python', 'Huaibo.xlsx', 'Data')

####################################################3

    def Algeria(self):
        self.firstPageUrl = r'https://sharek-algerie.com/ar/%d8%af%d9%84%d9%8a%d9%84-%d8%a7%d9%84%d8%ac%d9%85%d8%b9%d9%8a%d8%a7%d8%aa-%d8%a7%d9%84%d8%b4%d8%a8%d8%a7%d8%a8%d9%8a%d8%a9-%d8%a7%d9%84%d8%ac%d8%b2%d8%a7%d8%a6%d8%b1%d9%8a%d8%a9/'
        AmazBool = 'False'
        AmazList = []

        for page in range(1, 9):
            with open(f"D:\Python\Scrapping_template_Code\htmls\{page}.html", "r", encoding='utf-8') as f:
                self.HtmlParser(f, 'html.parser')

            for div in self.parsedHtml.find_all('div', class_='page padd'):
                for a in div.find_all('a', class_='card'):
                    url = a.get('href')
                    if url not in self.subpages:
                        self.subpages.append(url)
            
        for subpage in self.subpages:
            print(f'\nSubpage Num 00{self.subpages.index(subpage)}\n')
            self.DirectHtmlParser(subpage)
            Name = str('')
            for h1 in self.parsedHtml.find_all('h1', class_='name'):
                if Name != h1.text: 
                    Name = h1.text
                ######################
            for div in self.parsedHtml.find_all(class_='corp'):
                text = div.text
                if ("امازيغ" in text) or ("أمازيغ" in text) or ("سكان" in text) or ("أصل" in text) or ("تقاليد" in text) or ("زيغ" in text):
                    if ("امازيغ" in text) or ("أمازيغ" in text):
                        AmazBool = 'True Amazeg'
                    else:
                        AmazBool = 'True'
                    # AmazList.append(AmazBool)
                else:
                    AmazBool = 'False'
                    # AmazList.append(AmazBool)
                ######################
                ######################

                for a2 in div.find_all('a'):
                    if str(a2.get('href')).startswith('mailto'):
                        email = str(a2.get('href'))
            self.row_list.append([Name, email[7:], AmazBool])
            print(self.row_list)
            self.collective_list.append(self.row_list[0])
            self.row_list = []
        
        for i in self.collective_list:
            print(i)
        self.writeFromListofLists(self.collective_list, r'E:\ExtraC\Internships\Goodera\Contacts\Algeria', 'ALgeria', 'Data')

#####################################

    def medadcenter(self):

        self.GetPagsUrlsByIncrementV02(86, 1, 'https://medadcenter.org/charity/www.%20itqaan.net?page=', 0, '')
        for page in self.pagesUrls:
            print(f'Getting page || 0{self.pagesUrls.index(page)}', end='\n')
            self.DirectHtmlParser(page)
            self.textHtml
            for a in self.parsedHtml.find_all('a', class_ = "more"):
                link = a.get('href')
                if link not in self.subpages and link != '':
                    self.subpages.append(link)
                    print(link)
        
        for subpage in self.subpages:
            print(f'Getting Subpage || 0{self.subpages.index(subpage)}', end='\n')
            self.DirectHtmlParser(subpage)
            for div in self.parsedHtml.find_all('div', class_ = 'contentViewTitle'):
                Name = div.text

            for div1 in self.parsedHtml.find_all('div', class_ = 'charityPart1 clear'):
                for div2 in div1.find_all('div', class_ = 'textEffect1')[1]:
                    Country = div2
            
            for div3 in self.parsedHtml.find_all('div', class_ = 'charityPart1 clear'):
                for a2 in div3.find('a'):
                    Website = a2.get('href')
            
            self.row_list = [Name, Country, Website]
            print(self.row_list)
            self.collective_list.append(self.row_list)
            self.row_list = []

        for i in self.collective_list:
            print(f'Getting Email || 0{self.collective_list.index(i)}', end='\n\n ******************')
            self.GetEmailByRGXMethod(i[2])
            print(self.emailsList[-1][0])
        
        self.writeFromListofLists(self.collective_list, r'D:\Python\medad', 'medadcenterGolf', 'Golf')
        self.writeFromListofLists(self.emailsList, r'D:\Python\medad', 'medadcenterGolfEmails', 'Golfemails')

###################33
    def Bahrain(self):

        catgLinks = dict({
            'advocacy': {
                'human-rights': 'https://arab.org/directory/activity/human-rights/region/bahrain/',
                'labor-rights': 'https://arab.org/directory/activity/labor-rights/region/bahrain/',
                'legal-affairs': 'https://arab.org/directory/activity/legal-affairs/region/bahrain/',
                'media': 'https://arab.org/directory/activity/media/region/bahrain/',
                'civil-rights': 'https://arab.org/directory/activity/civil-rights/region/bahrain/',
                'security': 'https://arab.org/directory/activity/security/region/bahrain/'
            },

            'animals': {
                'animal-welfare': 'https://arab.org/directory/activity/animal-welfare/region/bahrain/',
                'hunting': 'https://arab.org/directory/activity/hunting/region/bahrain/',
                'wildlife-conservation': 'https://arab.org/directory/activity/wildlife-conservation/region/bahrain/'
            },

            'development': {
                'cultural': 'https://arab.org/directory/activity/cultural/region/bahrain/',
                'research': 'https://arab.org/directory/activity/research/region/bahrain/',
                'social': 'https://arab.org/directory/activity/social/region/bahrain/',
                'sports': 'https://arab.org/directory/activity/sports/region/bahrain/',
                'sustainability': 'https://arab.org/directory/activity/sustainability/region/bahrain/'
            },

            'education': {
                'education': 'https://arab.org/directory/activity/education/region/bahrain/',
                'skills-development': 'https://arab.org/directory/activity/skills-development/region/bahrain/'
            },

            'environment': {
                'conservation-protection': 'https://arab.org/directory/activity/conservation-protection/region/bahrain/'
            },

            'faith-Based': {
                'religious': 'https://arab.org/directory/activity/religious/region/bahrain/'
            },

            'finance': {
                'funding': 'https://arab.org/directory/activity/funding/region/bahrain/',
                'trade': 'https://arab.org/directory/activity/trade/region/bahrain/'
            },

            'food': {
                'food-security': 'https://arab.org/directory/activity/food-security/region/bahrain/'

            },

            'health': {
                'disabilities': 'https://arab.org/directory/activity/disabilities/region/bahrain/',
                'diseases-disorders': 'https://arab.org/directory/activity/diseases-disorders/region/bahrain/',
                'medical': 'https://arab.org/directory/activity/medical/region/bahrain/',
                'patient-support': 'https://arab.org/directory/activity/patient-support/region/bahrain/'
            },

            'people': {
                'children': 'https://arab.org/directory/activity/children/region/bahrain/',
                'elderly': 'https://arab.org/directory/activity/elderly/region/bahrain/',
                'family': 'https://arab.org/directory/activity/family/region/bahrain/',
                'human-settlements': 'https://arab.org/directory/activity/human-settlements/region/bahrain/',
                'population': 'https://arab.org/directory/activity/population/region/bahrain/',
                'women': 'https://arab.org/directory/activity/women/region/bahrain/',
                'youth': 'https://arab.org/directory/activity/youth/region/bahrain/'
            },

            'relief': {
                'disaster': 'https://arab.org/directory/activity/disaster/region/bahrain/',
                'humanitarian': 'https://arab.org/directory/activity/humanitarian/region/bahrain/'
            }


        })

        subCatgNums = [5,9,1,4,1,1,5,2,2,11,7,40,1,6,11, 1, 7, 1, 2, 1, 5,1,3,3,14,1,6,1,3,15,8,1, 1]

        mainCatg = ['advocacy', 'animals', 'development', 'education', 'environment',
                    'faith-Based', 'finance', 'food', 'health', 'people', 'relief']

        subCatg = [['civil-rights', 'human-rights', 'labor-rights', 'legal-affairs', 'media', 'peace', 'security'],
                   ['animal-welfare', 'hunting', 'wildlife-conservation'],
                   ['cultural', 'research', 'social', 'sports', 'sustainability'],
                   ['education', 'skills-development'],
                   ['bio-diversity', 'conservation-protection'],
                   ['beliefs', 'ethics', 'religious'],
                   ['funding', 'micro-financing', 'trade'],
                   ['agriculture', 'food-security', 'hunger', 'nutrition'],
                   ['ageing', 'disabilities', 'diseases-disorders',
                    'medical', 'patient-support'],
                   ['children', 'elderly', 'family', 'human-settlements',
                    'indigenous-people', 'population', 'women', 'youth'],
                   ['disaster', 'humanitarian', 'refugees']
                   ]

        ###########################################
        # Writing the Subpages on a list
        NofPagesIndex = int()
        catgIndex = int()
        for main in mainCatg:

            # The sub Category is list of lists
            if catgIndex == len(mainCatg):
                pass
            elif catgIndex < len(mainCatg):
                catgIndex += 1

            for sub in subCatg[catgIndex-1]:
                url = str()

                # Get the first page url
                try:
                    url = catgLinks[main][sub]
                except KeyError as error:
                    print(error)
                    continue

                # Add the first url that has no number
                self.pagesUrls.append(url)
                print(f'page added | {len(self.pagesUrls)}')

                # Generating the pages number or amount
                if NofPagesIndex == 32:
                    print(catgLinks[main][sub])

                while True:
                    try:
                        if (subCatgNums[NofPagesIndex]) > 5:
                            num = int((subCatgNums[NofPagesIndex] / 5) + 1)
                        else: 
                            num = 1
                        break
                    except IndexError as error:
                        print(error)
                        if NofPagesIndex > 32:
                            break
                        else:
                            pass

                # Adding the subpages with increment numbers
                self.GetSubPagsUrlsByIncrement(
                    num, 1, f'{self.pagesUrls[-1]}', 1, 'page/')

                # adding the categories to the lists
                for add in range(num):
                    self.Categories.append(main)
                    self.subCategories.append(sub)

                # To follow up with the pages numbers
                NofPagesIndex += 1

        ####################################################################
        # Getting the data

        listingNumList = list()
        print(f'{len(self.subpages)} page has been added')
        for i in range(len(self.subpages)):
            if 'ageing' in self.subpages[i]:
                print(i)

            if 'children' in self.subpages[i]:
                print(i)
                break

        w = open('D:\Python\Bahrain\Bahraian01.txt', 'a')
        for subpage in self.subpages:

            print('############################')
            print(f"Page {self.subpages.index(subpage)} is being scrapped")
            w.write(
                f"\n\nPage {self.subpages.index(subpage)} is being scrapped\n")
            w.write(f"{str(subpage)}\n")

            print(subpage)
            print('############################')
            print()

            self.DirectHtmlParseBlocked(subpage, 'html.parser')
            PageParsedHtml = self.parsedHtml

            for org in RGX.findall('wpbdp\-listing\-\d{3,6}', self.textHtml):

                if org not in listingNumList:
                    listingNumList.append(org)
                    for div1 in PageParsedHtml.find_all('div', class_=org):

                        print(
                            f'Org ||{len(self.collective_list)}|| is being scrapped')
                        w.write(
                            f'Org ||{len(self.collective_list)}|| is being scrapped\n')
                        print()
                        # Name storing
                        for div2 in div1.find_all('div', class_='listing-title'):
                            Name = ''
                            for a in div2.find_all('a'):
                                Name = str(a.text)
                                if len(Name) > 1:
                                    self.row_list.append(Name)
                                else:
                                    self.row_list.append('Not Found')

                        # The rest of the data:
                        for dataContainer in div1.find_all('div', class_='listing-details'):
                            # Here we can loop in the title and the data itself one by one

                            phone, acronym, offName, type, website, sMedia, activity = '', '', '', '', '', '', ''

                            for data in dataContainer.find_all('div', class_='wpbdp-field-display'):

                                # Title of the data is here
                                for span in data.find_all('span', class_='field-label'):
                                    title = str(span.text).strip()

                                # if condition to catch each type of data
                                if title.startswith("Organization's Official Na"):
                                    for value in data.find_all('div', class_="value"):
                                        for a1 in value.find_all('a'):
                                            offName = str(a1.text).strip()
                                            if len(offName) > 1:
                                                self.row_list.append(offName)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                                elif title.startswith("Acrony"):
                                    for value in data.find_all('div', class_="value"):
                                        acronym = str(value.text).strip()
                                        if len(acronym) > 1:
                                            self.row_list.append(acronym)
                                        else:
                                            self.row_list.append('Not Found')

                                elif title.startswith("Typ"):
                                    for value in data.find_all('div', class_="value"):
                                        type = str(value.text).strip()
                                        if len(type) > 1:
                                            self.row_list.append(type)
                                        else:
                                            self.row_list.append('Not Found')

                                elif title.startswith("Activit"):
                                    for value in data.find_all('div', class_="value"):
                                        temp = list()
                                        for a2 in value.find_all('a'):
                                            temp.append(a2.text)
                                        for act in temp:
                                            activity = activity + \
                                                f', {act}'.strip()
                                        activity = activity[2:]
                                        temp = list()
                                        if len(activity) > 1:
                                            self.row_list.append(activity)
                                        else:
                                            self.row_list.append('Not Found')

                                elif title.startswith("Phone"):
                                    for value in data.find_all('div', class_="value"):
                                        for a3 in value.find_all('a'):
                                            phone = str(a3.text).strip()
                                            if len(phone) > 1:
                                                self.row_list.append(phone)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                                elif title.startswith("Website"):
                                    for value in data.find_all('div', class_="value"):
                                        for a4 in value.find_all('a'):
                                            website = str(
                                                a4.get('href')).strip()
                                            if len(website) > 1:
                                                self.row_list.append(website)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                                # Getting the email
                                    if len(website) > 8:
                                        try:
                                            emailList = self.GetEmailByRGXMethod(
                                                website)
                                            if len(emailList) == 0:
                                                emailList = ['Not Found']
                                                self.emailsListofLists.append(
                                                    emailList)
                                            elif emailList == self.emailsListofLists[-1]:
                                                emailList = ['Not Found']
                                                self.emailsListofLists.append(
                                                    emailList)
                                            else:
                                                self.emailsListofLists.append(
                                                    emailList)
                                                emailList = ['Not Found']

                                        except BaseException as error:
                                            print(error)
                                            self.emailsListofLists.append(
                                                ['Error'])
                                            emailList = ['Not Found']
                                    else:
                                        emailList = ['Not Found']
                                        self.emailsListofLists.append(
                                            emailList)

                                    for em in self.emailsListofLists[-1]:
                                        if str(em).startswith('fancybox') or str(em).startswith('wght') or str(em).endswith('png') or str(em).endswith('localhost') or str(em).endswith('jpj') or len(em) < 5:

                                            indx = list(
                                                self.emailsListofLists[-1]).index(em)
                                            self.emailsListofLists[-1][indx] = "Not Found"

                                elif title.startswith("Social"):
                                    for value in data.find_all('div', class_="value"):
                                        for a5 in value.find_all('a'):
                                            sMedia = str(
                                                a5.get('href')).strip()
                                            if len(sMedia) > 1:
                                                self.row_list.append(sMedia)
                                            else:
                                                self.row_list.append(
                                                    'Not Found')

                            # print(Name)
                            # print(type)
                            # print(website)
                            # print(sMedia)
                            # print()

                            for c in range(len(self.row_list)):
                                if self.row_list[c] == '' or self.row_list[c] == ' ':
                                    self.row_list[c] = 'Not Found'
                                print(self.row_list[c])
                            print()

                            self.collective_list.append(self.row_list)
                            while len(self.emailsListofLists) < len(self.collective_list):
                                self.emailsListofLists.append(['Not Found'])
                            phone, acronym, offName, type, website, sMedia, activity = '', '', '', '', '', '', ''
                            div1, div2, dataContainer, data, span, a, a1, a2, a3, a4, a5, span, title = '', '', '', '', '', '', '', '', '', '', '', '', ''
                            self.row_list = list()

        # The writing part: ############

        self.writeFromListofStrings(
            self.Categories, 'D:\Python\Bahrain', 'CategoriesBahrain', "catgsData")
        self.writeFromListofStrings(
            self.subCategories, 'D:\Python\Bahrain', 'SubCategoriesBahrain', "subcatgsData")
        self.writeFromListofLists(
            self.collective_list, 'D:\Python\Bahrain', 'ArabOrghBahrain', 'Data')
        self.writeFromListofLists(
            self.emailsListofLists, 'D:\Python\Bahrain', 'EmailshBahrain', 'mails Lists')

    #################################################
    def JSJabanese(self):
        # import requests
        from lxml import html
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from time import sleep

        log = open('log.text', 'a')  

        self.initNames = []
        

        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        
        while True:
            try:
                log.write('Getting Main Page'), print('Getting Main Page')
                driver.get("https://www.npo-hiroba.or.jp/search/result.php")
                log.write('Getting Main Page'), print('Got Main Page')
                break
            except BaseException as e:
                print(e)
                log.write(str(e))


        html_ = ""
        html__ = ""

        for page in range(1, 500):
            
            log.write(f'Processing Page Number || {page}')
            print(f'Processing Page Number || {page}')

            while True:
                try:
                    print(f'Passing Javascript || {page}'), log.write(f'Passing Javascript || {page}')
                    driver.execute_script(f"fncNext({page});")
                    print(f'Passed Javascript || {page}'), log.write(f'Passed Javascript || {page}')
                    break
                except BaseException as e:
                    print(e)
                    log.write(str(e))

            print(f'Sleeping || {page}'), log.write(f'Sleeping || {page}')
            sleep(15)
            print(f'Woke Up || {page}'), log.write(f'Sleeping || {page}')

            print(f'Getting rendered HTML || {page}'), log.write(f'Getting rendered HTML || {page}')
            html_ = driver.page_source
            print(f'Got rendered HTML || {page}'), log.write(f'Got rendered HTML || {page}')

            while html_ == html__:
                html_ = driver.page_source    
            else:
                html__ = html_

            print(f'Parsing new html || {page}'), log.write(f'Parsing new html || {page}')
            h = BS(html_, 'lxml')
            print(f'Parsed new html || {page}'), log.write(f'Parsed new html || {page}')

            for table in h.find_all('table'):

                print(f'Getting Data || {page}'), log.write(f'Getting Data || {page}')
                print()
                
                try:
                    # table = BS(table, 'html.parser')
                    for td in table.find_all('td'):
                        for a in td.find_all('a'):
                            url = a.get('href')
                            url = f"https://www.npo-hiroba.or.jp/search/{url}"
                            if 'zoom' in url:
                                if url not in self.pagesUrls:
                                    self.pagesUrls.append([url])
                                    print(f"{url} || page {page} || {len(self.pagesUrls)}")
                                    print()
                except BaseException as e:
                    print (e)
                    log.write(str(e))
                    
                    pass
            print(f'Done Processing Page Number || {page}'), log.write(f'Done Processing Page Number || {page}')
            print()
            print()

        self.writeFromListofLists(self.pagesUrls, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hiroba', 'PagesUrls', 'Pages Stage01')          
    
    
    def getData(self):
        Book_r = readWorkbook('PagesUrls.xlsx')
        Sheet_r = Book_r.active
        
        for Id, page in enumerate(Sheet_r.values):
            page = page[0]
            print(f"\nPage Num || {Id+1} has been Scrapped ")


            while True:
                try:
                    self.DirectHtmlParser(page)
                    break
                except BaseException:
                    pass

            try:
                self.textHtml
                for table in self.parsedHtml.find_all('table', class_ = 'registration'):
                    # print(table)
                    for td in table.find_all('td'):
                        ele = str(td.text).strip()
                        self.row_list.append(ele)
                        
            except BaseException:
                self.row_list.append("Error")
                pass

            #---------------
            
            try:
                self.textHtml
                for div in self.parsedHtml.find_all('div', id='fragment-1'):
                    for table in div.find_all('table'):
                        for td in table.find_all('td'):
                            ele2 = str(td.text).strip()
                            # print(ele2)
                            self.row_list.append(ele2)
                        
            except BaseException:
                self.row_list.append("Error")
                pass
            
            #---------
            go = False
            done = False
            try:
                if self.row_list[18] == "" and self.row_list[16] != "":
                    try:
                        url = self.row_list[16] 
                        self.DirectHtmlParser(url)
                        go = True
                    except BaseException:
                        pass
                    
                    if go:
                        for a in self.parsedHtml.find_all('a'):
                            try:
                                href = str(a.get('href'))
                            except BaseException:
                                pass
                            
                            if href.startswith('mailto'):
                                self.row_list.append(a.text)
                                done = True
                        
                if done == False:
                    print('Get emails')
                    url = self.row_list[16]
                    temp_em = self.GetEmailByRGXMethod(url)
                    try:
                        print([i for i in temp_em])
                    except BaseException:
                        print(self.emailsList[Id])
                        # print(self.emailsList[Id])
                        
                    

                
                print(f"Page Num || {Id+1} has been Scrapped \n {self.row_list[18]}\n Email: {self.row_list[-1]}\n")
                print()
                self.collective_list.append(self.row_list)
                self.row_list = []
            
                if Id == 2000:
                    self.writeFromListofLists(self.collective_list, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hiroba', 'Organizations', 'Data Stage01')          
                    self.writeFromListofLists(self.emailsList, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hirobaEmails', 'Organizations', 'Emails Stage01')          
                
                if Id == 5000:
                    self.writeFromListofLists(self.collective_list, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hiroba', 'Organizations', 'Data Stage01')          
                    self.writeFromListofLists(self.emailsList, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hirobaEmails', 'Organizations', 'Emails Stage01') 
            except BaseException:
                self.collective_list.append(self.row_list)
                self.row_list = []   
            
        self.writeFromListofLists(self.collective_list, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hiroba', 'Organizations', 'Data Stage01')          
        self.writeFromListofLists(self.emailsList, r'E:\ExtraC\Internships\Goodera\Contacts\npo-hirobaEmails', 'Organizations', 'Emails Stage01')          
        


obj5 = Scrap()
obj5.getData()

