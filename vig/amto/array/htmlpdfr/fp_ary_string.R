## ----global_options, include = FALSE---------------------------------------------------------------------------------------------
try(source("../../../.Rprofile"))


## import numpy as np

## import string as string

## import random as random


## random.seed(123)

## it_word_length = 5

## st_rand_word = ''.join(random.choice(string.ascii_lowercase) for i in range(it_word_length))

## st_rand_word = st_rand_word.capitalize()

## print(f'{st_rand_word=}')


## random.seed(123)

## it_words_count = 15

## it_word_length = 5

## st_rand_word_block = ''.join(random.choice(string.ascii_lowercase) for ctr in range(it_word_length*it_words_count))

## ls_st_rand_word = [st_rand_word_block[ctr: ctr + it_word_length].capitalize()

##                    for ctr in range(0, len(st_rand_word_block), it_word_length)]

## print(f'{ls_st_rand_word=}')


## mt_st_rand_word = np.reshape(ls_st_rand_word, [3,5])

## print(f'{mt_st_rand_word=}')

## print(f'{mt_st_rand_word.shape=}')

## print(f'{type(mt_st_rand_word)=}')


## dc_invoke_main_args = {'speckey': 'ng_s_t',

##                        'numeric': 1.46,

##                        'ge': False,

##                        'multiprocess': False}

## 

## print(f'speckey in dc_invoke_main_args is {dc_invoke_main_args["speckey"]}.')

## print(f'numeric in dc_invoke_main_args is {dc_invoke_main_args["numeric"]}.')

## print(f'speckey in dc_invoke_main_args is {dc_invoke_main_args}.')


## ar_st_colnames = [ 's' + str(it_col) for it_col in np.array(range(1, 3))]

## print(ar_st_colnames)


## # define string

## ls_st_ignore = ['abc', 'efg', 'xyz']

## ls_st_loop = ['ab cefg sdf', '12345', 'xyz', 'abc xyz', 'good morning']

## 
## # zip and loop and replace

## for st_loop in ls_st_loop:

##   if sum([st_ignore in st_loop for st_ignore in ls_st_ignore]):

##     print('skip:', st_loop)

##   else:

##     print('not skip:', st_loop)

## 

## # define string

## st_full = """

## abc is a great efg, probably xyz. Yes, xyz is great, like efg.

## eft good, EFG capitalized, efg good again.

## A B C or abc or ABC. Interesting xyz.

## """

## 
## # define new and old

## ls_st_old = ['abc', 'efg', 'xyz']

## ls_st_new = ['123', '456', '789']

## 
## # zip and loop and replace

## for old, new in zip(ls_st_old, ls_st_new):

##   st_full = st_full.replace(old, new)

## 
## # print

## print(st_full)


## import textwrap

## 
## # A long Path

## st_path = """

## C:/Users/fan/Documents/Dropbox (UH-ECON)/Project Emily Minority Survey/EthLang/reg_lang_abi_cls_mino/tab3_fm/attain_m_vs_f/tab3_mand_talk_m2c_hfracle02.tex

## """

## 
## # Wrap text with tight width

## st_wrapped = textwrap.fill(st_path, width = 20)

## print(st_wrapped)


## 
## # Paths

## st_path_a = "C:/Users/fan/Documents/Dropbox (UH-ECON)/Project Emily Minority Survey/EthLang/reg_lang_abi_cls_mino/tab3_fm/attain_m_vs_f/tab3_mand_talk_m2c_hfracle02.tex"

## st_path_b = 'C:/Users/fan/R4Econ/support/development/fs_packaging.html'

## 
## # Combine Strings and Wrap

## str_dc_records = 'First Path:'.upper() + '\n' + \

##                  textwrap.fill(st_path_a, width=25) + '\n\n' + \

##                  'Second Path:'.upper() + '\n' + \

##                  textwrap.fill(st_path_b, width=25)

## 

## # Print

## print(str_dc_records)

