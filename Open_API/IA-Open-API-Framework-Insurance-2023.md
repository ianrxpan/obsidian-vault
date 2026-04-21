---
created: 2023-09-18
source: Insurance Authority (IA)
type: regulatory-framework
tags: [open-api, insurance, insurtech, hong-kong, digitalization]
related: [HKMA-Open-API-Framework-2018, open-banking]
---

# Open Application Programming Interface Framework for the Insurance Sector in Hong Kong

> **Publication Date:** 18 September 2023  
> **Source:** Insurance Authority (IA)  
> **URL:** https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Open_Application_Programming_Interface_Framework_for_the_Insurance_Sector.pdf

---

## Summary

保險業監管局（IA）發布的保險業 Open API 框架，旨在促進保險科技（Insurtech）生態系統的發展。與金管局的銀行業框架類似，採用協作分階段方式，而非強制性。框架強調數據交換、數據開放和數據互聯，最終目標是為公眾提供創新且可負擔的保險產品。

**背景：** 保險業越來越依賴數碼化來提高效率、簡化程序和降低營運支出。

---

## Policy Objectives (政策目標)

1. **促進數據共享** — 鼓勵持份者分享資訊，加強數據互聯
2. **提升系統接口** — 利用 Open API 增強系統接口和數據交換，營造創新和服務改進的環境
3. **推動創新合作** — 鼓勵市場參與者與 TSP 合作，利用 Open API 開發創新保險產品和服務
4. **靈活合規** — 允許獲授權保險公司灵活地将 Open API 整合到業務策略中，同時遵守行業標準和監管規定
5. **借鑒參考** — 參考本地、國家和海外金融監管機構發布的類似文件和指引

---

## Open API Possible Functions (可能的功能)

### Categories and Functions

| Category | Possible Functions |
|----------|-------------------|
| **Products and Services** | 產品詳情（ID、名稱、特色、保障、保費、T&C）、核保資訊（醫療記錄、年齡、性別、財務狀況） |
| **Customer Acquisition, Sales & Distribution** | 一般營銷和 URL 重定向、處理申請請求、追蹤申請狀態、合適性評估 |
| **Policy Administration & Servicing** | 檢索保單詳情、處理變更請求 |
| **Retrieval of Historical Data** | 萬能壽險產品履行比率和歷史紅利利率資訊 |
| **Claims Handling** | 處理和管理理賠 |
| **Others** | 客戶忠誠度和獎勵計劃資訊、售後服務、從其他金融機構獲取資訊、保險中介人管理 |

### Product Types Covered

**人壽保險：**
- 儲蓄保險 (Endowment)
- 投資相連保險 (Unit-linked)
- 萬能壽險 (Universal life)
- 終身壽險 (Whole life)
- 定期壽險 (Term life)
- 意外與健康保險 (Accident & health)
- 團體人壽保險 (Group life)

**一般保險：**
- 意外與健康、汽車、航空、船舶、財產損失、僱員補償、旅遊、醫療、家居及其他一般責任保險

---

## Open API Standard (API 標準)

### Communication Protocol
- **首選：** REST (Representational State Transfer) + JSON
- **另選：** SOAP + XML

### API Standards
- 支援不同版本並具有良好向後兼容性
- 允許功能錯誤的彈性處理

### Data Publication
- 須使用 **OpenAPI Specification (Swagger)** 發布數據定義和技術規格
- 可使用自有數據描述，無限制，但須公開

### Change Management
- 須有變更管理程序和適當披露
- 須安裝用戶報告問題/事件/故障的機制

---

## Security Standards (安全標準)

### Four Pillars
| Protection | Recommended Technology |
|-----------|----------------------|
| Authentication (TSP websites) | X.509 |
| Integrity & Confidentiality | Transport Layer Security (TLS) |
| Authentication of customers | Own methods |
| Authorization of customer | OAuth 2.0 |

### Key Requirements
- **密鑰/存取權杖保護** — 防止未經授權訪問的風險，配合加密和管理監督
- **風險基礎認證** — 僅在客戶同意下才授予合作 TSP 訪問特權
- **持續審查** — 須遵守監管機構关于安全使用科技的規定，並不時審查架構、API、數據和安全標準

---

## TSP Governance (第三方服務提供商管治)

### Core Principles
- 須涵蓋：內部控制、盡職調查、入職、監控、角色與責任劃分、問責、數據保護、安全、客戶保護、營運/基礎設施彈性、以及事件報告和處理
- 要求須公平、合理，並與涉及的風險相稱

### Contractual Arrangement
- 獲授權保險公司與合作 TSP 須簽訂雙邊協議
- 明確數據所有者和使用者的權利與責任

### Due Diligence (盡職調查)
- 參照 TSP 的業務概況、資質和財務狀況進行盡職調查

### Governance, Risk Management and Control
- 須有適當的風險治理框架和流程
- 包括風險管理和內部控制系統的政策和程序
- 須定期評估並採取適當的風險緩解措施，涵蓋：網路安全、系統彈性、數據洩露或隱私、數據誤用、責任和金融犯罪

