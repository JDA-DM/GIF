# コアデータモデル解説書  アクセシビリティ <!-- omit in toc -->

デジタル社会推進実践ガイドブック DS-436

2022年（令和4年）3月31日

デジタル庁

-----
**[キーワード]**

アクセシビリティ、データモデル、バリアフリー、介助

**[概要]**

施設やイベント等に付随するアクセシビリティに関する情報をシステム実装する際に参照すべきデータモデルについて解説するガイドブックです。このガイドに従いデータ設計を行うことで、同じ設計規則に従うシステム間、分野間でのデータ連携を容易かつ正確に行えるようになります。また、データ設計を実施するコストも削減することができます。

-----

## 改訂履歴 <!-- omit in toc -->

| 改訂年月日    | 改定箇所                               | 改定内容                                                                                                         |
|---------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------|
| 2023年8月31日 | 1.1 アクセシビリティデータモデルの項目 | 多目的トイレの呼称を国土交通省のガイドライン（建築物におけるバリアフリーについて）に従いバリアフリートイレに変更 |
| 2022年3月31日 | -                                      | 初版決定                                                                                                         |

## 目次 <!-- omit in toc -->

- [1. アクセシビリティのデータモデル](#1-アクセシビリティのデータモデル)
  - [1.1. アクセシビリティデータモデルの項目](#11-アクセシビリティデータモデルの項目)

-----
## 1. アクセシビリティのデータモデル

施設やイベント開催時に、利用者にバリアフリーの状況や対応可能な介助の種類など、アクセシビリティに関する情報を伝えるときのデータモデルです。アクセシビリティ情報を付加したい他のデータモデルとあわせて利用することを想定しています。

各項目は基本的に対応可または対応不可のいずれかの値をとります。文書で詳細を伝えたい場合は備考にその内容を記述することを想定しています。

すべて任意項目なので、用途に応じて項目を選択、あるいは独自項目を追加するなどのカスタマイズを行って利用してください。

### 1.1. アクセシビリティデータモデルの項目

アクセシビリティデータモデルの項目は表1の通りです。英語名や記入例などを含む詳細については、別添の「438_コアデータモデル_DMD.xlsx」を参照してください。

表1 アクセシビリティデータモデルの項目一覧

| 必須項目 | 項目名                             | 説明                                             |
|----------|------------------------------------|--------------------------------------------------|
|          | 車椅子可                           | 車椅子の使用可否を記載。                         |
|          | 車椅子貸出                         | 車椅子貸出の有無を記載。                         |
|          | ツエ貸出                           | ツエ貸出の有無を記載。                           |
|          | バリアフリートイレ                 | バリアフリートイレの有無を記載。                 |
|          | スロープ、エレベータ、エスカレータ | スロープ、エレベータ、エスカレータの有無を記載。 |
|          | 点字ブロック等の移動支援           | 点字ブロック等の移動支援の有無を記載。           |
|          | 点字や読上による支援               | 点字や読上による支援の有無を記載。               |
|          | 盲導犬・介助犬、聴導犬同伴         | 盲導犬・介助犬同伴の有無を記載。                 |
|          | 字幕                               | 字幕の有無を記載。                               |
|          | 筆談対応                           | 筆談対応の有無を記載。                           |
|          | 優先駐車場                         | 優先駐車場の有無を記載。                         |
|          | オストメイト対応トイレ             | オストメイト対応トイレの有無を記載。             |
|          | 備考                               | その他アクセシビリティ事項を記載。               |

-----