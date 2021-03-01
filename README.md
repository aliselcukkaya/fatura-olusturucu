# fatura-olusturucu
E-Arsiv portalı için fatura oluşturan bot


# !! Bu program eğitimim için yaptığım bir programdır ve herhangi bir ticari değer taşımaz. Fatura girmeyi kolaylaştırmak için yapılmıştır, normal bir insanın girebileceği şekilde bütün işlemleri yapmaktadır.

Bütün faturaların bir excel dosyasında olduğunu varsayıyorum. Programın içine hardcoded bir şekilde ad, soyad, fiyat, tarih vb. gibi bilgilerin bulunduğu excel sütununu yazmanız gerekiyor (eğer isterseniz bunu daha dinamik bir hale getirebilirsiniz).
Şuan program excelden aldığı tarihi (excelde tarihlerin arasında virgül olması gerek, bunu isterseniz dinamik hale getirebilirsiniz) yıl, gün, ay ve saat olarak ayırıyor, fiyat hesaplamasını yapıyor, ad ve soyadda büyük harf küçük harf sorunu oluyor onu hallettim (çok detaylı bir şekilde büyük küçük harf sorununa bakmadım, çoğunlukla yaşanan sorunları çözdüm yine eğer isterseniz bunuda daha kapsamlı hale getirebilirsiniz) vb. kodda detaylı olarak inceleyebilirsiniz comment olarak ekledim çoğu şeyi.

Program çalıştığı an bir log dosyası oluşturuyor çalıştığı tarihin ismi ile, bu log dosyasında programda karşılaşılan hatalar ve excelden EN SON GİRİLMEYE ÇALIŞILAN faturanın bilgileri bulunur yani log dosyasında yazan en son fatura bilgisi GİRİLMEMİŞTİR.

Sitedeki elementleri seçerken çoğunlukla XPATH kullandım çünki diğer seçicileri kullanırken birkaç sorun yaşadım böylesi daha stabil çalışıyordu fakat sitedeki en ufak bir değişiklikte programın tekrar düzenlenmesi gerekiyor. Siz bununla uğraşmak istemiyorsanız her element için uygun bir seçici bulup dinamik hale getirebilirsiniz.

config.txt ye
12345678
123456
bu şekilde kullanıcı adı ve şifreyi girebilirsiniz.

# Eğer programı kendinize göre ayarladıysanız ve faturaları girmeden önce denemek istiyorsanız (ki ben böyle yapmanızı kesinlikle öneriyorum) veri_girme.py dosyasının en sondaki 3 fonksiyonundan SONUNCU HARİÇ 2 tanesini comment olarak alırsanız program faturaları kaydetmeden sürekli bilgileri girerek sayfayı yenileyecektir, siz böylece bilgileri girereken sorun olup olmadığını görebilirsiniz.
