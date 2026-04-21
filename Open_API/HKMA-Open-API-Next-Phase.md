---
created: 2021-03
source: HKMA (commissioned Accenture research)
type: research-report
tags: [open-api, banking, hong-kong, fintech, smart-banking, phase-iii, phase-iv]
related: [HKMA-Open-API-Framework-2018, open-banking]
---

# The Next Phase of the Banking Open API Journey

> **Publication Date:** March 2021  
> **Source:** Hong Kong Monetary Authority (HKMA), research by Accenture  
> **URL:** https://www.hkma.gov.hk/media/eng/doc/key-functions/ifc/fintech/The_Next_Phase_of_the_Banking_Open_API_Journey.pdf

## Summary

2021年HKMA委托Accenture進行研究，分析香港銀行業Open API Phase I和II嘅實施狀況，並為Phase III（帳戶資訊）和Phase IV（交易）嘅實施提出建議。COVID-19加速了數碼化轉型，Open API成為銀行與第三方服務提供商（TSP）合作創新嘅關鍵技術。

---

## 實施狀況（截至2020年Q3）

### Phase I & II 成績

| 指標 | 數據 |
|------|------|
| 參與銀行 | 超過20間 |
| 推出Open API數量 | 超過800個 |
| TSP登記數量 | 超過900個（Q3 2020） |
| API呼叫增長 | Q3 2020相比Q4 2019增長70倍 |

### 銀行準備情況

| 範疇 | 準備好的銀行比例 |
|------|----------------|
| 已定義/Open API策略 | 93% |
| 已建立/計劃建立中央團隊 | 50% |
| 已建立/計劃建立業務單位 | 68% |
| 已建立/計劃建立IT團隊 | 68% |
| 已開發Open API基礎設施 | 86% |
| 已分配預算 | 89% |

### TSP準備情況

| 範疇 | 比例 |
|------|------|
| 已投資/計劃投資Open API | 68% |
| 投資金額≥US$500,000 | 52% |
| 已建立/計劃建立基礎設施 | 61% |

---

## Phase III & IV 面臨的挑戰

### 銀行和TSP的主要挑戰

1. **欺詐和網絡安全風險** — Phase III/IV涉及敏感客戶數據共享
2. **技術開發複雜性** — 整合 legacy 系統難度大
3. **識別使用場景困難** — 難以發現可行嘅商業模式
4. **擔心因合作方過失而被單獨追責**
5. **客戶對數據隱私嘅關注** — 71%香港客戶關注數據隱私

### SME關注點
- 對向TSP提供數據持謹慎態度
- 擔心數據洩露影響業務

---

## Phase III & IV 實施七大必要實踐

### 1. 採用適當的風險管理策略

**主要風險類型：**

| 風險類型 | 描述 |
|---------|------|
| 網絡安全風險 | 外部接口增加，駭客入侵風險上升 |
| 數據隱私風險 | 未經授權的數據訪問或用於同意範圍外用途 |
| 系統韌性風險 | 第三方連接增加，單點故障風險 |
| 欺詐風險 | 身份盜竊或未授權交易 |
| 洗錢風險 | 資金通過Open API流動 |

### 2. 引入適當的保護機制

#### 數據保護與保留
- 遵守《個人資料（私隱）條例》
- 與PCPD發布的相關執業守則一致

#### 客戶同意
- 明確同意才能使用帳戶資訊和交易
- 客戶可随时查閱、管理或撤回同意
- 建議使用雙重認證

#### 認證方式
1. **重新導向模式（Redirection）** — 客戶從TSP應用被導向銀行app認證
2. **解耦模式（Decoupled）** — 銀行和TSP分別認證，獨立驗證

#### 防止欺詐
- 識別並區分釣魚訊息
- 確保客戶面向界面有最新安全補丁
- 定期網絡安全意識培訓

#### 責任管理
- 客戶不對因TSP使用銀行Open API造成的未授權交易損失負責（除非欺詐或重大過失）
- 銀行和TSP合約中明確責任和結算安排

### 3. 為客戶設計有吸引力嘅Open API產品

**目標客戶群選擇** — 識別合適的目標細分市場

**釋放使用場景嘅全部潛力**
- 避免部分啟用的使用場景（例如：無直通式處理導致數據集不完整）
- 需要充分的研究和原型設計

