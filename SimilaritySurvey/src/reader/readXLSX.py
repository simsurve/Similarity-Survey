

import xlrd
import urllib2
import urllib
import os

class readXLSX(object):
    '''
    This class is made to read 'xlsx' file which is downloaded from "google.docs". It include the main function of reading which returns dictionary for each participant. 
    '''


    def __init__(self,titles=['Your Sehir Student Address','Gender','Age','Department','Hometown','Hobbies',0,0,'Choose Your Favorite 2 Book Genres','Your Favorite 2 Writers',0,'Choose Your Favorite 3 Music Genres','Your Favorite 3 Singers',0,0,'Your Favorite 5 Songs',0,0,0,0,'Your Favorite 2 Directors',0,'Your Favorite 3 Actors/Actress',0,0,'Your Favorite 3 Movies',0,0,'Your Favorite 3 Sport Branches',0,0,'Your Favorite Sport Team','Facebook Account Link','Twitter Account Link']
):
        self.titles = titles
 #       self.filePath = filePath
        '''
        'titles' is a list which involve survey questions.
        '''
    
    #To create a informative dinctionary
    
    def translate(self, to_translate, to_langage="auto", langage="auto"):
        '''Return the translation using google translate
        you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
        if you don't define anything it will detect it or use english by default
        Example:
        print(translate("salut tu vas bien?", "en"))
        hello you alright?'''
        agents = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}


        before_trans = 'class="t0">'

        link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, urllib.quote(to_translate.encode('utf8')))

        request = urllib2.Request(link, headers=agents)

        page = urllib2.urlopen(request).read()
        result = page[page.find(before_trans) + len(before_trans):]
        result = result.split("<")[0]

        return result

    def key_for_multiple_entry(self,a):
        
        for j in range(a):
            if self.titles[j]!=0:
                string=self.titles[j]
            
        return string
    
    def title_less_placing(self):
        
        a=dict()
        
        for i in self.titles:
            if self.titles==0:
                pass
            else:
                a[i]=[]
        return a
    
    def start_reading(self):
        filePath = os.path.expanduser("~/Desktop/software/SimSurve1.xlsx")
        workbook = xlrd.open_workbook(filePath)
        worksheet = workbook.sheet_by_name('Form Responses')
        num_rows = worksheet.nrows - 1
        num_cells = worksheet.ncols - 1
        curr_row = 0
        user_all = dict()
        
        while curr_row < num_rows:
            curr_row += 1
            curr_cell = 0
            a = self.title_less_placing()
                    
            while curr_cell < num_cells:
                curr_cell += 1
                cell_value = worksheet.cell_value(curr_row, curr_cell)
                if cell_value is str:
                    m = self.translate(cell_value, to_langage="en", langage="tr")
                else:
                    m = cell_value
                string2 = self.titles[curr_cell]

                if string2==0:
                    placeString = self.key_for_multiple_entry(curr_cell)
                    a.get(placeString).append(m)
                else:
                    a.get(string2).append(m)

            user_all[curr_row] = a
                                    
                    
        return user_all
    
    
    
        