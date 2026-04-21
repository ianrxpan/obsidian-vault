---
created: 2018-07-18
source: HKMA
type: regulatory-framework
tags: [open-api, banking, hong-kong, fintech, smart-banking]
related: [open-banking]
---

# Open API Framework for the Hong Kong Banking Sector

> **Publication Date:** 18 July 2018  
> **Source:** Hong Kong Monetary Authority (HKMA)  
> **URL:** https://www.hkma.gov.hk/media/eng/doc/key-information/press-release/2018/20180718e5a2.pdf

## Summary

香港金管局發布的銀行業 Open API 框架，是「智能銀行」七大舉措之一。框架採用**協作性、分階段**方式，而非強制性（不像歐盟、英國、澳洲）。目的是提升銀行業競爭力、提供安全的創新環境，與國際接軌。

---

## Policy Objectives (政策目標)

1. **確保銀行競爭力** — 保持香港銀行業的競爭力和相關性
2. **安全創新環境** — 為銀行與第三方服務提供商 (TSP) 提供安全、受控、便利的環境，開發創新整合服務
3. **國際接軌** — 跟上國際銀行服務交付的發展趨勢

---

## Open API Categories (四類功能)

| Category | Phase | Timeline | Protection Required |
|----------|-------|----------|---------------------|
| **Product & Service Information** | Phase I | 6 months | Integrity + Confidentiality |
| **Subscription / New Applications** | Phase II | 12-15 months | Authentication of TSPs + Banks + Integrity |
| **Account Information** | Phase III | TBD (within 12 months) | Authentication + Authorisation + Integrity + Confidentiality |
| **Transactions** | Phase IV | TBD (within 12 months) | All of the above |

---

## Phased Implementation Timeline

```
Publication (18 Jul 2018)
│
├─ Phase I:  Product & Service Information    → 6 months (Jan 2019)
│             (Open data - like IT industry familiar with)
│
├─ Phase II: Subscription & New Applications  → 12-15 months (Jul-Sep 2019)
│             (More sophisticated auth + infrastructure)
│
├─ Phase III: Account Information             → Within next 12 months
│              (Balance, transaction history, limits, payments)
│
└─ Phase IV:  Transactions                     → Within next 12 months
               (Payment/transfer initiation by authenticated customers)
```

---

## Guiding Principles (指導原則)

- **8.1** Open API 實施將為銀行和客戶帶來效益，行業界表示歡迎
- **8.2** 採用**協作分階段**方式，非強制性（對比歐盟、英國、澳洲）
- **8.3** 框架保持高層次，給予銀行彈性制定策略
- **8.4** Open API 功能基於效益和機會/風險優先排序
- **8.5** 借鑒現有國際/行業實踐

---

## TSP Governance (第三方服務提供商管治)

### Three Approaches

1. **Bilateral** — 銀行自行對 TSP 做風險評估和盡職調查
2. **Central Entity** — 所有銀行共同出资建立中央實體，統一 TSP 治理標準
3. **Bilateral with Common Baseline** ← **首選方式** — 銀行間建立共同基準，簡化入職流程

### Phase I (Product & Service Information)
- 簡單 TSP 登記制度
- 基本消費者保護措施

### Phase II and Beyond
- TSP 入職檢查 (onboarding checks)
- 持續監控 (ongoing monitoring)
- 雙邊合約關係

### Common Baseline Scope
- **Business:** 財務穩健、聲譽、管理質素、營運適當性
- **Risk Management:** 風險管理能力、網路安全、IT 控制（保密性、完整性、可用性）、應急計劃

### Streamlined Assessment Model
- 銀行間相互承認評估結果
- 或共同委託評估機構

### Liability (責任)
- 客戶不對因 TSP 使用銀行 Open API 進行的未授權交易直接損失負責（除非欺詐或重大過失）
- 銀行和 TSP 須在合約中明確責任和結算安排

---

## Open API Facilitation (配套措施)

- **Data Studio (香港科技園)** — 作為所有銀行 Open API 的單一登錄點（儀表板）
- 銀行可在自家網站或儀表板發布 Open API 詳細使用說明
- 須使用 **OpenAPI Specification (Swagger)** 發布技術規格
- 銀行須提供測試環境（含模擬客戶數據）協助 TSP

---

## Ongoing Development (持續發展)

- **HKAB (香港銀行公會)** — 成立委員會，與 HKMA 共同推動 Open API 持續發展
- 需要持續與 TSP 社群保持對話
- 未來可協調標準化，實現互操作性

---

## Key Technical Standards (Annex B)

Architecture, Security, Data Standards — 詳見附件 B（文檔中未完整展開）

---

## Open API Functions (Annex A) — Details

### Phase I: Product & Service Information

| Category | Functions |
|----------|-----------|
| **Deposits** | 存款產品詳情（儲蓄/支票/定期存款/外幣） |
| **Loans** | 信用卡、私人貸款、按揭貸款、抵押貸款產品詳情 |
| **Other Banking** | 保管箱、分行/ATM 資訊、外幣匯率 |
| **Investments** | 零售投資基金、結構性投資、貴金屬、股票交易產品詳情 |
| **Insurance** | 一般保險、人壽/長期保險產品詳情 |

### Phase II: Subscription & New Applications

| Category | Functions |
|----------|-----------|
| **Deposits** | 開立儲蓄/支票/定期/外幣帳戶 |
| **Loans** | 申請信用卡、按揭、私人貸款、抵押貸款 |
| **Other Banking** | 保管箱申請 |
| **Investments** | 開立投資基金、貴金屬、股票帳戶 |
| **Insurance** | 一般/人壽保險投保申請 |

### Phase III: Account Information

| Category | Functions |
|----------|-----------|
| **Deposits** | 存款帳戶詳情、交易明細 |
| **Loans** | 信貸限額、信用卡還款、交易、私人貸款詳情 |
| **Investments** | 零售基金、貴金屬、股票持倉資訊 |
| **Insurance** | 一般/人壽保險保單詳情、非財務保單變更 |
| **Other** | 帳單繳費歷史、EBPP 登記/取消、顧客聯絡資訊、支票簿申請 |

### Phase IV: Transactions
- 銀行交易和支付/轉帳

---

## Critical Interpretations

> [!important]
> **並非強制性** — HKMA 明確表示採用協作分階段方式，而非英國/歐盟的強制性 Open Banking。這賦予銀行較大彈性，但同時也意味著採進度可能較慢。

> [!warning]
> **TSP 責任** — TSP 收集的個人資料不視為銀行業務，TSP 須明確告知客戶並遵守個人資料保護條例。

---

## Metadata

- **Consultation Period:** 11 Jan 2018 – 15 Mar 2018
- **Industry Workshop:** 15 Aug 2017
- **Discussions with Open API Contacts:** Sep-Oct 2017
- **Covered Banks:** 20 retail + 3 foreign banks
- **Related:** Seven Smart Banking Initiatives

---

## Footnotes

[^1]: TSPs include other banks
[^2]: "Understanding the business relevance of Open APIs and Open Banking for banks", Euro Banking Association, May 2016
