#membuat class
class Mixer:
  kecepatan_sekarang = 0

  #fungsi construktor
  def __init__(self,nama_merk,jumlah_tungkai_pengaduk,kecepatan_mixer):
    self.nama_merk = nama_merk
    self.jumlah_tungkai_pengaduk = jumlah_tungkai_pengaduk
    self.kecepatan_mixer = kecepatan_mixer

#membuat fungsi dari mixer
  def nyalakanMixer(self):
    print('Mixer menyala ', self.nama_merk)

  def matikanMixer(self):
    print('Mixer dimatikan ', self.nama_merk)

  def menambahKecepatan(self):
    self.kecepatan_sekarang = self.kecepatan_sekarang + 2
    print('kecepatan_sekarang ', self.kecepatan_sekarang)

#membuat objek
mixer_dapur = Mixer('Philips','2','0')
mixer_kosan = Mixer('Miyako','2','0')

#memanggil fungsi dari objek
mixer_dapur.nyalakanMixer()
mixer_dapur.menambahKecepatan()

print(mixer_dapur.nama_merk)
print(mixer_dapur.jumlah_tungkai_pengaduk)
print(mixer_dapur.kecepatan_mixer)
# print(mixer_kosan.nama_merk)
