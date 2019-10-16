# nama file: getaran.py

# mengimpor Periode & frekuensi getaran
import getaran
def main():

  #periodegetaran
  t = 20 #waktu
  n = 5  #jumlah getaran

  pg = getaran.periodegetaran(t, n)

  print("Periode & frekuensi getaran")
  print("waktu\t\t:",t)
  print("jumlah getaran\t:",n)
  print("hasil\t\t:",pg)

  #frekuensigetaran
  n = 30 #jumlahgetaran
  t = 3  #waktu

  fg = getaran.frekuensigetaran(n, t)

  print("Periode & frekuensi getaran")
  print("jumlah getaran\t:",n)
  print("waktu\t:",t)
  print("hasil\t\t:",fg)

  #gelombanggetaran
  a = 1   #variabel
  f = 10  #frekuensi

  gg = getaran.gelombanggetaran(a, f)

  print("Periode & frekuensi getaran")
  print("variabel\t:",a)
  print("frekuensi\t:",f)
  print("hasil\t\t:",gg)

if __name__=="__main__":
   main()



