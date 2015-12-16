# -*- coding: utf-8 -*-

# Von Hamos Preview Tool for XDS Beamline
# Author: Rafael Pagliuca <rafael.pagliuca@lnls.br>
# Date created: 2015-12-02
# Date modified: 2015-12-11

import pandas
import numpy as np

class Tools:

    @staticmethod
    def dict_to_numpy(data):
        # Process list of dicts (data)
        df = pandas.DataFrame.from_dict(data, dtype='float') # use Pandas to convert to dataframe
        nparray = df.as_matrix(columns=data[0].keys()) # convert from Pandas to Numpy
        return nparray