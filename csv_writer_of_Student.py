import csv


if __name__=='__main__':
    with open( 'dat.csv', 'w' ,encoding='utf-8') as file_csv_w:
        worc_lst = ['математика' , 'физика' , 'сопромат' , 'динамика' , 'английcкий' , 'черчение' , 'металлообработка' , 'история']
        worc_dict = {}
        for index , val in enumerate(worc_lst):
            worc_dict[str(index)] = val
        csv_writer = csv.DictWriter(file_csv_w , fieldnames=[key for key in worc_dict], restval='None',dialect='excel-tab',quoting=csv.QUOTE_ALL)
        csv_writer.writeheader()
        csv_writer.writerows([worc_dict])