# JenTalk 網站動畫規範

動畫只用於引導閱讀、回應操作、揭露狀態或呈現進度。標題、表單及主要按鈕從第一個畫面即可讀取或操作。成人學習流程以清楚、安定為優先。

## 共用參數

`app/static/css/site-motion.css` 集中定義快速反饋 140 ms、狀態切換 220 ms、進場 340 ms，以及 45 ms 的同批錯開間隔。位移從 10 px 開始，卡片越過定位點最多 2 px。進場使用 `cubic-bezier(.16,1,.3,1)`，狀態淡入使用 ease-out。

## 元件與新增頁面

- 繼承 `base.html` 的頁面會載入共用資源。獨立 Jinja 頁面可在 head 引入 `_motion_assets.html`。
- 離開首屏的重點卡片可加 `data-motion-reveal`。共用 IntersectionObserver 在第一次入場後取消觀察。內容預設可見，焦點不等待動畫。
- 首頁 Hero 依原有文字行進場，合照與副標淡入。課程、教案及心得卡片採一次進場。按鈕用輕量的按壓和懸停變化。
- 保留原生 details、輪播的既有狀態與測驗的題目、答案、計分來源。課堂測驗只在目前題目、選項及已公開回饋上套用樣式。
- 原生 POST 表單可加 `data-motion-submit`，並放入帶 `role="status"` 的 `data-motion-status`。在原生驗證通過後顯示送出狀態並防止同頁連點。AJAX 表單及跨頁請求的伺服器端去重各有獨立責任。

## 無障礙與效能

揭露與空間位移僅在使用者允許動態效果時播放。減少動態效果時保留焦點外框、即時狀態及短淡入。以鍵盤及觸控確認可操作性，測量手機版是否溢出。動畫優先用 opacity、translate、scale，避免動畫化尺寸、陰影或濾鏡。避免全頁遮罩、捲動接管、持續動畫及逐幀版面測量。

## 工具選擇

已安裝 Web Animation Skills 的 60fps-animation、accessible-animation、ascii-animation、glassmorphism、gsap-web、lottie-animation、micro-interaction、page-transition-animation、svg-animation。技能套件採 MIT 授權。選用原生 CSS 與 JavaScript，進場、互動和降階方案可由 Flask 靜態檔提供，PythonAnywhere 不需 Node。

## 分支基準

此分支以 GitHub 上的 Flask／Jinja 品牌站原始碼為基準。正式站後續更新需在部署前併入，包含首頁合照、輪播、手機導覽和 Google 表單連結。每日英文獨立站位於 `kevinooll/daily-english-test`。
