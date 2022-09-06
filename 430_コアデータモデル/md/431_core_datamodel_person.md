デジタル社会推進実践ガイドブック DS-431

> コアデータモデル解説書  
> 個人

2022年（令和4年）3月31日

デジタル庁

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>[キーワード]</p>
<p>個人、データモデル、住民、社員、生徒</p>
<p>[概要]</p>
<p>個人の情報をシステム実装する際に参照すべきデータモデルについて解説するガイドブックです。このガイドに従いデータ設計を行うことで、同じ設計規則に従うシステム間、分野間でのデータ連携を容易かつ正確に行えるようになります。また、データ設計を実施するコストも削減することができます。</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 個人のデータモデル

個人の情報を記述する際のデータモデルです。行政組織が住民のデータを整備する場合の他、民間事業者や学校法人が社員や生徒、教員の情報を整備する場合などに活用されることを想定しています。氏名や連絡先などの基本的な情報は必須項目としています。

必須項目以外は任意項目なので、用途に応じて項目を選択、あるいは独自項目を追加するなどのカスタマイズを行って利用してください。

### 個人データモデルの項目

個人データモデルの項目は表1の通りです。英語名や記入例などを含む詳細については、別添の「438_コアデータモデル_DMD.xlsx」を参照してください。

表1 個人データモデルの項目一覧

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>必須<br />
項目</th>
<th>項目名</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>必</td>
<td>ID</td>
<td>個人番号、教員番号など。（ID情報型）</td>
</tr>
<tr class="even">
<td>必</td>
<td>氏</td>
<td>姓</td>
</tr>
<tr class="odd">
<td>必</td>
<td>名</td>
<td>名</td>
</tr>
<tr class="even">
<td>必</td>
<td>氏（カナ）</td>
<td>姓のカナ表記</td>
</tr>
<tr class="odd">
<td>必</td>
<td>名（カナ）</td>
<td>名のカナ表記</td>
</tr>
<tr class="even">
<td></td>
<td>氏（英字）</td>
<td>姓のローマ字表記</td>
</tr>
<tr class="odd">
<td></td>
<td>名（英字）</td>
<td>名のローマ字表記</td>
</tr>
<tr class="even">
<td></td>
<td>氏名</td>
<td>氏名（姓、名のセット）</td>
</tr>
<tr class="odd">
<td></td>
<td>氏名（カナ）</td>
<td>氏名（姓、名のセット）のカナ表記</td>
</tr>
<tr class="even">
<td></td>
<td>氏名（英字）</td>
<td>氏名（姓、名のセット）のローマ字表記</td>
</tr>
<tr class="odd">
<td></td>
<td>ミドルネームなど</td>
<td>ミドルネーム、旧姓、別名、通称名など（コード情報型）</td>
</tr>
<tr class="even">
<td></td>
<td>ミドルネームなど（カナ）</td>
<td>ミドルネームなどのカナ表記（コード情報型）</td>
</tr>
<tr class="odd">
<td></td>
<td>ミドルネームなど（英字）</td>
<td>ミドルネームなどのローマ字表記（コード情報型）</td>
</tr>
<tr class="even">
<td></td>
<td>戸籍氏名</td>
<td>戸籍上の氏名表記</td>
</tr>
<tr class="odd">
<td></td>
<td>国籍</td>
<td>国籍名（コード情報型）</td>
</tr>
<tr class="even">
<td></td>
<td>出生国</td>
<td>出生国名（コード情報型）</td>
</tr>
<tr class="odd">
<td>必</td>
<td>性別</td>
<td>性別名（コード情報型）</td>
</tr>
<tr class="even">
<td></td>
<td>生年月日</td>
<td>生年月日</td>
</tr>
<tr class="odd">
<td></td>
<td>死亡年月日</td>
<td>死亡している場合、死亡年月日</td>
</tr>
<tr class="even">
<td></td>
<td>年齢</td>
<td>記録時点の年齢</td>
</tr>
<tr class="odd">
<td></td>
<td>身長</td>
<td>記録時点の身長（単位：cm)</td>
</tr>
<tr class="even">
<td></td>
<td>体重</td>
<td>記録時点の体重（単位：kg)</td>
</tr>
<tr class="odd">
<td></td>
<td>機能支援の要否</td>
<td>身体障碍や車椅子など、何らかの補助が必要かどうか</td>
</tr>
<tr class="even">
<td></td>
<td>機能支援の種別</td>
<td>視覚支援、聴覚支援、移動支援など</td>
</tr>
<tr class="odd">
<td></td>
<td>備考</td>
<td>秘匿事項（DV等）など、その他特筆事項（コード情報型）</td>
</tr>
<tr class="even">
<td></td>
<td>世帯主</td>
<td>世帯主の情報</td>
</tr>
<tr class="odd">
<td></td>
<td>既婚・未婚</td>
<td>既婚か未婚の種別</td>
</tr>
<tr class="even">
<td></td>
<td>配偶者</td>
<td>配偶者の情報</td>
</tr>
<tr class="odd">
<td></td>
<td>子</td>
<td>子の情報（子の有無）</td>
</tr>
<tr class="even">
<td></td>
<td>学生</td>
<td>学生かどうか</td>
</tr>
<tr class="odd">
<td></td>
<td>収入の有無</td>
<td>記録時点の収入の有無</td>
</tr>
<tr class="even">
<td></td>
<td>居住住所</td>
<td>居住住所情報（住所型）</td>
</tr>
<tr class="odd">
<td></td>
<td>役割関与情報</td>
<td>委任先、保護者、続柄など（役割関与情報型）</td>
</tr>
<tr class="even">
<td>必</td>
<td>連絡先情報</td>
<td>連絡先住所の情報（個人連絡先型）</td>
</tr>
</tbody>
</table>