### Technology Risk Management & Cyber Security
TSP 須具備的風險管理政策和程序涵蓋：
- IT 控制
- 系統可用性和穩定性
- 系統測試
- 系統和數據加密
- 系統變更
- 系統監控和安全
- 網路安全控制
- 事件響應和管理

### Data Protection (數據保護)
- **敏感個人資訊** — 保單和服務中的客戶數據包含敏感個人資訊（醫療記錄、年齡、性別、宗教、金融狀況）
- TSP 須明確說明數據收集並非由獲授權保險公司進行
- 第三方訪問須獲得客戶明確同意
- 須遵守《個人資料（私隱）條例》（第 486 章）等適用法律

### Fair Treatment & Consumer Protection
- 堅持「公平待客」原則
- 評估和降低 Open API 對客戶的風險和責任
- 須向客戶明確傳達公平的結算安排
- 須設有公平、響應迅速的信訪處理和申訴救濟機制

### System Resilience & Contingency Management
- 須有業務連續性計劃 (BCP)，涵蓋：危機管理流程、呼叫樹、業務恢復計劃、技術恢復計劃和替代站點計劃

### Ongoing Monitoring
- 持續監控合作 TSP 的合規情況
- 重大事件（如數據洩露）須即時上報

---

## Open API Repositories (API 倉庫)

- 獲授權保險公司須在其網站和/或其他線上倉庫發布：
  - Open API 應用資訊
  - 合作 TSP 名單
  - 相關 Open API 產品和服務
- 須提醒客戶防範欺詐網站和詐騙
- 主動偵測冒充合作 TSP 或虛假聲稱與獲授權保險公司合作的網站，並及時通知

---

## Future Development (未來發展)

- **成功案例展示** — IA 將與業界密切對話，豐富使用案例範圍
- **跨行業協作** — 與其他金融監管機構合作，培養跨行業和跨境應用
- **大灣區機遇** — 把握粵港澳大灣區數據互聯的機遇
- **定期審查** — 每兩年審查一次框架
- **統一合規** — 未來可能發布新指引，實現統一的基線要求合規

---

## Commencement

**生效日期：2023 年 9 月 18 日**

---

## Appendix 1: Use Cases (使用案例)

### A. iAM Smart
- OGCIO 於 2020 年推出，超過 100 萬註冊用戶，可訪問 160+ 項線上服務
- 2020 年推出測試沙盒，46 家獲授權保險公司和持牌保險中介人已參與

### B. Customer Experience
- 某獲授權保險公司利用 Open API 即時獲取銀行帳戶餘額，加快新保單簽發（解決以往需時數天的問題）
- Phase III 銀行 Open API 開放帳戶餘額、信用卡餘額、交易記錄和信用限額變動的即時訪問

### C. Commercial Data Interchange (CDI)
- 2022 年 10 月投產
- 金融機構可通過 API 從企業（尤其是中小企）獲取數據
- 應用於：KYC、產品設計、客戶獲取、風險管理

### D. Product Innovation
- COVID-19 後，按揭還款能力受影響
- 某獲授權保險公司通過 Open API 即時從合作銀行獲取個人數據
- 推出創新的醫療和意外保險產品，保護按揭人免受失業、疾病和死亡的財務壓力

---

## Appendix 2: Risk Assessment Checklist (風險評估檢查清單)

### A. Governance and Risk Management
1. 雙邊協議
2. 盡職調查記錄
3. 內部控制
4. 科技風險管理和網路安全
5. 數據保護指引
6. 業務連續性計劃
7. 持續監控

### B. Sound Consumer Protection Practices
1. 公平待客政策和程序
2. 合作 TSP 名單（須上傳至網站/倉庫）
3. 欺詐偵測和預防程序
4. 投訴處理政策和程序

---

## Comparison with HKMA Banking Framework

| Aspect | HKMA (Banking) | IA (Insurance) |
|--------|---------------|----------------|
| **Publication Date** | Jul 2018 | Sep 2023 |
| **Regulator** | Hong Kong Monetary Authority | Insurance Authority |
| **Approach** | Collaborative, phased | Collaborative, principles-based |
| **Phase I Timeline** | 6 months | Not strictly phased (flexible) |
| **TSP Governance** | 3 approaches (Bilateral preferred) | Bilateral agreements, due diligence |
| **Standard** | REST/JSON preferred | REST/JSON preferred, SOAP/XML also accepted |
| **Consumer Protection** | Registration + Terms & Conditions | Fair treatment + BCP + Monitoring |

---

## Metadata

- **Working Group Members:** 獲授權保險公司、顧問公司、科技公司和金融科技社群代表
- **Review Cycle:** Every 2 years
- **Related Frameworks:** HKMA Open API Framework for Banking Sector (2018)

---

## Footnotes

[^1]: iAM Smart - OGCIO digital identity platform, launched 2020, >1M users, 160+ services
[^2]: CDI - Commercial Data Interchange, live Oct 2022
