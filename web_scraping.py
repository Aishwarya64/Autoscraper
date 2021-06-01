


from autoscraper import AutoScraper
url='https://www.amazon.in/Smartphones-Basic-Mobiles-Apple-Accessories/s?rh=n%3A1389432031%2Cp_89%3AApple'
wanted_list=["60,900","New Apple iPhone 12 Mini (64GB) - White"]

scraper=AutoScraper()
res=scraper.build(url,wanted_list)
#print(scraper.get_result_similar(url,grouped = True))
print('HIII')
data=scraper.get_result_similar(url,grouped = True)
keys=list(data.keys())
print(keys)
scraper.set_rule_aliases({str(keys[0]):'Price',str(keys[1]):'Model'})
scraper.keep_rules([str(keys[0]),str(keys[1])])
scraper.save('amazon-search')

test=scraper.get_result_similar(url,group_by_alias=True)
print(test['Price'])
print('Automating the scraper on other urls')
url2='https://www.amazon.in/Smartphones-Basic-Mobiles-Apple-Accessories/s?i=electronics&bbn=1389432031&rh=n%3A1389432031%2Cp_89%3ANokia&dc&qid=1622564190&rnid=3837712031&ref=sr_nr_p_89_2'
ans=scraper.get_result_similar(url2,group_by_alias=True)
print('Printing scraped data price for other url')
print(ans['Price'])

print('Displaying model')
print(ans['Model'])