#### 役割関与情報について

教育機関における保護者など、個人に紐づく別の個人についての情報は「役割関与情報」に記述します。ここで個人と個人の関係性と、指し示す個人（保護者であれば両親など）の情報を記述します。記述のフォーマットの詳細はDMDの役割関与情報型を参照してください。

#### 国の名称とコードの扱い

個人や住所のデータモデルでは国の名称や国を表すコードを扱う項目が存在します。これらについては国際標準であるISO 3166-1及びJISX0304に従って管理します。コードで表す必要がある場合はアルファベット3文字（日本ならば「JPN」）で表すISO 3166-1 alpha-3での管理を標準とします。

#### 性別のコードの扱い

個人のデータモデル等で性別をコードで管理する場合は、国際標準であるISO 5218に従って管理します。すなわち「0:不明」「1:男性」「2:女性」「9:その他」となります。ここでいう性別とは生物学的性差（sex）を差し、文化的社会的性差（gender）は別項目として管理します。

### 個人連絡先

「連絡先」のデータモデルを拡張して個人連絡先のデータモデルを作成しています。連絡先とは異なり、連絡先電話番号、郵便番号、連絡先住所の３つが必須項目となっています。個人連絡先のデータモデルの項目は図表2の通りです。英語名や記入例などを含む詳細については、別添の「438_コアデータモデル_DMD.xlsx」を参照してください。

図表2 個人連絡先データモデルの項目一覧

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 43%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>必須<br />
項目</th>
<th>項目名</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>連絡先名称</td>
<td>連絡先名称</td>
</tr>
<tr class="even">
<td>必</td>
<td>連絡先電話番号</td>
<td>電話番号、携帯電話番号</td>
</tr>
<tr class="odd">
<td></td>
<td>連絡先内線番号</td>
<td>内線番号</td>
</tr>
<tr class="even">
<td></td>
<td>連絡先メールアドレス</td>
<td>連絡先メールアドレス</td>
</tr>
<tr class="odd">
<td></td>
<td>連絡先FormURL</td>
<td>連絡先がWebFormの場合のURL</td>
</tr>
<tr class="even">
<td></td>
<td>連絡先備考（その他、SNSなど）</td>
<td>SNSなどの連絡手段がある場合に記入</td>
</tr>
<tr class="odd">
<td>必</td>
<td>郵便番号</td>
<td>郵便番号</td>
</tr>
<tr class="even">
<td>必</td>
<td>連絡先住所</td>
<td>連絡先住所の情報</td>
</tr>
</tbody>
</table>

## 変更履歴

| 改定年月日    | 改定箇所 | 改定内容 |
|---------------|----------|----------|
| 2022年3月31日 | \-       | 初版決定 |
