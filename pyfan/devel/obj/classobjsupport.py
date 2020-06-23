'''
Created on Mar 16, 2017

@author: fan
'''

def dynamic_obj_attr(attribute_array=['r_save', 'r_borr', 'delta'],
                     attribute_values_array=['0.02', '0.05', '0.10'],
                     print_values=False):

    class Object(object):
        pass
    standin_obj = Object()

    for index, param in enumerate(attribute_array):
        setattr(standin_obj, param, attribute_values_array[index])

    if(print_values == True):
        print(standin_obj.__dict__)

    return standin_obj

if __name__ == '__main__':

    dynamic_obj_attr(print_values=True)
