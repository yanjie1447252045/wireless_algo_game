# -*- coding: UTF-8 -*-

import numpy.fft as nf


class ChannelData(object):
    def __init__(self, first_att, second_att):
        self.__first_att = first_att
        self.__second_att = second_att

    @staticmethod
    def __get_ifft_matrix(channel_data):
        size = len(channel_data)
        ifft_res = []
        for i in range(size):
            row = channel_data[i]
            ifft_res.append(nf.ifft(row))
        return ifft_res

    def __get_matrix_mod(self, att):
        matrix = self.__get_ifft_matrix(att)
        rows = len(matrix)
        res = []
        for i in range(rows):
            row = matrix[i]
            each_row_res = []
            for j in range(len(row)):
                each_row_res.append(abs(row[j]))
            res.append(each_row_res)
        return res

    def calc_pdp_matrix(self):
        first = self.__get_matrix_mod(self.__first_att)
        second = self.__get_matrix_mod(self.__second_att)
        res = []
        res.extend(first)
        res.extend(second)
        return res


class FirstPathMatrix(object):
    def __init__(self, matrix):
        self.__matrix = matrix
