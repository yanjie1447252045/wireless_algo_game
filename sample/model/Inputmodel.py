# -*- coding: UTF-8 -*-

class Scene(object):
    def __init__(self, bs_num, bs_infos, beacon, ue_infos):
        self.__bs_num = bs_num
        self.__bs_infos = bs_infos
        self.__beacon = beacon
        self.__ue_infos = ue_infos


class BaseStation:
    def __init__(self, lon, lat, high):
        self.__lon = lon
        self.__lat = lat
        self.__high = high

    def get_lon(self):
        return self.__lon

    def get_lat(self):
        return self.__lat

    def get_high(self):
        return self.__high

    def to_string(self):
        return '' + self.get_lon() + " " + self.get_lat() + " " + self.get_high()


class Beacon(object):
    def __init__(self, lon, lat, high, bs_num, re_num, channel_data):
        self.__lon = lon
        self.__lat = lat
        self.__high = high
        self.__bs_num = bs_num
        self.__re_num = re_num
        self.__channel_data = channel_data

    def get_lon(self):
        return self.__lon

    def get_lat(self):
        return self.__lat

    def get_re_num(self):
        return self.__re_num

    def get_channel_data(self):
        return self.__channel_data


class UE:
    def __init__(self, high, srs_re_num, accessible_bs_num, bs_index_arr, bs_num, channel_data):
        self.__high = high
        self.__srs_re_num = srs_re_num
        self.__accessible_bs_num = accessible_bs_num
        self.__bs_index_arr = bs_index_arr
        self.__bs_bum = bs_num
        self.__channel_data = channel_data
