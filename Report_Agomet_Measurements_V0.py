#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 02:03:06 2022

@author: nico
"""

import numpy as np

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os

if __name__ == '__main__':
    path = '/home/nico/Documentos/Drought/Mediciones/figures/Validaciones_agromet/'
    #image_filename = os.path.join(os.path.dirname(path), 'test3_2012-2022_1.png')

    geometry_options = {"tmargin": "1cm", "lmargin": "0.5cm"}
    doc = Document(geometry_options=geometry_options)
    with doc.create(Section('Precipitation NaN')):
          with doc.create(Figure(position='h!')) as kitten_pic:
              #kitten_pic.add_image(image_filename, width='120px')
              image_filename = os.path.join(os.path.dirname(path), 'heatmap_dias_completos_mes.png')
              kitten_pic.add_image(image_filename, width='300px')
              kitten_pic.add_caption('Precipitación horaria pre>0 and pre < 50, agregación (suma) de la precipitación horaria entre 8am-8am, días completos sin falta de mediciones horarias')

    with doc.create(Section('Precipitation raw time series')):
          for figura in range(1,25):
              print(figura)
              with doc.create(Figure(position='h!')) as kitten_pic:
                  #kitten_pic.add_image(image_filename, width='120px')
                  image_filename = os.path.join(os.path.dirname(path), 'test3_2012-2022_'+str(figura)+'.png')
                  kitten_pic.add_image(image_filename, width='630px')
                  kitten_pic.add_caption('Time series of hourly precipitation, raw data. Y axes rage are 0-10 mm')

    doc.generate_pdf('Report_Agromet_Measurements_V0', clean_tex=False)
'''
    with doc.create(Section('The simple stuff')):
        doc.append('Some regular text and some')
        doc.append(italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')
        with doc.create(Subsection('Math that is incorrect')):
            doc.append(Math(data=['2*3', '=', 9]))

        with doc.create(Subsection('Table of something')):
            with doc.create(Tabular('rc|cl')) as table:
                table.add_hline()
                table.add_row((1, 2, 3, 4))
                table.add_hline(1, 2)
                table.add_empty_row()
                table.add_row((4, 5, 6, 7))

    a = np.array([[100, 10, 20]]).T
    M = np.matrix([[2, 3, 4],
                   [0, 0, 1],
                   [0, 0, 2]])

    with doc.create(Section('The fancy stuff')):
        with doc.create(Subsection('Correct matrix equations')):
            doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))

        with doc.create(Subsection('Alignat math environment')):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\frac{a}{b} &= 0 \\')
                agn.extend([Matrix(M), Matrix(a), '&=', Matrix(M * a)])

        with doc.create(Subsection('Beautiful graphs')):
            with doc.create(TikZ()):
                plot_options = 'height=4cm, width=6cm, grid=major'
                with doc.create(Axis(options=plot_options)) as plot:
                    plot.append(Plot(name='model', func='-x^5 - 242'))

                    coordinates = [
                        (-4.77778, 2027.60977),
                        (-3.55556, 347.84069),
                        (-2.33333, 22.58953),
                        (-1.11111, -493.50066),
                        (0.11111, 46.66082),
                        (1.33333, -205.56286),
                        (2.55556, -341.40638),
                        (3.77778, -1169.24780),
                        (5.00000, -3269.56775),
                    ]

                    plot.append(Plot(name='estimate', coordinates=coordinates))
    doc.generate_pdf('Report_Agromet_Measurements_V0', clean_tex=False)
'''