**教育客戶**
- 銀行帶頭教育客戶關於Open API嘅知識
- 提醒客戶查閱銀行的合作TSP列表
- 警惕假冒網站和電話詐騙

### 4. 理解銀行需要的能力

| 能力範疇 | 具體要求 |
|---------|---------|
| **願景與策略** | 明確定位（數據提供者/消費者/兩者） |
| **核心系統現代化** | 考慮解耦架構以支持數據共享 |
| **客戶認證** | OAuth 2.0、OpenID Connect框架 |
| **開發者入口網站** | 讓第三方開發者方便接入 |
| **信息安全與網絡韌性** | 訪問控制、數據丢失預防、漏洞管理、加密、交易風險分析 |

### 5. 理解TSP需要的能力

**TSP三種角色：**

| 角色 | 描述 |
|------|------|
| **帳戶資訊整合商** | 利用客戶數據提供個人/企業財務管理服務 |
| **支付啟動服務提供商** | 在第三方平台啟動支付 |
| **技術服務提供商** | 為其他TSP提供統一API連接不同銀行 |

**TSP數據管理能力：**
- 數據聚合 — 從各銀行攝取和整合原始數據
- 數據豐富 — 用額外上下文（地理位置、時間、設備等）強化數據
- 數據分割 — 分割數據集用於分析
- 數據分析和洞察 — 創建數據模型捕捉洞察

### 6. 選擇適當的商業/財務模式

**直接變現模式：**
- 免費增值模式（Freemium）
- 第三方支付
- 第三方收費
- 終端用戶支付

**間接變現模式：**
- 增加覆蓋和知名度
- 個性化提升
- 效率提升

### 7. 監察Open API生態系統

**欺詐監察**
- 定期檢討欺詐交易統計報告
- 識別系統性風險並開發解決方案

**API可用性和性能監察**
- 定期檢討KPI（API可用性、響應時間、成功呼叫率）
- 主動監察最新網絡威脅

---

## Phase III & IV 實施建議措施

### 5.1 分階段實施

| 階段 | 內容 | 建議時間表 |
|------|------|-----------|
| Phase III 第一批 | 存款帳戶資訊、信用卡資訊 | 2021-2022 |
| Phase III 第二批 | 投資、保險相關資訊 | 2022-2023 |
| Phase IV | 交易和支付 | 2023之後 |

### 5.2 Open API技術標準化

- REST + JSON（已確定）
- OAuth 2.0授權
- OpenAPI Specification (Swagger)
- FAPI（Financial API）標準

### 5.3 Common Baseline改進

Phase II及更高階段的TSP管治需要：
- 更嚴格的入職檢查
- 持續監控機制
- 銀行和TSP之間的雙邊合約

### 5.4 其他保護措施

- **披露和透明度** — 向客戶清楚展示數據收集和使用目的
- **投訴和補償管理** — 訂明銀行和TSP之間的投訴處理機制

---

## 與HKMA Open API Framework 2018嘅關係

| 項目 | 2018框架 | Next Phase建議 |
|------|---------|---------------|
| **Phase I/II** | 已實施 | 成效良好 |
| **Phase III** | 待定 | 建議分階段實施 |
| **Phase IV** | 待定 | 技術複雜性最高，需更多準備 |
| **TSP管治** | 共同基準（首選） | 建議更嚴格的持續監控 |
| **技術標準** | REST+JSON, OAuth 2.0 | 建議加入FAPI標準 |

---

## 重要術語

| 術語 | 解釋 |
|------|------|
| TSP | Third Party Service Provider 第三方服務提供商 |
| iCAST | Intelligence-led Cyber Attack Simulation Testing |
| CFI | Cybersecurity Fortification Initiative 網絡防衛計劃 |
| C-RAF | Cyber Resilience Assessment Framework |
| FAPI | Financial API |
| SME | Small and Medium Enterprise 中小企業 |

---

## Metadata

- **研究方法：** Accentrue對28間銀行（包括所有虛擬銀行）和31間TSP進行行業調查，並對53個機構進行訪談
- **調查時間：** 2020年9-10月
- **資訊來源：** HKMA官方網頁

---

*最後更新：2026-04-21*
