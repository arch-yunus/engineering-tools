# Bulut Bilişim ve Mikroservis Altyapıları (Cloud & DevOps)

Mühendislik uygulamaları artık sadece yerel bilgisayarlarda çalışmamakta; bulut platformları (AWS, Azure, GCP) üzerinde ölçeklenebilir mikroservis mimarileri olarak koşturulmaktadır. IoT (Nesnelerin İnterneti) sensör verilerinin toplanması, CAD çizimlerinin bulutta render edilmesi ve yapay zeka modellerinin eğitilmesi bu altyapılar sayesinde gerçekleştirilir.

## Docker ve Konteyner Teknolojisi

Konteynerleştirme, yazılım uygulamalarının ve tüm bağımlılıklarının (kütüphaneler, ayarlar) her ortamda (geliştirme, test, canlı sunucu) tutarlı bir şekilde çalışmasını sağlar. Docker, bu alandaki standart araçtır.

### Örnek Dockerfile (Python Uygulaması için)
Mühendislik veri analiz aracımızı konteyner haline getirmek için kullanılabilecek bir `Dockerfile`:

```dockerfile
# Resmi Python imajını kullan
FROM python:3.10-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli paket tanımlarını kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodları konteyner içine aktar
COPY . .

# Uygulamayı çalıştır
CMD ["python", "run_tools.py"]
```

### Örnek docker-compose.yml (Uygulama + Veri Tabanı)
Hem analiz aracını hem de PostgreSQL veri tabanını birlikte ayağa kaldırmak için:

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: eng_user
      POSTGRES_PASSWORD: eng_password
      POSTGRES_DB: eng_db
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  app:
    build: .
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://eng_user:eng_password@db:5432/eng_db
    stdin_open: true # CLI etkileşimi için
    tty: true

volumes:
  pgdata:
```

---

## AWS & Azure Mühendislik Servisleri

| Servis Alanı | AWS Çözümü | Azure Çözümü | Mühendislik Kullanım Senaryosu |
| :--- | :--- | :--- | :--- |
| **Sanal Sunucu** | EC2 | Virtual Machines | Ağır sonlu elemanlar analizi (FEA) simülasyonları çalıştırma |
| **Nesne Depolama** | S3 | Blob Storage | Büyük CAD montaj dosyalarının ve 3D modellerin saklanması |
| **IoT Veri Akışı** | IoT Core | IoT Hub | Fabrikadaki PLC'lerden gelen anlık sensör verilerinin toplanması |
| **Veritabanı** | RDS | Azure SQL | Kalite standartları ve üretim geçmişi verilerinin saklanması |
