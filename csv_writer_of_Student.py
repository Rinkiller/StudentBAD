import csv


if __name__=='__main__':
    worc_dict = {'математика':[4 , {'test1':45,'test2':100}], 'физика':[5,{'test1':12,'test2':12}] , 'сопромат':[5,{'test1':3}] , 'динамика жидкостей':[4,{'test1':3}] , 'английcкий':[4,{'test1':34}] , 'черчение':[5,{'test1':33}] , 'металлообработка':[3,{'test1':73}] , 'история':[4,{'test1':23}],'спермодинамика':[2,{'test1':0}]}
    with open( 'dat.csv', 'w' ,encoding='utf-8') as file_csv_w:
        
        # worc_dict = {}
        # for index , val in enumerate(worc_lst):
        #     worc_dict[str(index)] = val
        csv_writer = csv.DictWriter(file_csv_w , fieldnames=[key for key in worc_dict])
        csv_writer.writeheader()
        csv_writer.writerows([worc_dict])