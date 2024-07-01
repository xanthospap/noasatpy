#! /usr/bin/python
#-*- coding: utf-8 -*-

import yaml
import os

""" 
Parse an input SATELLITE configuration file (YAML format) and return 
the corresponding options as a dictionary.
"""
def parseConfigInout(fn: str):
    with open(fn, "r") as fin: 
        ymldata = fin.read()
    return yaml.safe_load(ymldata)

"""
Once we have parsed the YAML config file into a dictionary, we can use 
the following function to get a list of all the elements that are included.

Results should be something like:
['H', 'He', 'N', 'O']
"""
def configElements(dct: dict):
    return [ k['atom'] for k in dct['data_list']['element_list'] ]

"""
Once we have parsed the YAML config file into a dictionary, we can use
the following function to get a list of all the FITS images and related info 
that should be present.

Results should be something like: 
[
  {'element': 'H', 'spectrum' : 'i',  'atomic': 6563, 'fn': '/home/.../Hi_6563.fit'}
  {'element': 'H', 'spectrum' : 'i',  'atomic': 4861, 'fn': '/home/.../Hi_4861.fit'}
  {'element': 'H', 'spectrum' : 'i',  'atomic': 4340, 'fn': '/home/.../Hi_4340.fit'}
  {'element': 'H', 'spectrum' : 'i',  'atomic': 4101, 'fn': '/home/.../Hi_4101.fit'}
  {'element': 'He', 'spectrum': 'i',  'atomic': 5876, 'fn': '/home/.../Hei_5876.fit'}
  {'element': 'He', 'spectrum': 'i',  'atomic': 6678, 'fn': '/home/.../Hei_6678.fit'}
  {'element': 'He', 'spectrum': 'ii', 'atomic': 5412, 'fn': '/home/.../Heii_5412.fit'}
]
"""
def configFitsFileList(dct: dict):
    fns = []
    for element in dct['data_list']['element_list']: 
        for spec in element['spectrum']: 
            for atomic in element['spectrum'][spec]['atomic_list']:
                fn = element['atom'] + spec + '_' + str(atomic) + '.' + d['data_list']['suffix']
                fns.append({'element': element['atom'], 'spectrum': spec, 'atomic': atomic, 'fn': os.path.join(d['data_list']['prefix'], fn)})
    return fns

"""
Once we have parsed the YAML config file into a dictionary, we can use
the following function to get a dictionary with all the options concerning 
the specific slit analysis.

Results should be something like: 
{
    'pixel_scale': 100, 
    'energy_parameter': -20,
    'number_of_slits': 10, 
    'slit_width': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 
    'slit_length': [320, 25, 21, 42, 18, 8, 46, 25, 25, 320], 
    'x_coor': [153, 37, 68, 104, 140, 169, 202, 254, 285, 154], 
    'y_coor': [106, 148, 142, 135, 128, 123, 116, 106, 100, 126]
}
"""
def configSpecificSlitDict(dct: dict):
    dct = d['analysis']['specific_slit']
    num_slits = dct['number_of_slits']
    for key in ['slit_width', 'slit_length', 'x_coor', 'y_coor']:
        value = str(dct[key])
        if len(value.split(',')) == 1:
            dct[key] = [int(value)] * num_slits
        elif len(value.split(',')) == num_slits:
            dct[key] = [int(x) for x in value.split(',')]
        elif len(value.split(',')) < num_slits:
            dct[key] = [int(x) for x in value.split(',')]
            missing = num_slits - len(value)
            dct[key] = dct[key] + dct[key][-1]*missing
        else:
            raise RuntimeError("ERROR Incorrect option for specific slit analysis; key={:}".format(key))
    return dct

if __name__ == "__main__" :
    import sys
    d = parseConfigInout(sys.argv[1])
    print(d)
    print("Element dictionary is:")
    print(d['data_list']['element_list'])
    print("Element:")
    for element in d['data_list']['element_list']: 
        print(element['atom'])
        print('\tSpectrums:')
        for spec in element['spectrum']: 
            print("\t",spec)
            print("\t\tAtomics:")
            for atomic in element['spectrum'][spec]['atomic_list']:
                fn = element['atom'] + spec + '_' + str(atomic) + '.' + d['data_list']['suffix']
                print("\t\t{:} - expected fn: {:}".format(atomic, os.path.join(d['data_list']['prefix'], fn)))
    print("------------------------------------------------------------------")
    fns = configFitsFileList(d)
    for i in fns: print(i)
    print("------------------------------------------------------------------")
    print(d['analysis']['specific_slit'])
    print(configSpecificSlitDict(d))
