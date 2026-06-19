import streamlit as st

st.set_page_config(page_title="Your English Landing", layout="wide")

# ====== 你可以改成自己的品牌設定 ======
BRAND = "JenTalk"
CTA_TEXT = "立即索取免費課程"
TOP_MENU = ["優惠活動", "課程教材", "我們的老師", "部落格", "課程方案及費用", "聯絡我們", "企業培訓", "常見問題"]
PROMO_TEXT = "指定方案 $11,111 持續熱銷中｜雙 11 好評延長・年末加碼回饋"

# 圖片：建議換成你自己的（避免版權）
LEFT_IMG = "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=1200&q=80"
RIGHT_IMG = "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=1200&q=80"

# ====== CSS：做出類似 Engoo 的版面 ======
st.markdown(
    """
<style>
/* 全局 */
.block-container { padding-top: 0.7rem; padding-bottom: 0rem; max-width: 1200px; }
html, body, [class*="css"]  { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif; }
a { text-decoration: none; }

/* 頂部導覽列 */
.navbar {
  position: sticky; top: 0; z-index: 1000;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,0.06);
  padding: 14px 0;
}
.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 10px;
  display: flex;
  align-items: center;
  gap: 18px;
}
.brand {
  display: flex; align-items: center; gap: 10px;
  font-weight: 800; font-size: 20px; letter-spacing: 0.2px;
}
.brand-badge {
  width: 28px; height: 28px; border-radius: 8px;
  background: #ff7a00;
  display: inline-flex; align-items: center; justify-content: center;
  color: white; font-weight: 900;
}
.nav-links { display: flex; gap: 18px; flex-wrap: wrap; margin-left: auto; margin-right: 8px; }
.nav-links span { color: #222; font-size: 14px; opacity: 0.85; }
.nav-actions { display: flex; gap: 10px; align-items: center; }
.btn-ghost {
  padding: 8px 12px; border-radius: 999px;
  border: 1px solid rgba(0,0,0,0.12);
  background: white; color: #222; font-size: 14px;
}
.btn-primary {
  padding: 9px 14px; border-radius: 999px;
  border: 1px solid rgba(0,0,0,0.00);
  background: #ff7a00; color: white; font-size: 14px; font-weight: 700;
}

/* Hero 區 */
.hero-wrap {
  background: #efefef;
  border-radius: 18px;
  padding: 34px 28px;
  margin-top: 18px;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1.1fr 1fr;
  gap: 22px;
  align-items: center;
}
.hero-img {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 16px;
  overflow: hidden;
  background: #ddd;
}
.hero-img img { width: 100%; height: 100%; object-fit: cover; display: block; }
.hero-center { text-align: center; padding: 0 10px; }
.hero-title {
  font-size: 52px; font-weight: 900; line-height: 1.02;
  margin: 0 0 10px 0; color: #111;
}
.hero-sub { font-size: 22px; margin: 0 0 22px 0; color: #333; opacity: 0.9; }
.hero-cta {
  display: inline-flex; align-items: center; justify-content: center;
  background: #ff7a00; color: white;
  padding: 14px 22px;
  border-radius: 999px;
  font-size: 18px;
  font-weight: 800;
  border: none;
}
.hero-cta small { opacity: 0.9; font-weight: 700; }

/* 黑色促銷條 */
.promo-bar {
  margin-top: 16px;
  background: #0f0f0f;
  color: white;
  border-radius: 14px;
  padding: 16px 18px;
  font-size: 20px;
  font-weight: 800;
  display: flex;
  justify-content: center;
  text-align: center;
}
.promo-bar span { color: #ff7a00; margin: 0 6px; }

/* 內容區塊 */
.section { margin: 26px 0 0; }
.section h2 { font-size: 26px; margin: 0 0 10px; }
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}
.card {
  border: 1px solid rgba(0,0,0,0.08);
  background: white;
  border-radius: 16px;
  padding: 16px;
  box-shadow: 0 10px 26px rgba(0,0,0,0.04);
}
.card .k { font-weight: 900; font-size: 16px; margin-bottom: 6px; }
.card .d { color: #333; opacity: 0.85; font-size: 14px; line-height: 1.6; }

@media (max-width: 980px) {
  .hero-grid { grid-template-columns: 1fr; }
  .hero-center { order: 0; }
  .hero-title { font-size: 42px; }
  .cards { grid-template-columns: 1fr; }
  .nav-links { display: none; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ====== 導覽列 ======
nav_links_html = "".join([f"<span>{x}</span>" for x in TOP_MENU])

st.markdown(
    f"""
<div class="navbar">
  <div class="nav-inner">
    <div class="brand">
      <div class="brand-badge">J</div>
      <div>{BRAND}</div>
    </div>
    <div class="nav-links">{nav_links_html}</div>
    <div class="nav-actions">
      <button class="btn-ghost" onclick="window.scrollTo(0,0)">登入</button>
      <button class="btn-primary" onclick="window.location.href='#cta'">註冊會員</button>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ====== Hero ======
st.markdown(
    f"""
<div class="hero-wrap" id="top">
  <div class="hero-grid">
    <div class="hero-img"><img src="{LEFT_IMG}" alt="left"/></div>

    <div class="hero-center">
      <div class="hero-title">IMPROVE<br/>YOUR ENGLISH</div>
      <div class="hero-sub">Anytime, Anywhere</div>
      <a class="hero-cta" id="cta" href="#form">{CTA_TEXT} &nbsp;›</a>
      <div style="margin-top:10px; font-size:14px; color:#555; opacity:0.9;">
        外師一對一口說｜可客製教材｜可試聽再決定
      </div>
    </div>

    <div class="hero-img"><img src="{RIGHT_IMG}" alt="right"/></div>
  </div>
</div>

<div class="promo-bar">
  {PROMO_TEXT.replace("｜", "<span>•</span>")}
</div>
""",
    unsafe_allow_html=True,
)

# ====== 內容區（你可以改成你的文案） ======
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## 為什麼選我們？")

st.markdown(
    """
<div class="cards">
  <div class="card">
    <div class="k">一對一口說｜不尷尬</div>
    <div class="d">從旅遊到職場，老師會用你的程度帶你講出來，不是背完才敢開口。</div>
  </div>
  <div class="card">
    <div class="k">老師嚴選｜教法有系統</div>
    <div class="d">不是隨便聊天：每堂課有目標、有糾音、有回饋，讓你真的進步。</div>
  </div>
  <div class="card">
    <div class="k">教材客製｜你需要的才學</div>
    <div class="d">旅遊英文、面試英文、會議英文、托益口說，全部可依你的需求安排。</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("## 立即索取免費課程（示範表單）")
with st.form("form"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("姓名")
        line = st.text_input("LINE ID（或電話）")
    with c2:
        goal = st.selectbox("學習目標", ["旅遊口說", "職場口說", "面試英文", "基礎會話", "其他"])
        level = st.selectbox("目前程度", ["零基礎", "初階", "中階", "中高階"])
    msg = st.text_area("你最想解決的問題（選填）", placeholder="例如：出國不敢開口、面試回答很卡、發音想改善…")
    submitted = st.form_submit_button("送出資料")
    if submitted:
        st.success("已收到！(示範) 你可以在這裡改成寫入 Google Sheet / DB / 發送 LINE 通知。")

st.caption("⚠️ 圖片目前使用佔位圖。正式上線請改成你自己的圖片與品牌視覺，避免版權問題。")
