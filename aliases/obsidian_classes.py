import os
import distutils.dir_util as dd
import markdown
from directories import *
import re
import shutil


#%% Functions
def get_f_list(path):
    elements = os.listdir(path)
    page_elements=[j for j in elements if j.endswith('.md')]
    dir_list=[j for j in elements if len(j.split('.'))==1]
    return dir_list,page_elements

def get_r_pages(base_path):
    super_all_pages_list = []
    cond = True
    non_listed_paths = [base_path]
    while(cond):
        d_list, p_list = get_f_list(non_listed_paths[0])
        for page in p_list: super_all_pages_list.append(page)
        for j in d_list: non_listed_paths.append(non_listed_paths[0]+'/'+j)
        non_listed_paths.pop(0)
        cond=len(non_listed_paths)!=0
    return super_all_pages_list

def get_r_pages_dir(base_path):
    super_all_pages_list = []
    cond = True
    non_listed_paths = [base_path]
    while(cond):
        d_list, p_list = get_f_list(non_listed_paths[0])
        for page in p_list: super_all_pages_list.append(os.path.join(non_listed_paths[0],page))
        for j in d_list: non_listed_paths.append(non_listed_paths[0]+'/'+j)
        non_listed_paths.pop(0)
        cond=len(non_listed_paths)!=0
    return super_all_pages_list

def get_r_dirs(base_path):
    cond = True
    total_paths=[]
    non_listed_paths = [base_path]
    while(cond):
        d_list, p_list = get_f_list(non_listed_paths[0])
        for j in d_list: non_listed_paths.append(non_listed_paths[0]+'/'+j)
        for j in d_list: total_paths.append(non_listed_paths[0]+'/'+j)
        non_listed_paths.pop(0)
        cond=len(non_listed_paths)!=0
    return total_paths

def obsidian_bak():
    i=0
    total_num_copies=30

    safes_list=os.listdir(safe_obsidian)
    if 'Obsidian_copy_0' not in safes_list:
        os.mkdir(os.path.join(safe_obsidian, 'Obsidian_copy_0'))
        safes_list = os.listdir(safe_obsidian)
    num_saves=len(safes_list)
    if num_saves==1:
        destiny = os.path.join(safe_obsidian, 'Obsidian_copy_0')
        dd.copy_tree(obsidian_base_path, destiny)
    else:
        for i in range(num_saves):
            current_name = 'Obsidian_copy_{x}'.format(x=(num_saves-i-1))
            new_name= 'Obsidian_copy_{x}'.format(x=(num_saves-i))
            os.rename(os.path.join(safe_obsidian,current_name),os.path.join(safe_obsidian,new_name))
        destiny = os.path.join(safe_obsidian,'Obsidian_copy_0')
        # dd.copy_tree(obsidian_base_path,destiny)
        shutil.copytree(obsidian_base_path,destiny)
        if 'Obsidian_copy_{x}'.format(x=total_num_copies) in os.listdir(safe_obsidian):
            shutil.rmtree(os.path.join(safe_obsidian,'Obsidian_copy_{x}'.format(x=total_num_copies)))
    print('Bak done')

def aliases_finder():
    '''
    Esto me construye el diccionario de aliases
    :return:
    '''
    # El patrón de regex
    all_page_dirs=get_r_pages_dir(obsidian_base_path)
    aliases=0
    dict_aliases={}

    pattern='#alias=\'([_\w\d\s\.-]+)\''
    pat=re.compile(pattern)
    #Ahora es solo extraer el grupo y el nombre de la página.

    for page_dir in all_page_dirs:
        #primero se lee y se guarda tod\o el archivo
        with open(page_dir,'r') as file:
            for line in file.readlines():
                if pat.search(line) != None:
                    #Tenemos un match
                    #Extraemos el alias y el nombre de la página.
                    pag_name=page_dir.split('/')[-1].split('.md')[0]
                    dict_aliases[pag_name]=pat.search(line).group(1)
                    aliases+=1
    print('Finished aliases finder')
    print('N aliases: ', aliases)
    return dict_aliases

def aliases_applier(dict_aliases,make_backup=True):
    '''
    Leemos todas las páginas y las que tengan el siguiente elemento.
    [[original]]
    las transforma a [[original | alias]]
    :return: void
    '''
    #Antes de hacer nada realizamos una copia de seguridad.
    if make_backup: obsidian_bak()

    # El patrón de regex
    all_page_dirs=get_r_pages_dir(obsidian_base_path)
    changes=0
    for original,alias in dict_aliases.items():
        assert (type(original)==type('a') and type(alias)==type('a')), 'The key aliases are not Strings'

        pattern='\[\['+original+'\]\]'
        pat=re.compile(pattern)

        for page_dir in all_page_dirs:
            #primero se lee y se guarda tod\o el archivo
            file_lines=[]
            with open(page_dir,'r') as file:
                for line in file.readlines():
                    file_lines.append(line)

            with open(page_dir,'w') as file:

                for line in file_lines:
                    if pat.search(line) != None:
                        #Contamos el numero de matches.
                        n_matches=len([*re.finditer(pattern,line)])
                        for k in range(n_matches):
                            line=pat.sub(r'[['+original+'|'+alias+']]',line)
                            changes+=1

                    file.write(line)
    print('Finished applied changes')
    print('N changes: ',changes)

def aliases_corrector(dict_aliases):
    '''
    Leemos todas las páginas y las que tengan el siguiente elemento.
    [[original]]
    las transforma a [[original | alias]]
    :return: void
    '''
    # Antes de hacer nada realizamos una copia de seguridad.

    # El patrón de regex
    all_page_dirs = get_r_pages_dir(obsidian_base_path)
    changes = 0
    for original, alias in dict_aliases.items():
        assert (type(original) == type('a') and type(alias) == type('a')), 'The key aliases are not Strings'

        pattern = '\[\[' + original + '\|([\w\d\s]+)\]\]'
        pat = re.compile(pattern)

        for page_dir in all_page_dirs:
            # primero se lee y se guarda tod\o el archivo
            file_lines = []
            with open(page_dir, 'r') as file:
                for line in file.readlines():
                    file_lines.append(line)

            with open(page_dir, 'w') as file:

                for line in file_lines:
                    if pat.search(line) != None:
                        # Si hay un match miramos a ver si el grupo es igual al alias.
                        n_matches = len([*re.finditer(pattern, line)])
                        for k in range(n_matches):
                            if pat.search(line).group(1)!=dict_aliases[original]:
                                line = pat.sub(r'[[' + original + '|' + alias + ']]', line)
                                changes += 1

                    file.write(line)
    print('Finished alias corrections')
    print('N corrections: ', changes)

