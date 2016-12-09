
import os
import unittest
import uuid

from alfpy.utils import seqrecords
from alfpy import word_pattern
from alfpy import word_vector
from alfpy import word_distance
from alfpy.utils import distmatrix

ID_LIST = ['seq1', 'seq2', 'seq3']
SEQ_LIST = [
    'AACGTACCATTGAACGTACCGTAGG',
    'ctaggggacttatctagg',
    'CTAGGGAACATACCA'
]


class TestWordDistance(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestWordDistance, self).__init__(*args, **kwargs)
        self.seq_records = seqrecords.SeqRecords(ID_LIST, SEQ_LIST)
        self.p = word_pattern.create(self.seq_records.seq_list, 2)
        self.counts = word_vector.Counts(self.seq_records.length_list, self.p)
        self.freqs = word_vector.Freqs(self.seq_records.length_list, self.p)

    def test_euclid_squared_counts(self):
        dist = word_distance.Distance(self.counts, 'euclid_squared')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        # agrees with decaf+py
        data = ['   3',
                'seq1       0.0000000 57.0000000 30.0000000',
                'seq2       57.0000000 0.0000000 19.0000000',
                'seq3       30.0000000 19.0000000 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_euclid_squared_freqs(self):
        dist = word_distance.Distance(self.freqs, 'euclid_squared')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        # agrees with decaf+py
        data = ['   3',
                'seq1       0.0000000 0.1416402 0.0641298',
                'seq2       0.1416402 0.0000000 0.0677565',
                'seq3       0.0641298 0.0677565 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_euclid_norm_counts(self):
        dist = word_distance.Distance(self.counts, 'euclid_norm')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        # agrees with decaf+py
        data = ['   3',
                'seq1       0.0000000 7.5498344 5.4772256',
                'seq2       7.5498344 0.0000000 4.3588989',
                'seq3       5.4772256 4.3588989 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data)) 

    def test_euclid_norm_freqs(self):
        dist = word_distance.Distance(self.freqs, 'euclid_norm')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        # agrees with decaf+py
        data =['   3',
               'seq1       0.0000000 0.3763512 0.2532387',
               'seq2       0.3763512 0.0000000 0.2603008',
               'seq3       0.2532387 0.2603008 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data)) 

    def test_angle_cos_diss_freqs(self):
        dist = word_distance.Distance(self.freqs, 'angle_cos_diss')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        # agrees with decaf+py
        data = ['   3',
                'seq1       0.0000000 0.2797355 0.1500672',
                'seq2       0.2797355 0.0000000 0.1261027',
                'seq3       0.1500672 0.1261027 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data)) 

    def test_angle_cos_evol_freqs(self):
        dist = word_distance.Distance(self.freqs, 'angle_cos_evol')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        # agrees with decaf+py
        data = ['   3',
                'seq1       0.0000000 0.3281368 0.1625980',
                'seq2       0.3281368 0.0000000 0.1347925',
                'seq3       0.1625980 0.1347925 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data)) 

    def test_diff_abs_add_freqs(self):
        # agrees with decaf+py
        dist = word_distance.Distance(self.freqs, 'diff_abs_add')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        data = ['   3',
                'seq1       0.0000000 0.0810458 0.0507937',
                'seq2       0.0810458 0.0000000 0.0526611',
                'seq3       0.0507937 0.0526611 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_diff_abs_mult1_freqs(self):
        # agrees with decaf+py
        dist = word_distance.Distance(self.freqs, 'diff_abs_mult1')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        data = ['   3',
                'seq1       0.0000000 0.0621975 0.0501075',
                'seq2       0.0621975 0.0000000 0.0955847',
                'seq3       0.0501075 0.0955847 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_diff_abs_mult2_freqs(self):
        # agrees with decaf+py
        dist = word_distance.Distance(self.freqs, 'diff_abs_mult2')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        data = ['   3',
                'seq1       0.0000000 0.0621975 0.0404611',
                'seq2       0.0621975 0.0000000 0.0531478',
                'seq3       0.0404611 0.0531478 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_euclid_seqlen1_freqs(self):
        # agrees with decaf+py
        dist = word_distance.Distance(self.freqs, 'euclid_seqlen1')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        data = ['   3',
                'seq1       0.0000000 0.0065879 0.0032065',
                'seq2       0.0065879 0.0000000 0.0041065',
                'seq3       0.0032065 0.0041065 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_euclid_seqlen2_freqs(self):
        # agrees with decaf+py
        dist = word_distance.Distance(self.freqs, 'euclid_seqlen2')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        data = ['   3',
                'seq1       0.0000000 0.0072101 0.0038263',
                'seq2       0.0072101 0.0000000 0.0039866',
                'seq3       0.0038263 0.0039866 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

    def test_google_freqs(self):
        dist = word_distance.Distance(self.freqs, 'google')
        matrix = distmatrix.create(self.seq_records.id_list, dist)
        data = ['   3',
                'seq1       0.0000000 0.6078431 0.3809524',
                'seq2       0.6078431 0.0000000 0.3949580',
                'seq3       0.3809524 0.3949580 0.0000000\n']
        self.assertEqual(matrix.format(), "\n".join(data))

if __name__ == '__main__':
    unittest.main()