from gensim.utils import simple_preprocess

sentence = "BCA mengajukan permohonan kepada Bank Indonesia agar diperbolehkan mengeluarkan dan mengedarkan kartu kredit atas nama BCA yang berlaku internasional. Untuk itu, BCA bekerjasama dengan MasterCard. BCA juga memperluas jaringan kantor cabang secara agresif sejalan dengan deregulasi sektor perbankan di Indonesia. BCA mengembangkan berbagai produk dan layanan maupun pengembangan teknologi informasi, dengan menerapkan online system untuk jaringan kantor cabang, dan meluncurkan Tabungan Hari Depan (Tahapan) BCA. Pada tahun 1990-an BCA mengembangkan alternatif jaringan layanan melalui ATM (Anjungan Tunai Mandiri atau Automated Teller Machine). Pada tahun 1991, BCA mulai menempatkan 50 unit ATM di berbagai tempat di Jakarta. Pengembangan jaringan dan fitur ATM dilakukan secara intensif. BCA bekerja sama dengan institusi terkemuka, antara lain PT Telkom untuk pembayaran tagihan telepon melalui ATM BCA. BCA juga bekerja sama dengan Citibank agar nasabah BCA pemegang kartu kredit Citibank dapat melakukan pembayaran tagihan melalui ATM BCA."
corpus = [word.lower() for word in sentence.split()]
print(f'{corpus}, total word: {len(corpus)}')
print(' --- \n')
corpus2 = simple_preprocess(sentence)
print(f'{corpus2}, total word: {len(corpus2)}')
print(' --- \n')
print([word for word in corpus if word not in corpus2])
    