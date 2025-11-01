<h1 align="center">🤖 Zihin Sağlığı Destek Asistanı 🤖</h1>

<p align="center">
<a href="#kurulum"><img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python"></a>
<a href="#mimari"><img alt="Framework" src="https://img.shields.io/badge/LangChain-b504f4?style=for-the-badge&logo=langchain"></a>
<a href="#mimari"><img alt="Model" src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google"></a>
</p>

<p align="center">
<i>Akbank GenAI Bootcamp kapsamında, RAG mimarisi ile geliştirilmiş empatik bir chatbot.</i>
</p>




## 📌 İçindekiler


- [🎯 Projenin Amacı](#-projenin-amacı)
- [✨ Temel Özellikler](#-temel-özellikler)
- [📚 Veri Seti](#-veri-seti)
- [🛠️ Kullanılan Yöntemler ve Mimari](#%EF%B8%8F-kullanılan-yöntemler-ve-mimari)
- [🏗️ Proje Yapısı](#%EF%B8%8F-proje-yapısı)
- [🚀 Kurulum ve Çalıştırma Kılavuzu](#-kurulum-ve-çalıştırma-kılavuzu)
- [🧪 Test ve Geliştirme](#-test-ve-geliştirme)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📄 Lisans](#-lisans)


## 🎯 Projenin Amacı

Projenin temel hedefi, zihin sağlığı konularında güvenilir ve destekleyici bir diyalog ortamı sunmaktır. Chatbot, kullanıcılara tıbbi tavsiye vermeden, yalnızca sağlanan veri setindeki bilgiler doğrultusunda, şefkatli ve yargılayıcı olmayan bir üslupla yanıtlar üretir. Bu proje, RAG mimarisinin ve modern dil modellerinin (LLM) pratik bir uygulamasını sergilemeyi amaçlamaktadır.


## ✨ Temel Özellikler


- 🧠 **Empatik Yanıtlar:** Kullanıcıları yargılamadan, destekleyici bir tonla cevap üretir.
- 🔎 **RAG Tabanlı Mimari:** Dış kaynaklı bilgileri kullanarak daha doğru ve bağlama uygun sonuçlar üretir.
- ⚙️ **Modüler Kod Yapısı:** Gömme, getirici ve üretici bileşenler ayrı dosyalarda yönetilir.
- ☁️ **Google Colab Desteği:** Çevrimiçi çalıştırma için hazır Jupyter defteri içerir.
- 🧩 **Kolay Özelleştirme:** Model, veri seti ve prompt bileşenleri hızla güncellenebilir.


## 📚 Veri Seti


**Veri Seti İçeriği:** Zihin sağlığı, psikolojik durumlar, semptomlar ve başa çıkma stratejileri gibi çeşitli konuları kapsayan metinler içerir.


 **Hazırlık Süreci:** Veri seti, RAG mimarisine uygun hale getirmek için aşağıdaki adımlardan geçirilmiştir:


1. HuggingFaceDatasetLoader ile veri seti LangChain `Document` formatında yüklenir.
2. `RecursiveCharacterTextSplitter` ile metinler, anlamsal bütünlüğü koruyacak şekilde küçük parçalara ayrılır.
3. Her bir parça embedding modeli ile vektör uzayına taşınır ve FAISS üzerine indekslenir.


## 🛠️ Kullanılan Yöntemler ve Mimari


Proje, güncel bir RAG (Retrieval-Augmented Generation) mimarisi üzerine inşa edilmiştir. Bu mimari, dil modelinin yanıtlarını harici bir bilgi kaynağı ile zenginleştirerek daha doğru ve bağlama uygun sonuçlar üretmesini sağlar.


<p>
<img src="https://img.shields.io/badge/LangChain-b504f4?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
<img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
<img src="https://img.shields.io/badge/FAISS-4B83DE?style=for-the-badge" alt="FAISS">
<img src="https://img.shields.io/badge/Gradio-FF7600?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face">
</p>


### Çalışma Akışı

1. **Yükleme & Parçalama:** Zihin sağlığı veri seti (`aneerajsk/medchat_mental`) yüklenir ve anlamsal bütünlük korunarak parçalara ayrılır.
2. **Gömme (Embedding):** `all-MiniLM-L6-v2` modeli ile her parça vektörel temsile dönüştürülür.
3. **İndeksleme:** Vektörler FAISS veritabanına yüklenir ve hızlı arama için indekslenir.
4. **Sorgu & Getirme:** Kullanıcı sorgusu embedding'e dönüştürülerek en ilgili bağlam parçaları seçilir.
5. **Zenginleştirme & Yanıt:** Seçilen bağlam parçaları ile birlikte Gemini modeline gönderilen prompt, bağlama duyarlı ve empatik yanıtlar üretir.

## 🏗️ Proje Yapısı

```text
mental-health-chatbot/
├── app.py                # Gradio arayüzünü başlatır
├── embedder.py          # Embedding modelinin kurulumu ve kullanımı
├── generator.py         # LLM (Gemini) ile yanıt üretimi
├── retriever.py         # FAISS üzerinden bağlam getirme mantığı
├── mhcb.ipynb           # Colab üzerinde çalıştırılabilir not defteri
├── requirements.txt     # Proje bağımlılıkları
└── README.md            # Bu dosya
```

Bu yapı sayesinde her bileşen ayrı bir dosyada tutulur ve geliştirme süreci modüler hale getirilir.

## 🚀 Kurulum ve Çalıştırma Kılavuzu 

Projeyi ister Google Colab üzerinde ister yerelde çalıştırabilirsiniz.

### 🔑 Google Colab Üzerinde (Önerilen)

1. `mhcb.ipynb` dosyasını Google Colab'de açın.
2. Sol menüden **Anahtar (🔑)** simgesine tıklayarak yeni bir gizli bilgi ekleyin.
3. İsim olarak `GEMINI_API_KEY` girin ve Google AI Studio'dan aldığınız API anahtarınızı yapıştırın.
4. **Runtime ▸ Run all** seçeneği ile tüm hücreleri sırasıyla çalıştırın (gerekli kütüphaneler otomatik kurulacaktır).
5. Son hücre tamamlandığında `.gradio.live` uzantılı bir bağlantı oluşur; arayüze bu link üzerinden erişebilirsiniz.

### 💻 Lokal Üzerinde

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/Ms-Crocus/mental-health-chatbot.git
   cd mental-health-chatbot
   ```
2. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
3. **API anahtarınızı ayarlayın:** Proje kök dizininde `.env` dosyası oluşturup aşağıdaki değeri ekleyin:
   ```env
   GEMINI_API_KEY="BURAYA_API_ANAHTARINIZI_GIRIN"
   ```
   > `.env` dosyasının `.gitignore` içinde yer aldığından emin olun.
4. **Uygulamayı başlatın:**
   ```bash
   python app.py
   ```
   Komut, varsayılan olarak `http://127.0.0.1:7860` adresinde çalışan bir Gradio arayüzü başlatacaktır.

## 🧪 Test ve Geliştirme

- Kod değişikliklerinden sonra `python -m compileall` ile temel sözdizimi kontrolleri yapılabilir.
- Bileşenleri modüler olarak geliştirmek için `embedder.py`, `retriever.py` ve `generator.py` dosyaları ayrı ayrı test edilebilir.
- Deneysel prompt güncellemelerini `app.py` içindeki arayüz fonksiyonları veya `mhcb.ipynb` defteri üzerinden hızlıca doğrulayabilirsiniz.

## 🤝 Katkıda Bulunma

1. Fork alın ve yeni bir dal oluşturun.
2. Değişikliklerinizi yapıp test edin.
3. Açıklayıcı commit mesajları ile katkınızı gönderin.
4. Pull Request oluştururken yaptığınız değişiklikleri detaylıca anlatan bir açıklama ekleyin.


## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
