# -*- coding:utf-8 -*-
import argparse


class BaseOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.initialized = False

    def initialize(self):
        self.parser.add_argument('--dataset', type=str, default='./dataset/pems08.npz', help='path for dataset')
        self.parser.add_argument('--save_path', type=str, default='./checkpoint/PEMS08', help='path for saving model')
        self.parser.add_argument('--adj', type=str, default='./dataset/distance08.csv', help='filename for adjacency matrix')
        self.parser.add_argument('--Multidataset', type=str, default='./dataset/pems08_h2_d1_w1_p12_s1_MultiComponent.npz',
                                 help='whether existing Multidataset or Slidedataset, create one if not')

        self.parser.add_argument('--process_method', type=str, default='MultiComponent', help='MultiComponent |SlideWindow')
        self.parser.add_argument('--hdwps', type=str, default='2,1,1,12,1',
                                 help='hour, day, week, and shift are multiples of prediction length, ')

        self.parser.add_argument('--gcn1_out_feature', type=int, default=128, help='out_feature of GCN layer1')
        self.parser.add_argument('--gcn2_out_feature', type=int, default=64, help='out_feature of GCN layer2')
        self.parser.add_argument('--nb_time_filter', type=int, default=64, help='out_feature of CNN')
        self.parser.add_argument('--lstm_hidden', type=int, default=32, help='hidden size of lstm or gru')
        self.parser.add_argument('--dropout', type=float, default=0.8, help='only for DM-RGCN')
        self.parser.add_argument('--weight_decay', type=float, default=5e-4, help='weight decay')
        self.parser.add_argument('--model', type=str, default='MCSTGCN',
                                 help='DMRGCN |Baseline_LSTM |Baseline_GRU |MCSTGCN |ASTGCN |DM_LSTM_GCN')

    def parse(self):
        if not self.initialized:
            self.initialize()

        self.opt = self.parser.parse_args()

        self.opt.isTrain = self.isTrain
        args = vars(self.opt)

        return self.opt


class TrainOptions(BaseOptions):
    # Override
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--lr', type=float, default=1e-3, help='initial learning rate')
        self.parser.add_argument('--optimizer', type=str, default='adam', help='[sgd | adam]')
        self.parser.add_argument('--epoch', type=int, default=4, help='number of training epochs')
        self.isTrain = True


class TestOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.isTrain = False
