# Demo Instructions
# 
# Run in interactive mode: python -i training/word2vec/simple_preprocess/bcapara.py
# print(corpus)

import os
from gensim.utils import simple_preprocess

def single_para():
    sentence = "BCA mengajukan permohonan kepada Bank Indonesia agar diperbolehkan mengeluarkan dan mengedarkan kartu kredit atas nama BCA yang berlaku internasional. Untuk itu, BCA bekerjasama dengan MasterCard. BCA juga memperluas jaringan kantor cabang secara agresif sejalan dengan deregulasi sektor perbankan di Indonesia. BCA mengembangkan berbagai produk dan layanan maupun pengembangan teknologi informasi, dengan menerapkan online system untuk jaringan kantor cabang, dan meluncurkan Tabungan Hari Depan (Tahapan) BCA. Pada tahun 1990-an BCA mengembangkan alternatif jaringan layanan melalui ATM (Anjungan Tunai Mandiri atau Automated Teller Machine). Pada tahun 1991, BCA mulai menempatkan 50 unit ATM di berbagai tempat di Jakarta. Pengembangan jaringan dan fitur ATM dilakukan secara intensif. BCA bekerja sama dengan institusi terkemuka, antara lain PT Telkom untuk pembayaran tagihan telepon melalui ATM BCA. BCA juga bekerja sama dengan Citibank agar nasabah BCA pemegang kartu kredit Citibank dapat melakukan pembayaran tagihan melalui ATM BCA."
    corpus = simple_preprocess(sentence)
    return([corpus])

def multi_senc():
    file_dir = os.path.dirname(os.path.realpath(__file__)) + '/sentences.txt'
    corpus = list(map(simple_preprocess, open(file_dir).read().splitlines()))
    print(corpus[-6:], "\nSentences: -->", len(corpus))
    uniqset = set(word for l in corpus for word in l) 
    print(len(uniqset), "Unique Terms")
    return(corpus)

if __name__ == '__main__':
    corpus = multi_senc()