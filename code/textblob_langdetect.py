# -*- coding: utf-8 -*-
import csv
from langdetect import detect
import sys
import detectlanguage
from textblob import TextBlob

reload(sys)
sys.setdefaultencoding('utf8')

# folder = ["harvey", "irma"]

# folder = ["irma"]

# folder = ["japan_first5days"]

folder = ["hurricane_florence"]

detectlanguage.configuration.api_key = "5c8e2041feb6ad356921e04317fe25c5"

for f in folder:

    lst = f.split(',')

    # print lst[0], ' ', lst[1]

    #event = lst[0]
    #ev = lst[1]

    # with open('/Users/pk4634/Documents/phase3/' + f + '_new_temporal_data_csv/' + f + '_800000_noduplicate_1.csv') as fline,\
    #        open('/Users/pk4634/Documents/phase3/' + f + '_new_temporal_data_csv/' + f + '_800000_lang' + '/detectlanguage/' + f + '_800000_noduplicate_lang_1.csv', 'wb') as wfile:

    # with open('/Users/pk4634/Documents/phase3/' + f + '/japan_50000_fixed_noduplicate.csv') as fline,\
    #        open('/Users/pk4634/Documents/phase3/' + f + '/detectlanguage/' + f + 'japan_50000_fixed_noduplicate_lang.csv', 'wb') as wfile:

    with open('/Users/pk4634/Documents/phase3/' + f + '/kerala_floods_130000_fixed_noduplicate.csv') as fline,\
            open('/Users/pk4634/Documents/phase3/' + f + '/detectlanguage/' + 'kerala_floods_130000_fixed_noduplicate_lang.csv', 'wb') as wfile:

        writer = csv.writer(wfile, delimiter='\t', quotechar=None)

        c = 0

        for line in csv.reader(fline, delimiter='\t', skipinitialspace='True', quotechar=None):

            #lg = detect(line[1].decode('utf-8').strip())
            lang = ''
            conf = '-1'
            reliable = 'False'

            # b = TextBlob(line[1].decode('utf-8').strip())
            # lg = b.detect_language()
            lg = detectlanguage.detect(line[1].decode('utf-8').strip())

            c = c + 1
            print(f + ' ' + str(c))

            if len(lg) > 0:

                writer.writerow([line[0].strip().encode('utf-8'), line[1].strip().encode('utf-8'), line[2].strip().encode(
                    'utf-8'), line[3].strip().encode('utf-8'), line[4].strip().encode('utf-8'), line[5], lg[0]['language'], lg[0]['isReliable'], lg[0]['confidence']])

            else:
                writer.writerow([line[0].strip().encode('utf-8'), line[1].strip().encode('utf-8'), line[2].strip().encode(
                    'utf-8'), line[3].strip().encode('utf-8'), line[4].strip().encode('utf-8'), line[5], lang, reliable, conf])

    wfile.close()
print 'done'
