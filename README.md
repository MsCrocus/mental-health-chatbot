<h1 align="center">🤖 Zihin Sağlığı Destek Asistanı 🤖</h1>

<p align="center">
<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python"></a>
<a href="#"><img alt="Framework" src="https://img.shields.io/badge/LangChain-b504f4?style=for-the-badge&logo=langchain"></a>
<a href="#"><img alt="Model" src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google"></a>
</p>

<p align="center">
<i> Akbank GenAI Bootcamp kapsamında, RAG mimarisi ile geliştirilmiş empatik bir chatbot. </i>
</p>


🎯 1. Projenin Amacı

Projenin temel hedefi, zihin sağlığı konularında güvenilir ve destekleyici bir diyalog ortamı sunmaktır. Chatbot, kullanıcılara tıbbi tavsiye vermeden, yalnızca sağlanan veri setindeki bilgiler doğrultusunda, şefkatli ve yargılayıcı olmayan bir üslupla yanıtlar üretir. Bu proje, RAG mimarisinin ve modern dil modellerinin (LLM) pratik bir uygulamasını sergilemeyi amaçlamaktadır.


📚 2. Veri Seti Hakkında Bilgi

Projede, Hugging Face platformunda halka açık olarak sunulan aneerajsk/medchat_mental veri seti kullanılmıştır.
 

Veri Seti İçeriği:  Bu veri seti, zihin sağlığı, psikolojik durumlar, semptomlar ve başa çıkma stratejileri gibi çeşitli konuları kapsayan metinler içermektedir.

Hazırlık Süreci:  Veri seti, RAG mimarisine uygun hale getirmek için aşağıdaki adımlardan geçirilmiştir:

HuggingFaceDatasetLoader kullanılarak veri seti doğrudan LangChain Document formatında yüklenmiştir.

RecursiveCharacterTextSplitter ile metinler, anlamsal bütünlüğü koruyacak şekilde daha küçük ve yönetilebilir parçalara (chunk) ayrılmıştır.


🛠️ 3. Kullanılan Yöntemler ve Çözüm Mimarisi

Proje, güncel bir RAG (Retrieval-Augmented Generation) mimarisi üzerine inşa edilmiştir. Bu mimari, dil modelinin yanıtlarını harici bir bilgi kaynağı ile zenginleştirerek daha doğru ve bağlama uygun sonuçlar üretmesini sağlar.

Kullanılan Teknolojiler

<p>
<img src="https://img.shields.io/badge/LangChain-b504f4?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
<img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
<img src="https://img.shields.io/badge/FAISS-4B83DE?style=for-the-badge" alt="FAISS">
<img src="https://img.shields.io/badge/Gradio-FF7600?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face">
</p>




<details>
<summary><b>➡️ Detaylı Çalışma Akışını Görmek İçin Tıklayın</b></summary>
<p>
<ol>
<li><b>Yükleme & Parçalama:</b> Zihin sağlığı veri seti (<code>aneerajsk/medchat_mental</code>) yüklenir ve metinler, anlamsal bütünlüğü koruyacak şekilde daha küçük parçalara (<code>chunk</code>) ayrılır.</li>
<li><b>Gömme (Embedding):</b> Her bir metin parçası, <code>all-MiniLM-L6-v2</code> modeli kullanılarak anlamsal bir vektöre dönüştürülür. Bu vektörler, metnin anlamını sayısal olarak temsil eder.</li>
<li><b>İndeksleme:</b> Oluşturulan bu vektörler, hızlı ve verimli bir şekilde aranabilmeleri için FAISS vektör veritabanına yüklenir ve indekslenir.</li>
<li><b>Sorgu & Getirme (Query & Retrieval):</b> Kullanıcı bir soru sorduğunda, bu soru da aynı embedding modeli ile bir vektöre dönüştürülür. FAISS, bu sorgu vektörüne en çok benzeyen metin parçalarını (<code>context</code>) veritabanından bulur ve getirir.</li>
<li><b>Zenginleştirme & Oluşturma (Augment & Generation):</b> Kullanıcının orijinal sorusu ile veritabanından getirilen ilgili metin parçaları (<code>context</code>), Gemini modeline gönderilecek olan bir prompt şablonuna yerleştirilir.</li>
<li><b>Yanıt:</b> Gemini, bu zenginleştirilmiş prompt'u kullanarak, hem kullanıcının sorusuna cevap veren hem de sağlanan bağlama sadık kalan, tutarlı ve empatik bir yanıt üretir.</li>
</ol>
</p>
</details>

<p align="right"><a href="#-i̇çindekiler">🔝 Başa dön</a></p>

🚀 4. Çalıştırma Kılavuzu

Projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

 🔑 Google Colab Üzerinde (Önerilen)

1. Proje ipynb dosyasını Google Colab'de açın.

2. Sol taraftaki menüden Anahtar (🔑) simgesine tıklayın ve "Yeni sır ekle" seçeneğini kullanın.

3. İsim olarak GEMINI_API_KEY girin ve Değer olarak Google AI Studio'dan aldığınız API anahtarınızı yapıştırın.

4. "Tümünü çalıştır" seçeneği ile tüm hücreleri başlatın. Gerekli kütüphaneler otomatik olarak kurulacaktır.

5. Son hücre çalıştığında, herkese açık bir .gradio.live linki oluşturulur. Bu link üzerinden arayüze erişebilirsiniz.


💻 Lokal üzerinde

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1.  **Depoyu klonlayın:**
    ```bash
    git clone [https://github.com/Ms-Crocus/mental-health-chatbot.git](https://github.com/Ms-Crocus/mental-health-chatbot.git)
    cd mental-health-chatbot
    ```

2.  **Gerekli kütüphaneleri yükleyin:**
    Proje için bir `requirements.txt` dosyası oluşturmanız tavsiye edilir.

    ```bash
    pip install -r requirements.txt
    ```

3.  **API Anahtarınızı ayarlayın:**
    Proje kök dizininde `.env` adında bir dosya oluşturun ve içine Google Gemini API anahtarınızı ekleyin:
    ```
    GEMINI_API_KEY="BURAYA_API_ANAHTARINIZI_GIRIN"
    ```
    *(Not: `.gitignore` dosyanıza `.env` dosyasını eklemeyi unutmayın!)*

4.  **Uygulamayı çalıştırın:**
    (Gradio uygulamanızı çalıştıran Python dosyasının adını varsayarak, örn: `app.py`)
    ```bash
    python app.py
    ```
    Uygulama başladığında size yerel bir URL (örn: `http://127.0.0.1:7860`) verecektir.




6. 📦 Gerekli Kütüphaneler (requirements.txt)


   Projenin çalışması için gereken ana kütüphaneler:

-   `langchain-google-genai`
-   `langchain-core`
-   `langchain-text-splitters`
-   `langchain-community`
-   `faiss-cpu` (veya GPU versiyonu)
-   `gradio`
-   `sentence-transformers` (all-MiniLM-L6-v2 için)
