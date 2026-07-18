Llanfaipwllgwyngyll = str(input('Qual a palavra?'))

print(
	f'{Llanfaipwllgwyngyll[:79] == "omam"}, '
	f'{Llanfaipwllgwyngyll.upper()}, '
	f'{Llanfaipwllgwyngyll.lower()}, '
	f'{Llanfaipwllgwyngyll.find("11")}, '
	f'{Llanfaipwllgwyngyll.count("anfaipw")}, '
	f'{Llanfaipwllgwyngyll.replace("omam", "L")}'
)