import obsidian_classes as ob

dict_aliases=ob.aliases_finder()
reading=input('Print aliases?[Y/[n]]')
if reading in ['Y','y',1]:
    print('-'*40)
    for key,value in dict_aliases.items():
        print(key,'=>',value)
    print('-'*40)
ob.aliases_applier(dict_aliases,make_backup=True)
resp=input('Do you want to correct internal links that do not match the alias?[Y/[n]]')
if resp in ['Y','y',1]:
    ob.aliases_corrector(dict_aliases)
else:
    print('Not correcting')
