# -*- coding: UTF-8 -*-

import csv
from sample.model.Inputmodel import BaseStation
from sample.model.Inputmodel import Beacon
from sample.model.Inputmodel import UE
from sample.model.Inputmodel import Scene


class InputDataReader(object):
    """将输入文件转换时实体对象信息"""
    def __init__(self, path):
        self.__path = path
        self.__row_index = 0

    def read(self):
        with open(self.__path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            self.__row_index = 0
            scene_infos = []
            scene_num = self.__read_scene_num(data)
            for i in range(scene_num):
                scene = self.__read_scene_info(data)
                scene_infos.append(scene)
            return scene_infos

    def __read_scene_info(self, data):
        bs_num = data[self.__return_and_add()][0]
        bs_infos = self.__read_base_station_infos(data, bs_num)
        beacon = self.__read_beacon_infos(bs_num, data)
        ue_infos = self.__read_ue_infos(bs_num, data)
        return Scene(bs_num, bs_infos, beacon, ue_infos)

    def __read_ue_infos(self, bs_num, data):
        ue_infos = []
        ue_num = data[self.__return_and_add()][0]
        for _ in range(ue_num):
            ue_info_row = data[self.__return_and_add()]
            high = ue_info_row[0]
            srs_re_num = ue_info_row[1]
            accessible_bs_num = ue_info_row[2]
            bs_index_arr = []
            for i in range(accessible_bs_num):
                bs_index_arr.append(int(ue_info_row[i + 3]))
            channel_data = []
            for i in range(bs_num * srs_re_num * 2):
                channel_data.append(data[self.__return_and_add()])
            curr_ue = UE(high, srs_re_num, accessible_bs_num, bs_index_arr, bs_num, channel_data)
            ue_infos.append(curr_ue)
        return ue_infos

    def __read_beacon_infos(self, bs_num, data):
        beacon_info_row = data[self.__return_and_add()]
        lon = beacon_info_row[0]
        lat = beacon_info_row[1]
        high = beacon_info_row[2]
        re_num = beacon_info_row[3]
        channel_data = []
        for _ in (range(bs_num * 2 * re_num)):
            each = data[self.__return_and_add()]
            channel_data.append(each)
        beacon = Beacon(lon, lat, high, bs_num, re_num, channel_data)
        return beacon

    def __read_scene_num(self, data):
        return data[self.__return_and_add()][0]

    def __return_and_add(self):
        curr = self.__row_index
        self.__row_index = self.__row_index + 1
        return curr

    def __read_base_station_infos(self, data, bs_num):
        bs_infos = []
        for i in range(int(bs_num)):
            row = data[self.__return_and_add()]
            station = BaseStation(row[0], row[1], row[2])
            bs_infos.append(station)
        return bs_infos
