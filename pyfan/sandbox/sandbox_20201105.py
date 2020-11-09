# list update
dc_invoke_main_args_default = {'speckey': 'ng_s_t',
                               'ge': False,
                               'multiprocess': False,
                               'estimate': False,
                               'graph_panda_list_name': 'min_graphs',
                               'save_directory_main': 'simu',
                               'log_file': False,
                               'log_file_suffix': ''}
dc_invoke_main_args = dc_invoke_main_args_default
dc_invoke_main_args['speckey'] = 'b_ge_s_t_bis'
dc_invoke_main_args['ge'] = True
print(f'speckey in dc_invoke_main_args is {dc_invoke_main_args["speckey"]}.')
print(f'speckey in dc_invoke_main_args_default is {dc_invoke_main_args_default["speckey"]}.')

# raise error
ls_st_spec_key_dict = ['NG_S_D', 'NG_S_D=KAP_M0_NLD_M_SIMU=2=3']
st_connector = '='
ls_st_esti_simu = ['esti', 'simu']
for st_spec_key_dict in ls_st_spec_key_dict:
    for st_esti_simu in ls_st_esti_simu:
        it_len_spec_key_split = st_spec_key_dict.split(st_connector)
        if st_esti_simu == 'simu':
            if it_len_spec_key_split == 1:
                print('simulate with ' + st_spec_key_dict)
            else:
                st_error = 'st_spec_key_dict=' + st_spec_key_dict + ' can n'
                raise ValueError(st_error)
